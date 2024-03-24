def Temps (T):
    h = T // 3600
    r = T % 3600
    m = r//60
    s = r % 60
    print(T, "seconds",h,"heures",m,"minutes",s,"seconds")
T= float(input("entrer le temps T:"))
Temps (T)