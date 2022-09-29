from application.current_date import *
from application.db.createdb.models_main import *
from application.db.people import *
from application.salary import *
from application.db.createdb import config as cg

print(get_today())
print(create_db(cg))
print(get_employees())
print(calculate_salary())
