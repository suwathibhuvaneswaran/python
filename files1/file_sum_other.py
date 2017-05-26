f=open("first.txt","r")
total = 0
for data in f:
    num = int(data)
    total = num + total
print("sum",total)
f.close()
f=open("second.txt","w+")
total=str(total)
f.write(total)
f.close()
