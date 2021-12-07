# function 입력 파라미터에 기본값 지정 
# \ 를 사용해서 코드를 다음 라인에서 사용가능함 
def profile(name, age=17, main_lang="파이썬"):
    print("{0}, {1}\t {2}"\
        .format(name, age, main_lang))


profile("aaa")

