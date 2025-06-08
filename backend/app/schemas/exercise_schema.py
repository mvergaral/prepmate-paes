from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from ..models.exercise import Exercise

class ExerciseSchema(SQLAlchemySchema):
    class Meta:
        model = Exercise
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)
    title = auto_field(required=True)
    description = auto_field()
    options = auto_field(required=True)
    correct_answer = auto_field(required=True)
    subject_id = auto_field(required=True)
    difficulty = auto_field()
    tags = auto_field()
    created_at = auto_field(dump_only=True)
