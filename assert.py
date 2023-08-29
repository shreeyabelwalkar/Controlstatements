#x=10
x=int(input('Enter any number greater than 1:'))
try:
    assert (x>1)
    print("value of x=",x)
except AssertionError:
    print("Wrong value of input")