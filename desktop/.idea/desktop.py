# -*- coding: UTF-8 -*-
# 环境要求:python2.7x,PIL,pywin32
# 备注:只在win7系统试过正常
# 创建时间:2015-1

import Image
import win32api, win32con, win32gui
import re, os
import time,datetime


def set_wallpaper_from_bmp(bmp_path):
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmp_path, win32con.SPIF_SENDWININICHANGE)


def set_wallpaper(img_path):
    # 把图片格式统一转换成bmp格式,并放在源图片的同一目录
    img_dir = os.path.dirname(img_path)
    bmpImage = Image.open(img_path)
    new_bmp_path = os.path.join(img_dir, 'wallpaper.bmp')
    bmpImage.save(new_bmp_path, "BMP")
    set_wallpaper_from_bmp(new_bmp_path)

def get_pic_by_week(date):
    dic='C:\\Users\\zhuzhengren\\Desktop\\壁纸\\'
    week_pic={
        0:'1-月球.jpg',
        1:'2-火星.jpg',
        2:'3-水星.jpg',
        3:'4-木星.jpg',
        4:'5-金星.jpg',
        5:'6-土星.jpg',
        6:'7-太阳.png'
    }
    pic = dic+week_pic[date.weekday()]
    return pic

if __name__ == '__main__':
    date = datetime.datetime.now()
    pic=unicode(get_pic_by_week(date),'utf-8')
    print(pic)
    set_wallpaper(pic)