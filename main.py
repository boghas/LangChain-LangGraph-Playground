import os

from dotenv import load_dotenv

load_dotenv()


print(os.environ.get("OPENAI_API_KEY"))


def main():
    print("Hello from langchain-langgraph-course!")


if __name__ == "__main__":
    main()
