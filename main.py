

from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os

# --- Basic Setup ---
app = FastAPI()

# Allow all origins for simplicity. In production, restrict this to your frontend's domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Directory and Template Setup ---

# This tells FastAPI where to find your HTML files.
templates = Jinja2Templates(directory="templates")

# Define the directory where uploaded PDFs will be stored.
UPLOAD_DIRECTORY = "uploaded_pdfs"

# Create the upload directory if it doesn't already exist.
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


# --- Frontend Serving Endpoints ---

@app.get("/", response_class=HTMLResponse)
async def serve_upload_page(request: Request):
    """
    Serves the main PDF uploader page (index.html).
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
async def serve_chat_page(request: Request):
    """
    Serves the chatbot interface page (chat.html).
    """
    return templates.TemplateResponse("chat.html", {"request": request})


# --- API Endpoints ---

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Handles the PDF file upload from the frontend.
    It saves the file to the server's filesystem.
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only PDF files are allowed."
        )

    # Sanitize filename to prevent security risks like directory traversal.
    filename = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    
    print(f"Saving file to: {file_path}")
    
    try:
        # Asynchronously read the file content and write it to the server.
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
            
        return JSONResponse(
            status_code=200,
            content={"message": f"Successfully uploaded {filename}"}
        )
    
    except Exception as e:
        print(f"Error saving file: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to save file on the server: {str(e)}"
        )
user_message=""
@app.post("/chat")
async def chat_endpoint(request: Request):
    """
    Receives a chat message, processes it, and returns a reply.
    (This is where you would add your RAG/LLM logic).
    """
    data = await request.json()
    user_message = data.get("message", "")
    
    print(f"Received message: {user_message}")
    
    # --- Placeholder for your AI logic ---
    # In a real app, you would use the user_message to query your
    # processed PDF data and generate a response from an LLM.
    bot_reply = f"I received your message about the PDF: '{user_message}'. My AI brain is still under construction!"
    # ------------------------------------
    
    print("bot reeeeeee-----------------",user_message)
    return JSONResponse(content={"reply": bot_reply})
