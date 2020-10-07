import time

print("Gemaakt door Jelani Alexis.")
print()
time.sleep(2)

tekstOpdracht1 = 'De Python lessen worden gegeven voor Erik, Erwin en ook door Hidde'
voornaam1 = tekstOpdracht1[37:41]
voornaam2 = tekstOpdracht1[43:48]
voornaam3 = tekstOpdracht1[61:66]

print("Opdracht 1: Voornamen uit de volgende tekst halen:")
print(tekstOpdracht1)
print()
time.sleep(1)
print("De namen zijn" , voornaam1 + "," , voornaam2 , "en " + voornaam3)
time.sleep(2)
print()
print()

tekstOpdracht2 = 'SD vakken zijn Python, UXD, Frontend development en Backend development en nog veel meer ...'
vaknaam1 = tekstOpdracht2[15:21]
vaknaam2 = tekstOpdracht2[23:26]
vaknaam3 = tekstOpdracht2[28:48]
vaknaam4 = tekstOpdracht2[52:71]

print("Opdracht 2: Vakken uit de volgende tekst halen:")
print(tekstOpdracht2)
print()
time.sleep(1)
print("De vakken heten" , vaknaam1 + "," , vaknaam2 + "," , vaknaam3 , "en" , vaknaam4)
time.sleep(2)
print()
print()

tekstOpdracht3 = 'Wat is hier het laatste woord?'
laatste3Woorden = tekstOpdracht3[24:30]

print("Opdracht 3: Laatste 6 letters uit de volgende tekst halen:")
print(tekstOpdracht3)
print()
time.sleep(1)
print("De laatste 6 letters zijn" , ("'") + laatste3Woorden + ("'"))
time.sleep(2)
print()
print()

tekstOpdracht4 = 'Het www is ontwikkeld vanaf 1989 door Tim Berners-Lee'
letters5tm8 = tekstOpdracht4[5:8]
letters29tot33 = tekstOpdracht4[29:32]

print("Opdracht 4: 5e t/m de 8e letter & 29 tot de 33e letters uit de tekst halen:")
print(tekstOpdracht4)
print()
time.sleep(1)
print("De 5e t/m 8e letters zijn" , letters5tm8 , "en de 29e tot de 33e zijn" , letters29tot33 + ".")
print()
print()

print("Einde Opdracht.")