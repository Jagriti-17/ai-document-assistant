from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
from openai import OpenAI
import os

app = FastAPI()

# -------- CORS --------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- OpenAI --------
client = OpenAI(api_key="YOUR_API_KEY_HERE") 

# -------- GLOBAL STORAGE --------
stored_text = ""

# -------- HOME --------
@app.get("/")
def home():
    return {"message": "Backend is running"}

# -------- UPLOAD --------
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    global stored_text

    filename = file.filename
    print("File received:", filename)

    # ---------- PDF OPTION ----------
    if filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        text = ""

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content

        if text.strip() == "":
            return {"message": "Could not extract text from PDF"}

        stored_text = text[:3000]

        print("Extracted text length:", len(stored_text))

        return {"message": "PDF uploaded and processed successfully"}

    
    elif filename.endswith((".mp3", ".wav", ".mp4", ".avi")):
        stored_text = ""  # reset
        return {
            "message": "Audio/Video uploaded successfully. Transcription feature not enabled yet."
        }

    else:
        return {"message": "Unsupported file type"}

# -------- CHAT OPTION --------
@app.post("/chat")
async def chat(data: dict):
    global stored_text

    if not stored_text:
        return {
            "answer": "Text-based querying is currently available only for PDF documents."
        }

    question = data.get("question")

    if not question:
        return {"answer": "Please enter a question."}

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": f"{stored_text}\n\nQuestion: {question}"}
            ]
        )

        answer = response.choices[0].message.content
        return {"answer": answer}

    except Exception as e:
        print(e)
        return {
            "answer": "AI response is currently unavailable due to service limits. Your document has been processed successfully."
        }

# -------- SUMMARY OPTION --------
@app.post("/summary")
async def summary():
    global stored_text

    if not stored_text:
        return {
            "summary": "Summary is available only for PDF documents."
        }

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": f"Summarize this:\n{stored_text}"}
            ]
        )

        summary_text = response.choices[0].message.content
        return {"summary": summary_text}

    except Exception as e:
        print(e)
        return {
            "summary": "AI summary is currently unavailable due to service limits."
        }