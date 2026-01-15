from fastapi import FastAPI

from pydantic import BaseModel


app =FastAPI()

class student(BaseModel):
    name: str
    age: int
    grade: str
    id:int

MockDB=[{
  "name": "praba",
  "age": 20,
  "grade": "b+",
  "id": 2
},{
  "name": "karan",
  "age": 20,
  "grade": "b+",
  "id": 1
},{
  "name": "kamal",
  "age": 16,
  "grade": "c+",
  "id": 4
},{
  "name": "thaya",
  "age": 21,
  "grade": "d+",
  "id": 3
}]
@app.post("/addstuden/")
async def newstn(new:student):
    MockDB.append(new.dict())
    return {'msg':"new stutend add succ","newstutand":new}
@app.get("/student/{studen_id}")
async def list_of_stn(studen_id:int):
    var=0
    for s in MockDB:
        if  s["id"]==studen_id:
            return s
   
    return{"msg":"student not fond"}
@app.get("/student/fliter")
async def fliter(find_stn:str):
    if find_stn:
        result = [s for s in MockDB if s["grade"] == find_stn]
        return result
    
    return {"status": "error", "message": "Student not found"}

