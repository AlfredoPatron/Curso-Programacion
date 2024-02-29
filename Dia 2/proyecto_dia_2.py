nombre = input("Ingrese su nombre: ")

ventas = float(input("¿Cúanto has vendido en este mes?: ".format(nombre)))
ventas = int(ventas)

comision = ventas * 13 / 100
comision = round(comision,2)

print(f"Hola {nombre}, tus comisiones totales de este mes son de ${comision}")


