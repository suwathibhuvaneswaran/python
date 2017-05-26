f = open("dictionary.txt","r")
temp={}
for line in f.readlines() :
    a,b,c= line.split()
    temp[a]=int(b),int(c)
print(temp)
