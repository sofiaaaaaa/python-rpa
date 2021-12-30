#배열 
data = [1,2,3,4]
data = [[1,2], [1,2,3]]

# 특정 알파벳 빈도수 구하기 
dataset = [
'aaa',
'abc',
'cca',
'dde',
'ca'
]

m_count = 0 
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'a':
            m_count+=1

print(m_count)