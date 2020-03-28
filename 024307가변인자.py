 
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#      print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#      print(lang1,lang2,lang3,lang4,lang5)

# profile ("유재식", 20, "Python", "Java", "C", "c++", "C#")
# profile ("김태홍",25,"Kotlin", "Swift",",","")

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print (lang, end=" ")
    print()

profile ("유재식", 20, "Python", "Java", "C", "c++", "C#","JavaScript")
profile ("김태홍", 25, "Kotlin", "Swift")

