from conexao import criar_conexao


class EnviandoParaBanco:

    def dados(descricao, quantidade, valor_uni):
        EnviandoParaBanco.enviando(descricao, quantidade, valor_uni)   

    def enviando(descricao, quantidade, valor_uni):
        con = criar_conexao("localhost", "root", "Elt@n123", "crud_simples")
        cursor = con.cursor()
        sql = "INSERT INTO produtos (descricao, quantidade, valor) values(%s, %s, %s)"
        valores = (descricao, quantidade, valor_uni)
        cursor.execute(sql, valores)
        cursor.close()
        con.commit()