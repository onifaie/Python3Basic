#this coment about this command line code 

x1=input("enter the frist number ")
x2=input ("enter the scand number ")
print (int(x1)+int(x2))

def result(x):
    
    if x>=50 and x<=60:
        print ("fiuld")
    if x>=60 and x<=70:
        print ("Good")
    if x>=70 and x<=80:
        print ("Very Good ")
    if x>=90 and x<=100:
        print ("Exlant")
   
        
  #This varible to input value inside x  
x=input("enter the Your Mark  ")    
#this call funcation and send x as intger value to testing mark 
result(int(x))    