import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="aula",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

def INSERT():
    sql =""" 
        INSERT INTO usuarios (nome, email, endereco)
        VALUES (%s, %s, %s);
    """
    
    nome = input("digita o seu nome: ")
    email= input("dijite o seu email")
    endereco = input("dijite o seu endereço")
    
    cur.execute(sql, (nome,email,endereco))
    conn.commit()
    
def select():
    sql = """
        SELECT * FROM usuarios;
    """
    cur.execute(sql)
    dados = cur.fetchall()
    coluna = ()
    for x in cur.description:
        coluna += (x[0],)
    
    tabela = pd.DataFrame(dados, columns=coluna)
    print(tabela)
    
    #conn.comment()

select()    
INSERT()
select()

cur.close()
conn.close()

console.log("Hello word")