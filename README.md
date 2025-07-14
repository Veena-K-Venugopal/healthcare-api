# 🩺 Healthcare Patient Records API

A simple RESTful API built with FastAPI to simulate a backend system for managing patients, appointments, and medications. Designed for learning, portfolio building, and backend development practice.

---

## 🚀 Features

- `GET /patients` – List all patients  
- `GET /patients/{id}` – Get patient by ID  
- `GET /appointments` – List all appointments  
- `GET /appointments/{id}` – Get appointment by ID  
- `GET /medications` – List all medications  
- `GET /medications/{id}` – Get medication by ID

---

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI  
- **Server**: Uvicorn (ASGI)  
- **Dev Tools**: VS Code, Git, GitHub  
- **Deployment**: Coming soon on [Render](https://render.com/)

---

## 📦 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/healthcare-api.git
cd healthcare-api

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload

```

## 🔗 Live Demo

[https://healthcare-api-2c8b.onrender.com/](https://healthcare-api-2c8b.onrender.com/)

- `/patients`
- `/appointments`
- `/docs` (Swagger UI)
