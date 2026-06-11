#========================================================================
'''
Text Structure Splitter 
This method splits text based on its structure, such as paragraphs, sentences, or sections.
This approach can help maintain the semantic integrity of the text, as it tries to keep related information together.
However, it may result in chunks of varying lengths, and in some cases, it might not split the text into manageable pieces if the structure is not well-defined. 
'''
#========================================================================
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_aws import ChatBedrock
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

try:
    load_dotenv()
    # Example text to split
    text = """
    Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

    These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
    """

    # Initialize the splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=0,
    )

    # Perform the split
    chunks = splitter.split_text(text)

    print(len(chunks))
    #print(chunks[0])
    print(chunks)


except Exception as e:
    print(f"An error occurred: {e}")
    
    