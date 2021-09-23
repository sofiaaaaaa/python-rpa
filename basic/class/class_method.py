class Unit: 
    def __init__(self, name, hp, damage): #생성자 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} aa ".format(self.name))
        print("{0} aa ".format(self.hp))
        print("{0} aa ".format(self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage): 
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} {1} "\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1}".format(self.name, damage))
        self.hp -= damage
        print("{0}: {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : gone".format(self.name))

firebat1 = AttackUnit("vvv", 50, 16)
firebat1.attack("5555")
firebat1.damaged(25)
firebat1.damaged(25)

