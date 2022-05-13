import psycopg2
from psycopg2._psycopg import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DataBaseService:
    def __init__(self):
        self.create_table()

    def create_table(self):
        execute("CREATE TABLE IF NOT EXISTS tasks (title text, deadline date, status boolean)")

    def insert_value(self, word, deadline, status):
        execute(f"""INSERT INTO tasks VALUES {word, str(deadline), status}""")

    def delete_one(self, value, date):
        delete_one_query = f"""DELETE FROM tasks WHERE (title='{value}') AND (deadline = '{date}')"""
        execute(delete_one_query)

    def delete_all(self):
        execute("DELETE FROM tasks")

    def update_value(self, value, date, status):
        execute(f"UPDATE tasks SET status={status} WHERE (title='{value}') AND (deadline = '{date}')")

    def select_value(self, word):
        connection = create_connection()
        cur = connection.cursor()
        cur.execute(f"SELECT * FROM tasks ORDER BY {word}")
        return cur.fetchall()


def create_connection():
    return psycopg2.connect(
        user="postgres",
        password="qweqwe",
        host="127.0.0.1",
        port="5432",
        database="todolist"
    )


def execute(query):
    conn = create_connection()
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    try:
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.close()
    except Error as e:
        print(e)
