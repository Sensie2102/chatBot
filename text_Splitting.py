import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from connectDB import get_db
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain.embeddings import HuggingFaceEmbeddings

def load_and_split_documents(directory: str, splitter: RecursiveCharacterTextSplitter) -> list:
    """Load all .txt files from a directory and split them into chunks."""
    chunks_list = []
    for dir in directory:
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    chunks = splitter.split_text(text)
                    chunks_list.extend(chunks)
    return chunks_list

def add_embeddings():
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    
    
    directory = ["scraped_texts_mparticle","scraped_texts_segment"]
    
    
    all_chunks = load_and_split_documents(directory, text_splitter)
    print(f"Total chunks created: {len(all_chunks)}")
    
    
    documents = [Document(page_content=chunk) for chunk in all_chunks]
    
    
    collection = get_db()
    
    
    collection.delete_many({})
    
    
    
    # Create and store the documents in the MongoDB Atlas vector store
    docsearch = MongoDBAtlasVectorSearch.from_documents(
        documents, 
        embeddings, 
        collection=collection, 
        index_name="vector_index"
    )
    
    print("Documents and embeddings stored successfully in MongoDB Atlas vector store.")

if __name__ == "__main__":
    add_embeddings()