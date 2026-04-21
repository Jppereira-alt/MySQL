import sqlite3

conexao = sqlite3.connect("login.db")
cursor = conexao.cursor()
cursor.execute("DROP TABLE IF EXISTS conta_acesso")
cursor.execute ("""CREATE TABLE IF NOT EXISTS conta_acesso (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone INTEGER NOT NULL,
                idade INTEGER NOT NULL
                )""")

cursor.execute("""INSERT INTO conta_acesso
               (nome, telefone, idade) VALUES
               ('joao', '91993736687', '18')""")

cursor.execute("""SELECT nome, telefone, idade FROM conta_acesso""")

contas = cursor.fetchall()

for conta in contas:
    nome, telefone, idade = conta
    print (f"""
           nome: {nome}
           telefone: {telefone}
           idade: {idade}""")
    
conexao.commit()
conexao.close()