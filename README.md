# Student Management System

A simple Student Management System built using **FastAPI**, **HTML**, and **Jinja2 Templates**. This project allows users to manage student records through a web interface without using a database.

## Features

- Add a new student
- View all students
- Edit student details
- Delete a student
- Search students by name
- Simple HTML forms with FastAPI
- Server-side rendering using Jinja2 templates

## Technologies Used

- Python
- FastAPI
- Jinja2 Templates
- HTML
- Uvicorn

## Project Structure

```
student-management-system/
│
├── app/
│   └── main.py
│
├── templates/
│   ├── home.html
│   ├── about.html
│   ├── add_students.html
│   ├── students.html
│   └── edit_student.html
│
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management-system.git
```

### 2. Open the project

```bash
cd student-management-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

## Available Pages

| Route | Description |
|-------|-------------|
| `/` | Home Page |
| `/about` | About Page |
| `/students/add` | Add Student |
| `/students` | View Students |
| `/students/edit/{student_id}` | Edit Student |
| `/students/delete/{student_id}` | Delete Student |

## Future Improvements

- Add CSS styling
- Store data in SQLite
- Add