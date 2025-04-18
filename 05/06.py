language = {}
i=0
while(i<5):
    language.update({input("Enter your name: "):input("Enter your fav language: ")})
    i+=1

print(language)