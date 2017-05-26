stack=[]
max=3
count = 0
con=int(input("1 to con.."))
while con ==1 :
  print("------------------------------------------")
  print("1--push  2-->pop  3-->top  4-->traversal")
  print("------------------------------------------")
  option=int(input("enter the option :"))
  if option == 1:
      if count < max :
          element = int(input("enter the element --->"))
          stack.append(element)
          print(stack)
          count = count + 1
      else :
          print("stack full")
  elif option == 2:
      if len(stack) > 0:
          pop_ele = stack.pop()          
          print("list after pop  :",stack)
          count = count - 1
      else :
          print("stack underflow")
  elif option == 3:
      if len(stack) > 0:
          print("stack top",stack[-1])          
      else :
          print("stack  empty")
  elif option == 4 :
      if len(stack) != 0:
         print( ' '.join(map(str, stack[::-1])))
      else :
          print("stack empty")
  con=int(input("1 to con.."))
