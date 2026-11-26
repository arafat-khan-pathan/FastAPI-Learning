# from fastapi import FastAPI

# app = FastAPI()

# students = {
#     "S001": {"name": "Ravi", "marks": 85, "grade": "A"},        #error codes 
#     "S002": {"name": "Priya", "marks": 72, "grade": "B"},
#     "S003": {"name": "Arjun", "marks": 91, "grade": "A+"},
# }



# @app.get("/student/{student_id}")    #invalid id  give error and crush 
# def get_student(student_id: str):
#     return students[student_id]


from fastapi import FastAPI, HTTPException  

# HTTPException  
# raise HTTPException(status_code=404, detail="Student not found")

app = FastAPI()

students = {
    "S001": {"name": "Ravi", "marks": 85, "grade": "A"},
    "S002": {"name": "Priya", "marks": 72, "grade": "B"},
    "S003": {"name": "Arjun", "marks": 91, "grade": "A+"},
}

@app.get("/student/{student_id}")
def get_student(student_id: str):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail=f"student with ID {student_id} does not exists",
        )

    return students[student_id]


# matched = next(
#     (info for sid, info in students.items() if info["name"].lower() == student_name.lower()),
#     None,
# )
# if matched is None:
#     raise HTTPException(status_code=404, detail=f"Student '{student_name}' not found")
# return matched


