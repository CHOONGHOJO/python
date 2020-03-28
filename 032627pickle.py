#program상에서 data로 사용하는것을 file형태로 저장하여 재 사용
# import pickle
# profile_file = open("profile.pickle","wb") # b is binary
# profile = {"이름" : "박명순", "나이":30, "취미" : ["축구", "골프", "코딩"]}
# print (profile)
# pickle.dump(profile, profile_file) # profile data를 profile_file에 저장
# profile_file.close()


import pickle
profile_file = open("profile.pickle","rb") # b is binary
profile = pickle.load(profile_file) # profile_file data를 profile에 저장
print (profile)
profile_file.close()
