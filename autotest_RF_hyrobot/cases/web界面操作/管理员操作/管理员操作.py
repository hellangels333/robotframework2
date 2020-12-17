import time

from hyrobot.common import *
from lib.webui import *

## 套件级别的setup、teardown
# def suite_setup():
#     INFO('suite_setup 一个测试套件的全局setup')
#     wd = open_browser()
#     mgr_login(wd)
#
#
# def suite_teardown():
#     INFO('suite_teardown 一个测试套件的全局teardown')
#     wd = get_global_webdriver()
#     wd.quit()
force_tags = ['冒烟测试', 'UI测试', '套件py文件级别标签']  # 套件py文件级别标签，执行的时候可以根据这个标签筛选，注:一定要放在列表中


class c1(object):
    """
    一个c1是一个用例(即一个功能)，包含一种或很多种场景
    """

    tags = ['这是一个标签', '用例级别标签']  # 用例级别标签
    name = "管理员首页 UI-0101"  # 用例可能是口语化的名字或者不规范，所以不放在类名中

    ## 用例级别的setup、teardown
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
        STEP(1, '登陆网站')
        # wd = open_browser()
        # mgr_login(wd)
        wd = get_global_webdriver()

        STEP(2, '获取左侧信息')  # 在控制台输出日志
        # 根据标签名找到元素
        wd.find_element_by_tag_name('button').click()
        # 先找到上层节点再缩小范围
        sidebarMenu = wd.find_element_by_class_name('sidebar-menu')
        # 再找到内部的各个元素
        element = sidebarMenu.find_elements_by_tag_name('span')

        STEP(3, '对比是否符合预期')  # 在控制台输出日志
        menuTitles = []
        for ele in element:
            INFO(ele.text)  # INFO() RF框架内置函数，在控制台的日志输出提示信息
            menuTitles.append(ele.text)

        CHECK_POINT("侧边栏菜单是否正确",
                    menuTitles[:3] == ['客户', '药品', '订单'])  # CHECK_POINT() RF框架内置函数， 检查点

        # print('*****检查点*****  侧边栏菜单是否正确----------', end='')
        # if menuTitles[:3] == ['客户', '药品', '订单']:
        #     print('通过')
        # else:
        #     print("不通过")
        #     exit(1)
        # wd.quit()


# 类名保证唯一，推荐包含用例编号
class c2:
    name = '管理员首页 - UI-0102'

    # def setup(self):
    #     wd = open_browser()
    #     mgr_login(wd)
    #
    # def teardown(self):
    #     wd = get_global_webdriver()
    #     wd.quit()

    def teststeps(self):
        STEP(1, '登陆网站')
        wd = get_global_webdriver()

        # 根据标签名查找元素
        wd.find_element_by_tag_name('button').click()

        STEP(2, '点击左侧客户菜单')

        # 先找到上层节点，缩小查找范围
        sidebarMenu = wd.find_element_by_class_name('sidebar-menu')

        # 再找到内部元素
        elements = sidebarMenu.find_elements_by_tag_name('span')

        # 第一个span对应的菜单是 客户，点击它
        elements[0].click()

        STEP(3, '添加客户')

        # 点击添加客户按钮
        wd.find_element_by_class_name('glyphicon-plus').click()

        # form-contorl 对应3个输入框
        inputs = wd.find_element_by_class_name('add-one-area') \
            .find_elements_by_class_name('form-control')

        # 输入客户姓名
        inputs[0].send_keys('南京中医院')
        # 输入联系电话
        inputs[1].send_keys('2551867858')
        # 输入客户描述
        inputs[2].send_keys('江苏省-南京市-秦淮区-汉中路-16栋504')

        # 第1个 btn-xs 就是创建按钮， 点击创建按钮
        wd.find_element_by_class_name('add-one-area') \
            .find_element_by_class_name('btn-xs') \
            .click()

        # 等待1秒
        time.sleep(1)

        STEP(4, '检查添加信息')

        # 找到 列表最上面的一栏
        item = wd.find_elements_by_class_name('search-result-item')[0]

        fields = item.find_elements_by_tag_name('span')[:6]

        texts = [field.text for field in fields]
        print(texts)

        # 预期内容为
        expected = [
            '客户名：',
            '南京中医院',
            '联系电话：',
            '2551867858',
            '地址：',
            '江苏省-南京市-秦淮区-汉中路-16栋504'
        ]

        CHECK_POINT('客户信息和添加内容一致 ',
                    texts == expected)
