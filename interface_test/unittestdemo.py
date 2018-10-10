import requests
import unittest
import json
import Config
class GetParam(unittest.TestCase):
    def setUp(self):
        host = Config.url()
        endpoint = 'get'
        self.url = ''.join([host,endpoint])

    def test_get_param(self):
        params = {"show_env":1}
        r = requests.get(self.url,params=params)
        resp = r.json()
        connect = resp.get('headers').get('Connection')
        self.assertEqual(connect,'close')
#        print(r.text)
#        print(r.request.headers)
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()