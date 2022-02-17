def prime_no(n) :
    if n<2 :
        print("Enter no. greater than 1")
    elif n==2 :
        print("Number 2 is prime number.")
    else :
        for i in range(2,n) :
            if n%i!=0 :
                a = "Number " + str(n) + " is prime number."
                continue
            else :
                a = "Number " + str(n) + " is not prime number."
                break
        print(a)
n=int(input("Enter no. for checking prime no. : "))
prime_no(n)
