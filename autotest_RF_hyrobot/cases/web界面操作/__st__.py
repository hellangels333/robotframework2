from lib.webui import *


def suite_setup():
    INFO('suite_setup “web界面操作”测试套件的全局setup')
    wd = open_browser()
    mgr_login(wd)


def suite_teardown():
    INFO('suite_teardown “web界面操作”测试套件的全局teardown')
    wd = get_global_webdriver()
    wd.quit()
