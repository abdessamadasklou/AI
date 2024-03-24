def tri(T):
    if T[0] > T[9]:
        print("non trié")
    else:
        for i in range(len(T) - 1):
            if T[i] > T[i+1]:
                print("non trié")
                return
        print("trié")

T = []
for i in range(10):
    x = int(input("Entrez un élément pour le tableau T : "))
    T.append(x)

tri(T)
