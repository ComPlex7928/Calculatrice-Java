a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a+b>c and a+c> b and b+c>a:
    print("Ces longueurs peuvent former un triangle.")
    if a==b==c:
        print("C'est un triangle équilatéral.")
    elif a==b or a==c or b==c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("C'est un triangle rectangle isocèle.")
        else:
            print("C'est un triangle isocèle.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Ce triangle est rectangle.")
else:
    print("Ces longueurs ne peuvent pas former un triangle.")
