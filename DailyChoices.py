import time

print("You wake up to your alarm ringing very loudly at 5:30 AM. Do you SNOOZE or GETUP?")
choice1 = input()
if choice1 == 'GETUP':
    print("You jump out of bed, and feel like shit because it's Monday.")
elif choice1 == 'SNOOZE':
    print("You sleep in for another 2 hours, and eventually wake up")
time.sleep(2)

print("You're very hungry, so what are you having for breakfast? FRIEDEGG or GRANOLA?")
choice2 = input()
if choice2 == 'FRIEDEGG':
    print("You proceed to fry an egg and eat it. It was delicious.")
elif choice2 == 'GRANOLA':
    print("You proceed to pour some milk in a bowl and then add granola like the psychopath you are.")
time.sleep(2)

print("You haven't showered in 3 days. Are you going to SHOWER or NOT?")
choice3 = input()
if choice3 == 'SHOWER':
    print("You decide to shower, and feel very clean.")
elif choice3 == 'NOT':
    print("You decide not to shower, you filthy boy.")
time.sleep(2)

print("Are you going to wear a HOODIE or a SUIT?")
choice4 = input()
if choice4 == 'HOODIE':
    print("You put on a hoodie and go out with swag.")
elif choice4 == 'SUIT':
    print("You put on a nice suit and go out looking like a classy gentleman.")
    if choice3 ==  'NOT':
        time.sleep(2)
        print("Too bad you didn't shower, you would've been the ultimate gentleman at work.")
time.sleep(2)

print("Are you going to work by BUS or by BIKE?")
choice5 = input()
if choice5 == 'BUS':
    print("You take the bus and get to work on time.")
elif choice5 == 'BIKE':
    print("You grab your bike and ride it to work, but since you're so damn slow you come in 10 minutes late. Hey, at least you burnt like 100 calories right?")
    