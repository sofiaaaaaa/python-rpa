try: 
    print("aaaa")
    num1 = int(input("first: "))
    num2 = int(input("second: "))
    
    print("{0} {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError: 
    print("error ")
except ZeroDivisionError as err:
    print(err)


try: 
    print("aaaa")
    nums = []
    nums.append(int(input("first: ")))
    nums.append(int(input("second: ")))
    # nums.append(int(int(nums[0]/nums[1])))1
    print("{0} {1} {2} ".format(nums[0], nums[1], nums[2]))
except ValueError: 
    print("error ")
except ZeroDivisionError as err:
    print(err)
except: 
    print("bbbbbb")