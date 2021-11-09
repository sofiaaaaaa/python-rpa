# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# # 매개변수의 순서와 상관없이 지정 가능함. 
# profile(name="bbb", main_lang="ccc", age=15)

# def profile(name, age, lang1, lang2, lang3):
#     print("{0} {1} \t".format(name, age), end=" ") # end = 다음 출력구문이 같은 줄에 출력됨 
#     print(lang1, lang2, lang3)

# profile("bbb", 222, "aaa", "ccc", "")


# 가변인자 
def profile(name, age, *language):
    print("{0} {1} \t".format(name, age), end=" ") # end = 다음 출력구문이 같은 줄에 출력됨 
    for lang in language:
        print(lang, end=" ")
    print()

profile("bbb", 222, "aaa", "ccc", "")
