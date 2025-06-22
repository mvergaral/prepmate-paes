from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from ..models.assignment import Assignment

class AssignmentSchema(SQLAlchemySchema):
    class Meta:
        model = Assignment
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)
    user_id = auto_field(required=True)
    exercise_id = auto_field(required=True)
    respuesta_entregada = auto_field(required=True)
    correcta = auto_field()
    created_at = auto_field(dump_only=True)
