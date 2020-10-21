schooldayInput = input("What day is it today? Answer in lowercase: ")
if schooldayInput == 'monday' or 'tuesday' or 'wednesday' or 'thursday' or 'friday':
    schoolday = True
elif schooldayInput == 'saturday' or 'sunday':
    schoolday == False
else:
    print("Please enter a valid day.")

if schoolday == True:
    print("Get yo ass to school asap!")
elif schoolday == False:
    print("Gaming time.")