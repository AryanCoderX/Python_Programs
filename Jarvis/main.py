import speech_recognition as sr
import webbrowser
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


if __name__=="__main__":