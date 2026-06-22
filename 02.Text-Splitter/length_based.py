'''
Spliting by fixed length of characters. This is the most basic way to split text, and it can be useful for 
certain applications where you want to ensure that each chunk of text is a specific length. 
However, it can also lead to chunks that are not semantically meaningful, as it may split sentences or paragraphs in the middle.

'''
#from langchain.text_splitter import CharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

try:

    loader = PyPDFLoader('dl-curriculum.pdf')

    docs = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=0,
        separator=''
    )

    result = splitter.split_documents(docs)
    
    print(len(result))

    print(result[2].page_content)

except Exception as e:
    print(f"An error occurred: {e}")
    


    
    