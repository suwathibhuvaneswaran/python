try :
    f= open("test.txt","r")
    f.write("file open for encrypted")
except IOError :
    print("Error: cant find file")
else :
    print("file encrypted")
