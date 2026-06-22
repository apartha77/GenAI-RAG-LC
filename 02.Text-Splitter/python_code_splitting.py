'''
Python Code Splitter: This method is designed to split Python code into smaller, manageable chunks. It can identify logical breaks in the code, such as 
function definitions, class definitions, or even code blocks. This approach can help maintain the semantic integrity of the code, 
making it easier to understand and work with, especially for tasks like code analysis or refactoring.
'''
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

try:

    text = """
    class Student:
        def __init__(self, name, age, grade):
            self.name = name
            self.age = age
            self.grade = grade  # Grade is a float (like 8.5 or 9.2)

        def get_details(self):
            return self.name"

        def is_passing(self):
            return self.grade >= 6.0


    # Example usage
    student1 = Student("Aarav", 20, 8.2)
    print(student1.get_details())

    if student1.is_passing():
        print("The student is passing.")
    else:
        print("The student is not passing.")

    """

    # Initialize the splitter
    splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=300,
        chunk_overlap=0,
    )

    # Perform the split
    chunks = splitter.split_text(text)

    print(len(chunks))
    print(chunks[0])
    
except Exception as e:
    print(f"An error occurred: {e}")
    