import time
import datetime
import webbrowser
import os
nu = datetime.datetime.now()
Jelani = ("Jelani")
jelani = ("jelani")


print("Hello You!, ik ben Jelani.")
time.sleep(1.5)
print("Wie ben jij? (Voer je naam in en druk op Enter.)")
naam = input()
print("Aan het scannen...")
time.sleep(2)
print("Welkom! Jouw naam is" , naam + "!")
if naam == Jelani or jelani:
    time.sleep(2)
    print("Alhoewel ik een vermoeden heb dat je lult laat ik je wel inloggen, 1 seconde...")
    time.sleep(2.5)
print("Login Time:")
print(nu)
time.sleep(1)
print("Wil je dit programma herstarten of doorgaan naar de video? R om te herstarten, V voor video")
antwoord = input()
if antwoord == ("V") or ("v"):
    webbrowser.open('https://www.youtube.com/watch?v=0nP_qjGpLlo')
if antwoord == ("R") or ("r"):
     os.execv(HelloWorld.py)