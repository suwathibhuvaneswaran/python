import os.path
print("            WELCOM TO MYSQL USER PROMPT  ")
print("Your MySql user id is 18 ")
print("MySQL Version 5.7.12")
print("Type help to know more ")
print(" ")
while True :
    try:
        need = input("mysql> ").split()    
        if need[0] == "help" : #help command
            print("-"*43)
            print(''' create : Table Creation
            Syntax : create table tablename ''')
            print("-"*43)
            print(''' view   : View Table 
            Syntax : view tablename''')
            print("-"*43)
            print(''' Insert : Insert into table
            Syntax : insert into table name ''')
            print("-"*43)
            print(''' Tables : List of tables available
            Syntax : show tables ''')
            print("-"*43)
    
        elif need[0]=="create" : #table creation
            try:
                if need[1]=="table" :
                    try :
                        if (len(need[2])>0) and len(need)==3:                    
                            file_name=need[2]+".txt"
                            
                            if os.path.isfile(file_name) == True :
                                print( " table",file_name," already created")
                            else :
                                f = open(file_name ,"w")
                                print("table created <0.0s> ")
                            f.close()
                        else :
                            print("Unknown Command")
                    except :
                        print("specify the table name to be created ")
            except :
                 print("Error in syntax.Expected 'table' ")

        elif need[0]== "view" :  # view table
            try :
                file_name=need[1]+".txt"
                if len(need[1]) > 0 and len(need)== 2:
                    if os.path.isfile(file_name) == True :
                        #print( " table exisis")
                        f=open(file_name,"r")
                        if os.stat(file_name).st_size == 0 :
                            print("empty set")
                        else :
                             print("+"+"-"*13+"+")
                        for lines in f.readlines():
                            some=lines.strip()
                            #print(lines.strip())
                            print("|" '{0:11s}  |'.format(some))
                            print("+"+"-"*13+"+")
                else :
                    print("Unknown Command")
            except :
                print("Table not exists")

        elif need[0]== "insert" : #insert into table
            try :
                if need[1]=="into" :        
                    try :
                        if (len(need[2])> 0) and len(need)==3:                
                            file_name=need[2]+".txt"                    
                            if os.path.isfile(file_name) == True:
                                content= input()
                                f = open(file_name,"a+")                    
                                f.write(content)
                                f.close()
                                print("table affected <0.0s> ")
                            else :
                                print("File not exists ")
                        else :
                            print("Unknown Command")
                    except :
                        print("specify the table name to view ")
            except :
                print("Invalid Syntax")

        elif need[0]== "show" : #list of tables
            try :
                if need[1] == "tables" :
                    print("+"+"-"*10+"+")
                    print("| tables   |")
                    print("+"+"-"*10+"+")
                    for file in os.listdir():                    
                        if file.endswith(".txt"):
                            #print(" "+file[:-4] +"|")
                            print("|"+"  " '{0:8s}|'.format(file[:-4]))
                            print("+"+"-"*10+"+")
                else :
                    print("Error.Expected 'tables' ")
            except :
                print("Invalid Syntax")               

      
        elif need[0] == "exit" :
            break
        else :
            print("Unknown Command")
    except :
        print("Unknown Command ") 
          
