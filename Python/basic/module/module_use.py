# import module

# module.price(4)

# import module as m

# m.price(3)


# 모듈명 사용 없이 바로 함수 호출 가능 
# from module import * 
# price(3)

# 특정 함수만 사용 
# from module import price, price_morning 
# price(3)

# 메서드에 별명 붙일 수 있음 
from module import price as p
p(3)
