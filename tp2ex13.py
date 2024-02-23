A=int(input("donner l'année :"))
if ((A%4==0) and A%100!=0 ):
    print(A,"est bissextile")
elif (A%400==0):
        print(A,"est bissextile")
else:
      print(A,"n'est pas bissextile")
