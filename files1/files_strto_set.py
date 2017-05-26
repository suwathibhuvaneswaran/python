f=open("sample_set.txt","r+")
data =f.readlines()
set_temp=set() 
for i in range(0,len(data)):    
    temp=data[i].strip()
    #print(temp)
    set_temp.update([temp])
    print(set_temp)
    
