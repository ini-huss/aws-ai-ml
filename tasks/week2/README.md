## Week 2: Mini Semantic Search Engine
*** Project Overview ***
A beginner-friendly semantic search engine that retrieves FAQ documents based on their meaning rather than relying only on exact keyword matches.

*** Technologies Used ***
# Python
# Pandas
# Sentence Transformers
# ChromaDB
# Google Colab

*** Features ***
# Loads FAQ data from CSV
# Cleans missing and empty records
# Combines questions and answers into searchable documents
# Generates vector embeddings using all-MiniLM-L6-v2
# Stores embeddings in ChromaDB
# Returns the top three semantically similar FAQs
# Supports interactive user queries

*** How It Works ***
# Load and clean the FAQ dataset.
# Prepare FAQ documents.
# Generate embeddings for each document.
# Store documents and embeddings in ChromaDB.
# Embed the user’s query and retrieve the three closest matches.

*** Example Query ***
# Query: How can I track changes in my code?
The system searches for FAQs with similar meanings and returns the three closest results.

*** How to Run ***
Open semantic_search.ipynb in Google Colab and execute the cells from top to bottom.

*** Learning Outcomes ***
Data loading and cleaning with Pandas
Text preparation
Embeddings and vector representations
Vector database storage and retrieval
Semantic similarity search