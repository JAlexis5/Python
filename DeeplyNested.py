if !hungry:
	dontDoAnything()
else:	
	if !WantToCook:
		if !Leftovers:
			if money > 20:
				orderPizza()
            else:
                cook()
        else:
			finishLeftovers()
		
			
	else:
		cook()
		