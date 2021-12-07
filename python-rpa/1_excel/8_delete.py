from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active 

# 7번째 줄 지우기 
# ws.delete_rows(8)
#ws.delete_rows(8,3)

# B열 삭제 
ws.delete_cols(2)


ws.save("sample_delete_col.xlsx")