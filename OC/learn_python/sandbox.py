# def afficher_flottant(nb):
# 	if type(nb) is not float:
# 		raise TypeError("Please input a float")

# 	nb = str(nb)
# 	ent, flottant = nb.split(".")
# 	return ",".join([ent, flottant[:3]])


# print(afficher_flottant(3.9999))



# def afficher(*parametres, sep=' ', fin='\n'):
#     """Fonction chargée de reproduire le comportement de print.
    
#     Elle doit finir par faire appel à print pour afficher le résultat.
#     Mais les paramètres devront déjà avoir été formatés. 
#     On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :

#     print(chaine, end='')"""
    
#     # Les paramètres sont sous la forme d'un tuple
#     # Or on a besoin de les convertir
#     # Mais on ne peut pas modifier un tuple
#     # On a plusieurs possibilités, ici je choisis de convertir le tuple en liste
#     parametres = list(parametres)
#     # On va commencer par convertir toutes les valeurs en chaîne
#     # Sinon on va avoir quelques problèmes lors du join
#     for i, parametre in enumerate(parametres):
#         parametres[i] = str(parametre)
#     # La liste des paramètres ne contient plus que des chaînes de caractères
#     # À présent on va constituer la chaîne finale
#     chaine = sep.join(parametres)
#     # On ajoute le paramètre fin à la fin de la chaîne
#     chaine += fin
#     # On affiche l'ensemble
#     print(chaine, end='')


# inventaire = [
#     ("fraises", 76),
#     ("prunes", 51),
#     ("pommes", 22),
#     ("poires", 18),
#     ("melons", 4),
# ]

# inventaire_reverse = [(fruit, qtt) for qtt, fruit in inventaire]
# print(inventaire_reverse)

# print([(fruit, qtt) for qtt, fruit in sorted(inventaire_reverse)])
# 

# echiquier = {}
# echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
# echiquier['b', 1] = "cavalier blanc" # À droite de la tour
# echiquier['c', 1] = "fou blanc" # À droite du cavalier
# echiquier['d', 1] = "reine blanche" # À droite du fou
# # ... Première ligne des blancs
# echiquier['a', 2] = "pion blanc" # Devant la tour
# echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion
# # ... Seconde ligne des blancs
# print(echiquier)
# 
# fruits = {"pommes":21, "melons":3, "poires":31}
# for cle in fruits.keys():
#      print(cle)

my_string="Hello world!"

print(my_string.split())