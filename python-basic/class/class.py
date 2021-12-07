class Unit: 
    def __init__(self, name, hp, damage): #생성자 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} aa ".format(self.name))
        print("{0} aa ".format(self.hp))
        print("{0} aa ".format(self.damage))

marine1 = Unit("1", 40, 5)
marine2 = Unit("2", 41, 1)

print("{0}, {1}".format(marine1.damage, marine2.damage))

# 파이선은 외부에서 객체에 변수를 추가할 수 있다. 


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass 

def game_start():
    print("bb")
    pass

game_start()


class BuildingUnit2(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name,hp,0) 
        self.location = location

        