import pickle

# pickle에서는 바이너리 타입으로 써야함
# profile_file = open("profile.pickle", "wb")
# profile = {"aaa": "ccc", "bbb": "ddd"}
# print(profile)
# pickle.dump(profile, profile_file) # 프로필에 있는 정보를 파일에 저장함 
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()


