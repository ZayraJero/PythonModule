edad_cliente = 27
nombre_cliente = "Fulanito"
compras_mensual_cliente = 13000

if edad_cliente >= 18 and edad_cliente <= 60 and 50000 >= compras_mensual_cliente > 10000:
    print("fifi")
elif 60 >= edad_cliente >= edad_cliente >= 18 and compras_mensual_cliente <= 10000: 
    print("chairos")
elif edad_cliente < 18 and compras_mensual_cliente > 10000:
    print("juniors")
elif edad_cliente < 18 and compras_mensual_cliente <= 10000:
    print("aficionados")
elif edad_cliente >= 60 and compras_mensual_cliente <= 50000:
    print("pejes")
elif edad_cliente >= 60 and compras_mensual_cliente > 50000:
    print("mi abuelo favorito")

edad_cliente = 45
nombre_cliente = "Fulanito"
compras_mensual_cliente = 60000

if edad_cliente >= 60 and compras_mensual_cliente > 50000:
    print("mi abuelo favorito")
elif edad_cliente >= 60:
    print("pejes")
elif compras_mensual_cliente > 50000:
    print("chava iglesias")
elif edad_cliente >= 18 and compras_mensual_cliente > 10000:
    print("fifi")
elif edad_cliente >= 18:
    print("chairos")
elif edad_cliente < 18 and compras_mensual_cliente > 10000:
    print("juniors")
elif edad_cliente < 18:
    print("aficionados")

###

precio_diario_promedio = [100, 60, 80, 90, 100, 120, 140]
a = 0
for i in range(len(precio_diario_promedio)):

    a = a + precio_diario_promedio[i]
    print(a)

promedio = a/len(precio_diario_promedio)
print(promedio)

precio_diario_promedio = [100, 60, 80, 90, 100, 120, 140]

x = precio_diario_promedio.count(100)

print(f"el número de coincidencias con 100 es: {x} " )

precio_diario_promedio = [100, 60, 80, 90, 100, 120, 140]

veces_100 = [ i for i in precio_diario_promedio if i == 100]
print(len(veces_100))

### SET
A = {12, 15, 16, 17, 18}

B = {10, 4, 12, 4, 9, 15}

C = {10, 4}

D = {1, 2, 3}

#UNIÓN
A | B #Elementos que estan en A junto con elementos en B 

#INTERSECCIÓN
A & B #Elementos que estan en B y A 

#DIFERENCIA 
A - B #Elementos que estan en A y no en B
B - A #Elementos que estan en B y no en A

#DIFERENCIA SIMETRICA
C ^ D #Elementos que estan en C y no estan en D unión
      #Elementos que estan en D y no estan en C unión
B ^ C
A ^ B

C <= B # C es subconjunto de B? 
C >= B # C es superconjunto de B? 

 #metodos de los SET
add #agarra un elemento
update #agrega multiples elementos
remove #eliminar un determinado elemento
discard #eliminar un elemento, no mandar error
pop #selecciona un elemento y lo elimina de manera aleatoria, regresa elemento
clear #limpia, deja sin elementos al conjunto set

A.add(100)
A.add(11, 12, 100) #error
A.add([11, 12, 100]) #error

A.update([11, 12, 100])

A.remove(11)
A.remove(102) #error, si no lo encuentra te manda error

A.discard(102)

A.pop()

A.clear() 

###DICCIONARIOS
#Ejemplo con horas de sueño
l_nomnres2= ['ale', 'gabriela', 'emmanuel']
l_horas = [7, 6, 6]
ejemplo1 ={'ale': 
    {
        'horas de sueño': 7,
        'minutos al trabajo': 20
    }
}
horas_suenio_dict = {
    'ale': 7,
    'gabriela': 6,
    'emmanuel': 6
}
#.ITEMS
horas_suenio_dict.items()

for llave, valor in horas_suenio_dict.items():
    print(f'{llave} duerme {valor}')

#.KEYS
horas_suenio_dict.keys()
#si se necesita tener las llaves como listas
list(horas_suenio_dict.keys())

for llave in horas_suenio_dict.keys():
    print(f'{llave} duerme {horas_suenio_dict[llave]}')

#.VALUES
suma_horas = 0
for valor in horas_suenio_dict.values():
    print(valor)
    suma_horas += valor

print(f'El promedio de horas de suelos es: {suma_horas/ len(horas_suenio_dict)'})

#.CLEAR 
#DEJA VACIO EL DICCIONARIO

#.COPY 
#CREA UN ACOPIA NUEVA

#.FROMKEYS
horas_suenio_dict_2 = dict.fromkeys(['artur','oscar', charlie], 8)
print(horas_suenio_dict_2)

#CONSULTAS
#.GET
horas_suenio_dict_2.get('ale')
horas_suenio_dict_2.get('arturo')

#.POP
horas_suenio_dict_2.pop('arturo')

#.SETDEFAULT, agrega un elemento parecido al get
horas_suenio_dict_2.setdefault('arturo', 7) #agrega arturo con 7 hrs de sueño y no marca error como el get

#.UPDATE
#RECIBE UN DICCCIONARIO
horas_suenio_dict_2.update({'ale': horas_suenio_dict_2['ale']})
print(horas_suenio_dict_2)
horas_suenio_dict_2['ale'] = 10
horas_suenio_dict_2['gil'] = 10 #gil no existe y se le da valor de 10
horas_suenio_dict_2.get('gustavo', "no se encontro el nombre")

#VALIDAR QUE LA LLAVE EXISTE
if "gustavo" in horas_suenio_dict_2.keys():
    print('sabemos cuanto duermes gus')
else:
    print('sabemos cuanto duerme gus')

#WHILE
# while condicion:
#     codigo
i = 0
while i == 0: #imprime un 0
    print(i)
    break

i = 0
while i != 0: #no imprime nada
    print(i)
    break

i = 0
while i < 11: #imprime del 1 al 10
    i += 1
    print(i)

i = 0
while True:
    i += 1
    if i == 10:
        break
    else:
        print(i)

i = 0
while True:
    i += 1
    print(i)
    if i == 10:
        break

i = 0
while True:
    i += 1
    if i == 11:
        break
    else:
        print(i)

  
#BREAK
#CONTINUE no se ejecuta lo que esta abajo del continue
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

i = 0
while i < 10:
    i += 2
    print(i)

#PASS pasa el flujo, no se puede dejar un if vacio
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        pass
    print(i)

#ZIP crea diccionarios/ iterar en datos
dict(zip(l_nomnres2, l_horas))

for i, j in zip(l_nomnres2, l_horas):
    print(f'{i} duerme {j} horas')

dict_ejercicio = {}

for i, j in zip(l_nombres2, l_horas):
    dict_ejercicio.update({i : j})
    # dict_ejercicio.setdefault(i , j)
    # dict_ejercicio[i] = j
    print(f'{i} duerme {j} horas')

#FOR A IN ZIP() dupla [()]
[(i, j) for i, j in horas_suenio_dict_2.items()]

list(horas_suenio_dict_2.items())

#MEZCLAR DICCIONARIOS Y LISTAS
ejemplo_mixto = {'arturo': {'vision computacional': [10, 9, 7]}}
ejemplo_mixto['arturo'].get('vision computacional')[2] #en el ultimo se accese lo que quieres ver
{'uno': {'dos': valor}}

input ('inserta un valor')
inserta un valor12
'12'

#EJERCICIO
nombre = input('¿cual es tu nombre')
minutos = input('¿cuanto minutos tarda en el trabajo?')
print()

