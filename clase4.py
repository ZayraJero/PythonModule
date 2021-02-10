### 1 Crear dos variables que representen dos productos, asignarle un precio
a = 30
b = 40

### 2 Aplicarle iva (16% adicional del precio)
iva = .16
precio = 100.0
valor_total = precio * (1 + iva)
impuestos = precio * iva
valor_total = precio + impuesto 

### 3 Calcular el precio total de una pieza por producto
prodcuto1 = 200.00
producto2 = 100.00

iva = 0.16
subtotal1 = prodcuto1 * (1 + iva)
subtotal2 = prodcuto2 * (1 + iva)

impuesto_total = (producto1 * iva) + (prodcuto2 * iva)
total_compra = subtotal1 + subtotal2

print(prodcuto1)
print(prodcuto2)

print('subtotal es:' impuesto_total, 'pesos')
print('tu compra es de:' total_compra, 'pesos')

### 4 Calcular el precio total de 4 pieza del producto 1 y 5 del producto 2
iva = .16
precio = 100.0
valor_total = precio * (1 + iva)
impuesto = precio * iva
valor_total = precio + impuesto

### 5 Aplicar 2 operaciones con entero
### 6 Aplicar 2 operaciones con flotantes
### 7 Aplicar 2 operaciones con strings
### 9 Crear una lista (l_nombres) con los nombres de 5 compañeros
l_nombres = ["Ale Paez","Gabriela Camarillo","Emmanuel Cianca","Gilberto Garcia","Liliana Juarez"]
print(l_nombres)
### 10 Crear una lista (l_dato) con el tiempo que tardan a llegar el trabajo
### o edad
l_dato=[20, 0, 10, 35, 40]
print("minutos",l_dato)
### 11 Cambiar el tiempo (edad) del 3er compañero
l_dato[2] = 30
# l_dato.pop(2)
# l_dato.insert(2,30)
# print(l_dato)
### Mostrar los compañeros con menos de 26 años 

##
l_resultado=[l_nombres[i] for i in range(len(l_nombres)) if l_dato[i] < 26]
print( l_resultado)
### Crear una lista con los compañeros de horas de sueño promedio
l_nombres2 = ['Ale Paez', 'Gabriela Camarillo', 'Emmanuel Cianca', 'Gilberto Garcia', 'Liliana Juárez']
l_horas = [7, 6, 6, 3, 8]
print(l_horas)
### Mostrar los compañeros que sólo duermen mas de 8 horas
l_mas8=[l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] >8]
print(l_mas8)
### Mostrar los compañeros que sólo duermen menos de 8 horas y a los que
### duermen menos 4 sustituir su nombre por vampiro
l_vampiros = [l_nombres2[i] + " es un vampiro" if l_horas[i] < 4 else l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] < 8]
print(l_vampiros)
### 8 ¿Aplicar 2 operaciones con Bool?

#< menor que
#> mayor que
#>= mayor o igual que
#<= menor o igual que
# and, &
# or, |
# True & True = True

print("True & True", True & True)
# True & False = False
print("True & False", True & False)
# False & True = False
print("False & True", False & True)
# False & False = False
print("False & False", False & False)
# True | True = True
print("True | True", True | True)
# False | True = True
print(F"False | True", False | True)
# True | False = True
print("True | False", True | False)
# False | False = False
print("False | False", False | False)

# if (expresion1 devuelve True, False):
#     codigo 1
# elif (expresion2 devuelve True, False):    
#     codigo 2
# elif (expresion3 devuelve True, False):    
#     codigo 3
# elif (expresion4 devuelve True, False):    
#     codigo 4  
# else:
#     codigo 5

# if condición:
### para corregirlo puedes cambiar el orden
horas_suenio = 6
if horas_suenio < 8:
    print("duermes poco")
elif horas_suenio < 4:
    print("eres un vampiro")
else:
    print("que envidia")