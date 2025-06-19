# A python program to know how a function can return anotherfunction.
def display():
    def message():
        return "hii..!"
    return message()
a=display()
print(a)