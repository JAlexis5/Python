import sys
import time

def callMe(name, number):
	print("1: Ewa")
	time.sleep(1)
	print("2: Fakka" , name)
	time.sleep(2)
	print("1: Alles rustig man bro?")
	time.sleep(2.5)
	print("2: Ja man met jou?")
	time.sleep(2)
	print("1: Je weet zelf al")
	time.sleep(3)
	print("1: Ey maar kom 2 uur station ok")
	time.sleep(1)
	print("1: Is belangrijk")
	time.sleep(1)
	print("2: Isg man")
	time.sleep(3)
	print("2: Geef me ff je nr dan kan ik je zeggen wnr ik aankom ok?")
	time.sleep(5)
	print("1: Ai isg me nr is" , number + ", spreek je later")
	time.sleep(1)
	print("2: Later man")

callMe(sys.argv[1], sys.argv[2])