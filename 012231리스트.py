 
subway = ["aa","bb","cc"]
 
print(subway)
print (subway.index("bb"))

subway.insert(4,"dd")
print(subway)

subway.insert(4,"dd")
print(subway)
subway.insert(1,"00")
print(subway)

print(subway.pop())
print(subway)

subway.append("aa")
print(subway)
print(subway.count("aa"))

subway.sort()
print(subway)

subway.reverse()
print(subway)

subway.clear()
print(subway)

mixlist=["한글", "English", 10, True ]
numlist = [1,2,3,4,5]
numlist.extend(mixlist)
print(numlist)