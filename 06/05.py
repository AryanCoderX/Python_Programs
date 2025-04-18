name =[ "Aryan", "Bhavya", "Chavi", "Drishti", "Rimili"]
namecheck= input("Enter the name to be checked: ")

i= 0
while(i<4):
    
    if(namecheck==name[i]):
        print("Name is present")
        break
    i+=1
else:
        print("Name is not present")