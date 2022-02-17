set1 = set()
set2 = set()
n = int(input("Enter how many elements you want in set :"))

for i in range(n):
    element1 = input(f"Enter element {i + 1} of set1 :")
    set1.add(element1)
print()

for i in range(n):
    element2 = input(f"Enter element {i + 1} of set2 :")
    set2.add(element2)
print("\nset 1 : ",set1)
print("set 2 : ",set2)
print("\nIntersection of set 1 and set 2 :",set1.intersection(set2))
print("union of set 1 and set2 : ",set1.union(set2))
print("Is set 1 disjiont of set2 : ",set1.isdisjoint(set2))
print("Is set 1 subset  of set2 : ",set1.issubset(set2))
print("Difference of set 1 and set2 : ",set1.difference(set2))