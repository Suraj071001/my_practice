def fabonacci(n) :
    n1 = 0
    n2 = 1
    if n<=2 :
        print("Enter number greater than 2")
    else :
        for i in range(1,n+1) :
            print(n1,end=" ")
            n3 = n2 + n1
            n1 = n2
            n2 = n3
n = int(input("Enter number for fabonacci series :"))
fabonacci(n)

