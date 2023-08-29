x=1
while x<=100:
    print(x)
    x+=2
print("End of the programme")

x=150
while x>=101:
    print(x)
    x-=2
print("End of the programme")

x=100
while x>=100 and x<=200:
    print(x)
    x+=2

m,n=[int(i) for i in input("Enter the minimum and maximum number:").split()]
x=m
if x%2!=0:
    x=x+1

while x>=m and x<=n:
    print(x)
    x+=2
print("End of the programme")



