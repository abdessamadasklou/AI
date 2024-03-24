def entier(n):
   S=0
   for i in range (1,n):
      if n%i==0:
        S += i
        return S
n= int(input("entrez n:"))
if entier(n) :
   print(n,"est un nbr parfait")
else:
   print(n,"n'est pas parfait")