def predict(data):
    return {
        "diagnosis": "Likely Healthy",
        "confidence": 0.85,
        "input_summary": f"{data.name}, age {data.age}, reported symptom: {data.symptom}"
    }