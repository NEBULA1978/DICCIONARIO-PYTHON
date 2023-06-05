# DICCIONARIO-PYTHON

import random

my_dict = {"Juan": {"edad": 30, "casado": True}}

print(my_dict)#{'Juan': {'edad': 30, 'casado': True}}

# Dict comprehension(Arreglos)
name=["Alex","Anna","Petter","Angela"]
age=[22,33,43,51]

my_dict ={name[i]:age[i] for i in range(len(name))}

print(my_dict)#{'Alex': 22, 'Anna': 33, 'Petter': 43, 'Angela': 51}

# Random  edad
my_dict ={name[i]:random.randint(10,50) for i in range(len(name))}
print(my_dict)#{'Alex': 22, 'Anna': 33, 'Petter': 43, 'Angela': 51}

# Otra forma

other_dict = {
    "a":23,
    "b":551,
    "c":98
}

my_dict={key:value for (key,value) in other_dict.items()}

print(my_dict)#{'a': 23, 'b': 551, 'c': 98}

# Elevamos valores al cuadrado
my_dict={key:value**2 for (key,value) in other_dict.items()}

print(my_dict)#{'a': 529, 'b': 303601, 'c': 9604}

# Para no se warde el valor de b
my_dict={key:value**2 for (key,value) in other_dict.items() if key != "b"}

print(my_dict)#{'a': 529, 'c': 9604}

Ejemplo 2: Asignación de edades aleatorias

En este ejemplo, utilizamos la función random.randint() para asignar edades aleatorias a los nombres.
import random

name = ["Alex", "Anna", "Petter", "Angela"]

my_dict = {name[i]: random.randint(10, 50) for i in range(len(name))}
print(my_dict)  # {'Alex': 22, 'Anna': 33, 'Petter': 43, 'Angela': 51}

Ejemplo 3: Creación de un nuevo diccionario

En este ejemplo, creamos un nuevo diccionario a partir de otro diccionario existente.

other_dict = {
    "a": 23,
    "b": 551,
    "c": 98
}

my_dict = {key: value for (key, value) in other_dict.items()}
print(my_dict)  # {'a': 23, 'b': 551, 'c': 98}

Ejemplo 4: Elevación al cuadrado

En este ejemplo, elevamos al cuadrado los valores de un diccionario existente.
my_dict = {key: value ** 2 for (key, value) in other_dict.items()}
print(my_dict)  # {'a': 529, 'b': 303601, 'c': 9604}

Ejemplo 5: Exclusión de un elemento

En este ejemplo, excluimos un elemento específico del diccionario utilizando una condición en la comprensión.
my_dict = {key: value ** 2 for (key, value) in other_dict.items() if key != "b"}
print(my_dict)  # {'a': 529, 'c': 9604}

Contribución

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, puedes seguir estos pasos:

    Realiza un fork de este repositorio.
    Crea una rama con una descripción clara de tu contribución.
    Realiza los cambios en tu rama.
    Envía una pull request explicando los cambios realizados.
    


