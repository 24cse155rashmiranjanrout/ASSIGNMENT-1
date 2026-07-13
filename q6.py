def number(a,b,c):
    if(a>b and a>c):
        print("a is greatest")
    elif(b>=c):
        print("b is greatest")
    else:
        print("c is greatest")
a= int(input("Enter the number"))
b= int(input("Enter the number"))
c= int(input("Enter the number"))
print("greatest number=",number(a,b,c))
