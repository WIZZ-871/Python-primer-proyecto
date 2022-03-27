import json
from ..models.contactos import contactos
from ..view.view import View

class Controller:
   def __init__(self):
       self.opcion_seleccionada = 0
       self.vista = View()
       self.personas = []

   def acciones(self):
       while self.opcion_seleccionada != 5:
           self.opcion_seleccionada= self.vista.seleccionar_opcion_menu()
           if self.opcion_seleccionada == 1:
               self.crear_contacto()
           if self.opcion_seleccionada == 2:
               self.listar_contactos()
           if self.opcion_seleccionada == 3:
               self.exportar_contactos()
           if self.opcion_seleccionada == 4:
               self.cargar_contactos()

   def crear_contacto(self):
       contacto = self.vista.datos_contactos()
       self.personas.append(contacto)
       self.vista.contacto_creado_correctamente(contacto.nombre)

   def listar_contactos(self):
       for persona in self.personas:
           print(persona.expotar())

   def exportar_contactos(self):
       nombre_archivo = self.vista.nombre_archivo()
       lista_para_exportar= []
       for persona in self.personas:
           lista_para_exportar.append(persona.expotar())
       with open("personas.json", "w") as fp:
           json.dump(lista_para_exportar, fp)
       self.vista.error_archivo()
   def cargar_contactos(self):
       nombre_archivo = self.vista.nombre_archivo()
       try:
           with open(f"data/{nombre_archivo}.json", "r") as fp:
               data = json.load(fp)

           for contacto in data:
               self.personas.append(
                   Person(
                       nombre=persona["nombre: "],
                       apellido=persona["apellido:"],
                       apodo=persona["apodo: "],
                       telefono=persona["telefono"],
                       correo=persona["correo"],
                       cumpleaños=persona["cumpleaños"],
                   )
               )
       except Exception as e:
           self.vista.error_archivo(e)

   def salir(self):
       pass