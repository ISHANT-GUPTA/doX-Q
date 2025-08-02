from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIRECTORY = "uploaded_pdfs"

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    """
    Serves the frontend HTML file.
    """
    try:
        with open("index.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "index.html not found. Please place the frontend HTML file in the same directory."

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Handles the PDF file upload from the frontend.
    """
    
    
    if not file.filename.endswith('.pdf'):
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only PDF files are allowed."
        )


    filename = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    
    print(f"Attempting to save file to: {file_path}")
    
    try:

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
            
        success_message = f"Successfully uploaded {filename}"
        
        
        return JSONResponse(content={"message": success_message})
    
    except Exception as e:
       
        print(f"Error saving file: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to save file on the server: {str(e)}"
        )

@app.post("/chat")
async def chat_message(request: Request):
    """
    Receives chat messages from the frontend and stores them in a variable.
    """
 
    data = await request.json()
    

    user_message = data.get("message", "")
    

    print(f"Received message from frontend: {user_message}")
    
    return JSONResponse(content={"reply": "Message received!"})
