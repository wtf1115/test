import logging
import time
import os


class Logger(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        file_name = time.strftime("%Y%m%d %H%M",time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + "\\logs\\"
        full_path = log_path + file_name+'.log'         # file_name+'.log'是文件名     前面的log_path 是它的路径
        # 通过 FileHandler() 方法来创建handler 存放地   -----> 有一个绝对路径的参数
        file_handler = logging.FileHandler(full_path)
        # 再给他设置一个日记级别    因为在 DEBUG 下  只能比它的级别高，或相等  一般用INFO
        file_handler.setLevel(logging.INFO)

        # 再定义一个 （Handler定义成输出到控制台）
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)



        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)


    def getlog(self):
        return self.logger