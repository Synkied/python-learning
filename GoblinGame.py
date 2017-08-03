# SUPERCLASS
class GameObject:
    """
    This class instantiates the objects of the game (chars, weapons...)
    """
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

    def say_name(self):
        return "Hi my name is " + self.name


class Goblin(GameObject):

    def __init__(self, name):
        self.class_name = "goblin"
        self.desc = "A foul creature"
        self.health = 30
        super().__init__(name)


class Human(GameObject):
    def __init__(self, name):
        self.class_name = "human"
        self.desc = "A destructor of the earth"
        self.health = 100
        super().__init__(name)
    

goblin = Goblin("Gobbly")
human = Human("Thor")


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)


def talk(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].say_name()
    else:
        return "There is no {} here.".format(noun)


def get_input():
    command = input("input a command: ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}". format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print (verb(noun_word))
    else:
        print(verb("nothing"))


def say(noun):
    return 'You said "{}"'.format(noun)


verb_dict = {
    "say": say,
    "examine": examine,
    "talk": talk,
}

while True:
    get_input()


