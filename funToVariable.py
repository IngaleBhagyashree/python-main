# A python program to see how to assign a function to a variable.
def display(st):
    return "hai" + st

x = display("cse")
print(x)

greet = display #Assigning Function to a Variable
print(greet("ECE"))  # Output: haiECE
