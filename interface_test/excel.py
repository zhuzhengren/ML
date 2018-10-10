import os
import xlrd
from datetime import datetime,date

newpath = os.chdir(r'C:\Users\zhuzhengren\Desktop\测试')
filename = '朱正仁测试用例0724.xlsx'
file = os.path.join(os.getcwd(),filename)

'''1.打开文件'''
xl = xlrd.open_workbook(file)

'''2.获取sheet'''
print(xl.sheet_names())

'''3.获取sheet中的数据'''
table1 = xl.sheet_by_name('进入横屏页面')
print(table1.name)
print(table1.ncols)
print(table1.nrows)

'''4.单元格批量获取'''
print(table1.row_values(6))
print(table1.row_types(0))

'''5.获取特定的单元格数据'''
#取值
print(table1.cell(5,6).value)
print(table1.cell_value(5,6))
print(table1.row(5)[6].value)
#取类型
print(table1.cell(5,6).ctype)
print(table1.cell_type(5,6))
print(table1.row(5)[6].ctype)

'''6.常用技巧（0，0）转换成A1'''
print(xlrd.cellname(0,0))
print(xlrd.cellnameabs(0,0))
