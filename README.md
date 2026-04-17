# AI-Powered Document & Multimedia Q&A Web Application

## Overview
This project is a full-stack web application that allows users to upload documents and interact with them using an AI-powered chatbot.

---

## Features
- Upload PDF documents
- AI-powered chatbot for document-based Q&A
- Document summarization
- Audio/Video upload support (transcription to be added)
- Fallback response when AI service is unavailable
- Basic API testing using pytest


---

## Tech Stack
### Frontend:
- React.js
- Axios
- CSS 

### Backend:
- FastAPI (Python)
- pypdf (PDF text extraction)
- OpenAI API 

### Testing:
- Pytest

### DevOps:
- Docker (Dockerfile included)
- GitHub Actions (CI pipeline)

---


## How to Run Locally

### Backend
- pip install -r requirements.txt
- uvicorn main:app --reload

### Frontend
- cd frontend
- npm install
- npm start

---

## Deployment
- Backend: https://ai-document-assistant-b2i2.onrender.com
- Frontend: https://ai-document-assistant-webapp.vercel.app/

---

## Limitations
- AI responses depend on OpenAI API quota
- If quota is exceeded, fallback messages are shown
- Audio/Video transcription is not implemented yet
- Data is stored temporarily (no persistent DB in final version)

--- 

## Future Improvements
- Vector search using FAISS or Pinecone
- Audio/Video transcription using Whisper API
- User authentication (JWT/OAuth)
- Cloud deployment (AWS/GCP/Azure)
- Real-time chat streaming
- Database integration (MongoDB/PostgreSQL)

---

## Demo

A walkthrough video demonstrating the features and code structure explanation.

Video Link: https://drive.google.com/file/d/1dqlqTfS20ll73EtypqjvbViZN7PKOSaP/view?usp=sharing
