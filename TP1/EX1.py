def moy(A,B,C):
     M= (A+B+C)/3
     if(A or B or C)>20:
             print("les notes entre 0 et 20")
     else:
             if M>=16:
                     print("le moyenne", M,"tres bien freind")
             elif M>=14 and M<16:
                     print("le moyenne",M,"bien freind")
             elif M>=12 and M<14:
                     print("le moyenne",M,"assez bien freind")
             elif M>=10 and M<12:
                     print("le moyenne",M,"passable freind")
             else :
                     print("le moyenne",M,"Insuffisant friend")
A= float(input("entrer la note A:"))
B= float(input("entrer la note B:"))
C= float(input("entrer la note C:"))
moy(A,B,C)
