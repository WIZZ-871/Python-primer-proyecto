#este programa sirve para saber si la segunda palabra ingresada es anagrama o no

print("este programa sirve para verificar si una palabra es anagrama de otra"
      " por favor ingrese la palabras a comparar")
palabra1 = str(input("ingrese la primera palabra: "))
palabra2 = str(input("ingrese la segunda palabra: "))
def verificar_anagrama(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return "la palabra 2 no puede ser anagrama de la palabra 1 porque no " \
               "tiene la misama cantidad de letras"
    a = {}
    b = {}
    for i in palabra1:
        if i not in a.keys():
            a[i] = 1
        else:
            a[i] += 1
    for i in palabra2:
        if i not in b.keys():
            b[i] = 1
        else:
            b[i] += 1

    return "la plabra 2 es anagrama de la palabra 1" if a == b else "la palabra 2 no es anagrama de la palabra1"
resultado = verificar_anagrama(palabra1, palabra2)
print(resultado)








