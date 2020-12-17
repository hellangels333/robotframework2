from lib.webui import *


class c1(object):
    """
    一个c1是一个用例(即一个功能)，包含一种或很多种场景
    """
    name = "药品管理 UI-0101"  # 用例可能是口语化的名字或者不规范，所以不放在类名中

    # def setup(self):
    #     wd = open_browser()
    #     mgr_login(wd)
    #     print("这里是用例级别的setup")
    #
    # def teardown(self):
    #     wd = get_global_webdriver()
    #     wd.quit()
    #     print("这里是用例级别的teardown")

    def teststeps(self):
        STEP(1, '药品操作')
        pass
