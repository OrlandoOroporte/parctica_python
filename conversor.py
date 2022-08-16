#conversor de moneda bolivares a otra 

message = """
Bienvenido a mi conversor, elija una opcion: 
1.- Bolivares a Dolares.
2.- Bolivares a Pesos.
3.- Bolivares a Yuanes. 
0.- Salir. 
"""
print(message)
option = int(input("opcion?"))

if option == 1:
    my_change = float(input("ingres el monto"))
    total = my_change * 6.1
    print(f"al cambio es {round(total,2)} dolares")
elif option == 2:
    pass
elif option == 3:
    pass
else:
    print("gracias por preferinos")
