from app import create_app, db
from app.models import Subject, Exercise, Student, Admin

EXERCISE_DATA = [
    {
        "subject": "Matemática M1",
        "level": "fácil",
        "question": "¿Cuál es el resultado de 25 + 36?",
        "options": ["51", "61", "71", "81"],
        "correct": "61",
        "explanation": "25 + 36 = 61",
    },
    {
        "subject": "Matemática M1",
        "level": "fácil",
        "question": "¿Cuál es el doble de 8?",
        "options": ["14", "16", "18", "20"],
        "correct": "16",
        "explanation": "El doble de 8 es 16",
    },
    {
        "subject": "Matemática M1",
        "level": "media",
        "question": "¿Cuál es el valor de x en la ecuación 3x - 7 = 11?",
        "options": ["2", "4", "6", "8"],
        "correct": "6",
        "explanation": "3x - 7 = 11 → 3x = 18 → x = 6",
    },
    {
        "subject": "Matemática M1",
        "level": "difícil",
        "question": "¿Cuál es el dominio de la función f(x) = √(x - 2)?",
        "options": ["x ≥ 2", "x > 0", "x ≠ 2", "x < 2"],
        "correct": "x ≥ 2",
        "explanation": "La raíz cuadrada solo está definida para x - 2 ≥ 0 → x ≥ 2",
    },
    {
        "subject": "Matemática M2",
        "level": "fácil",
        "question": "¿Cuál es la derivada de f(x) = x²?",
        "options": ["x", "2x", "x²", "2"],
        "correct": "2x",
        "explanation": "La derivada de x² es 2x",
    },
    {
        "subject": "Matemática M2",
        "level": "media",
        "question": "Calcula el límite de f(x) = (2x² - 3)/(x² + 1) cuando x → ∞",
        "options": ["2", "0", "1", "Infinito"],
        "correct": "2",
        "explanation": "Dividiendo numerador y denominador por x², el límite es 2",
    },
    {
        "subject": "Matemática M2",
        "level": "difícil",
        "question": "¿La serie ∑ (1/n²) converge o diverge?",
        "options": ["Converge", "Diverge", "No se puede determinar", "Es alternante"],
        "correct": "Converge",
        "explanation": "Es una serie p con p > 1, por lo tanto converge",
    },
    {
        "subject": "Competencia Lectora",
        "level": "fácil",
        "question": "Según el texto, ¿cuál es la idea principal del párrafo 2?",
        "options": ["A", "B", "C", "D"],
        "correct": "B",
        "explanation": "El texto menciona explícitamente la idea en la línea 3 del párrafo",
    },
    {
        "subject": "Competencia Lectora",
        "level": "media",
        "question": "¿Cuál es la intención del autor al citar a un experto?",
        "options": ["Apoyar su argumento", "Contradecirlo", "Introducir un tema", "Desviar la atención"],
        "correct": "Apoyar su argumento",
        "explanation": "Usa la cita para respaldar su postura",
    },
    {
        "subject": "Competencia Lectora",
        "level": "difícil",
        "question": "¿Cuál de las siguientes afirmaciones es una inferencia válida del texto?",
        "options": ["A", "B", "C", "D"],
        "correct": "C",
        "explanation": "La inferencia se deduce del contexto del último párrafo",
    },
    {
        "subject": "Historia y Ciencias Sociales",
        "level": "fácil",
        "question": "¿En qué año ocurrió la Independencia de Chile?",
        "options": ["1810", "1818", "1833", "1821"],
        "correct": "1818",
        "explanation": "La independencia oficial se declaró en 1818",
    },
    {
        "subject": "Historia y Ciencias Sociales",
        "level": "media",
        "question": "¿Qué consecuencia tuvo el golpe de Estado de 1973?",
        "options": ["Democracia inmediata", "Dictadura militar", "Guerra civil", "Reforma agraria"],
        "correct": "Dictadura militar",
        "explanation": "El golpe instauró una dictadura que duró hasta 1990",
    },
    {
        "subject": "Historia y Ciencias Sociales",
        "level": "difícil",
        "question": "Analiza las implicancias sociales de la Constitución de 1980.",
        "options": ["A", "B", "C", "D"],
        "correct": "A",
        "explanation": "Establece el marco para el modelo neoliberal y restringe la participación política",
    },
    {
        "subject": "Ciencias",
        "level": "fácil",
        "question": "¿Cuál es la función principal del sistema respiratorio?",
        "options": ["Digestión", "Transporte de nutrientes", "Intercambio de gases", "Producción de hormonas"],
        "correct": "Intercambio de gases",
        "explanation": "Permite el ingreso de oxígeno y salida de CO₂",
    },
    {
        "subject": "Ciencias",
        "level": "media",
        "question": "¿Qué diferencia hay entre una reacción endotérmica y exotérmica?",
        "options": ["Temperatura", "Luz", "Absorción o liberación de calor", "Color"],
        "correct": "Absorción o liberación de calor",
        "explanation": "Endotérmica absorbe calor, exotérmica lo libera",
    },
    {
        "subject": "Ciencias",
        "level": "difícil",
        "question": "Explica el principio de conservación de la energía en un circuito cerrado.",
        "options": ["A", "B", "C", "D"],
        "correct": "B",
        "explanation": "La energía total se conserva: la suma de energías es constante",
    },
]


def seed_data():
    app = create_app()
    with app.app_context():
        db.create_all()
        if not Subject.query.first():
            unique_subjects = {ex["subject"] for ex in EXERCISE_DATA}
            subjects = []
            for name in unique_subjects:
                subjects.append(
                    Subject(
                        name=name,
                        description=name,
                        area=name.split()[0]
                    )
                )
            db.session.add_all(subjects)
            db.session.commit()
        else:
            subjects = Subject.query.all()

        if not Exercise.query.first():
            letters = ["A", "B", "C", "D"]
            subject_map = {s.name: s.id for s in subjects}
            ex_list = []
            for ex in EXERCISE_DATA:
                if ex["subject"] not in subject_map:
                    subj = Subject(name=ex["subject"], description=ex["subject"], area=ex["subject"].split()[0])
                    db.session.add(subj)
                    db.session.commit()
                    subject_map[subj.name] = subj.id
                options = {letters[i]: opt for i, opt in enumerate(ex["options"])}
                correct_letter = letters[ex["options"].index(ex["correct"])]
                ex_list.append(
                    Exercise(
                        title=ex["question"],
                        description=ex.get("explanation", ""),
                        options=options,
                        correct_answer=correct_letter,
                        subject_id=subject_map[ex["subject"]],
                        difficulty=ex.get("level"),
                        tags="",
                    )
                )
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
