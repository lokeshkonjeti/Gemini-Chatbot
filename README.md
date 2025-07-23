# Gemini-Chatbot

Built a Chatbot on the University at Buffalo's International Student Services Website using RAG and Gemini API.
Used pinecone to store the vectors from the data scraped from the UB ISS website.

Built a crawler function which will parse through all the links with the prefix: https://www.buffalo.edu/international-student-services and index these pages into a pinecone vector database.

After indexing the data into a pinecone database, use the Gemini API to retrieve the data and answer any queries.
