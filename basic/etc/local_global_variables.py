gun = 10 

def checkpoint(soldiers):
    global gun # 전역공간의 gun 변수 사용 
    gun = gun - soldiers
    print("{0}".format(gun))

print("aa {0}".format(gun))
checkpoint(4)
print("bb {0}".format(gun))


def checkpoint_return(gun, solders):
    gun = gun - solders
    print("{0}".format(gun))
    return gun

print("aa {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("bb {0}".format(gun))

