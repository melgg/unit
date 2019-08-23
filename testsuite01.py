#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, unittest

# 1、设置待执行用例的目录
test_dir = os.path.join(os.getcwd())

# 2、自动搜索指定目录下的cas，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
discover = unittest.defaultTestLoader.discover(test_dir+'/scripts', pattern='test*.py')

# 实例化TextTestRunner类
runner = unittest.TextTestRunner()

# 使用run()方法运行测试套件（即运行测试套件中的所有用例）
runner.run(discover)
