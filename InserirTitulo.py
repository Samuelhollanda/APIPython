import mysql.connector
import os
from dotenv import load_dotenv

def inserir_titulo():
    
    load_dotenv()
    
    try:
        conn = mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
        )
        
        cursor = conn.cursor()
        descricao = input("Informe a descrição do título: ")
        data_titulo = input('Digite a data do titulo (AAA-MM-DD): ')
        data_venc = input('Data de vencimento (AAA-MM-DD): ')
        id_cliente = int(input('Código do cliente (ID): '))
        natureza = input('Natureza do título: ')
        valor = float(input('Digite o valor do título: '))
        situacao = input('Situação do título: ').upper()
        
        sql="""
            INSERT INTO TB_TITULOS
            (Descricao, DataTitulo, DataVencimento, IDCliente, NaturezaTitulo, ValorTitulo, SituacaoTitulo)
            VALUES(%s,%s,%s,%s,%s,%s,%s)
        """
        valores = (descricao, data_titulo, data_venc, id_cliente, natureza, valor, situacao)
        cursor.execute(sql, valores)
        conn.commit()
        print("\n Título inserido com sucesso!")
    except mysql.connector.Error as err:
        print(f'\n Erro no banco de Dados: {err}')
    except ValueError:
        print('\n Erro: Certifique-se de digitar números válidos para ID e Valor. ')
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
        inserir_titulo()

