class BigBumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try :
    print ("한 자리 숫자 전용 계산기")
    num1 = int(input("첫 번째 숫자 입력 :"))
    num2 = int(input("두 번째 숫자 입력 :"))
    if num1 >= 10 or num2 >=10 :
        raise BigBumberError("입력값 : {0}, {1}".format(num1,num2))
    print ("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
    print ("한 자리 숫자만 입력요!")

except ZeroDivisionError as err :
    print(err)
except BigBumberError as err:
    print ("에러가 발생함, 한 자리 숫자만 입력요!")
    print(err)
finally : 
    print ("계산기를 이용해 주심을 감사!")