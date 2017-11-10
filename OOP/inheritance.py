class Personne:
    """Classe représentant une personne"""

    def __init__(self, nom, prenom, sexe):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{} {}".format(self.prenom, self.nom)


class Characteristics:

    def __init__(self, noise):
        self.noise = noise

    def cur_mood(self, mood):
        self.mood = "Happy"
        return self.mood

    def imc(self, height, weight):
        self.height = height
        self.weight = weight
        return round(weight / (height**2), 1)


class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""

    def __init__(self, nom, prenom, sexe, matricule):
        """Un agent se définit par son nom et son matricule"""
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self, nom, prenom, sexe)
        self.matricule = matricule

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {}, matricule {}, sexe {}".format(self.nom, self.matricule, self.sexe)


class Student(Personne, Characteristics):

    def __init__(self, nom, prenom, sexe, grade, noise):

        Personne.__init__(self, nom, prenom, sexe)
        Characteristics.__init__(self, noise)
        self.grade = grade

    def __str__(self):
        return "Etudiant {} {}, sexe {}, note {}. Elle fait {}".format(self.nom, self.prenom, self.sexe, self.grade, self.noise)


hitman = AgentSpecial("Hitman", "Martine", "Male", 47)
print(hitman)

print(hitman.prenom)


lola = Student("Pannet", "Lola", "Female", 18, "Youhou !")

print(lola)

print(lola.cur_mood("Happy"))

print(lola.imc(1.48, 45))
