from application.current_date import get_today
from application.db.createdb.models_main import create_db
from application.db.people import get_employees
from application.salary import calculate_salary
from application.db.createdb import config as cg

if __name__ == '__main__':
    print(get_today())
    print(create_db(cg))
    print(get_employees())
    print(calculate_salary())
