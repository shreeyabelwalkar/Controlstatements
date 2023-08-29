for i in range(3):
    for j in range (4):
        print("i=",i, '\t',"j=",j)
    print('------------------------------')


x=1
while(x==1):
    x+=1
    while(x<=10):
        print("x=",x)
        x+=1
    print("end of the program")

x=1
while(x<=10):
    print("square of %i=%i"%(x,x*x))
    x+=1

for i in range(1,11):
    for j in range(1,11):
        print("{:8}".format(i*j),end='')
    print()