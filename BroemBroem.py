def bereken_maandkosten():

	liter_per_kilometer = 0.2
	benzine_kosten_per_liter = 1.54
	verzekering_per_maand = 23
	
	km_per_maand = input("Gereden KM per maand: ")

	while not isinstance(km_per_maand, float):
		try:
			km_per_maand = float(km_per_maand)
			maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
			maandkosten = round(maandkosten, 2)
			print("Je moet maandelijks" , maandkosten , "euro aan je scooter besteden.")
		except ValueError:
			print(km_per_maand , "is geen geldig getal! Herstart het programma en voer een geldig getal in (. ipv ,).")
			break

bereken_maandkosten()