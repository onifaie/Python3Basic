import time
x=input("Enter Your years Brith day ")
r=[12,44,55,66]

def cal(x):
    if int(x)>= 2022:
        print ("your Age very young .....")
    else:
        print (f"your Age {int(2022)-int(x)} Years Old ")
    
cal(x)

xy=[10,20,44,66,2]

def addtolist():
    for i in list(xy):
        if i == 66:
            continue
        else:
            print (i)
        
    
    
    
addtolist()