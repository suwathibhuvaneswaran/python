with open("hello.txt","a+") as f:
    f.seek(0)
    print("before read")
    print(f.read())
    f.write("karpagam dons")
    print("after append")
    f.seek(0)
    print(f.read())
    f.close()

'''with open("hello.txt","w+") as f:
    f.write("sankavi")
    f.seek(0)
    print(f.read())'''
