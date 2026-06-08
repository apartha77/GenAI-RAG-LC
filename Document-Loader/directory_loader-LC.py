#========================================================================
'''
Directory Loader - If you have multiple PDF files in a directory
All document loader are under langchain_community
DirectoryLoader is used to load all PDF files from a directory. It takes the directory path and a glob pattern as input and returns a list of Document objects. Each Document object contains the page content and metadata.
'''
#========================================================================

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

try:
    # DirecotryLoader - glob pattern specify the file type
    loader = DirectoryLoader(
        path='Data', # Specify the directory path where your PDF files are located. In this case, it is 'Data'.
        glob='*.pdf',
        loader_cls=PyPDFLoader
    )
    # Lazy load the documents from the directory - Lazy loading is useful when you have a large number of documents and you want to load them one by one instead of loading all at once. It helps in reducing memory usage and improving performance.
    # Using Lazy Load instead of Load()
    docs = loader.lazy_load()
    # docs = loader.load() # Use this if you want to load all documents at once. It will return a list of Document objects.
    # print(docs[1].page_content)
    # print(docs[1].metadata)
    
    #loop through the documents and print the metadata
    for document in docs:
        print(document.metadata)
        
except Exception as e:
    print(f"Error occurred: {str(e)}")  