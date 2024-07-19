from httpx import AsyncClient


async def test_add_student(ac: AsyncClient):
    response = await ac.post("/student", json={
        "id_student": 0,
        "name_student": "Juan",
        "surname_student": "Perez",
        "age_student": "30",
        'email_student': "hacas@dsndm",
        'phone_student': "1234567890",
        'family_discount': 0.1
    })

    assert response.status_code == 201


async def test_consult_student(ac: AsyncClient):
        # Add a student first to ensure there's data
    await ac.post("/student", json={
        "id_student": 1,
        "name_student": "Maria",
        "surname_student": "Lopez",
        "age_student": "25",
        'email_student': "maria@correo.com",
        'phone_student': "0987654321",
        'family_discount': 0.1
    })

    response = await ac.get("/student")
    assert response.status_code == 200
    students = response.json()
    assert isinstance(students, list)
    assert len(students) > 0


async def test_consult_student_id(ac: AsyncClient):
        # Add a student first to ensure there's data

    response = await ac.get("/student/2")
    assert response.status_code == 200
    student = response.json()
    assert student["id_student"] == 2
    assert student["name_student"] == "Jane"
    assert student["surname_student"] == "Smith"
    assert student["age_student"] == "21"
    assert student["email_student"] == "jane.smith@example.com"
    assert student["phone_student"] == "234-567"
    assert student["family_discount"] == 0