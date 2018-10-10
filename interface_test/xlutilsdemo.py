import xlrd
import xlutils.copy

xl =xlrd.open_workbook('test.xlsx')

workbook = xlutils.copy.copy(xl)


worksheet = workbook.get_sheet(0)

worksheet.write(0,0,'changed')


'''不能复制格式  只支持2003'''
workbook.save(r'xutils-save.xls')