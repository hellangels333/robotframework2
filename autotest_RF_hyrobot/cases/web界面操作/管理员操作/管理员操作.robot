*** Settings ***

Library  管理员操作.py   WITH NAME  F

Force Tags     冒烟测试   UI测试   套件py文件级别标签  

Library  管理员操作.c1   WITH NAME  c1

Library  管理员操作.c2   WITH NAME  c2



*** Test Cases ***

管理员首页 UI-0101
  [Tags]      这是一个标签   用例级别标签

  c1.teststeps


管理员首页 - UI-0102

  c2.teststeps
