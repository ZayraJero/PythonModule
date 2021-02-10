###Listas
#isinstance

isinstance(14, int)
isinstance(14.5, int)
isinstance(14.5, float)
isinstance("14", float)
isinstance("14", str)

#Listas

mi_primer_lista = [1,3.1416, "Hola mundo"]

x = [1, 2] #se crea la variable x
y = x
x[0] = 0 # x valdra 0 y no 1
y

x = [1, 2] #se crea la variable x
y = x.copy()
x[0] = 0 
y

list([1,2,3]) 

#append
mi_lista_1 = [1,2,3]
mi_lista_2 = [1,3]

mi_lista_1.append(mi_lista_2)

#extend
mi_lista_1 = [1,2,3]
mi_lista_2 = [1,3]

mi_lista_1.extend(mi_lista_2)

#remove
#[1,2,3[1,3]]
mi_lista_1.remove(2) #elimina el primer 2

mi_lista_1.remove([1,3])

#pop
ejemplo = [1,2,3]
ejemplo.pop(2)

#extend
mi_lista_1 = [1,2,3]
mi_lista_2 = [1,3]

mi_lista_1.index(3)

mi_lista_1.index([1,3])

mi_lista_1 =[1,2,3,[1,3],3]
print(mi_lista_1.index(3))

#count
mi_lista_1 =[1,2,3,[1,3],3]
mi_lista_1.count(3)

#reverse
mi_lista_1[::-1]
mi_lista_1.reverse()
mi_lista_1[::-1].reverse()

#insert
mi_lista_1.insert(2,"texto")

#sort
mi_lista_1.remove([1,3])
mi_lista_1.pop(3)
mi_lista_1 =[1,2,3,[1,3],3]
mi_lista_1.sort()

mi_lista =[ "b", "d", "e", "a", "c"]
mi_lista.sort()
mi_lista

mi_lista[::-1].reverse()

# + los junta como extend
mi_lista_1 + mi_lista_2
mi_lista_1 += mi_lista_2

#indices
[inicio:(fin + 1):salto]

x = [1,2,1,2,2,1,1,2,1,2,2]
x[::] #todos  los elementos
x[1::] #del elemento 1 al len(x) -1
x[1:len(x):] #del elemento 1 al len(x) -1
x[len(x)-1] #ultimo elemento
x[-1] #ultimo elemento
x[::-1][0] #primero lo voltea despues agarra el primer elemento
x[len(x)-1:] #regresa una lista

#FOR en Listas
for i in range(10):
    # pass
    print(i)

lista_con_for =[i * 100 for i in range(100)]

#IF en Listas
i = 100
#para obtener numeros pares
[i for i in range(100) if i % 2 == 0] #igualdad
#para obtener numeros impares
[i for i in range(100) if not i % 2 == 0] # not , != , diferente
[i for i in range(100) if i % 2 != 0]

i = 100
[i for x in range(100)]
if i % 2 == 0

# ELSE en Listas
x = [i if i % 2 == 0 else "no es par" for i in range(100)]

#For usando listas
#a lista anterior sumarle 1 a los numeros enteros
[i + 1 for i in x if isinstance(i, int)]
[x + 1 for i in x if i % 2 == 0]
[x [i] + 1 for i in range(len(x)) if i % 2 == 0] #suma 1 al par

[i + 1 if isinstance(i, int) else i for i in x] #regrea texto y par

[i if isinstance(i, str) else i + 1 for i in x]
[i if isinstance(i, str) else x[i] + 1 for i in x] #para tener texto y par

#esto es un error
x[0] = "no es par"
[i + 1 for i in x if isinstance(i, int)]
[x [i] + 1 for i in range(len(x)) if i % 2 == 0]

[for variable_que_recorre_el_for in objeto_iterable if condicion depende variable_que_recorre_el_for]

# x = 1 if activado else 0
# x

### IF A LA DERECHA
activado = False #crea una lista vacia
[i for i in range(100 if activado)]

activado = True #crea una lista con los numeros
[i for i in range(100 if activado)]

### IF A LA IZQUIERDA
activado = False #crea una lista de 100 0
[i if activado else 0 for i in range(100)]

activado = True #crea una lista con los numeros
[i if activado else 0 for i in range(100)]

[i if i % 2 == 1 else "no es impar" for i in range(100) if i < 50 ]

