import random

def shuffle1(word1):
	random1 = ''.join(random.sample(word1, len(word1)))
	return(random1)

def shuffle2(word2):
	random2 = ''.join(random.sample(word2, len(word2)))
	return(random2)

def shuffle3(word3):
	random3 = ''.join(random.sample(word3, len(word3)))
	return(random3)

geshuffeldeString1 = shuffle1("Dit is een zin")
geshuffeldeString2 = shuffle2("Dit is ook een zin")
geshuffeldeString3 = shuffle3("Dit is nog een zin")
print(geshuffeldeString1)
print(geshuffeldeString2)
print(geshuffeldeString3)