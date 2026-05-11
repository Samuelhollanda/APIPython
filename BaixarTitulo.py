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
id_titulo = int(input("Informe o ID do título: "))
nova_situacao = input("Informe a nova situação (ex: Pago, Cancelado, Pendente): ")
novo_valor = float(input("Informe o novo valor do Título: "))
sql_update = """
UPDATE TB_TITULOS
SET SituacaoTitulo = %s
valortitulo = %s
WHERE IDTitulo = %s
"""
cursor.execute(sql_update, (nova_situacao, novo_valor, id_titulo))
conn.commit()
sql = "SELECT * FROM LOG_TITULO WHERE IDTitulo = %s"
cursor.execute(sql, (id_titulo,))
print(f"\nTítulos com situação: {nova_situacao}")
for row in cursor.fetchall():
    print(row)
conn.commit()
print(" Log inserido com sucesso!")
cursor.close()
conn.close()
print("\nConexão encerrada com sucesso.")