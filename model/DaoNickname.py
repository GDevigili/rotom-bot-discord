import sqlite3

class DaoNickname:


    def __init__(self, db_file):
        conn = None

        try:
            conn = sqlite3.connect(db_file)
            print("Conexão bem sucedida")

        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

        def insert(self, nickname):
            conn = None

            try:
                conn = sqlite3.connect(db_file)
                print("Conexão bem sucedida")
            except sqlite3.Error as e:
                print(e)
            finally:
                if conn:
                    conn.close()