

try:
	print("Saisissez un numérateur")
	numerator = input()
	print("Saisissez un dénominateur")
	denominator = input()
	res = int(numerator) / int(denominator)
except ValueError as VE:
	print("Ce n'est pas un nombre. Voici l'erreur :", VE)
except ZeroDivisionError as ZDE:
	print("Le dénominateur vaut 0. Voici l'erreur :", ZDE)
else:
	print("Le résultat est : ", res)
finally:
	print("Eh bien, on passe à la suite ?")