# Acceder a valores usando claves
# Puedes acceder a los valores de un diccionario proporcionando la clave correspondiente:

building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

print(building_heights["Burj Khalifa"])  # Imprime 828
print(building_heights["Ping An"])      # Imprime 599

zodiac_elements = {
    "water": ["Cáncer", "Escorpio", "Piscis"],
    "fire": ["Aries", "Leo", "Sagitario"],
    "earth": ["Tauro", "Virgo", "Capricornio"],
    "air": ["Géminis", "Libra", "Acuario"]
}

print(zodiac_elements["earth"])  # Imprime ['Tauro', 'Virgo', 'Capricornio']
print(zodiac_elements["fire"])   # Imprime ['Aries', 'Leo', 'Sagitario']

# Manejo de claves inexistentes
# Intentar acceder a una clave que no existe genera un KeyError:

# Descomentar la siguiente línea provocará un error:
# print(building_heights["Landmark 81"])  # KeyError

# Para evitar errores, verifica si la clave existe antes de acceder a ella:
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights[key_to_check])
else:
    print(f"{key_to_check} no se encuentra en las alturas de los edificios.")

# Agregar un nuevo par clave-valor
zodiac_elements["energy"] = "No es un elemento del zodiaco"
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])  # Imprime "No es un elemento del zodiaco"

# Usando el método get()
# Obtener un valor de forma segura sin generar un error si la clave no existe:
print(building_heights.get("Shanghai Tower"))  # Imprime 632
print(building_heights.get("My House"))        # Imprime None

# Valores predeterminados con get()
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

tc_id = user_ids.get("teraCoder", 1000)
print(tc_id)  # Imprime 100019

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)  # Imprime 100000

# Eliminar elementos con pop()
# El método pop() elimina un par clave-valor y devuelve el valor eliminado:
raffle = {
    223842: "Oso de peluche",
    872921: "Entradas para un concierto",
    320291: "Canasta de regalo",
    412123: "Collar",
    298787: "Máquina para hacer pasta"
}

print(raffle.pop(320291, "Sin premio"))  # Imprime "Canasta de regalo"
print(raffle)                            # Diccionario actualizado

print(raffle.pop(100000, "Sin premio"))  # Imprime "Sin premio"
print(raffle)                            # Elementos restantes

# Ejemplo de uso de pop() en un juego
available_items = {
    "poción de salud": 10,
    "pastel de la cura": 5,
    "elixir verde": 20,
    "sándwich de fuerza": 25,
    "granos de resistencia": 15,
    "estofado de poder": 30
}

health_points = 20
health_points += available_items.pop("granos de resistencia", 0)
health_points += available_items.pop("estofado de poder", 0)
health_points += available_items.pop("pan místico", 0)

print(available_items)  # Elementos restantes
print(health_points)    # Puntos de salud actualizados

# Acceder a todas las claves
# Usa keys() para obtener una lista de todas las claves en un diccionario:
test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}

print(list(test_scores.keys()))  # Imprime todas las claves
for student in test_scores.keys():
    print(student)  # Imprime el nombre de cada estudiante

# Acceder a todos los valores
# Usa values() para obtener una lista de todos los valores en un diccionario:
for score_list in test_scores.values():
    print(score_list)

# Sumar valores
num_exercises = {
    "funciones": 10,
    "sintaxis": 13,
    "flujo de control": 15,
    "bucles": 22,
    "listas": 19,
    "clases": 18,
    "diccionarios": 18
}

total_exercises = 0
for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)  # Imprime el total de ejercicios

# Acceder a todos los elementos
# Usa items() para obtener pares clave-valor:
biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

for company, value in biggest_brands.items():
    print(f"{company} tiene un valor de {value} mil millones de dólares.")

pct_women_in_occupation = {
    "CEO": 28,
    "Gerente de ingeniería": 9,
    "Farmacéutico": 58,
    "Médico": 40,
    "Abogado": 37,
    "Ingeniero aeroespacial": 9
}

for occupation, percentage in pct_women_in_occupation.items():
    print(f"Las mujeres representan el {percentage}% de los {occupation}s.")
