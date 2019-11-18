"""
CSV(comms-separated-value)

CSV文件是由任意的数据格式组成，记录以某种换行符分割，每行记录由换行符组合

例：
ID， Username，Age，Country
1001， dana， 18， China
1002， hanghzong，28，China
"""

import csv
headers = ['ID', 'Username', 'Age', 'Country']

rows = [
    ('1001', 'dana', '18', 'China'),
    ('1002', 'huangzhong', '28', 'China'),
    ('1003', 'yiteng', '23', 'Japan')
]

with open('test.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)