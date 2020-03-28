# self.name, self.hp, self.damage 가 멤버 벼수가 된다.
# 즉 class 내에서 정의된 변수

class Unit :     
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print ("{0} 유닛이 생성됨". format(self.name))
        print ("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150,15)

#레이스 : 공중 유닛, 비행기, 크로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

#마인드 콘크롤 : 상대방 유닛을 낸것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스",80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print ("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))





