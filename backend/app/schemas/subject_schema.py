from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from ..models.subject import Subject

class SubjectSchema(SQLAlchemySchema):
    class Meta:
        model = Subject
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)
    name = auto_field(required=True)
    description = auto_field()
    area = auto_field()
