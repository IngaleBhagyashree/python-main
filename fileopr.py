f = open('data.txt','r')
print(f.read())
print(f.readline(),end="")
print("______")
f.close()
print("'readed and closed'")

f1= open('abc','w')
f1.write("helloo")
f1.write(" people")
f1.write('abc','a')
f1.write(" use laptop ")
f1.write("bye")

for data in f:
    print(data)

for data in f:
    f1.write(data)

f2=open('wallpaper.jpeg','rb')
# print(f2.read)
for i in f2:
    print(i)
    
f3=open('mywallpaper.jpeg','wb')
for i in f2:
    f3.write(i)