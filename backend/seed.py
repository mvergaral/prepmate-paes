from app import create_app, db
from app.models import Subject, Exercise, Student, Admin


def seed_data():
    app = create_app()
    with app.app_context():
        db.create_all()
        if not Subject.query.first():
            subjects = [
                Subject(name="Matemática M1", description="Matemáticas", area="Mathematics"),
                Subject(name="Ciencias", description="Área de ciencias", area="Science"),
                Subject(name="Competencia Lectora", description="Lectura", area="Language"),
            ]
            db.session.add_all(subjects)
            db.session.commit()
        else:
            subjects = Subject.query.all()

        if not Exercise.query.first():
            ex_list = [
                Exercise(
                    title="¿Cuánto es 1+1?",
                    description="Suma simple",
                    options={"A": "1", "B": "2", "C": "3", "D": "4"},
                    correct_answer="B",
                    subject_id=subjects[0].id,
                    difficulty="easy",
                    tags="aritmetica",
                ),
                Exercise(
                    title="¿Cuál es la capital de Francia?",
                    description="Pregunta de geografía",
                    options={"A": "Madrid", "B": "Paris", "C": "Roma", "D": "Lisboa"},
                    correct_answer="B",
                    subject_id=subjects[1].id,
                    difficulty="easy",
                    tags="geografia",
                ),
            ]
            db.session.add_all(ex_list)
            db.session.commit()

        if not Student.query.first():
            s = Student(email="student@example.com", role="student", name="Estudiante", rut="1-9", age=18)
            s.set_password("1234")
            db.session.add(s)
        if not Admin.query.first():
            a = Admin(email="admin@example.com", role="admin", name="Admin", rut="2-7", age=30, accepted_terms=True)
            a.set_password("admin")
            db.session.add(a)
        db.session.commit()

        print("Datos de prueba creados")


if __name__ == "__main__":
    seed_data()
