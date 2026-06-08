#========================================================================
'''
Document Loader - Text Loader 
All document loader are under langchain_community
TextLoader is used to load text files. It takes the file path and encoding as input and returns a list of Document objects. Each Document object contains the page content and metadata.
 
'''
#========================================================================
from langchain_community.document_loaders import TextLoader
#from langchain_openai import ChatOpenAI
from langchain_aws import ChatBedrock
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

try:
    load_dotenv()

    # Claude for model usage. 
    model = ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0", 
        region_name="us-east-1",
        credentials_profile_name="EBU"
        ) 
    #model = ChatOpenAI()

    loader = TextLoader('Data/my_text.txt', encoding='utf-8')
    docs = loader.load()
    print(type(docs))
    print(len(docs))
    #print(docs[0])
    print(docs[0].page_content)
    print(docs[0].metadata)
    print("-------------------------------------------------------------------------------------")

    # Define the prompt template and output parser
    prompt = PromptTemplate(
        template='Write a summary for the following poem in 50 words- \n {poem}',
        input_variables=['poem']
    )
    # Define the output parser to extract the summary from the model's response
    parser = StrOutputParser()

    # Define the chain to process the document and generate the summary
    chain = prompt | model | parser
    # Invoke the chain with the document content and print the summary
    print(chain.invoke({'poem':docs[0].page_content}))

    # Print the chain for visuals using grandalf
    chain.get_graph().print_ascii()

except Exception as e:
    print(f"Error occurred: {str(e)}")