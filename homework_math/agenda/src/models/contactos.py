
class contactos:
   def __init__(self, nombre, apellido, apodo, telefono, correo, cumpleaños):
       self.nombre = nombre
       self.apellido = apellido
       self.apodo = apodo
       self.telefono = telefono
       self.correo = correo
       self.cumpleaños = cumpleaños

   def expotar(self):
       return {"nombre": self.nombre, "apellido": self.apellido, "apodo": self.apodo,
               "telefono": self.telefono, "correo": self.correo, "cumpleaños": self.cumpleaños}