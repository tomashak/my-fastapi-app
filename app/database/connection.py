import mysql.connector
from mysql.connector import Error
from fastapi import HTTPException

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="testlab2.tesena.com",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        return connection
    except Error as e:
        raise HTTPException(status_code=500, detail="Failed to connect to database")

def execute_query(query, params=None):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail="Failed to execute query")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()