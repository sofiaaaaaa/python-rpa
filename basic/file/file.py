# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# 수정 
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("zzzzz")
# score_file.write("\nppppp")
# score_file.close()


# 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# # print(score_file.readline(), end="") # 한줄식 읽고 커서 이동.
# # print(score_file.readline(), end="") # 한줄식 읽고 커서 이동.
# # print(score_file.readline(), end="") # 한줄식 읽고 커서 이동.
# # print(score_file.readline(), end="") # 한줄식 읽고 커서 이동.
# # score_file.close()

# # while True:
# #     line = score_file.readline()
# #     if not line:
# #         break
# #     print(line)

# # score_file.close()

# # 리스트에 파일의 모든 내용을 저장함
# list = score_file.readlines()

# for line in list:
#     print(line, end="")
# score_file.close()




for i in range(1, 2):
    with open("./aa/"+str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("{0}".format(i))
        report_file.write("\naaaa")
    