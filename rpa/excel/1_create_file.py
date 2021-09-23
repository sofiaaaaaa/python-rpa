# pip install openpyxl

# pip install openpyxl --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org



from openpyxl import Workbook
wb = Workbook() #새 워크북 생성 
ws = wb.active #현재 활성화된 시트 가져옴 
ws.title = "Jihoo's New Seet" 
wb.save("sample.xlsx")
wb.close()

