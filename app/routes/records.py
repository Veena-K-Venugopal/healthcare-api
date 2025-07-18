from fastapi import APIRouter

router = APIRouter()

# Simulated in-memory data
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

medications = [
    {"id": 1, "patient_id": 1, "name": "Atorvastatin", "dose": "10mg", "frequency": "Once daily"},
    {"id": 2, "patient_id": 2, "name": "Metformin", "dose": "500mg", "frequency": "Twice daily"},
    {"id": 3, "patient_id": 1, "name": "Albuterol", "dose": "2 puffs", "frequency": "As needed"},
]

# Patients
@router.get("/patients")
def get_patients():
    return {"patients": patients}

@router.get("/patients/{patient_id}")
def get_patient_by_id(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return {"error": "Patient not found"}

# Appointments
@router.get("/appointments")
def get_appointments():
    return {"appointments": appointments}

@router.get("/appointments/{appointment_id}")
def get_appointment_by_id(appointment_id: int):
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            return appointment
    return {"error": "Appointment not found"}

# Medications
@router.get("/medications")
def get_medications():
    return {"medications": medications}

@router.get("/medications/{medication_id}")
def get_medication_by_id(medication_id: int):
    for medication in medications:
        if medication["id"] == medication_id:
            return medication
    return {"error": "Medication not found"}
