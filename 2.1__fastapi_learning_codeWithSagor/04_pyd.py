from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

#this is input schema
class LoadApplication(BaseModel):
    name:str
    age: int
    income: float
    load_amount: float
    employeement_years: int
    
    
    
@app.post("/predict")
def predict_loan(application: LoadApplication):
    approved = (
        application.income > 50000
        and application.employeement_years > 2
        and application.age >= 21
    )

    return {
        "applicant name": application.name,
        "loan_amount": application.loan_amount,
        "decision": "approved" if approved else "rejected",
        "reviewe_income": application.income,
    }
