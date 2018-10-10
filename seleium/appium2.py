# coding=utf-8

from appium import webdriver
import time
desired_caps = {

                'platformName': 'Android',

                'deviceName': '80QBCNM225ZW',

                'platformVersion': '5.0',

                # apk包名

                'appPackage': 'com.baofeng.mj',

                # apk的launcherActivity

                'appActivity': 'com.baofeng.mj.ui.activity.SplashActivity',

                'unicodeKeyboard':True,

               'retsetKeyboard':True

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(8)


def loginout():
    driver.find_element_by_name('我的').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/login').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/et_phonenum').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/et_phonenum').send_keys('18310406456')
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/et_password').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/et_password').send_keys('888888')
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/login_sure').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/account_setting_relative').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/exit_btn').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/logout_confirm').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/app_title_back_imagebtn').click()

def search():
    driver.find_element_by_name('首页').click()
    driver.find_element_by_id('com.baofeng.mj:id/app_title_search_left').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/key_word').click()
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/key_word').send_keys(u'美女')
    time.sleep(1)
    driver.find_element_by_id('com.baofeng.mj:id/cancel').click()
#    driver.find_element_by_name('晚娘怪谈').click()


loginout()

search()