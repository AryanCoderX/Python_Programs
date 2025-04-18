import pyttsx3 #The engine speaks whatever is said to speak
engine = pyttsx3.init()
name= input("Enter your name: ")
engine.say(name+" Good Morning")
engine.runAndWait()

print(name+" Good Morning") #this was used before f string came in python

print(f"{name} Good Morning") #this is how we use a f string