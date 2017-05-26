try:
   fh = open("testfi", "r")
   try:
      fh  = open("testf", "r")   
      fh.close()
   except IOError :
          print("file not open")
except IOError:
   print ("Error: can\'t find file or read data")
finally :
    print("printed")
