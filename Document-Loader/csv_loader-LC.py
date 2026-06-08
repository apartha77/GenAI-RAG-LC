#========================================================================
'''
CSV Loader = CSV file extraction and loading
CSVLoader is used to load CSV files. It takes the file path as input and returns a list of Document objects. 
Each Document object contains the content of a row in the CSV file and metadata such as the row number.
In this example, we are using the CSVLoader to load a CSV file containing social network ads
'''
#========================================================================

from langchain_community.document_loaders import CSVLoader

try:    
    loader = CSVLoader(file_path='Data/Social_Network_Ads.csv')

    docs = loader.load()
    # Lazy loading is also supported, which allows you to load the documents one by one instead of loading all at once. This can be useful for large CSV files.
    #docs = loader.lazy_load()

    print(len(docs))
    print(docs[0])

except Exception as e:
    print(f"Error occurred: {str(e)}")
    