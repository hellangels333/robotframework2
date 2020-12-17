*** Settings ***

Library  药品管理.py   WITH NAME  F

Library  药品管理.c1   WITH NAME  c1



*** Test Cases ***

药品管理 UI-0101

  c1.teststeps
