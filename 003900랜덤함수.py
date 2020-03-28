from random import *
print (random())  # 0.0 ~ 1.0 미만 임의의 값 생성
print (int(random() *10) + 1) # 1 ~ 10 이하의 값 
print (int(random() *49) + 1) # 1 ~ 49 이하의 값 

print (randrange(1,50)) # 1 ~ 50 미만 임의값 생성

print(randint(1,49)) # 1 ~ 49 사이의 값 임의 생성 