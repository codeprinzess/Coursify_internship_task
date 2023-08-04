import mysql.connector
from mysql.connector import Error


def connect():
    try:
        connection = mysql.connector.connect(
            host='your_host',
            database='your_database',
            user='your_user',
            password='your_password'
        )
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print('Error:', e)
        return None


def fetch_jobs():
    connection = connect()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = 'SELECT * FROM jobs'
        cursor.execute(query)
        jobs = cursor.fetchall()
        cursor.close()
        connection.close()
        return jobs


if __name__ == '__main__':
    jobs = fetch_jobs()
    print(jobs)
