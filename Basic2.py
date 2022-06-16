import time
x=input("Enter Your years Brith day ")
def cal(x):
    if int(x)>= 2022:
        print ("your Age very young .....")
    else:
        print (f"your Age {int(2022)-int(x)} Years Old ")
    
cal(x)