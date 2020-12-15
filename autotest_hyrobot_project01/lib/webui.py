from selenium import webdriver
from hyrobot.common import *


def open_browser():
    print('打开浏览器')
    wd = webdriver.Chrome(r'C:\Users\Administrator\chromedriver.exe')
    wd.implicitly_wait(5)
    GSTORE['global_webdriver'] = wd  # 设置一个全局变量
    return wd


def get_global_webdriver():
    return GSTORE['global_webdriver']


def mgr_login(wd):
    wd.get('http://127.0.0.1/mgr/sign.html')

    # 根据 ID 选择元素，并且输入字符串
    wd.find_element_by_id('username').send_keys('byhy')
    wd.find_element_by_id('password').send_keys('88888888')

    # 根据标签名查找元素
    wd.find_element_by_tag_name('button').click()
