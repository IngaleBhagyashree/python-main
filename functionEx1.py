# A python program to know how to define a function inside another function. 
def dislay(st):
    def hii():
        print("hello")
        return "how r u?"
    res=hii()+st
    return res
x=dislay(" world")
print(x)