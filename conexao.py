import mysql.connector

def criar_conexao(host, usuarion, senha, banco):
    return mysql.connector.connect(host=host, user = usuarion, password = senha, database = banco )


def fechar_conexao(con):
    return con.close()