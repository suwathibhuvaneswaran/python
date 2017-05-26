f = open("prime.txt","r+")
data = f.readlines()
print(data[0])
data = list((map(int,data[0].split(" "))))
print(data)
print(len(data))
flag = 0
for i in range(0,len(data)) :
    print("num  :",data[i])
    num = data[i]
    if num >1 :
        for j in range(2,num) :
            if num%j == 0 :
                flag=1
                break
            else :
                flag = 0
    elif num==2:
        flag = 1
    else :
       flag = 0
    if flag == 1:
        print("not prime")
    else :
        print("prime")
f.close()
