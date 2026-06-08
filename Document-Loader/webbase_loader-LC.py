#========================================================================
'''
Web Base Loader - Web page extraction and loading
WebBaseLoader is used to load web pages. It takes the URL as input and returns a list of Document objects. Each Document object contains the page content and metadata.
Under the hood, it uses the BeautifulSoup library to parse the HTML content of the web page and extract the text. It also handles pagination and can load multiple pages if needed.
In this example, we are using the WebBaseLoader to load the content of a product page from Amazon. We then use a prompt template to ask a question about the product and use the ChatBedrock model to get the answer. 
Finally, we use the StrOutputParser to extract the answer from the model's response and print it out.
'''
#========================================================================

from langchain_community.document_loaders import WebBaseLoader
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
    # Prompt template to ask question from the web page content
    prompt = PromptTemplate(
        template='Answer the following question \n {question} from the following text - \n {text}',
        input_variables=['question','text']
    )
    # Define the output parser to extract the answer from the model's response
    parser = StrOutputParser()

    url = "https://www.amazon.co.uk/s?k=windscreen+repair+kit&crid=65QW7KM4PKAG&sprefix=windscreen+re%2Caps%2C101&ref=nb_sb_ss_mvt-t11-ranker_1_13"
    #url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
    loader = WebBaseLoader(url)
    # You get one document per url, so if you want to load multiple pages, you can pass a list of urls to the loader.
    docs = loader.load()
    #print(docs[0].page_content)


    chain = prompt | model | parser

    print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))

except Exception as e:
    print(f"Error occurred: {str(e)}")
