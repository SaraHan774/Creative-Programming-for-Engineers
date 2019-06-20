class Hero:

    def __init__(self, name):
        self.name = name

    def change_me_hero(self):
        print("Hello this is %s " % self.name)  # gets the name from the constructor
        name = "Superman"
        print("My new name is %s" % name)  # applies the variable from right above

    name = "Sara"
    print("Howdy, I am %s" % name)  # runs when the class is initialized


if __name__ == '__main__':
    hero = Hero("Ben")
    hero.change_me_hero()
    print("Name : " + hero.name)
