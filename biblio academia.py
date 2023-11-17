import mysql.connector

banco = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="302302",
    database="academia_vinicius"
)

def inserir_registro (tabela, campos, valores):
    cursor = banco.cursor()
    comando = f'INSERT INTO {tabela} ({", ".join(campos)}) VALUES ({", ".join(["%s"] * len(valores))})'
    cursor.execute(comando, valores)
    banco.commit()
    cursor.close()

def visualizar_registros(tabela):
    cursor = banco.cursor()
    pesquisa = f'select * from {tabela};'
    cursor.execute(pesquisa)
    resultados = cursor.fetchall()
    for x in resultados:
        print(x)
    cursor.close()

def atualizar_registro(tabela, campo, valor, condicoes):
    cursor = banco.cursor()
    comando = f'UPDATE {tabela} SET {campo} = %s WHERE {condicoes};'
    cursor.execute(comando, (valor,))
    banco.commit()
    cursor.close()


def deletar_registro(tabela, condicoes):
    cursor = banco.cursor()
    comando = f'DELETE FROM {tabela} WHERE {condicoes};'
    cursor.execute(comando)
    banco.commit()
    cursor.close()