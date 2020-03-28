# google serch : list of python modules
# python module index

# glob : 경로 내의 폴더 / 파일 목록 조회 ( 윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일
# print(glob.glob("*.*")) # 모든 파일

# import os
# print (os.listdir())  # directory와 file listing


# OS : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "simple_dir"

# if os.path.exists(folder) :
#     print ("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")


# import time # 시간 관련 함수
# print (time.localtime())
# print (time.strftime("%y-%m-%d %H:%M:%S"))  # yy-mm-dd hh-mm-ss

import datetime
print("오늘 날자는 ", datetime.date.today())  # yyyy-mm-dd

# timedelta : 두 날자 사이의 간격
import datetime
today = datetime.date.today()
td = datetime.timedelta(days = 10) # 10일 저장
print("우리가 만나지 10일은?" , today + td) # 오늘 부터 10일 후









