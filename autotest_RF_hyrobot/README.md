## 笔记20201217

## 1 运行方法

    框架：在Terminal执行 run 
    被测对象：参考页面http://www.python3.vip/prac/pub/info/bysms/

## 2 实现原理

    在Terminal执行 run 后是先把py文件转为robot文件后用RF框架执行并生成报告 
    默认是run.bat文件为启动文件，若代码没动可以启动rf.bat直接生成报告

## 3.建议阅读顺序

- 熟悉需求
- 查看用例，梳理用例
- 看case，梳理testcase
- 运行，熟悉框架代码

## 4.选择部分用例执行

### 4.1 根据用例名称、套件名称来执行(支持通配符)

    --test testA  # 执行名为testA的用例
    --test testA --test testB # 执行名为testA和testB的用例
    --suit 客户操作  # 执行名为 客户操作 的套件
    例如： run --test "管理员首页 UI-0101"  只执行这个name的用例class，有空格的要用引号引起来
    例如2：run --test *0101   用通配符来找一类的用例class
    例如3：run --suit *操作   用通配符来找一类的套件suit来执行

### 4.2 把参数放在一个文件里执行

    在args写如下内容:
    --test "管理员首页 UI-0101"
    --test *0101
    执行的时候用如下命令执行: 
    run -A args

### 4.3 用标签来筛选【冒烟测试、UI测试、非必须执行用例】

#### 4.3.1 三种级别的标签

    1. 在__st__.py里面加的话是给当前范围内的所有用例打标签
    force_tags = ['冒烟测试', 'UI测试', '当前目录下的全局级别标签']  # 当前目录下的全局级别标
    2. 在套件py文件里打标签
    force_tags = ['冒烟测试', 'UI测试', '套件py文件级别标签']  # 套件py文件级别标签
    3. 在用例class内
    tags = ['这是一个标签', '用例级别标签']  # 用例级别标签

#### 4.3.2 挑选执行

    # 执行包含 标签 '冒烟测试' 的用例. 
    --include 冒烟测试
    # 执行不包含标签 '冒烟测试' 的用例.
    --exclude 冒烟测试
    # 执行 有冒烟测试、UITest 两个标签的用例
    --include 冒烟测试ANDUITest
    # 执行 有 冒烟测试 或者 UITest 标签 的用例
    --include 冒烟测试   --include UITest
    # 执行标签格式为 A*B 的用例，比如 A5B， AB， A444B
    --include A*B

#### 4.3.3 基于标签，可以指定关键用例（只要有没过的都是不通过，报告的背景绿色变红色）【注：若没指定就是全部都是关键用例】

    指定 只有具有 first 标签的用例才是关键用例 其它都不是
    run --critical first
    指定 具有 first 标签的用例是非关键用例，其他用例都是关键用例
    run --noncritical first
    指定 具有 以 basic 开头 或者 important开头 的标签 的用例都是关键用例，其他用例都不是关键用例
    run --critical basic*  --critical important*
    执行时指定这个用例为非关键用例
    run --nocritical order1

## 5.一些特殊参数

    清除所有robot用例文件
    使用参数 run.bat --delrf 删除已经存在的 robotframework格式的用例，不执行测试
    只转化Python用例为robotframework格式用例
    使用参数 run.bat --torf 只执行转化Python用例为RF用例，不执行转化好的RF测试用例
    只运行测试
    使用参数 run.bat --runrf 直接执行已经存在的robotframework用例，不执行转化Python用例为RF用例操作
    只汉化测试报告
    使用参数 run.bat --hanrf 只执行把测试报告汉化的工作，不执行转化和测试

### 测试用例设计原则

- 会话保持，提高连贯性
- 谁初始化动了环境谁负责清除环境

### tips

- 一个套件 可以是一个py文件也可以是一个目录
- 一个class是一个用例
- 套件名和用例名可以中文，用例名一定要和测试用例一致 这样更直观
- 该框架是RF框架的升级版本，支持报告汉化、修改书写时候的语法(RF的语法改为Python语法)
- 报告是层层嵌套的，一个断言失败了会在很多处出现，注意观察格式