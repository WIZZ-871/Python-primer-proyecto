#color del texto
rojo= '\033[31m'
verde= '\033[32m'
azul= '\033[34m'
magenta= '\033[35m'
negro= '\033[30m'
#DATOS REGISTRADOS PREVIAMENTE
print(azul+" ESTE PROGRAMA SIMULA EL LOGIN DE UNA PAGINA CON UN USUARIO Y CONTRASEÑA "
      "DEFINIDOS PREVIAMENTE")
print(azul+"EL USUARIO Y CONTRASEÑA SON:")
print(rojo+"*******************************************")
print(rojo+"*"+magenta+ "   usuario:danielchaparro@gmail.com      "+rojo+"*" )
print(rojo+"*"+magenta+"   contraseña:1234abcde                 "+rojo+"*" )
print("*******************************************")
print(verde+"PARA REALIZAR EL LOGIN EN NUESTRA PAGINA DEBERA DIGITAR EL USUARIO"
      " Y CONTRASEÑA REGISTRADOS PREVIAMENTE")
usuario= str ("danielchaparro@gmail.com")
contraseña= str("1234abcde")
ingresar_usuario= str(input(negro+"ingrese el usuario:"))
while usuario != ingresar_usuario:
    print(rojo+"el usuario ingresado es distinto al registrado por favor"
          " digite esl usuario correcto ")
    ingresar_usuario= str(input(rojo+"ingrese el usuario correcto:"))
print(verde+"el usuario ingresado es correcto por favor ingrese la contraseña:")
ingresar_contraseña = str(input(negro+"ingrese la contraseña:"))
while ingresar_contraseña!= contraseña:
        print(rojo+"la contraseña ingresada es distinta a la registrada"
              "por favor ingrese una contraseña correcta")
        ingresar_contraseña= str(input(rojo+"ingrese la contraseña:"))
print(verde+"EL USUARIO Y CONTRASEÑA INGRESADOS SON CORRECTOS LOGIN COMPLETADO")