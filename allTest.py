import unittest
import os
import HTMLTestRunner
import time
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# sys.path.append('D:\Program Files (x86)\python\Lib\site-packages')

def allTest():
    '''获取到所有的模块'''
    suite=unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None)
    return suite


def getNowTime():
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def run():
    fileName=os.path.join(os.path.dirname(__file__),'report',getNowTime()+'report.html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fileName,'wb'),
        title='UI 测试自动化报告',
        description='UI自动化详细报告测试').run(allTest())
if __name__ == '__main__':
    run()