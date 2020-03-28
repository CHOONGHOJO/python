# 클래스 나 함수는 import를 직접 바로 할 수 없다
# 그러나 from travel.thailand import ThailandPackage 로는 사용가능하다 
# travel package밑에 thailand 모듈밑에  ThailandPackage 클래스
import travel.thailand
# from travel.thailand import ThailandPackage
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail() 