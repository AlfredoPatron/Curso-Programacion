def suma():
    n1 = int(input("numero 1: "))
    n2 =  int(input("numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")


try:
    suma()
except:
    print("Algo no ha salido bien")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")