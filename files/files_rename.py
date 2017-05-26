import os
f= open("original.txt","w+")
os.rename("original.txt","another.txt")
print(f.name)
