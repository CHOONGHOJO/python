class Unit :    # 연관있는 함수와 변수의 집합
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print ("{0} 유닛이 생성됨". format(self.name))
        print ("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150,15)


