from lib.webui import *


def suite_setup():
    INFO('suite_setup "管理员操作”下的全局“setup')
    # wd = open_browser()
    # mgr_login(get_global_webdriver())
    pass


# def suite_teardown():
#     INFO('suite_teardown "管理员操作”测试套件的全局teardown')
#     wd = get_global_webdriver()
#     wd.quit()


force_tags = ['冒烟测试', 'UI测试', '当前目录下的全局级别标签']  # 当前目录下的全局级别标签
