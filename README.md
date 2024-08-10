# Document Summarizer

## Overview
This web application allows users to upload documents (PDF, DOCX, TXT) and receive summarized versions using a locally deployed Language Model (LLM).

## Features
- Upload documents via a simple React frontend.
- Summarize the content using a locally hosted LLM.
- Dockerized for easy deployment.

## Components
- **Backend**: Built with FastAPI, handles file uploads and document summarization.
- **Frontend**: Built with React, provides a user interface for uploading files and displaying summaries.
- **LLM Deployment**: Integrates a pre-trained model (e.g., GPT-2) for generating text summaries.

## Prerequisites
- Docker and Docker Compose installed on your machine.
- Node.js and npm installed (if running the frontend separately).
- Python 3.9 or higher installed (if running the backend separately).

## Setup Instructions

### Using Docker Compose
  1. Clone the repository:
     ```bash
     git clone https://github.com/yushprince/doc-summarizer.git
     cd doc-summarizer
  
  2. Build and run the application:
     ```bash
         docker-compose up --build2.
     
  3. Access the application:
  
        Frontend: http://localhost:3000
     
        Backend API: http://localhost:8000  


## Usage
- Visit the frontend URL (http://localhost:3000) to upload documents and view summaries.
- The backend API can be accessed directly via http://localhost:8000

## Challenges and Solutions
- Large File Handling: Implemented file size checks and optimized the backend to handle large files efficiently.
- Model Performance: Chose a lightweight LLM (e.g., DistilBART) to balance performance and accuracy for local deployment.

## Future Improvements
- Add support for more document types (e.g., PDF, DOCX).
- Implement authentication and user management.
-  Improve the UI/UX of the frontend.

## Bibliography
- FastAPI Documentation: https://fastapi.tiangolo.com/
-  React Documentation: https://reactjs.org/docs/getting-started.html
-  Transformers Library: https://huggingface.co/transformers/
