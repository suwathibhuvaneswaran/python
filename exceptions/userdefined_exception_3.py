class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
        print(self.args)
 
try:
    raise Networkerror("Error")
 
except Networkerror as e:
    print (e.args)
