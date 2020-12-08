import sqlite3


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(f"Conexão bem sucedida\nversão: {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"..\databases\db_nicknames.db")

# Tutorial: https://www.sqlitetutorial.net/sqlite-python/creating-database/
