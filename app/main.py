from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates   
from fastapi.responses import RedirectResponse
from typing import Optional
app = FastAPI()

templates = Jinja2Templates(directory="templates")

student_records = []
next_student_id = 1
@app.get("/")
def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )

@app.get("/about")
def about_page(request: Request):
    # print("ABOUT ROUTE CALLED SUCCESSFULLY")
    
    # This explicit layout bypasses the internal Starlette 1.0 mapping bug entirely
    return templates.TemplateResponse(
        request=request, 
        name="about.html", 
        context={}
    )

@app.get("/students/add")
def add_student_page(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="add_students.html",
        context={}
    )

@app.post("/students/add")
def add_student(name: str= Form(...),
                    roll_no: str=Form(...),
                    phone: str=Form(...),
                    email: str=Form(...),
                    age: int=Form(...),
                    course: str=Form(...),
                    address: str=Form(...)
):
    global next_student_id
    student = {
        "id": next_student_id,
        "name":name,
        "roll_no":roll_no,
        "phone":phone,
        "email":email,
        "age":age,
        "course":course,
        "address":address
        }

    student_records.append(student)
    next_student_id +=1

    return RedirectResponse(
        url="/students",
        status_code=303
    )

@app.get("/students")
def view_all_students(request:Request, search: Optional[str]=None):
    filtered_students = []
    if search:
        for student in student_records:
            if search.lower() in student['name'].lower():
                filtered_students.append(student)
    else:
        filtered_students = student_records

    return templates.TemplateResponse(
        request= request,
        name= 'students.html',
        context={"student_records": filtered_students}
    )


@app.get("/students/edit/{student_id}")
def edit_student(request:Request, student_id: int):
    for student in student_records:
        if student["id"] == student_id:
            return templates.TemplateResponse(
                request=request,
                name='edit_student.html',
                context={"student": student}
            )
    return {"message": "student not found"}


@app.post("/students/edit/{student_id}")
def update_student(student_id: int,
                    name: str = Form(...),
                    roll_no: str = Form(...),
                    phone: str = Form(...),
                    email: str = Form(...),
                    age: int = Form(...),
                    course: str = Form(...),
                    address: str = Form(...)
                ):

    for student in student_records:
        if student['id'] == student_id:
            student["name"] = name
            student["roll_no"] = roll_no
            student["phone"] = phone
            student["email"] = email
            student["age"] = age
            student["course"] = course
            student["address"] = address
            break

    return RedirectResponse(
        url="/students",
        status_code=303
    )


@app.get("/students/delete/{student_id}")
def delete_student(student_id:int):
    for student in student_records:
        if student['id']== student_id:
            student_records.remove(student)
            break
    return RedirectResponse(
        url="/students",
        status_code=303

    )