f=open("hello.txt","r+")
print(len(f.read()))

print(f.read())
#f.seek(2)
f.seek(-10,2)
#print(f.seek(0,1))
print(f.read())

