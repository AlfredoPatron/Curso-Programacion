texto = input("Ingrese un texto a tu elección: ")
letras = []

texto = texto.lower()

letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\n")
print("Cantidad de Letras")
cantidad_letras = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Se ha encontrado la letra '{letras[0]}' repetida {cantidad_letras} veces")
print(f"Se ha encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Se ha encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("Cantidad de Palabras")
palabras = texto.split()
print(f"Se han encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("Letras del inicio y fin")
letra_inicial = texto[0]
letra_final = texto [-1]
print(f"La letra inicial es '{letra_inicial}' y la letra final es '{letra_final}'")

print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si invertimos tu texto va a decir: '{texto_invertido}'")

print("\n")
print("Buscando la palabra Phyton")

buscar_python = 'phyton' in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'Phyton' {dic[buscar_python]} se encuentra en el texto")