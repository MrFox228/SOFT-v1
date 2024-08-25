from .connection import get_db_connection

def get_user_by_username(username: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def insert_user(username: str, password: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    connection.commit()
    cursor.close()
    connection.close()
