# Quiz) 사이트별로 비밀번호 만들어 주는 프로그램 작성

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 3자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성
#                     (nav)         (5)              (1)      (1)
# 예) 생성된 비밀번호 : nav51!

my_url = "http://naver.com"
url = my_url.replace("http://","")
url= url[:url.index(".")]
psw = url[:3] + str(len(url)) + str(url.count("e")) + "!"
print ("생성된 {0}의 비밀번호는 {1} 입니다. ".format(my_url,psw))