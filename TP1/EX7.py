def SC(n):
    c=0
    for i in range (1,n+1):
        c += i**2
    print(c)
n= int(input("entrez la valeur n :"))
SC(n)