from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from ..models.student import Student

class StudentSchema(SQLAlchemySchema):
    class Meta:
        model = Student
        load_instance = True
        include_fk = True

    id = auto_field()
    name = auto_field()
    email = auto_field()
    rut = auto_field()
    age = auto_field()
    accepted_terms = auto_field()
