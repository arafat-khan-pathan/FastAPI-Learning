from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

class LoadApplication(BaseModel):
    age: int
    income: float
    load_amount: float
    employeement_years: int
    
@app.get("/")
def printHello():
    return "hi how are you"

@app.post("/predict")
def predict_load(application: LoadApplication):
    if application.income < 100000 and application.employeement_years > 5:
        decision = "Approve"
    else:
        decision = "Reject"
    return {
        "application_age": application.age,
        "application_income": application.income,
        "application_load_amount": application.load_amount,
        "application_employeement_years": application.employeement_years,
        "prediction": decision
        }