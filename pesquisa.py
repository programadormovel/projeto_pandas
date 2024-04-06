import sqlite3
import pandas as pd

con = sqlite3.connect('agenda.db')

cur = con.cursor()

resultado = cur.execute("select * from CONTATO")

nomes = []
enderecos = []

for linha in resultado.fetchall():
    print(linha[0])
    print(type(linha))
    nomes.append(linha[0])
    enderecos.append(linha[1])
    
print(pd.Series(nomes))

dados = pd.DataFrame({'Nomes': nomes, 'enderecos': enderecos})

print(dados)
