import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


conn = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE")
    )

cursor = conn.cursor()

situacao = input("Digite a Situação do Título para filtrar: ")

sql = "SELECT * FROM TB_TITULOS WHERE SituacaoTitulo = %s"

cursor.execute(sql, (situacao,))

print(f"\nTítulos com situação: {situacao}")

for row in cursor.fetchall():
    print(row)
    
cursor.close()

conn.close()
