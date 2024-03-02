nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,38]
ciudades = ['Mexico', 'Medellin', 'Madrid']

combinados = list(zip(nombres, edades, ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y es de {ciudad}")