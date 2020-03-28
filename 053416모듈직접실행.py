class ThailandPackage:
    def detail(self):
        print ("[태국 패키지 3밧 5일] 방콕, 파타야 여행 (야시장투어) 500달러")
        
if __name__ ==  "__main__" :
    print ("이 문장은 모듈을 직접 실행할 때만 실행됩니다.")
    print ("Thailand 모듈을 직접 실행")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print ("Thailand 외부에서 모듈 호출")