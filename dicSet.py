# Dictionaries store key-value pairs. Sets store unique values.
student = {"name": "Asha", "age": 20}
colors = {"red", "green", "blue","blue"} #set
print(student,colors)
print(f"{student}\n{colors}")

# Python does not maintain the insertion order of elements in a set.
# Internally, sets are implemented using hash tables, which means the order is determined by the hash values of the elements — not the order you added them.