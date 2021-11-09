class Unit: 
    def __init__(self, name, hp): #생성자 
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage): #생성자 
        Unit.__init__(self, name, hp)
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



class Flyable: 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} {1} {2}".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


valkyrie = FlyableAttackUnit("aaa", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")