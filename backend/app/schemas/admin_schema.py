from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from ..models.admin import Admin

class AdminSchema(SQLAlchemySchema):
    class Meta:
        model = Admin
        load_instance = True
        include_fk = True

    id = auto_field()
    email = auto_field()
    name = auto_field()
    rut = auto_field()
    age = auto_field()
    accepted_terms = auto_field()
