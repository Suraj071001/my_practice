a = True
while a :
    c = input("you wanna print employee details enter :\t'y' for 'yes', \t'n' for 'no':")
    if c == "y" :
        name = input("Enter the name of employee : ")
        age = input("Enter the age of employee : ")
        post = input("Enter the work post of employee : ")
        print("Name :",name)
        print("Age :",age)
        print("Post :",post)
    elif c == "n":
        a = False


