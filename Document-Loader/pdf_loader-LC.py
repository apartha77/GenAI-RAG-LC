#========================================================================
'''
Document Loader - PDF Loader 
All document loader are under langchain_community
PyPDFLoader is used to load PDF files. It takes the file path as input and returns a list of Document objects. Each Document object contains the page content and metadata.
It is not greate with scanned PDF or complex PDF with images and tables. It works best with simple PDF files with text content. 
For complex PDF files use PDFPolumber or PyMuPDFLoader. For scanned PDF files PyTesseractLoader, UnstructuredLoader or TextractLoader.
'''
#========================================================================
from langchain_community.document_loaders import PyPDFLoader
from langchain_aws import ChatBedrock
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

try:    
    load_dotenv()

    model = ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        region_name="us-east-1",
        credentials_profile_name="EBU"
    )

    loader = PyPDFLoader('Data/dl-curriculum.pdf')

    docs = loader.load()
    
    #Number of pages in the PDF document
    print(len(docs))
    #Print the content and metadata of the first page
    print(docs[0].page_content)
    print(docs[0].metadata)

except Exception as e:
    print(f"Error occurred: {str(e)}")