import sqlite3

class Database:

    def configurar_base_dados(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS utilizadores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
        )
                       """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tempos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tempo FLOAT
        )
                       """)
        conn.commit()
        conn.close()

    def insert_utilizadores(self, username, password):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO utilizadores(username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()

    def ver_dados(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, username, password FROM utilizadores")
        dados_puros = cursor.fetchall()

        conn.close()
        return dados_puros
    def existe_utilizadores(self, username):
        if username2 in self.ver_dados():
            print("O utilizador já existe, tente outro nome.")
        elif username not in self.ver_dados():
            print("O utlizador foi criado")