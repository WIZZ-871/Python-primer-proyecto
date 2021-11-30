#CALCULADORA
print("CALCULADORA: \n"
      "menu principal \n"
      "lea atentamente las siguientes opciones y seleccione la operacion que desea realizar: \n "
      "-escriba 1 si desea hacer una suma \n"
      "-escriba 2 si desea hacer una resta \n"
      "-escriba 3 si desea hacer una multiplicacion\n"
      "-escriba 4 si desea hacer una division")
var1= int(input())
while 1<= var1 <=4:
    if var1 == 1:
        num1 = float(input("digite los numeros que desea sumar \n"))
        num2 = float(input())
        suma= num1 + num2
        print("la suma de los numeros ingresados es:\n", suma)
    elif var1== 2:
        num1 = float(input("digite los numeros que desea restar: \n"))
        num2 = float(input())
        resta= num1 - num2
        print("la resta de los numeros ingresados es:", resta)
    elif var1 == 3:
        num1 = float(input("digite los numeros que desea multiplicar: \n"))
        num2 = float(input())
        multiplicacion = num1 * num2
        print("la multiplicacion de los numeros es:", multiplicacion)
    elif var1 == 4:
        num1 = float(input("digite los numeros que desea dividir: \n"))
        num2 = float(input())
        if num2==0:
            print("error, el divisor no puede ser 0")
        else:
            division = num1 / num2
            print("la division de los numeros ingresados es:", division)
    break