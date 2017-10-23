class RevStr(str):
	"""Classe reprenant les méthodes et attributs des chaînes construites
	depuis 'str'. On se contente de définir une méthode de parcours
	différente : au lieu de parcourir la chaîne de la première à la dernière
	lettre, on la parcourt de la dernière à la première.
	
	Les autres méthodes, y compris le constructeur, n'ont pas besoin
	d'être redéfinies"""

	def __init__(self, chaine_a_parcourir):
		"""On se positionne à la fin de la chaîne"""
		self.chaine_a_parcourir = chaine_a_parcourir
		self.position = len(chaine_a_parcourir)

	def __next__(self):
		"""Cette méthode doit renvoyer l'élément suivant dans le parcours,
		ou lever l'exception 'StopIteration' si le parcours est fini"""
		
		if self.position == 0: # Fin du parcours
			raise StopIteration
		self.position -= 1 # On décrémente la position
		return self.chaine_a_parcourir[self.position]

	def __iter__(self):
		"""Cette méthode renvoie un itérateur parcourant la chaîne
		dans le sens inverse de celui de 'str'"""
		
		return self # On renvoie l'itérateur créé pour l'occasion


s = RevStr('Bonjour')

for letter in s:
	print(letter)



def intervalle(borne_inf, borne_sup):
	"""Générateur parcourant la série des entiers entre borne_inf et borne_sup.
	Notre générateur doit pouvoir "sauter" une certaine plage de nombres
	en fonction d'une valeur qu'on lui donne pendant le parcours. La
	valeur qu'on lui passe est la nouvelle valeur de borne_inf.
	
	Note: borne_inf doit être inférieure à borne_sup"""
	borne_inf += 1
	while borne_inf < borne_sup:
		valeur_recue = (yield borne_inf)
		if valeur_recue is not None: # Notre générateur a reçu quelque chose
			borne_inf = valeur_recue
		borne_inf += 1


generateur = intervalle(10, 25)
for nombre in generateur:
	if nombre == 15: # On saute à 20
		generateur.send(20)
	print(nombre, end=" ")
print()