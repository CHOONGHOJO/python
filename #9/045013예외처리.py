try:
    print ("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("분모를 입력하세요 :")))
    nums.append(int(input("분자를 입력하세요 :")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print ("Wrong number.")   
except Exception as err  :
    print (err)

