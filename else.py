#lst=[1,2,3,4,5]
#lst = input("Enter the list of element:")
#print
lst=[]
for i in range(10):
    x=int(input())
    lst.append(x)
print(lst)
search = int(input("Enter the element you want to search in the list:"))
for item in lst:
    if search == item:
        print("Element %d is found in the list"%item)
        break
else:
    print("Element is not found in the list")