import app_name
from app_name import get_app

app=get_app("init_db")

app_name.database.init_db(app)
