class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg


try: 
   print("bbb")
   num1 = int(input("first: "))
   num2 = int(input("second: "))
   if num1 >= 10 and num2 >= 10: 
       raise BigNumberError("aaa") # 에러 발생     
   print("{0} {1} = {2}".format(num1, num2, int(num1/num2)))
except BigNumberError as err:
    print("value error ", err) 
finally:
    print("bbbbbccc")