class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print ("한 자리 숫자 전용 계산기")
    num1 = int(input("분모를 입력하세요 : "))
    num2 = int(input("분자를 입력하세요 : "))
    if num1 > 9 or num2 >9 :
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1,num2,int(num1 /num2)))

except BigNumberError as err:
    print("잘못된 값을 입력하였습니다.")
    print(err) 
except Exception as err:
    print(err)

finally:
    print ("계산기를 이용해 주셔서 감사합니다.")