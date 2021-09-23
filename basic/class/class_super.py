class Unit: 
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() # self 매개변수 생략 > 다중상속의 경우 맨처음 클래스만 상속됨
        Flyable.__init__(self)
        Unit.__init__(self)


dropship = FlyableUnit()





