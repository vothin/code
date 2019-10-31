'''
OS 文件/目录方法

os模块:
    os.listdir()        列出指定目录下所有文件
    os.getcwd()         获取当前文件路径
    os.remove()         删除文件
    os.unlink()         删除文件
    os.rename()         重命名文件
    os.chdir()          改变当前工作目录
    os.mkdir()          新建目录
    os.rmdir()          删除空目录(删除非空目录, 使用shutil.rmtree())
    os.makedirs()       创建多级目录
    os.removedirs()     删除多级目录
    os.stat(file)       获取文件属性
    os.chmod(file)      修改文件权限
    os.utime(file)      修改文件时间戳
    os.name(file)       获取操作系统标识
    os.system()         执行操作系统命令
    os.execvp()         启动一个新进程
    os.fork()           获取父进程ID，在子进程返回中返回0
    os.execvp()         执行外部程序脚本（Uinx）
    os.spawn()          执行外部程序脚本（Windows）
    os.access(path, mode) 判断文件权限(详细参考cnblogs)
    os.wait()           暂时未知
'''

