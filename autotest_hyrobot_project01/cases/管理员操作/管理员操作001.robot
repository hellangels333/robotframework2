*** Settings ***

Library  管理员操作001.py   WITH NAME  F

Library  管理员操作001.c1   WITH NAME  c1

Library  管理员操作001.c2   WITH NAME  c2



*** Test Cases ***

管理员首页 UI-0101
  [Setup]     c1.setup
  [Teardown]  c1.teardown

  c1.teststeps


管理员首页 - UI-0102
  [Setup]     c2.setup
  [Teardown]  c2.teardown

  c2.teststeps
