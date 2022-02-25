#color del texto
rojo= '\033[31m'
verde= '\033[32m'
azul= '\033[34m'
magenta= '\033[35m'
negro= '\033[30m'

#DATOS REGISTRADOS PREVIAMENTE
def mensaje_bienvenida():
    print(azul + " ESTE PROGRAMA SIMULA EL LOGIN DE UNA PAGINA CON UN USUARIO Y CONTRASEÑA "
                 "DEFINIDOS PREVIAMENTE")
    print(azul + "EL USUARIO Y CONTRASEÑA SON:")
    print(rojo + "*******************************************")
    print(rojo + "*" + magenta + "   usuario:danielchaparro@gmail.com      " + rojo + "*")
    print(rojo + "*" + magenta + "   contraseña:1234abcde                 " + rojo + " *")
    print("*******************************************")
    print(verde + "PARA REALIZAR EL LOGIN EN NUESTRA PAGINA DEBERA DIGITAR EL USUARIO"
                  " Y CONTRASEÑA REGISTRADOS PREVIAMENTE")
def error_usuario():
    print(rojo+"el usuario ingresado es distinto al registrado por favor"
          " digite el usuario correcto:")

def error_contraseña():
    print(rojo + "la contraseña ingresada es distinta a la registrada"
                 "por favor ingrese una contraseña correcta:")

mensaje_bienvenida()
usuario_1= str ("danielchaparro@gmail.com")
usuario_2= str ("daniel@gmail.com")
contraseña_1= str("1234abcde")
contraseña_2= str ("abcde")


ingresar_usuario= str(input(negro+"ingrese el usuario:"))

while usuario_1 or usuario_2 != ingresar_usuario:
    error_usuario()
    ingresar_usuario= str(input())
print(verde+"el usuario ingresado es correcto por favor ingrese la contraseña:")

ingresar_contraseña = str(input(negro+"ingrese la contraseña:"))

while ingresar_contraseña!= contraseña_1 or contraseña_2:
    error_contraseña()
    ingresar_contraseña= str(input())

print(verde+"EL USUARIO Y CONTRASEÑA INGRESADOS SON CORRECTOS LOGIN COMPLETADO")