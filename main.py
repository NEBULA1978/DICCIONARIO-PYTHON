my_dict = {"Juan": {"edad": 30, "casado": True}}

print(my_dict)#{'Juan': {'edad': 30, 'casado': True}}

# Dict comprehension(Arreglos)
name=["Alex","Anna","Petter","Angela"]
age=[22,33,43,51]

my_dict ={name[i]:age[i] for i in range(len(name))}

print(my_dict)#{'Alex': 22, 'Anna': 33, 'Petter': 43, 'Angela': 51}