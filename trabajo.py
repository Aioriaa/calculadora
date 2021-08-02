
menu = """
Bienvenidos a la calculadora
1 - suma
2 - resta
3 - multiplicacion 
4 - divicion 
Elige una opcion porfavor: """

opcion = int(input(menu))

if opcion == 1:
    número = int(input("Esciba un nimero: "))
    numero2 = int(input("Esciba un numero: "))
    Resultado = número + numero2 
    print("El resultado es" +str(resultado))
elif opcion == 2:
    número = int(input("Esciba un nimero: "))
    numero2 = int(input("Esciba un numero: "))
    Resultado = número - numero2 
    print("El resultado es" +str(resultado))
elif opcion == 3:
    número = int(input("Esciba un nimero: "))
    numero2 = int(input("Esciba un numero: "))
    Resultado = número × numero2 
    print("El resultado es" +str(resultado))
elif opcion == 4:
    número = int(input("Esciba un nimero: "))
    numero2 = int(input("Esciba un numero: "))
    Resultado = número ÷ numero2 
    print("El resultado es" +str(resultado))
else:
    print("Eliga una opcion correcta por favor")
