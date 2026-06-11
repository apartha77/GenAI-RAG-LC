'''
Markdown Splitter: This method is designed to split markdown text into smaller chunks while preserving the markdown formatting.
It's particularly useful for splitting documentation, README files, or any content that uses markdown syntax.
'''

from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

try:

    text = """
    # Project Name: Smart Student Tracker

    A simple Python-based project to manage and track student data, including their grades, age, and academic status.


    ## Features

    - Add new students with relevant info
    - View student details
    - Check if a student is passing
    - Easily extendable class-based design


    ## 🛠 Tech Stack

    - Python 3.10+
    - No external dependencies


    ## Getting Started

    1. Clone the repo  
    ```bash
    git clone https://github.com/your-username/student-tracker.git

    """

    # Initialize the splitter
    splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.MARKDOWN,
        chunk_size=200,
        chunk_overlap=0,
    )

    # Perform the split
    chunks = splitter.split_text(text)

    print(len(chunks))
    print(chunks[1])
    
except Exception as e:
    print(f"An error occurred: {e}")