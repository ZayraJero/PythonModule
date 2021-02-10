### String y Metodos

# Python no tiene i++

print("Inicializando i con un valor de 1")
i = 1

print("Sumamos una unidad")
i += 1

print("El resultado es:" + str(i))
# Nombre
j = 10
texto_resultado = "El resultado es: {var1} texto adicional: {var2}"
# Posicion
texto_resultado.format(var1 = i, var2 = j)
texto_resultado = texto_resultado.format(var1 = i, var2 = j)
print(texto_resultado)

x, y = 10, 11

nombre = "Zayra"
apellido = "Jeronimo"

print(f"Hola {nombre} {apellido}")

"""Texto
...otro
...otro
"""

mi_empresa = "Nombre empresa"
la_empresa = "Descripción de la empresa otra descripción"
objetivos = "Objetivos de la empresa"

print(f"La empresa {mi_empresa} se dedica {la_empresa} nos enfocamos {objetivos}")

# funciones type, len

print("5 es un entero", type(5))
print("'5' es un string", type('5'))
print("true es un booleano", type(true))
print("3.333 es un float", type(3.333))

x = 5
print("5 es un entero", type(x))

len("Texto, texto otro...")

#metodos

nombre_completo = "zayra jeronimo"

nombre_completo.find("a")
nombre_completo[:nombre_completo.find(" ")]

nombre_completo.upper()
nombre_completo = nombre_completo.upper()
print(nombre_completo)

print(mi_empresa.replace("texto"))
print(mi_empresa.replace("a", "o"))

texto_entrada = "12|13|14"
lista_texto_entrada = texto_entrada.split("|")

"|".join(lista_texto_entrada)

lista_texto_entrada[0].isdigit()