from fastapi import FastAPI,Path
from pydantic import BaseModel, Field


app=FastAPI()



class student(BaseModel):
    name :str =Field(...,title="name",max_length=40)
    Class: str =Field(...,title="class",max_length=10)


class subject(student):
    tamil:int =Field(...,title="tamil",ge=0,le=100)
    english:int =Field(...,title="english",ge=0,le=100)
    maths:int =Field(...,title="maths",ge=0,le=100)
    science:int =Field(...,title="science",ge=0,le=100)
    social:int =Field(...,title="social",ge=0,le=100)



@app.get("/")
async def root():
    return{"msg":"Welcome to Grade Checker API"}






mddb:list[subject]=[]

@app.get("/check-grade/{marks}")

async def check_grade(marks: subject=Path(...,title="marks",ge=0,le=100)):
    TotalMarks=marks.tamil+marks.english+marks.maths+marks.science+marks.social
    Percentage=(TotalMarks/500)*100
    if Percentage>=90:
        grade="A+"
    elif Percentage>=80:
        grade="A"
    elif Percentage>=70:
        grade="B+"
    elif Percentage>=60:
        grade="B"
    elif Percentage>=50:
        grade="C"
    elif Percentage>=40:
        grade="D"
    else:
        grade="F"
    return{"msg":f"Total Marks: {TotalMarks} Percentage: {Percentage} Grade: {grade}"}