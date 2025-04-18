num= int(input("Enter the number to be checked: "))

i=2
while(i*i<=num):
    if(num%i==0):
        print("Not a Prime Number")
        break
    i+=1
else:
    print("Prime Number")