def summation(a): 
    if(a<0):
         return 0
    else:
         return a+ summation(a-1)

num= int(input("Enter the number: "))


print(f"Sum of {num} natural number are:",summation(num))