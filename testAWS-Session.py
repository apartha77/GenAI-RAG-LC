#========================================================================
'''
Check AWS Session everyday before start of Dev Work 
'''
#========================================================================
import langchain
import boto3
import subprocess
import sys
from botocore.exceptions import UnauthorizedSSOTokenError, NoCredentialsError

print(langchain.__version__)

def check_and_refresh_aws_session(profile_name='EBU'):
    """
    Check AWS session and refresh if expired using SSO
    """
    try:
        # Try to create session and get credentials
        session = boto3.Session(profile_name=profile_name)
        credentials = session.get_credentials()
        
        # Test credentials by making a simple AWS call
        sts_client = session.client('sts')
        identity = sts_client.get_caller_identity()
        
        print(f"✅ AWS session is valid for profile '{profile_name}'")
        print(f"Account: {identity.get('Account')}")
        print(f"User: {identity.get('Arn')}")
        
        return session, credentials
        
    except UnauthorizedSSOTokenError:
        print(f"❌ SSO session expired for profile '{profile_name}'")
        print(f"🔄 Initiating SSO login...")
        
        try:
            # Run aws sso login command
            result = subprocess.run(
                ['aws', 'sso', 'login', '--profile', profile_name],
                capture_output=True,
                text=True,
                check=True
            )
            
            print("✅ SSO login successful")
            
            # Create new session after login
            session = boto3.Session(profile_name=profile_name)
            credentials = session.get_credentials()
            
            # Verify new session
            sts_client = session.client('sts')
            identity = sts_client.get_caller_identity()
            
            print(f"✅ New session created for profile '{profile_name}'")
            print(f"Account: {identity.get('Account')}")
            
            return session, credentials
            
        except subprocess.CalledProcessError as e:
            print(f"❌ SSO login failed: {e}")
            sys.exit(1)
            
    except NoCredentialsError:
        print(f"❌ No credentials found for profile '{profile_name}'")
        print("Please check your AWS configuration")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

def set_aws_env_vars(credentials):
    """
    Set AWS credentials as environment variables
    """
    import os
    
    os.environ['AWS_ACCESS_KEY_ID'] = credentials.access_key
    os.environ['AWS_SECRET_ACCESS_KEY'] = credentials.secret_key
    if credentials.token:
        os.environ['AWS_SESSION_TOKEN'] = credentials.token
    
    print("✅ AWS credentials set as environment variables")

if __name__ == "__main__":
    # Test the function
    session, credentials = check_and_refresh_aws_session('EBU')
    set_aws_env_vars(credentials)
    
    # Test Bedrock access
    try:
        bedrock_client = session.client('bedrock-runtime', region_name='us-east-1')
        print("✅ Bedrock client created successfully")
    except Exception as e:
        print(f"❌ Failed to create Bedrock client: {e}")