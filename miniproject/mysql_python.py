import os
import os.path
import datetime
flag = 0
while True :
    first = input("--> ").split()
    if first[0]=="mysql" and len(first)==4 :
        if first[1] == "-u" :
            if first[2] =="-p" :
                if first[3] =="root" :
                    print ("USERNAME : root")
                    password=input("PASSWORD :")
                    if password ==  "root" :
                        flag = 1
                        break
                    else :
                        print("Invalid Password")
            else :
                print("Error in sql line")
        else :
            print("Error in sql line")
    else :
        print("Error in sql line")
        
if flag == 1:
    print("            WELCOM TO MYSQL USER PROMPT  ")
    print("Your MySql user id is 18 ")
    print("MySQL Version 5.7.12")
    print("Type help to know more ")
    print(" ")
    while True :
        try:
            need = input("mysql> ").split()            
            if need[0] == "help" : #help command
                print("-"*45)
                print(''' create : Table Creation
                Syntax : create table tablename ''')
                print("-"*45)
                print(''' view   : View Table 
                Syntax : view tablename''')
                print("-"*45)
                print(''' Insert : Insert into table
                Syntax : insert into table name ''')
                print("-"*45)
                print(''' Delete : Table Deletion
                Syntax : drop table tablename ''')
                print("-"*45)
                print(''' Rename : Rename tables 
                Syntax : rename source table  destination table ''')
                print("-"*45)
                print(''' Descriptions : Table modification details
                Syntax : table details tablename ''')
                print("-"*45)
                print(''' Tables : List of tables available
                Syntax : show tables ''')
                print("-"*45)                
        
            elif need[0]=="create" : #table creation
                try:
                    if need[1]=="table" :
                        try :
                            if (len(need[2])>0) and len(need)==3:                    
                                file_name=need[2]+".txt"
                                
                                if os.path.isfile(file_name) == True :
                                    print( " table",file_name," already created")
                                    print("time " ,os.path.getmtime(file_name))
                                else :
                                    f = open(file_name ,"w")
                                    print("table created <0.0s> ")
                                f.close()
                            else :
                                print("Unknown Command")                    
                        except :
                            print("specify the table name to be created ")
                    else : 
                        print("Invalid syntax")
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
                            print("table not exists")
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
                                    f.write("\n")
                                    f.write(content)
                                    f.close()
                                    print("table affected <0.0s> ")
                                else :
                                    print("File not exists ")
                            else :
                                print("Unknown Command")
                        except :
                            print("specify the table name to view ")
                    else :
                        print("Invalid syntax")
                except :
                    print("Invalid Syntax")

            elif need[0] == "drop" : #table deletion
                try :
                    if need[1] == "table" and len(need) ==3 :
                        if len(need[2]) > 0 and len(need)==3:
                            file_name = need[2]+".txt"
                            if os.path.isfile(file_name) == True:
                                os.remove(file_name)
                                print("table deleted <0.0)s")
                            else :
                                print("Table not exists")
                        else :
                            print("Error in syntax")
                    else :
                        print("Invalid syntax")
                except :
                    print("Invalid syntax")

            elif need[0]== "rename": #rename table
                try :
                    if len(need[1])> 0 and len(need)==3 :        
                        try :
                            if (len(need[2])> 0) and len(need)==3:                
                                file_name=need[1]+".txt"
                                file_rename = need[2]+".txt"
                                if os.path.isfile(file_name) == True:
                                    os.rename(file_name ,file_rename)
                                    print("table rename affected (0.0s)")
                                else :
                                    print("table not exists")
                            else :
                                print("Invalid syntax1")
                        except :
                            print("Invalid syntax2")
                    else :
                        print("Invalid syntax3")
                except :
                    print("Invalis syntax4")
                    
            elif need[0]== "show" : #list of tables
                try :
                    if need[1] == "tables" :
                        print("+"+"-"*10+"+")
                        print("| tables   |")
                        print("+"+"-"*10+"+")
                        for file in os.listdir():                    
                            if file.endswith(".txt"):                            
                                print("|"+"  " '{0:8s}|'.format(file[:-4]))
                                print("+"+"-"*10+"+")
                    else :
                        print("Error.Expected 'tables' ")
                except :
                    print("Invalid Syntax")

            elif need[0]=="table" : #table description
                file_name=need[2]+".txt"
                try :
                    if need[1] == "details" :
                        def modification_date(file_name):
                            t = os.path.getmtime(file_name)
                            return datetime.datetime.fromtimestamp(t)
                        
                        if len(need[2]) > 0 and len(need)==3 :
                            file_name=need[2]+".txt"
                            if os.path.isfile(file_name) == True:
                                print(modification_date(file_name))
                            else :
                                print("table not exists")
                        else :
                            print("Invalid syntax1")
                    else :
                        print("Invallid syntax2")
                except :
                    print("Invalid syntax3 ")

          
            elif need[0] == "exit" :
                break
            else :
                print("Unknown Command")
        except :
            print("Unknown Command ") 
              
