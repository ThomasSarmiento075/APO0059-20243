# Información inicial para representar diferentes escenarios
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

print("Sensors:", sensors)
print("Number of cameras:", num_cameras)
print("Translations:", translations)

# Arreglando un problema donde las claves eran listas, que no son válidas
# Se reemplazan por tuplas para evitar errores
##powers = {(1, 2, 4, 8, 16): 2, (1, 3, 9, 27, 81): 3}
##print("Powers:", powers)

# Relación de familias y nombres de sus hijos
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
print("Children:", children)

# Un ejemplo de cómo se ve un diccionario vacío
my_empty_dictionary = {}
print(my_empty_dictionary)

# Agregando un nuevo elemento a un menú de precios
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Menu before:", menu)
menu["cheesecake"] = 8
print("Menu after adding cheesecake:", menu)

# Reescribiendo el contenido del diccionario con nuevos datos
animals_in_zoo = {"dinosaurs": 0} 
animals_in_zoo = {"horses": 2}  # Ahora solo incluye caballos
print(animals_in_zoo)

# Ampliando el alcance de los datos en el diccionario `sensors`
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("Updated sensors:", sensors)

# Agregar nuevos usuarios a un sistema de identificaciones
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print("User IDs before update:", user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print("User IDs after update:", user_ids)

# Modificando un valor específico en el menú
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Menu before change:", menu)
menu["oatmeal"] = 5
print("Menu after changing 'oatmeal':", menu)

# Editando y expandiendo un diccionario con información de ganadores de premios
oscar_winners = {
    "Best Picture": "La La Land", 
    "Best Actor": "Casey Affleck", 
    "Best Actress": "Emma Stone", 
    "Animated Feature": "Zootopia"
}
print("Oscar winners before update:", oscar_winners)
oscar_winners.update({"Supporting Actress": "Viola Davis"})  # Se agrega una nueva categoría
print("Oscar winners after adding 'Supporting Actress':", oscar_winners)
oscar_winners["Best Picture"] = "Moonlight"  # Ajustando un error en el dato original
print("Oscar winners after correcting 'Best Picture':", oscar_winners)

# Crear un diccionario utilizando listas como base
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key: value for key, value in zip(names, heights)}
print("Students:", students)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
drinks_to_caffeine = {key: value for key, value in zip(drinks, caffeine)}
print("Drinks to caffeine:", drinks_to_caffeine)

# Introducir y ajustar datos en un diccionario de canciones populares
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key: value for key, value in zip(songs, playcounts)}
print("Plays before update:", plays)
plays.update({"Purple Haze": 1, "Respect": 94})  # Modificar y añadir datos en una sola línea
print("Plays after update:", plays)

# Creando una biblioteca para organizar canciones
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print("Library:", library)
