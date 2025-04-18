f= open("donkey.txt", "r")

text= f.read()
f.close()


f= open("donkey.txt", "w")

text_new= text.replace("donkey", "######")
f.write(text_new)

f.close()
