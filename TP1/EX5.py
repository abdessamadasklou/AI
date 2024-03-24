def oper(a,b,operateur):
    if operateur == "+":
        print("L'addition de a et b est :", a + b)
    elif operateur == "-":
        print("La soustraction de a et b est :", a - b)
    elif operateur == "*":
        print("La multiplication de a et b est :", a * b)
    elif operateur == "/":
        if (b != 0):
            print("La division de a et b est :", a / b)
        else:
             print('error b doit etre different de 0')
       

a= int(input("entrez la valeur a :"))
b= int(input("entrez la valeur b :"))
operateur= str(input("entez l'operateur + , -, *, ou / :"))
oper(a,b,operateur)