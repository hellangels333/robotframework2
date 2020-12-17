注：setup、teardown 优先级

### 1.写在__st__.py 是当前目录下的全局setup、teardown，最先执行【注：文件你爱放哪放哪，反正就是位置决定覆盖的范围】
### 2.套件(py文件)级别的setup、teardown 第二优先级
### 3.用例(class)级别的setup、teardown 最后优先级执行