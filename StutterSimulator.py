import time
woorden = ""

print("Stutter Simulator")
print("by Jelani Alexis")

zin  = input()
algemeneLijst = zin.split(' ')
for woord in algemeneLijst:
    if len(woord) >3:
        stotter = woord[:2] + ".."
    woorden += (stotter + " " + woord + " ")
print(woorden)
time.sleep(5)
