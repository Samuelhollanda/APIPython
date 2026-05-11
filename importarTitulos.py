import pandas as pd
import mysql.connector

df = pd.read_excel('titulos.xlsx')
df.columns = df.columns.str.strip().str.lower()

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='#kzp32Mk',  # minha senha do MySQL
    database='db_importDados'  # meu banco de dados
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
