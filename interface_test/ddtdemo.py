import requests
import json
import unittest
from ddt import ddt,data,unpack
import xlrd

xl = xlrd.open_workbook(r'C:\Users\zhuzhengren\Desktop\test.xlsx')
AllData = xl.sheet_by_name('AllData')
TestData = xl.sheet_by_name('TestData')
print(AllData)
print(AllData.cell_value(1,1))

@ddt
class GetNothingTest(unittest.TestCase):
    def setUp(self):
        endpoint = 'get'
        self.url = 'http://httpbin.org/get'

    '''一个参数通过data的元组执行多次'''
    '''
    @data(200,400,500,201)
    def test_1(self,result):
        r =requests.get(self.url)
        status_code =r.status_code
        self.assertEqual(status_code,result)
      '''
    @data(('headers','Connection','close'),('headers','Host','httpbin.org'))
    @unpack
    def test_2(self,headers,value,result):
        print(headers)
        print(value)
        r = requests.get(self.url)
        resp = r.json()
        print(resp)
        connect = resp[headers][value]
        self.assertEqual(connect,result)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()