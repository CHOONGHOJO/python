
# print ("Python", "Java", "JavaScript", sep=" , ",end="?")
# print  (" 무엇이 더 재밌을까요?")

# import sys
# print("Python","Java",file=sys.stdout)
# print("Python","Java",file=sys.stderr)

#시험성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject,score in scores.items():
#   #  print (subject.ljust(8),score) # left 정렬 8칸 확보
#     print (subject.ljust(8), str(score).rjust(4), sep=":") # right 정렬 4칸 확보

# #은행 대기순번표 001,002,003...
# for num in range(1,21):
#     print ("대기번호표 :" + str(num).zfill(3))


answer = input("아무 값이나 입력하세요 :")
print ("입력하신 값은 " + answer + "입니다.")


