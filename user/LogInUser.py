import database.DatabaseConfig as dbConfig


def logInUser(user_email, user_password):
    connection = dbConfig.create_db_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM public.users WHERE email = '{user_email}'"
    cursor.execute(query)

    # Fetch the results
    existing_user = cursor.fetchone()
    print('---------&s7s7s7s7s77s')
    print(existing_user)

    if existing_user and existing_user[2] == user_email and existing_user[
        3] == user_password:  # Assuming email is at index 1 and password is at index 3
        return True
    else:
        return False

