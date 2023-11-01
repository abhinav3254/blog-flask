import database.DatabaseConfig as dbConfig
import classes.User as User



def signUpUser(user):
    email = user.email
    password = user.password
    role = user.role
    status = user.status

    print('user email ' + email + ' password = ' + password + ' role is ' + role)
    connection = dbConfig.create_db_connection()
    cursor = connection.cursor()

    create_table_query = '''
            CREATE TABLE IF NOT EXISTS USERS (
                id SERIAL PRIMARY KEY,
                name VARCHAR(200) NOT NULL,
                email VARCHAR(200) NOT NULL,
                password VARCHAR(200) NOT NULL,
                role VARCHAR(20) NOT NULL,
                status BOOLEAN NOT NULL
            );
        '''
    cursor.execute(create_table_query)

    if checkExistingUser(email, cursor):
        insert_values_query = f'''
                INSERT INTO USERS (name, email, password, role, status) VALUES (
                    '{user.name}', '{user.email}', '{user.password}', '{user.role}', {user.status}
                );
            '''
        cursor.execute(insert_values_query)
        connection.commit()
        return True
    else:
        cursor.close()
        connection.close()
        return False


def checkExistingUser(email,cursor):
    user_email = email

    # SQL query to check for an existing user based on email
    existing_user_query = f"SELECT * FROM public.users WHERE email = '{user_email}'"

    # Execute the query
    cursor.execute(existing_user_query)

    # Fetch the results
    existing_user = cursor.fetchone()  # Fetch one row, if any

    if existing_user:
        # user found
        return False
    else:
        # no user found
        return True




