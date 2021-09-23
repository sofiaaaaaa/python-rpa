class Unit: 
    def __init__(self, name, hp, speed): #생성자 
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("move {0} {1} {2}".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): #생성자 
        Unit.__init__(self, name, hp, speed)
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


class Flyable: 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} {1} {2}".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)


vulture = AttackUnit("aaa", 80, 10, 20)

c = FlyableAttackUnit("bbb", 500, 25, 3)

vulture.move("111")
c.fly("eee")
