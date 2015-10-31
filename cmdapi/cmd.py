#encoding: utf-8
import os

os.system('ping www.baidu.com')
# a=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
# 	subprocess.Popen(CMD,stdout=what,stderr=what)
#a=subprocess.Popen('ping www.baidu.com',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

p = subprocess.Popen('ping www.baidu.com', shell=True, close_fds=True, # 必须加上close_fds=True，否则子进程会一直存在
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


raw_input();