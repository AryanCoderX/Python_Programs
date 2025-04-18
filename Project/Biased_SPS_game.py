import pyttsx3 #The engine speaks whatever is said to speak
import random
engine = pyttsx3.init()


name= input("Enter your name: ")

if(name==""):
    name="user"

engine.say(f"Hello {name}")
engine.runAndWait()
engine.say("This is a Stone paper scissors game")
engine.runAndWait()


        
engine.say("In the Stone-Paper-Scissors game, both you and computer choose one of the three options—Stone, Paper, or Scissors—at the same time. Stone beats Scissors because a rock can crush scissors, Scissors beat Paper because scissors can cut paper, and Paper beats Stone because paper can wrap a rock. If both players choose the same option, the game results in a draw.")
engine.runAndWait()

print("In the Stone-Paper-Scissors game, both players choose one of the three options—Stone, Paper, or Scissors—at the same time. Stone beats Scissors because a rock can crush scissors, Scissors beat Paper because scissors can cut paper, and Paper beats Stone because paper can wrap a rock. If both players choose the same option, the game results in a draw.")
engine.runAndWait()

win=0
lose=0
draw=0 

def game(option1,option2):
    if(option1==option2):
        return 0
    
    if(option2==1):
        if(option1==0):
            return 1
        elif(option1==-1):
            return -1
    
    elif(option2==0):
        if(option1==1):
            return -1
        elif(option1==-1):
            return 1
        
    elif(option2==-1):
        if(option1==0):
            return -1
        elif(option1==1):
            return 1

while(True):
    engine.say("Press 0 if you want to exit the game Press any other number if you want to play the game")
    engine.runAndWait()
    escape= int(input("Press 0 if you want to exit the game Press any other number if you want to play the game: "))
    if(escape==0):
        break
    else:   
        engine.say('''Enter "St" for Stone similarly Enter "P" for paper similarly Enter "Sc" for Scissors''')
        engine.runAndWait()


        user_input= input('''Enter "St" for Stone similarly Enter "P" for paper similarly Enter "Sc" for Scissors: ''')

        if(user_input!="St" and user_input!="P" and user_input!="Sc"):
            engine.say("What the Fuck You entered an invalid input take this game seriously")
            engine.runAndWait()
            print("You entered an invalid input take this game seriously")
            continue

        option={"St":1,"P":0,"Sc":-1}
        option_rev={1:"Stone",0:"Paper",-1:"Scissors"}

        computer_choice= random.choice([1, 0, -1])
        user_choice= option.get(user_input)


        engine.say(f"Your choice was {option_rev.get(user_choice)}")
        engine.runAndWait()
        print(f"Your choice was {option_rev.get(user_choice)}")
        engine.say(f"Computer choice was {option_rev.get(computer_choice)}")
        engine.runAndWait()
        print(f"Computer choice was {option_rev.get(computer_choice)}")

        
        if(game(user_choice,computer_choice)==0):
            if(name=="Rimili"):
                win+=1
                engine.say("Congratulations you have won Howww?? because you are my Crush and the game was made by Aryan ofcourse it is biased")
                engine.runAndWait()
            else:
                draw+=1
                engine.say("Its a draw lets play again")
                engine.runAndWait()
                print("Its a draw lets play again")
        elif(game(user_choice,computer_choice)==1):
            win+=1
            engine.say("Congratulations you have won but its not the end i will win next time for sure lets play again")
            engine.runAndWait()
            print("Congratulations you have won but its not the end i will win next time for sure lets play again")
        elif(game(user_choice,computer_choice)==-1):
            if(name=="Rimili"):
                win+=1
                engine.say("Congratulations you have won Howww?? because you are my crush and the game was made by Aryan ofcourse it is biased")
                engine.runAndWait()
                print("Congratulations you have won Howww?? because you are my crush and the game was made by Aryan ofcourse it is biased")
            else:
                lose+=1
                engine.say("Oh no you lost but dont worry lets play again and this time i hope you win")
                engine.runAndWait()
                print("Oh no you lost but dont worry lets play again and this time i hope you win")


print(f"You won {win} times")
engine.say(f"You won {win} times")
engine.runAndWait()
print(f"You lost {lose} times")
engine.say(f"You lost {lose} times")
engine.runAndWait()
print(f"You got draw {draw} times")
engine.say(f"You draw {draw} times")
engine.runAndWait()


print(f"Thankyou for playing the game")
engine.say("Thankyou for playing the game")
engine.runAndWait()
