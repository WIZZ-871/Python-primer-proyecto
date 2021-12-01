#CALCULADORA

def mensaje_bienvenida():
    print("Esta es una calculadora con la cual puede realizar operaciones matematicas entre dos numeros")
def menu():
    print("menu principal: \n"
          "-escriba 1 si desea hacer una suma \n"
          "-escriba 2 si desea hacer una resta \n"
          "-escriba 3 si desea hacer una multiplicacion\n"
          "-escriba 4 si desea hacer una division")
def selecionar_opcion():
    print("lea atentamente las opciones del menu y seleccione la operacion que desea realizar: ")
    return int(input())
def suma_de_dos_numeros(num1, num2):
    print("la suma de los numeros ingresados es: " + str(num1+num2))
def resta_de_dos_numeros(num1, num2):
    print("la resta de los numeros ingresados es: " + str(num1-num2))
def multiplicacion_de_dos_numeros(num1, num2):
    print("la multiplicacion de los numeros ingresados es: " + str(num1*num2))
def division_de_dos_numeros(num1, num2):
    print("la division de los numeros ingresados es: " + str(num1/num2))
mensaje_bienvenida()
menu()
opciones= selecionar_opcion()
print("digite los numeros que desea operar: \n")
primer_numero= float(input("primer numero:"))
segundo_numero= float(input("segundo numero"))

if opciones== 1:
    suma_de_dos_numeros(primer_numero,segundo_numero)
elif opciones== 2:
    resta_de_dos_numeros(primer_numero,segundo_numero)
elif opciones== 3:
    multiplicacion_de_dos_numeros(primer_numero,segundo_numero)
elif opciones==4:
    if segundo_numero== 0:
        print("error el divisor no puede ser 0")
    else:
        division_de_dos_numeros(primer_numero, segundo_numero)
else:
    print("gracias por usar nuestra calculadora")


