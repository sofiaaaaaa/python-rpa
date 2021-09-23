# 방법1 
print("aaa %d" % 20)
print("aaa %s" % "bbb")

print("aaa %c" % "A")

print("%s %s" % ("aaa", "ddd"))


# 방법 2
print("zzz {} zzz".format(20))
print("zzz {} zzz {}".format(20, 40))
print("zzz {0} zzz {1}".format(20, 40))
print("zzz {1} zzz {0}".format(20, 40))


# 방법 3 
print("zzz {age} zzz {color}".format(age=20, color=40))
print("zzz {color} zzz {age}".format(age=20, color=40))



# 방법 4 (version 3.6 이상)
age = 20
color = "red"
print(f"aaaa {age}, {color} bbb")

