a= int(input("Enter 1st number: "))
b= int(input("Enter 2nd number: "))
c= int(input("Enter 3rd number: "))
d= int(input("Enter 4th number: "))

if(a>b and a>c and a>d):
    print("1st number is the greatest",a)
elif(b>a and b>c and b>d):
    print("2nd number is the greatest",b) 
elif(c>a and c>b and c>d):
    print("3rd number is the greatest",c) 
elif(d>a and d>b and d>c):
    print("4th number is the greatest",d)    