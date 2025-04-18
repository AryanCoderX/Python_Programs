maths = int(input("Enter your maths marks: "))
science = int(input("Enter your science marks: "))
computer = int(input("Enter your computer marks: "))

if(maths>=33 and science>=33 and computer>=33):
    if((maths+science+computer)/3>= 40):
        print("Congratulations you have passed")
    else:
        print("You have passed in all subject but failed over all")

else:
    print("You have failed in a subject")