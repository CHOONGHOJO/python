# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬, 총 10자리 공간 확보
print("{0: >10}".format(12345))

# 영수일 때 +로 , 음수일 때 -로 표시
print("{0: >+10}".format(12345))
print("{0: >+10}".format(-12345))

# 왼 쪽 정렬, 빈칸으로 _로 표시
print("{0:_<+10}".format(12345))

#세자리마다 콤마를 찍고, +/- 표시
print("{0:+,}".format(-1234567890))

#소숫점 2 자리까지 출력, 3째자리 반올림
print("{0:.2f}".format(5/3))


 