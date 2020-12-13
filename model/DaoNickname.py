import sqlite3


class DaoNickname:

    def __init__(self, db_file=r"databases/db_nicknames.db."):
        conn = None
        self.db_file = db_file

        try:
            conn = sqlite3.connect(db_file)
            print("Conexão bem sucedida")
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

    # This function is only useful when creating a new database, so I have commented it
    '''
    def create_table(self):
        conn = None

        try:
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS nicknames(
                            id INTEGER PRIMARY KEY,
                            discord_nick TEXT, 
                            game_nick TEXT
                        );
                        """)

            self.close(conn)
            print("tabela criada com sucesso")

            return 1
        except sqlite3.Error as e:
            print(e)
            self.close(conn)
            return 0
    '''

    def select_all(self):
        conn = None

        try:
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()

            cur.execute("SELECT * FROM nicknames;")

            select = cur.fetchall()
            self.close(conn)

            return select

        except sqlite3.Error as e:
            print(e)
            self.close(conn)

            return None

    def insert(self, discord_nick, game_nick):
        conn = None

        try:
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()

            cur.execute(f"""INSERT INTO nicknames (
                                discord_nick,
                                game_nick
                            ) 
                            VALUES (
                                '{discord_nick}',
                                '{game_nick}'
                            );
                        """)
            conn.commit()

            conn.close()

            return 1
        except sqlite3.Error as e:
            print(e)
            return 0
        finally:
            if conn:
                conn.close()

    def select_nickname(self, discord_nick):
        conn = None

        try:
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()

            cur.execute(f"""SELECT game_nick 
                        FROM nicknames 
                        WHERE discord_nick = '{discord_nick}'
                        ORDER BY id DESC
                        LIMIT 1;""")

            select = cur.fetchall()
            self.close(conn)

            return select
        except sqlite3.Error as e:
            print(e)
            self.close(conn)
            return 0

    @staticmethod
    def close(conn):
        if conn:
            conn.close()


if __name__ == '__main__':
    c = DaoNickname()
    print(c.select_all())
    print("--------")
    print(c.select_nickname("Giraffes are Fake#5632"))
