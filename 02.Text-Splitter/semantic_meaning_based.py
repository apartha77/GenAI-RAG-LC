'''
Semantic Meaning Splitter: This method uses natural language processing techniques to split text based on its semantic meaning. 
It can identify logical breaks in the text, such as sentence boundaries, paragraph breaks, or even topic shifts. 
This approach can create more meaningful chunks of text that are easier to understand and work with, especially for tasks like summarization or question-answering.
'''
#from langchain_text_splitters import SemanticChunker
from langchain_experimental.text_splitter import SemanticChunker
from langchain_aws import ChatBedrock
from langchain_aws import BedrockEmbeddings
from langchain_core.output_parsers import StrOutputParser   
# from langchain_experimental.text_splitter import SemanticChunker
# from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

try:
    load_dotenv()
    # Initialize Bedrock embeddings
    embeddings = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v2:0",
        region_name="us-east-1",
        credentials_profile_name="EBU"
    )
    
    # Initialize the text splitter with Bedrock embeddings
    text_splitter = SemanticChunker(
        embeddings, breakpoint_threshold_type="standard_deviation",
        breakpoint_threshold_amount=3
    )
    # Example text to split
    sample = """
    Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


    Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
    """
    # Split the text
    docs = text_splitter.create_documents([sample])
    print(len(docs))
    print(docs)

except Exception as e:
    print(f"An error occurred: {e}")
    
