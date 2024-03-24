def produit_scalaire(v1, v2):
    if len(v1) != len(v2):
        return "Les vecteurs doivent être de même longueur pour calculer le produit scalaire."
    
    produit = 0
    for i in range(len(v1)):
        produit += v1[i] * v2[i]
    
    return produit

N = int(input("Entrez la taille des vecteurs : "))

v1 = []
v2 = []
for i in range(N):
    composante = float(input("Entrez les composantes du premier vecteur : "))
    v1.append(composante)
for i in range(N):
    composante = float(input("Entrez les composantes du deuxième vecteur : "))
    v2.append(composante)

resultat = produit_scalaire(v1, v2)
print("Le produit scalaire des deux vecteurs est :", resultat)
