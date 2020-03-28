absent = [2,5] # 결석
no_book = [7] # no book
for student in range(1,11):  # 1~10
    if student in absent:
        continue
    elif student in no_book:
        print ("오늘 수업 끝. {0}는 교무실로!".format(student))
        break
    print("{0}, 책을 일어봐".format(student))