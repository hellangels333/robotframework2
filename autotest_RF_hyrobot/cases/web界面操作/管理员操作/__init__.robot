*** Settings ***

Library  __st__.py   WITH NAME  D

Suite Setup    D.suite_setup

Force Tags     冒烟测试   UI测试   当前目录下的全局级别标签  

