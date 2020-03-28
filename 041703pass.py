# 연산자 오버로딩 :  자식크래스에서 정의한 메소드를  쓰고 싶을 때 새롭게 정의해서 쓰는것

class Unit :     
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print ("[지상유닛 이동]")
        print ("{0} : {1} 방행으로 이동합니다. [속도 {2}]"
            .format(self.name, location, self.speed))

class AttackUnit (Unit):     
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print ("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print ("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0 :
            print ("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중유닛 : 수송기 , 마린/퍼이어벳/텡크등을 수송/ 공격능력없음
#날  수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print ("{0} : {1} 방향으로 날아감. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스     
class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피트 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print ("[격 유닛 이동]")
        self.fly(self.name, location)

# 건물 
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 서플라이 디포 : 건물 1 =  8 unit 
supply_depot = BuildingUnit("서플라이 디포", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작함.")

def game_over():
    pass


game_start()
game_over()





 





















