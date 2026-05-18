import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

df = pd.read_excel('titulos.xlsx')
df.columns = df.columns.str.strip().str.lower()

conn = mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DATABASE')
)

cursor = conn.cursor()

for _, row in df.iterrows():
    sql = """
        INSERT INTO TB_TITULOS
        (IDTitulo, Descricao, DataTitulo, DataVencimento, IDCliente, Naturezatitulo, ValorTitulo, SituacaoTitulo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        row['idtitulo'],
        row['descricao'],
        row['datatitulo'],
        row['datavencimento'],
        row['idcliente'],
        row['naturezatitulo'],
        row['valortitulo'],
        row['situacaotitulo']
    )
    cursor.execute(sql, values)

conn.commit()
cursor.close()
conn.close()
