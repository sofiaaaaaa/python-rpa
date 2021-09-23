import pickle

# with 구문을 활용하면 close 구문을 따로 쓰지 않아도 됨. 
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("zzzzzzzzzz")


with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())