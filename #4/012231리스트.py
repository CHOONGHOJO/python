# 순서를 가지는 개체의 집합

subway = ['홍길동','bb','cc','bb']
print (subway.index('cc'))

print(subway.append("dd"))
 
print(subway.insert(0,"AA"))
 
print(subway.pop())
print(subway)

print(subway.count('bb'))
 
# subway.sort()
subway.reverse()
print(subway)

num = [5,4,3,2,1]
num.sort()
print(num)

num.extend(subway)
print(num)
num.sort()


subway.clear()
print(subway)