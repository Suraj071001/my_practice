D = {}
n = int(input("Enter how many students marks you wanna add :"))
s = int(input("Enter how many subjects marks do you wanna add :"))
def add_student(n) :
    for i in range(n) :
        name = input("\nEnter name of student :")
        d = {}
        D[name] = d
        for j in range(s) :
            subject = input("\nEnter name of subject :")
            marks = input("Enter marks :")
            d[subject] = marks
add_student(n)

for key,value in D.items() :
    print("\nMarks of ",key,":")
    for k,v in value.items() :
        print(k,"marks :",v)