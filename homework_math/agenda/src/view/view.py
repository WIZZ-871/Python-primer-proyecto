from ..models.contactos import contactos


class View:
   def seleccionar_opcion_menu(self):
       print("este programa simula una agenda virtual el cual tiene distintas opciones "
             "para guardar los contactos")
       print("1. agregar contactos")
       print("2. Listar contactos")
       print("3. Exportar contactos ")
       print("4. Cargar contactos")
       print("5. Salir")
       return int(input("seleccione una ocion del menu: "))

   def datos_contactos (self):
       nombre = str(input("ingrese el nombre: "))
       apellido = str(input("ingrese el apellido: "))
       apodo = str(input("ingrese el apodo: "))
       telefono = int(input("ingrese el numero de telefono:  "))
       correo = str(input("ingrese el correo electronico:"))
       cumpleaños = str(input("Ingrese la fecha de cumpleaños en el siguiente formato: dia-mes(ene,feb...)-año  "))
       return contactos(nombre, apellido, apodo, telefono, correo, cumpleaños)

   def contacto_creado_correctamente(self, name):
       print(" el contacto fue creado correctamente correctamente")

   def nombre_archivo(self):
       return str(input("Ingrese un nombre para el archivo: "))

   def error_archivo(self):
       print("no se encuentra el archivo pedido ")
