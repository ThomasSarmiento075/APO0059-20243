###########################################
###########################################
#################LISTAS####################
###########################################
###########################################

# Definimos una lista con colores
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

# Imprimimos la lista y verificamos su tipo
print(my_lista)
print(type(my_lista))

# Accedemos al tercer elemento (índice 2)
print(my_lista[2])

# Tamaño de la lista
print("my_lista size:", len(my_lista))

# Slices de la lista
print(my_lista[0:2])  # Primeros dos elementos
print(my_lista[:2])    # Lo mismo que la línea anterior

# Agregar un elemento al final de la lista
my_lista.append('Blanco')
print(my_lista)

# Insertar un elemento en la posición 3
my_lista.insert(3, 'Negro')
print(my_lista)

# Agregar múltiples elementos a la lista
my_lista.extend(['Marrón', 'Gris'])
print(my_lista)

# Obtener el índice de 'Azul'
print(my_lista.index('Azul'))

# Eliminar 'Marrón' de la lista
my_lista.remove('Marrón')
print(my_lista)

# Insertar 'Marrón' en la posición 8 (¡Cuidado si la lista tiene menos elementos!)
if len(my_lista) > 8:
    my_lista.insert(8, 'Marrón')
else:
    my_lista.append('Marrón')
print(my_lista)

# Extraer el último elemento con pop()
print(my_lista.pop())

# Verificar el tamaño de la lista después del pop
size = len(my_lista)
print("size =", size)

# Multiplicar la lista (repetir sus elementos 3 veces)
my_lista_3 = my_lista * 3
print("my_lista_3:", my_lista_3)

# Intento de ordenación incorrecto
print("Sort:")
my_lista.sort()  # Se ordena en el lugar
print(my_lista)  # Mostramos la lista ordenada

# Lista numérica desordenada
my_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Ordering my_NumList:")
my_NumList.sort()  # Orden ascendente
print(my_NumList)

# Ordenando la lista de mayor a menor
my_NumList.sort(reverse=True)
print("De mayor a menor:", my_NumList)

###########################################
###########################################
#################TUPLAS####################
###########################################
###########################################

# Convertir una lista a tupla
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")

my_tupla = tuple(my_lista)
print("\n\nmy_tuple:", my_tupla)

# Accediendo a elementos de la tupla
print(my_tupla[0])
print(my_tupla[2])

# Evaluar si un elemento está contenido en la tupla
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

# Error corregido: Crear una tupla con un solo elemento
my_tupla_unitaria = ('Blanco',)  # Debe llevar una coma
print(my_tupla_unitaria)

# Empaquetado de tupla
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

# Desempaquetado de tupla
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

# Mostrar los valores desempaquetados
print(f"Nombre: {nombre} - Día: {dia} - Mes: {mes} - Año: {año}")

# Convertir una tupla en una lista
my_lista2 = list(my_tupla)
print(my_lista2)
