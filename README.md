# Banking AI Assistant - Advanced RAG System
> An intelligent Banking Assistant powered by Advanced RAG to provide high-precision answers from complex financial documents.
> Live demo [_here_](https://g6y3w846zs.us-east-1.awsapprunner.com/).
![Banking Bot Demo](./img/demo.gif)
> ## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- This project addresses the challenge of "hallucinations" in LLMs when dealing with specific, private banking regulations and fees.
- The purpose is to build a reliable RAG pipeline capable of parsing complex tables and structured headers from PDF documents.
- I undertook this project to demonstrate the ability to optimize large Docker images and deploy production-grade AI on AWS.


## Technologies Used
- LangChain - version 0.3.0
- Docling (IBM) - version 2.15.1
- Docker - Multi-stage build optimization
- AWS App Runner & ECR - Cloud Deployment
- Groq (Llama 3 / Mistral) - High-speed LLM Inference
- FAISS - Vector Database for semantic search


## Features
List the ready features here:
- **Advanced Table Parsing**: Leverages IBM's Docling to maintain table structures that standard PDF parsers miss.
- **Ensemble Retrieval**: Combines BM25 and Vector Search to ensure both keyword and semantic accuracy.
- **Markdown Header Splitting**: Splits documents by logical sections (H1, H2, H3) to maintain context.
- **Production-Ready CI/CD**: Fully containerized and deployed on AWS App Runner for scalability.
  
## Setup
The project dependencies are managed in the `requirements.txt` file located in the root directory.

To set up your local environment:
1. Clone the repository:
   ```bash
   git clone https://github.com/ThanhCongLuong/langchain-financial-chatbot.git
   cd langchain-financial-chatbot
   
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
3. Configure Environment Variables:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   
## Project Status
Project is: complete. The core RAG pipeline is functional and successfully deployed to AWS.

## Room for Improvement

- Adding a "Self-Correction" layer to evaluate retrieved document relevance before answering.

- Enhancing the UI to support multi-file uploads for real-time document analysis.

## Acknowledgements
This project was inspired by the need for high-accuracy RAG in the FinTech industry.

Many thanks to the LangChain community.

## Contact
Created by [@thanhcongluong](https://github.com/ThanhCongLuong) - feel free to contact me!
