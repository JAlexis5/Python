import time
import datetime
import sys

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
if naam == Jelani:
    time.sleep(2)
    print("Alhoewel ik een vermoeden heb dat je lult laat ik je wel inloggen, 1 seconde...")
    time.sleep(2.5)
if naam == jelani:
    time.sleep(2)
    print("Alhoewel ik een vermoeden heb dat je lult laat ik je wel inloggen, 1 seconde...")
    time.sleep(2.5)

print("Login Time:")
print(nu)
time.sleep(1)

print("D om door te gaan, H om te sluiten.") 
antwoord = input()
if antwoord == "h" or "H":
    print("Herstart door het bestand weer te openen.")
    time.sleep(2.5)
    sys.exit()


time.sleep(2)  
print("Vraag 1:")
time.sleep(1.5)
print("Hoe oud denk je dat ik ben?")
print("A: 15")
print("B: 16")
print("C: 17")
leeftijd = input()
if leeftijd != A:
    print("Fout! Probeer het nog eens.")