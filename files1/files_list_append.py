f = open("list.txt","r+")
temp = []
data = f.readlines()
print(data)
for word in range(0,len(data)) :
    print(data[word])
    temp.append(data[word].strip())
    
print(temp)
f.close()
