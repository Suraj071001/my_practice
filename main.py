"""____PROGRAM FOR FINDING ROOTS OF QUADRATIC EQUATION"""
print("General quadratic eqn : (ax^2 + bx +c)")
a = int(input("enter the cofficient of x^2 : "))
b = int(input("enter the cofficient of x : "))
c = int(input("enter the constant term : "))
print("Quadratic eqn : ("+str(a)+"x^2 + "+str(b)+"x +"+str(c)+")")
D = (b**2) - 4*a*c
print("Discriminant of eqn(D) :",D)
if D>0 :
    x1 =(-b + (D)**(1/2))/2*a
    x2 =(-b - (D)**(1/2))/2*a
    print("Eqn has two real roots : ",x1,",",x2)
elif D==0 :
    x1 = (-b + (D)**1/2)/2*a
    print("Eqn has two equal roots : ",x1)
elif D<0 :
    print("Eqn has no real roots.")

