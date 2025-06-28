# Create iterators using yield
def gen():
    for i in range(3):
        yield i
# value=gen()
for value in gen():
    print(value)
         

        