cabinet = {3:"삼길동", 100:"백길동"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5])
print(cabinet.get(5))
print(cabinet.get(5),"사용가능")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"a-3":"유재석","b-100":"김태호"}
print(cabinet)

# 새 손님
cabinet["a-3"] = "김종국"
cabinet ["c-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["a-3"]
print(cabinet)

# key
print(cabinet.keys())

# value
print(cabinet.values())

# key & value
print(cabinet.items())

# clear
cabinet.clear()
print(cabinet)
