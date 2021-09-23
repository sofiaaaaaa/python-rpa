# 패키지 사용 방법 
# import travel.thailland

# trip_to = travel.thailland.ThaillandPackage()
# trip_to.detail()

# from travel.thailland import ThaillandPackage

# trip_to = ThaillandPackage()
# trip_to.detail()

# 랜덤 모듈의 모든걸 다 쓰겠다.
# from random import * 

# 트래블 패키지의 모든 클래스를 사용하고 싶을 때, 접근 권한을 미리 설정해줘야한다. __init__.py에 선언함.
# from travel import * 
# trip_to = thailland.ThaillandPackage()
# trip_to.detail()


#random 클래스의 파일 위치를 알 수 있는 방법 
import inspect
import random

print(inspect.getfile(random))


# pypi로 패키지 받는 방법 
# www.pypi.org 
# 21만개 이상의 패키지 다운 가능.. 
웹스크래핑 유명한거 설치하기 
pip install beautifulsoup4 --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org


