import webbrowser
import time



startnr = 1000
while startnr > 10:
	print(startnr)
	time.sleep(0.01)
	startnr -= 1

while startnr < 11:
	print(startnr)
	time.sleep(1)
	startnr -= 1
	if startnr == -1:
		break

webbrowser.open("https://www.youtube.com/watch?v=uY_gmP66EFA")