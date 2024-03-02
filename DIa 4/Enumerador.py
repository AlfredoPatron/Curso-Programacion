lista = ['a', 'b', 'c']

for indice,item in enumerate(range(50,55)):
    print(indice,item)


lista2 = ['d', 'e', 'f']

mis_tuples = list(enumerate(lista2))
print(mis_tuples[1][0])