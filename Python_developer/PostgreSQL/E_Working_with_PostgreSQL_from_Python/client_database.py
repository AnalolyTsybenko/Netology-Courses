import os


def create_database(name, user):
    os.system(f'createdb -U {user} {name}')
    print(f'- Database "{name}" created')


def create_table(connection, cursor, name_table, **table_columns):
    cursor.execute(f"""
        DROP TABLE IF EXISTS {name_table} CASCADE;
        """)
    connection.commit()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {name_table}(
            {name_table}_id SERIAL PRIMARY KEY);
        """)
    connection.commit()
    for name_column, type_column in table_columns.items():
        cursor.execute(f"""
            ALTER TABLE {name_table}
            ADD COLUMN {name_column} {type_column}
            """)
        connection.commit()
    print(f'- Table "{name_table}" created')


def add_client(connection, cursor, name_table, **values):
    cursor.execute(f"""
        INSERT INTO {name_table}(
            {', '.join(key for key in values.keys())})
        VALUES(
            {', '.join(item for item in values.values())})
        RETURNING first_name, last_name, {name_table}_id;
        """)
    connection.commit()
    result = cursor.fetchone()
    print(f'- Client "{result[0]} {result[1]}" added "id = {result[2]}"')


def add_phone(connection, cursor, name_table, client_id, phone):
    cursor.execute(f"""
        INSERT INTO {name_table}(
            client_id, phone)
        VALUES(
            {client_id}, '{phone}')
        RETURNING phone;
        """)
    connection.commit()
    cursor.execute(f"""
        SELECT first_name, last_name, phone 
        FROM {name_table}
        JOIN client USING(client_id);
        """)
    result = cursor.fetchone()
    print(f'- Phone "{result[2]}" added for client "{result[0]} {result[1]}"')


def change_client(connection, cursor, name_table, client_id, **values):
    for key, value in values.items():
        cursor.execute(f"""
            UPDATE {name_table}
            SET {key} = {value}
            WHERE client_id =%s;
            """, (client_id,))
        connection.commit()
    cursor.execute(f"""
        SELECT * FROM {name_table}
        WHERE client_id =%s;
        """, (client_id,))
    result = cursor.fetchone()
    print(f'- Client update "{result[1]} {result[2]}", "id = {result[0]}"')


def delete_phone(connection, cursor, name_table, client_id, phone):
    cursor.execute(f"""
        DELETE FROM {name_table}
        WHERE client_id =%s AND phone =%s;
        """, (client_id, phone,))
    connection.commit()
    print(f'- Phone "{phone[1:-1]}" delete')


def delete_client(connection, cursor, name_table, client_id):
    cursor.execute(f"""
        DELETE FROM {name_table}
        WHERE client_id =%s;
        """, (client_id,))
    connection.commit()
    print(f'- Client "id = {client_id}" delete')


def find_client(cursor, **values):
    for key, value in values.items():
        cursor.execute(f"""
            SELECT client_id, first_name, last_name, email, phone
            FROM client
            JOIN phone USING(client_id)
            WHERE {key} = '{value}'
            """)
        result = cursor.fetchall()
        if result:
            print(f'- Result "{result[0][1]} {result[0][2]} {result[0][3]}", '
                  f'"id = {result[0][0]}"')
        else:
            print(f'- Result "client not found"')
