from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from ..models.user import User

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

    id = auto_field()
    email = auto_field()
    role = auto_field()
    is_active = auto_field()
