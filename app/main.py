from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.records import router as records_router
from app.routes.prediction import router as prediction_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(records_router)
app.include_router(prediction_router)

@app.get("/")
def read_root():
    return {"message": "Healthcare API Enhancer - Mock Version"}