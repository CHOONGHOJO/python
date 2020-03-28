
class Unit :     
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print ("{0} 유닛이 생성됨".format(name))

    def move(self, location):
        print ("[지상유닛 이동]")
        print ("{0} : {1} 방행으로 이동합니다. [속도 {2}]"
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print ("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))

        if self.hp <= 0 :
            print ("{0} : 파괴되었습니다.".format(self.name))


class AttackUnit (Unit):      
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print ("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

# 마린 
class Marine (AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀펙 ; 일정 시간 동안 이동 및 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print ("{0} : 스팀팩을 사용. [Hp 10 감소]".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 못사용".format(self.hp))
 # 탱크
class Tank(AttackUnit):
     # 시즈모드 : 탱크를 지상에 고정시켜 더 높은 파워로 공격 가능, 이동 불가
    seize_developed = False # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35) 
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈 모드 아닐 때  ---> 시즈 모드 온
        if self.seize_mode ==False:
            print("{0} : 시즈모드 전환".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
         # 현재 시즈 모드 일 때   --->> 시즈 모드 오프
            print("{0} : 시즈모드 해제".format(self.name))
            self.damage /= 2
            self.seize_mode = False


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
        print ("[공격 유닛 이동]")
        self.fly(self.name, location)

#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print ("{0} : 클로킹 모드 해제함".format(self.name))
            self.clocked = False
        else:
            print ("{0} : 클로킹 모드 설정함".format(self.name))
            self.clocked = True


