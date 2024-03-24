import math
def equa2 (a,b,c):
    d= (b**2)-4*a*c
    if (d<0):
        print("y a pas de solution")
    elif (d==0):
        X= -b/2*a 
        print("il ya une seul solution :",X)
    elif (d>0):
        X1= (-b+ math.sqrt (d))/(2*a)
        X2= (-b- math.sqrt (d))/(2*a)
        print("1er solution est :",X1,"2eme solution est :",X2)
a= float(input("entrer la valeur A:"))
b= float(input("entrer la valeur B:"))
c= float (input("entrer la valeur C:"))
equa2(a,b,c)

