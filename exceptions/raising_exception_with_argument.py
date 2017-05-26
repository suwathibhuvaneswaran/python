def functionName( level ):
   if level <1:
      raise Exception(level)      
   return level

try:
   l = functionName(-10)
   print ("level = ",l)
except Exception as e:
   print ("error in level argument",e.args[0])
