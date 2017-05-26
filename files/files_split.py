f = open("sample1.txt","r+")
data=f.readlines()
print(data)
for line in data :
    words = line.split()
print(words)
