###FUNCIONES
def nombre_funcion(parametros):
    codigo

def suma(x, y):
    return(x + y)

def resta(x, y):
    return(x - y)

def multiplicacion(x, y):
    return(x * y)

def division(x, y):
    if y == 0:
        print("no se puede dividir entre cero")
        return None
    return(x / y)

def calculadora(x, y, operacion):
    print('se usará la operacion', operacion)
    if operacion == "suma":
        return(suma(x, y))
    if operacion == "resta":
        return(resta(x, y))
    if operacion == "multiplicacion":
        return(multiplicacion(x, y))
    if operacion == "division":
        return(division(x, y))