# GitHub Repo Summarizer

A fullstack web app that summarizes GitHub repositories using the content of their `README.md` file. Built with **React**, **FastAPI**, and **OpenAI GPT-4**.

##   Live Demo

🌐 Frontend: [repo-summarizer-frontend.onrender.com](https://repo-summarizer-frontend.onrender.com)  
🔙 Backend: [repo-summarizer.onrender.com](https://repo-summarizer.onrender.com)

---

##   Features

- Enter any public GitHub repository URL
- Extracts and parses the `README.md` file
- Summarizes the content using OpenAI's GPT-4 API
- Responsive and simple frontend interface
- Graceful error handling for missing or invalid repos

---

##   Tech Stack

### Frontend
- [React](https://reactjs.org/)
- [Axios](https://axios-http.com/) for API requests

### Backend
- [FastAPI](https://fastapi.tiangolo.com/)
- [PyGithub](https://pygithub.readthedocs.io/) for GitHub API
- [OpenAI Python SDK](https://github.com/openai/openai-python)

---

##  Project Structure

repo-summarizer/
├── backend/
│ ├── app.py
│ ├── github_helpers.py
│ ├── llm_helpers.py
│ └── requirements.txt
├── frontend/
│ ├── src/
│ │ └── App.js
│ ├── public/
│ └── .env
├── README.md
└── .gitignore
