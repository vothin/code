#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: start_appiumServer.py
    @time: 2019/10/29 11:57
    @desc:
'''
# ********************************************************

import subprocess, os
from time import ctime
from yzmbwf.base.globalpath import appium_log_path
from yzmbwf.common.recordlog import logs
import psutil, time

# 查看程序是否运行
def judgeProcess(pro_name):

    '''查看程序是否运行'''
    p = psutil.pids()
    for pid in p:
        if psutil.Process(pid).name() == pro_name:
            return True

    else:
        print('not found')
        return False


# 链接设备devices
def connect_deiver():

    '''链接设备devices'''
    # cmd = 'adb connect 127.0.0.1:62001'
    # os.popen(cmd, mode='r')
    os.system(r'.\connect_moniqi.bat')


# 启动模拟器
def start_moniqi(p_name):
    os.system(r'.\start_moniqi.bat')
    time.sleep(10)
    if judgeProcess(p_name):
        connect_deiver()
    else:
        logs.error('device is False')


# 查看进行ID
def kill_APPiumS(port):

    '''查看进行ID'''
    try:
        process = os.popen('netstat -aon |findstr %s' % port).read()
        print(process)
        pid = process.split()[4]
        print("%s端口的进程ID为: \033[31;1m%s\033[0m" % (port, pid))
    except Exception as e:
        print("not found port")

# 停止进程
def stop_process(pro_id):

    '''停止进程'''
    try:
        os.system('taskkill -f -pid %s' % pro_id)   # 显示乱码，可在setting->editor->File Encodings->设置global_encoding设置GBK
    except Exception:
        pro_id('not found process')


# 启动appium服务
def start_appium(host, port):

    '''启动appium服务'''
    bootstrap_port = str(port + 1)  # 启动多个端口
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' bootstrap-port ' + str(bootstrap_port)  # 注意前后空格
    print('%s at %s' % (cmd, ctime()))
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdout=open('%s/' % appium_log_path + str(port) + '_device.log', 'a'),
                         stderr=subprocess.STDOUT)
    p.wait()



if __name__ == '__main__':
    # connect_deiver()
    # start_moniqi('Nox.exe')
    host = '127.0.0.1'
    port = 4723
    start_appium(host, port)
    # judgeProcess('Nox.exe')
    # kill_APPiumS(4723)
    # stop_process(8444)








