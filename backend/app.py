import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .github_utils import get_readme_from_repo
from .llm_utils import summarize_text


app = FastAPI()

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RepoRequest(BaseModel):
    repo_url: str

@app.post("/summarize")
async def summarize_repo(req: RepoRequest):
    readme = get_readme_from_repo(req.repo_url)
    if not readme:
        raise HTTPException(status_code=404, detail="Could not fetch README from repo.")
    summary = summarize_text(readme)
    return {"summary": summary}
