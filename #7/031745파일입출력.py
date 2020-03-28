# score_file = open("score.txt","w", encoding = "utf8")
# print("수학 : 0",file=score_file)
# print("영어 : 100",file=score_file)
# score_file.close()

# score_file = open("score.txt","a", encoding = "utf8")
# score_file.write("과학 : 99")
# score_file.write("\nCoding : 100")
# score_file.close()

# score_file = open("score.txt","r", encoding = "utf8")
# print(score_file.read())   # 전체내용을 읽어온다
# score_file.close()

# score_file = open("score.txt","r", encoding = "utf8")
# print(score_file.readline(),end="")   # 한 줄 내용을 읽어온다 
# print(score_file.readline(),end="")   # 한 줄 내용을 읽어온다
# print(score_file.readline())   # 한 줄 내용을 읽어온다
# score_file.close()

# end of file 까지 읽어서 처리하기
# score_file = open("score.txt","r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()
    
# List로 처리하기
score_file = open("score.txt","r", encoding = "utf8")
lines = score_file.readlines() # list형태로 저장

for line in lines:
    print(line,end="")
    
score_file.close()
 
