def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance,money):
    print("{1}원 입금 완료됨. 잔액은 {0}원 입니다".format(balance+money,money))
    return balance+money

def withdraw(balance,money):
    if balance >= money:
        print("{1}원 출금 완료됨. 잔액은 {0}원 입니다".format(balance - money,money))
        return balance - money
    else:
        print("{1}원 출금 불가함. 잔액은 {0}원 입니다".format(balance,money))
        return balance

def withdraw_night(balance,money):
    commission = 100
    return commission, balance-money-commission



balance = 00
balance = deposit(balance,1000)

# balance = withdraw(balance,51234)
commission, balance = withdraw_night(balance,500)
print("수수료는 {}원이고 잔액은 {}원 입니다".format(commission,balance))