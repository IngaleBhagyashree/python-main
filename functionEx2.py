#  A python program to know how to pass a function as parameter to another function.
def display(f):
    return "hello...! "+f
def message():
        return"how R U?"
X=display(message())
print(X)