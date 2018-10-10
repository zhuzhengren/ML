import xlsxwriter
import datetime

'''创建文件'''
workbook = xlsxwriter.Workbook('test.xlsx')
'''创建表'''
worksheet = workbook.add_worksheet('test')


'''设定单元格格式'''
top = workbook.add_format({'border':1,'font_size':13,'bold':True,'align':'center','bg_color':'cccccc'})
'''特定单元格写入'''
worksheet.write('A1','朱正仁',top)
worksheet.write(1,0,'朱正仁',top)
worksheet.write(0,1,'555555',top)
worksheet.set_row(0,40,top)

'''写入数字和函数'''
worksheet.write(0,1,32)
worksheet.write(1,1,44)
worksheet.write(2,1,'=sum(B1,B2)')

'''写入日期'''
worksheet.write(0,2,datetime.datetime.strptime('2017-11-11','%Y-%m-%d'),workbook.add_format({'num_format':'yyyy-mm-dd'}))

'''插入图片'''
worksheet.insert_image(0,4,'测试知识结构.jpg')
worksheet.insert_image(0,5,'测试知识结构.jpg',{'x_scale':0.2,'y_scale':0.2})


'''批量写入单元格'''
worksheet.write_column('A22',[1,2,3,4])
worksheet.write_row('A21',[1,2,3,4])

'''合并单元格写入'''
worksheet.merge_range(4,0,5,5,'正仁')