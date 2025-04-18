f= open("poem.txt")

text= f.read()

if("twinkle" in text):
    print("It is present")
else:
    print("It is not present")
