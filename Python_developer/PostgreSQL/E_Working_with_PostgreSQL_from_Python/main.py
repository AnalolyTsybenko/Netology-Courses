import psycopg2
import config as cg
from client_database import *

DATABASE_NAME = 'clientdb'
CLIENT = ['Lee', 'Jae Young', '1@samsung.com', '88005555555']

if __name__ == '__main__':
    create_database(DATABASE_NAME, cg.USER)
    conn = psycopg2.connect(dbname=DATABASE_NAME, user=cg.USER, password=cg.PASSWORD, host=cg.HOST, port=cg.PORT)
    with conn:
        with conn.cursor() as cur:
            create_table(conn, cur, 'client', first_name='VARCHAR(20)', last_name='VARCHAR(20)', email='VARCHAR(50)')
            create_table(conn, cur, 'phone', client_id='INTEGER REFERENCES client(client_id)', phone='VARCHAR(20)')
            add_client(conn, cur, 'client', first_name=f"'{CLIENT[0]}'", last_name=f"'{CLIENT[1]}'", email=f"'{CLIENT[2]}'")
            add_phone(conn, cur, 'phone', 1, f'{CLIENT[3]}')
            change_client(conn, cur, 'client', 1, first_name="'Lee'", last_name="'Byung-chul'")
            delete_phone(conn, cur, 'phone', 1, '88005555555')
            delete_client(conn, cur, 'client', 1)
            find_client(cur,  first_name='Lee')
