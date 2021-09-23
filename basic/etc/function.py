def open_account():
   print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. {0}".format(balance + money))

deposit(1000, 2000)

balance = 0
balance = deposit(balance, 1000)

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. {0}".format(balance - money))
#         return balance - money
#     else: 
#         print("fail")
#         return balance

# balance = withdraw(balance, 2000)

# return tuple type
def withdraw_might(balance, money):
    return balance, money

print(withdraw_might(balance, 4000))

