import sqlite3
from datetime import date


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

        # Uma linha por cada intervenção (cada vez que se carrega em "Parar" numa linha da tabela)
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS intervencoes(
                                                                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                  user_id INTEGER NOT NULL,
                                                                  partido TEXT NOT NULL,
                                                                  data TEXT NOT NULL,
                                                                  duracao REAL NOT NULL,
                                                                  FOREIGN KEY (user_id) REFERENCES utilizadores(id)
                           )
                       """)

        conn.commit()
        conn.close()

    # ---------------- Utilizadores ----------------

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

    def verificar_login(self, username, password):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM utilizadores WHERE username = ? AND password = ?",
            (username, password)
        )
        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None

    def obter_id_utilizador(self, username):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM utilizadores WHERE username = ?",
            (username,)
        )
        resultado = cursor.fetchone()
        conn.close()
        return resultado[0] if resultado else None

    # ---------------- Intervenções ----------------

    def inserir_intervencao(self, user_id, partido, duracao):
        """Grava uma intervenção individual (duracao em segundos)."""
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO intervencoes(user_id, partido, data, duracao) VALUES (?, ?, ?, ?)",
            (user_id, partido, date.today().isoformat(), duracao)
        )
        conn.commit()
        conn.close()

    def obter_historico(self, user_id):
        """Todas as intervenções guardadas, mais recentes primeiro."""
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT data, partido, duracao FROM intervencoes "
            "WHERE user_id = ? ORDER BY data DESC, id DESC",
            (user_id,)
        )
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    def obter_totais_por_partido(self, user_id):
        """Soma da duração e nº de intervenções, agrupado por partido."""
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT partido, SUM(duracao), COUNT(*) FROM intervencoes "
            "WHERE user_id = ? GROUP BY partido ORDER BY SUM(duracao) DESC",
            (user_id,)
        )
        resultado = cursor.fetchall()
        conn.close()
        return resultado
