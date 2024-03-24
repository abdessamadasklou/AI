def impot (age,sexe):
    if(sexe=="homme" and age >= 20):
        print("il faut que vous payez les impots")
    elif(sexe=="femme" and age >= 18 and age < 35):
        print("il faut que vous payez les impots")
    else :
        print("live free")
age= float(input("entrez votre age :"))
sexe= str(input("votre sexe :"))
impot(age,sexe)