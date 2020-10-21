# Doel:
# Hoger / Lager spelletje moet als volgt werken.
# De speler wordt een willekeurig getal tussen 1 en 10 getoond
# De speler moet daarna raden of het volgende getal hoger of lager wordt
# Aan het einde moet de speler weten of hij/zij gewonnen heeft

import random
import time

print("RNG Higher/Lower")
print("By Jelani Alexis")
time.sleep(1.5)
prnit("Generating number...")
time.sleep(2)

randomnr = random.randrange(1, 11)
print(randomnr)
time.sleep(2.5)

print("Guess if the next number will be higher or lower. H for higher, L for lower.")
answer = input()
print("Generating number...")
print(randomnr)
time.sleep(1)
if answer = "H":
    