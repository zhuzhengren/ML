#  -*- coding:utf-8 -*-
from uiautomator import device as d
import time
import unittest

class MyTestSuite(unittest.TestCase):
    # 初始化工作
    def setUp(self):
        print("--------------初始化工作")

    # 退出清理工作
    def tearDown(self):
        print("--------------退出清理工作")

    #***************************方法**************************************
    # 判断控件是否存在 & text
    def check_controls_exists(self, controls_text):
        if d(text=controls_text).exists:
            return 1
        else:
            return 0

    # 判断按钮是否置灰 & text & clickable
    def check_controls_click_text(self, controls_text):
        if d(text=controls_text).info.get("clickable") is True:
            return 1
        else:
            return 0

    #assertIn(a, b)     a in b
    def check_ainb(self,resourceid,b):
        if d(resourceId=resourceid).info.get("text") in  b:
            return 1
        else:
            return 0

    #***********************************************************

    # 注册模块
    def test_Aregister(self):
            time.sleep(2)
            #猫宁考勤开启全新时代
            self.assertEqual(self.check_controls_click_text("注册"),1,u"猫宁考勤开启全新时代")
            # 猫宁考勤开启全新时代--》点击注册按钮进入注册猫宁界面
            d(text="注册").click()
            time.sleep(3)
            #注册猫宁界面
            self.assertEqual(self.check_text("com.isentech.attendancet:id/regis_phone","请输入手机号码"),
                                              1,u"注册页面-》请输入手机号码")
            self.assertEqual(self.check_text("com.isentech.attendancet:id/regis_verifycode","请输入验证码"),
                                              1,u"注册页面-》请输入验证码")
            self.assertEqual(self.check_controls_click_text("获取验证码"), 0,u"注册页面-》获取验证码")
            self.assertEqual(self.check_controls_click_text("《中科爱讯服务协议》"), 1,u"注册页面-》《中科爱讯服务协议》")
            self.assertEqual(self.check_controls_click_text("注册"), 0,u"注册页面-》注册")
            time.sleep(2)
            #《中科爱讯服务协议》
            d(text="《中科爱讯服务协议》").click()
            time.sleep(2)
            self.assertEqual(self.check_ainb("com.isentech.attendancet:id/title","服务协议"), 1,u"注册页面-》服务协议")
            time.sleep(1)
            d(resourceId="com.isentech.attendancet:id/title_back").click()
            time.sleep(1)
            #手机号不输入是否能注册
            d(text="注册").click()
            time.sleep(3)
            # 手机号只输入1个数字是否能注册&只输入1个数字是否能获取验证码
            d(resourceId="com.isentech.attendancet:id/regis_phone").set_text("1")
            self.assertEqual(self.check_controls_click_text("获取验证码"), 0)
            time.sleep(1)
            d(text="注册").click()
            time.sleep(1)
            d(resourceId="com.isentech.attendancet:id/regis_phone").clear_text()
            time.sleep(1)
            #只输入5个数字是否能获取验证码
            d(resourceId="com.isentech.attendancet:id/regis_phone").set_text("11111")
            self.assertEqual(self.check_controls_click_text("获取验证码"), 0)
            time.sleep(1)
            d(resourceId="com.isentech.attendancet:id/regis_phone").clear_text()
            time.sleep(1)
            #只输入手机号是否能注册
            d(resourceId="com.isentech.attendancet:id/regis_phone").set_text(phone_number)
            self.assertEqual(self.check_controls_click_text("注册"), 0)
            time.sleep(1)
            d(text="注册").click()
            time.sleep(1)
            #输入正确的验证码&获取验证码是否高亮
            d(resourceId="com.isentech.attendancet:id/regis_verifycode").set_text("5648")
            time.sleep(1)
            self.assertEqual(self.check_controls_click_text("获取验证码"), 1)
            time.sleep(2)
            #密码只输入1个数字是否能注册&注册按钮是否高亮
            d(resourceId="com.isentech.attendancet:id/regis_pass").set_text("1")
            d(resourceId="com.isentech.attendancet:id/regis_passAgain").set_text("1")
            time.sleep(1)
            self.assertEqual(self.check_controls_click_text("注册"), 0,u"密码只输入1个数字是否能注册")
            time.sleep(1)
            d(resourceId="com.isentech.attendancet:id/regis_pass").clear_text()
            d(resourceId="com.isentech.attendancet:id/regis_passAgain").clear_text()
            time.sleep(1)
            #输入不相同的密码是否能注册
            d(resourceId="com.isentech.attendancet:id/regis_pass").set_text("123456")
            d(resourceId="com.isentech.attendancet:id/regis_passAgain").set_text("12345")
            time.sleep(1)
            self.assertEqual(self.check_controls_click_text("注册"), 0,u"输入不相同的密码是否能注册")
            time.sleep(1)
            d(resourceId="com.isentech.attendancet:id/regis_pass").clear_text()
            d(resourceId="com.isentech.attendancet:id/regis_passAgain").clear_text()
            time.sleep(1)
            #输入正确的密码是否能注册&我已同意是否打钩
            d(resourceId="com.isentech.attendancet:id/regis_pass").set_text("123456")
            d(resourceId="com.isentech.attendancet:id/regis_passAgain").set_text("123456")
            time.sleep(1)
            self.assertEqual(self.check_controls_click_resourceId("com.isentech.attendancet:id/regis_agree"), 1)
            self.assertEqual(self.check_controls_click_text("注册"), 1)
            time.sleep(2)
            d(text="注册").click()
            time.sleep(8)
def test_app():
    test_unit = unittest.TestSuite()
    test_unit.addTest(MyTestSuite("test_Aregister"))

if __name__ == "__main__":
    # 测试app
    unittest.main()