from fastapi import FastAPI

app = FastAPI(
    title="CampusHub API",
    description="A simple University Management API",
    version="1.0"
)

students = [
    {
        "id": 1,
        "name": "Ali",
        "department": "Software Engineering",
        "semester": 7
    },
    {
        "id": 2,
        "name": "Ahmed",
        "department": "Computer Science",
        "semester": 5
    },
    {
        "id": 3,
        "name": "Sara",
        "department": "Artificial Intelligence",
        "semester": 3
    }
]

teachers = [
    {
        "id": 1,
        "name": "Dr. Khan",
        "subject": "Database Systems"
    },
    {
        "id": 2,
        "name": "Prof. Ahmed",
        "subject": "Operating Systems"
    }
]

courses = [
    {
        "id": 1,
        "course": "Web Development"
    },
    {
        "id": 2,
        "course": "Machine Learning"
    },
    {
        "id": 3,
        "course": "Python Programming"
    }
]


@app.get("/")
def home():
    return {
        "message": "Welcome to CampusHub API",
        "status": "Running Successfully"
    }


@app.get("/students")
def get_students():
    return students


@app.get("/teachers")
def get_teachers():
    return teachers


@app.get("/courses")
def get_courses():
    return courses


@app.get("/students/count")
def student_count():
    return {
        "Total Students": len(students)
    }


@app.get("/teachers/count")
def teacher_count():
    return {
        "Total Teachers": len(teachers)
    }


@app.get("/courses/count")
def course_count():
    return {
        "Total Courses": len(courses)
    }