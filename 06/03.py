a= "Make a lot of money"
b= "buy now"
c= "subscribe this"
d= "click this"

message= input("Enter the comment: ")

if((a in message)or(b in message)or(c in message)or(d in message)):
    print("This message is a spam")
else:
    print("This message is not a spam")
