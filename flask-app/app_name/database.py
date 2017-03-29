from flask_sqlalchemy import SQLAlchemy
from flask_security.utils import encrypt_password

db = SQLAlchemy()

import app_name.auth as auth

def init_db(app, drop_all=True):
    with app.app_context():
        try:
            if drop_all:
                db.drop_all()
            db.create_all()
            user_role = auth.models.Role(name='user')
            db.session.add(user_role)
            db.session.commit()

            # Add Users
            test_user = auth.user_datastore.create_user(
                first_name='Admin',
                email='admin',
                password=encrypt_password('admin'),
                roles=[user_role]
            )

            db.session.commit()
            print("created db")

        except Exception as ex:
            print("db already exists")
