def factorial(n) :
    f=1
    if n<0 :
        print("Enter poistive number")
    elif n==0 :
        print("Factorial of 0 is 1.")
    else :
        for i in range(1,n + 1) :
            f = f * i
        print("Factorial of "+str(n)+" is :",f)
n = int(input("Enter number for factorial : "))
factorial(n)

