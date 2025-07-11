from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Healthcare API!"}

patients = [
    {"id": 1, "name": "John Doe", "dob": "1990-01-01", "conditions": ["hypertension", "asthma"]},
    {"id": 2, "name": "Jane Smith", "dob": "1985-07-14", "conditions": ["diabetes"]},
    {"id": 3, "name": "Sponge Bob", "dob": "1992-03-22", "conditions": ["high cholesterol"]},
]

appointments = [
    {"id": 1, "patient_id": 1, "date": "2025-07-02", "time": "10:00 AM", "doctor": "Dr. Smith"},
    {"id": 2, "patient_id": 2, "date": "2025-07-03", "time": "02:30 PM", "doctor": "Dr. Adams"},
    {"id": 3, "patient_id": 1, "date": "2025-07-10", "time": "09:15 AM", "doctor": "Dr. Smith"},
]

@app.get("/patients")
def get_patients():
    return {"patients": patients}

@app.get("/patients/{patient_id}")
def get_patient_by_id(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return {"error": "Patient not found"}

@app.get("/appointments")
def get_appointments():
    return {"appointments": appointments}