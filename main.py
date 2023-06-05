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
