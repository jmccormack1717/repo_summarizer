import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Custom helper functions
from github_helpers import get_readme_from_repo
from llm_helpers import summarize_text

# Initialize the FastAPI application
app = FastAPI()

# Get the frontend URL from environment variables for CORS; fallback to local dev frontend
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# Enable CORS so the frontend can make requests to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],  # Only allow requests from the frontend
    allow_methods=["*"],           # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],           # Allow all headers (e.g., content-type)
)

# Define the shape of incoming POST request body using Pydantic
class RepoRequest(BaseModel):
    repo_url: str  # Expected field in the JSON body

# Define the API endpoint that accepts a GitHub repo URL and returns a summary
@app.post("/summarize")
async def summarize_repo(req: RepoRequest):
    # Attempt to fetch the README from the given GitHub repo
    readme = get_readme_from_repo(req.repo_url)
    if not readme:
        # If README not found or fetch fails, return a 404 error to the client
        raise HTTPException(status_code=404, detail="Could not fetch README from repo.")
    
    # Send the README content to OpenAI and get the summary
    summary = summarize_text(readme)
    
    # Return the summary in a JSON response
    return {"summary": summary}
