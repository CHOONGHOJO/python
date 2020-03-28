try:
    print ("한 자리 숫자 전용 계산기")
    num1 = int(input("분모를 입력하세요 : "))
    num2 = int(input("분자를 입력하세요 : "))
    if num1 > 9 or num2 >9 :
        raise ValueError
    print("{0} / {1} = {2}".format(num1,num2,int(num1 /num2)))

except ValueError:
    print("한 자리 숫자만 입력하세요.") 
except Exception as err:
    print(err)