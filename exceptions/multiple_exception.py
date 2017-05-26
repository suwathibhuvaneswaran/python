try :
    5//0
    count = count + 1
    print("counted")
except (NameError,ZeroDivisionError) :
    print("name error")
    print("Error")
else :
    print("success")
