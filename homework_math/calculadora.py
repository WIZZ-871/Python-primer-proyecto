#CALCULADORA

def mensaje_bienvenida():
    print("Esta es una calculadora con la cual puede realizar operaciones matematicas entre dos numeros")
def menu():
    print("menu principal: \n"
          "-escriba 1 si desea hacer una suma \n"
          "-escriba 2 si desea hacer una resta \n"
          "-escriba 3 si desea hacer una multiplicacion\n"
          "-escriba 4 si desea hacer una division\n")
def sel_op():
    opcion = int(input())
    return opcion

def suma_de_dos_numeros(num1,num2):
    return num1 + num2
def resta_de_dos_numeros(num1, num2):
    return num1 - num2
def multiplicacion_de_dos_numeros(num1, num2):
    return num1 * num2
def division_de_dos_numeros(num1, num2):
    return num1 / num2

mensaje_bienvenida()
print("presione cualquier numero distinto de 0 para iniciar la calculadora y "
      "poder mostrarle el menu")
sel = sel_op()
while sel !=0:
    menu()
    sel = sel_op()
    print("digite los numeros que desea operar: ")
    num1 = float(input("primer numero:"))
    num2 = float(input("segundo numero"))
    if sel == 1:
        resultado= suma_de_dos_numeros(num1,num2)
        print("la suma de los numeros ingresados es: ",resultado)
    elif sel == 2:
        resultado= resta_de_dos_numeros(num1,num2)
        print("la resta de los numeros ingresados es: ",resultado)
    elif sel == 3:
        resultado= multiplicacion_de_dos_numeros(num1,num2)
        print("la multiplicacion de los numeros ingresados es: ",resultado)
    elif sel == 4:
        if num2 == 0:
            print("error el divisor no puede ser 0")
        else:
            resultado= division_de_dos_numeros(num1,num2)
            print("la division de los numeros ingresados es: ",resultado)
    repetir = input("si desea realizar otra operacion escriba si, de "
                    "lo contrario escriba no: \n")
    if repetir == "no":
        break
print("gracias por usar la calculadora")