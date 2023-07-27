tupla =(('chave', 'valor'), ('nome', 'Hugo'), ('idade', 40))

print(tupla)
print(tupla[1][1])

dicionario = dict((x, y) for x, y in tupla)

print(dicionario)

print(dicionario['nome'])
print(dicionario['idade'])

print(type(tupla))
print(type(dicionario))