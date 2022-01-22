import json
print("1. Signup \n2. Login ")

ch=input("choose what you want : ")

if ch=="1":
    username=input("enter username : ")
    password=input("enter password : ")
    if (password>="a" and password<="z") or (password>="A" and password<="Z") or (password<="0" and password>"9") or (password=="@",password=="#"):
        if len(password)>=6 and len(password)>=12:
            print("correct password")
        else:
            print("incorrect password","Try again!")
        
    description=input("enter description : ")
    dob=input("enter dob : ")
    hobbies=input("enter your hobbies : ")
    gender=input("enter gender : ")

    b=[username]
    c=[password]
    d=[description]
    e=[dob]
    f=[hobbies]
    g=[gender]
        
    i=0
        
    dict2={}
    dict3={}
    dict4={}
    dict5={}
    dict6={}
    dict7={}
    dict8={}
    dict9={}
    dict10={}
    dict10={}
    dict11={}
    dict12={}
    dict13={}
    dict14={}
        
    while i<len(b):
        dict2=username
        dict3=password
        dict4=description
        dict5=dob
        dict6=hobbies
        dict7=gender
        i=i+1
    dict8["username"]=dict2
    dict9["password"]=dict3
    dict10["description"]=dict4
    dict11["dob"]=dict5
    dict12["hobbies"]=dict6
    dict13["gender"]=dict7

    dict14.update(dict8)
    dict14.update(dict9)
    dict14.update(dict10)
    dict14.update(dict11)
    dict14.update(dict12)
    dict14.update(dict13)

    x=json.dumps(dict14)
    print(x)
    with open("linu.json","w") as file:
       json.dump(dict14,file,indent=4)


elif ch=="2":
    username=input("enter username : ")
    password=input("enter password : ")
    if (password>="a" and password<="z") or (password>="A" and password<="Z") or (password<="0" and password>"9") or (password=="@",password=="#"):
        if len(password)>=6 and len(password)>=12:
            print("correct password")
        else:
            print("incorrect password","Try again!")

    a=[username]
    b=[password]
    i=0
    dict1={}
    dict2={}
    dict3={}
    dict4={}
    dict5={}
    while i<len(a):
        dict1=username
        dict2=password
        i=i+1
    dict3["username"]=dict1
    dict4["password"]=dict2
    dict5.update(dict3)
    dict5.update(dict4)

    x=json.dumps(dict5)
    print(x)

    if username in "linu.json":
        print("username is already exit")
    elif username not in "linu.json":
        print("username is allow")
    with open("linu.json","w") as file:
        # if "username" in "linu.json":
        #     print("username is already exit")
        # elif "username" not in "linu.json":
        #     print("username is allow")
        json.dump(dict5,file,indent=4)