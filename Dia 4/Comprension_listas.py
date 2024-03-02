valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [valor ** 2 for valor in valores]
print(valores_cuadrado)


valores2 = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores2 if valor % 2 == 0]
print(valores_pares)


temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(temperatura - 32) * (5 / 9) for temperatura in temperatura_fahrenheit]
print(grados_celsius)