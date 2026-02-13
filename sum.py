n=int(input("Enter the size of the list:"))
lst=[]
print("Enter elements")
for i in range(0,n):
    lst.append(int(input(" ")))
print("Sum of the elements is:",sum(lst))
