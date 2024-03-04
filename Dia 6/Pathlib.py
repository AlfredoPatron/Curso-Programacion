from pathlib import Path

carpeta = Path("C:/Users/alfre/PycharmProjects/pythonProject/Proyectos/Dia 6/prueba.txt")

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, si existe")