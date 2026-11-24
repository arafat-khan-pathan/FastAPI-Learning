from fastapi import FastAPI

app = FastAPI()

Notes = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 1200.0, "in_stock": True},
    {"id": 2, "name": "Notebook", "category": "stationery", "price": 5.5, "in_stock": True},
    {"id": 3, "name": "Headphones", "category": "electronics", "price": 150.0, "in_stock": False},
]


@app.get("/")
def root():  
    return {"message": "Hello World"}

@app.get("/notes")
def get_notes():
    return Notes

@app.get("/notesQuery")
def get_notes(tag: str | None = None):      #/notesQuery?tag=Laptop
    if tag:
        return [note for note in Notes if note["category"] == tag]
    return Notes




@app.get("/terms")
def get_notes(tag: str | None = None):      #/terms?tag=electronics
    result =[]
    for note in Notes:
        if tag and tag not in note["name"]:
            continue        
        result.append(note)
    return result

@app.get("/terms")
def get_notes(tag: str | None = None, q: str | None = None):      #/terms?q=electronics
    result =[]
    for note in Notes:
        if tag and tag not in note["name"]:
            continue        
        if q and q not in note["category"]:
            continue
        result.append(note)
    return result


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in Notes:
        if note["id"] == note_id:
            return note
    return {"message": "Note not found"}







@app.post("/notes")        #@app.post("/notes",status_code=201)
def create_note(note: dict):
    Notes.append(note)
    return {"message": "Note created successfully"}

@app.post("/notes",status_code=201)
def create_note(note: dict):
    new_note = {"id": len(Notes) + 1}    #    new_note = {"id": len(Notes) + 1, **note}
    new_note.update(note)
    Notes.append(new_note)
    return new_note




@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: dict):
    for i, note in enumerate(Notes):
        if note["id"] == note_id:
            Notes[i] = updated_note
            return {"message": "Note updated successfully"}
    return {"message": "Note not found"}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    global Notes
    Notes = [note for note in Notes if note["id"] != note_id]
    return {"message": "Note deleted successfully"}


