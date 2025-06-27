
# 1. Takes a function as input
# 2. Defines a new function that adds behavior
# 3. Adds behavior before the original function
# 4. Calls the original function
# 5. Adds behavior after the original function
# 6. Returns the new function
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()

# This is syntactic sugar for:
# say_hello = decorator(say_hello)
# Using a decorator makes your code more modular, reusable, and readable, especially in larger applications.