# -*-coding:utf-8 -*-
# File :run.py
# Author:George
# Date : 2019/9/21
# motto: Someone always give up while someone always try!

import unittest
from BSTestRunner import BSTestRunner
import time
import os


def weather_api_run():
    """
    This is the switch function for the whole testcase
    :return:
    """

    # get current file dictionary
    base_dir = os.path.dirname(__file__)
    print("The project direction is {}".format(base_dir))

    # get testcase file dictionary
    testcase_dir = '/'.join([base_dir, 'testcase'])
    print("The testcase dir is {}".format(testcase_dir))

    # get test report dectionary
    report_dir = '/'.join([base_dir, 'reports'])
    print("The report direction is {}".format(report_dir))

    # instantiation a discovery object which could find testcase in corresponding dictionary  with regex match file
    discovery = unittest.defaultTestLoader.discover(testcase_dir, pattern='weather*.py')

    # get time then
    time_now = time.strftime("%Y-%m-%d_%H_%M_%S")

    # to joint the  report file path
    report_path = report_dir + '/' + time_now + 'test_report.html'

    # handle the test report with stream method
    with open(report_path, 'wb') as fw:
        runner = BSTestRunner(stream=fw, title='weather api test', description="天气接口测试报告")
        runner.run(discovery)


if __name__ == "__main__":
    weather_api_run()
