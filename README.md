# 🩺 Healthcare Patient Records & Prediction API

A simple but scalable RESTful API built with FastAPI to simulate a backend system for managing patient records, appointments, medications, and mock diagnostic predictions.

This project is designed for learning, backend development practice, and demonstrating modular API architecture with prediction capabilities.

---

## 🚀 Features

- `GET /` – Root welcome message  
- `GET /patients` – List all patients  
- `GET /patients/{id}` – Get patient by ID  
- `GET /appointments` – List all appointments  
- `GET /appointments/{id}` – Get appointment by ID  
- `GET /medications` – List all medications  
- `GET /medications/{id}` – Get medication by ID
- `POST /predict` – Submit basic patient info and get a mock diagnosis result with enhanced metadata

---

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI  
- **Server**: Uvicorn (ASGI)  
- **Dev Tools**: VS Code, Git, GitHub  
- **Deployment**: Live on [Render](https://healthcare-api-2c8b.onrender.com/)

---

## ✅ Project Enhancements – Phase 1 Complete

- Refactored codebase into modular structure (`app/`, `routes/`, `services/`, `utils/`)
- Added `POST /predict` endpoint with mock ML prediction logic
- Implemented output enhancement for future integration with real AI/ML models
- Input validated using Pydantic
- Swagger UI now includes all active endpoints

---

## 📦 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Veena-K-Venugopal/healthcare-api.git
cd healthcare-api

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set PYTHONPATH and run the app
export PYTHONPATH=.
uvicorn app.main:app --reload

```

## 🔗 Live Demo

[Render](https://healthcare-api-2c8b.onrender.com/)

- `/patients`
- `/appointments`
- `/predict`
- `/docs` (Swagger UI)

📌 Roadmap available upon request — contact vkvenu10@gmail.com
