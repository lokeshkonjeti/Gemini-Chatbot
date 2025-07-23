import argparse
from crawler import get_subpath_links
from loader import load_documents
from database_setup import pinecone_setup

ROOT_URL = "https://www.buffalo.edu/international-student-services.html"
ALLOWED_PREFIX = "https://www.buffalo.edu/international-student-services"

GEMINI_KEY = "Gemini_Key"
PINECONE_KEY = "Pinecone_Key"
INDEX_NAME = "gemini-chatbot-3"

def run_indexing():
    urls = get_subpath_links(ROOT_URL, ALLOWED_PREFIX)
    documents_parsed = load_documents(urls)
    index = pinecone_setup(
        chunk_size=512,
        t_dimensions=768,
        gemini_key=GEMINI_KEY,
        api_key=PINECONE_KEY,
        index_name=INDEX_NAME,
        documents=documents_parsed
    )
    print("Indexing complete.")

def run_query():
    index = pinecone_setup(
        chunk_size=512,
        t_dimensions=768,
        gemini_key=GEMINI_KEY,
        api_key=PINECONE_KEY,
        index_name=INDEX_NAME,
        documents=None  # no documents needed
    )
    query_engine = index.as_query_engine(similarity_top_k=5)
    while True:
        q = input("You: ")
        if q.lower() == "exit":
            break
        response = query_engine.query(q)
        print("Gemini:", response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["index", "query"], required=True)
    args = parser.parse_args()

    if args.mode == "index":
        run_indexing()
    elif args.mode == "query":
        run_query()
