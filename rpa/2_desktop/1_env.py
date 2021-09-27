# pip install pyautogui openpyxl --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
# pip install pillow --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
import pyautogui

# 현재 화면의 스크린 사이즈
size = pyautogui.size()

print(size[0], size[1])