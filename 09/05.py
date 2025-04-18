f =open("donkey2.txt","r")
text= f.read()

f.close()

words = ["donkey", "brat", "foolish", "idiot", "beast"]


for word in  words:
    text= text.replace(word,"######")

f= open("donkey2.txt","w")

f.write(text)

f.close()