n=3

for i in range(1,n+1):
    if(i!=2):
         print("*"*n)
    else:
         a=n-i
         print("*"*a + " "*a + "*"*a)