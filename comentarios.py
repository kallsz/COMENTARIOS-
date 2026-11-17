
# Importa a biblioteca do sqlite3
import sqlite3

# Inicia um bloco de tratamento de erros
try:

    # Cria uma conexão com o banco de dados (banco.db)
    banco = sqlite3.connect('banco.db')

    # Cria um cursor que executa comandos SQL no banco de dados
    cursor = banco.cursor()

    # Cria uma tabela chamada aluno com as informações:
    cursor.execute("CREATE TABLE aluno(id_aluno int, Nome text, idade int, email text)")

    # Primeiro aluno da tabela
    cursor.execute("INSERT INTO aluno VALUES (1, 'JOÃO',20,'joaozinholeroy@gmail.com') ")

    # Segundo aluno da tabela
    cursor.execute("INSERT INTO aluno VALUES (2, 'jheimes',25,'rick@gmail.com') ")

    # Terceiro aluno na tabela
    cursor.execute("INSERT INTO aluno VALUES (3, 'ricardo',26,'jheimesbrow@gmail.com') ")

    # Salva e "comita" alterações realizadas no banco de dados
    banco.commit()

    # Printa a informação que os dados foram adicionados
    print("Os dados foram adicionados com sucesso!!")

    # Seleciona todos os registros da tabela aluno
    cursor.execute("Select *FROM aluno")

    # Exibe todos os registros encontrados
    print(cursor.fetchall())

    # Remove da tabela aluno o registro do aluno com idade igual a 20
    cursor.execute("DELETE from aluno WHERE idade = 20")

    # Salva e "comita" alterações realizadas no banco de dados
    banco.commit()

    # Fecha a conexão com o banco de dados
    banco.close()

    # Printa a informação de que os dados foram removidos com sucesso
    print("Os dados foram removidos com sucesso!!")

# Mostra erros relacionados ao SQLite durante a execução do código
except sqlite3.Error as erro:

    # Exibe uma mensagem informando que ocorreu um erro e mostra sua descrição
    print("Erro ao excluir: ", erro)
