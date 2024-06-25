# -*- coding: utf-8 -*
# Filename: comment.py
""" 在原有的代码基础上添加图形化界面, 且仅只能通过右键或者拖拽文件夹到exe上添加备注 """


import sys
import os
from pathlib import Path

import tkinter as tk
from tkinter import Text, Tk

DEBUG=0

defEncoding = sys.getfilesystemencoding() # 获取系统编码，确保备注不会出现乱码

def sys_encode(content):
    """ 将代码中的字符转换为系统编码 """
    return content.encode(defEncoding).decode(defEncoding)


def get_info_tip(filepath, encoding='GBK'):
    """ 获取文件的InfoTip信息 """
    # 确保文件路径与系统编码兼容
    filepath_encoded = sys_encode(filepath)
    
    # 打开并读取文件内容
    with open(filepath_encoded, 'r', encoding=encoding) as file:
        for line in file:
            if line.startswith('InfoTip='):
                # 获取等号后面的部分，并去除前后的空格
                info_tip = line.strip().split('=', 1)[1]
                break
            
    return info_tip


def run_command(command):
    os.system(command)


def get_setting_file_path(fpath):
    """ 获取设置文件路径 """
    return fpath + os.sep + 'desktop.ini'


def update_folder_comment(fpath, comment):
    """ 更新文件夹备注 """
    content = sys_encode(u'[.ShellClassInfo]' + os.linesep + 'InfoTip=')
    # 开始设置备注信息
    setting_file_path = get_setting_file_path(fpath)
    with open(setting_file_path, 'w') as f:
        f.write(content)
        f.write(sys_encode(comment + os.linesep))

    # 添加保护
    run_command('attrib \"' + setting_file_path + '\" +s +h')
    run_command('attrib \"' + fpath + '\" +s ')
    # 备注可能过一会才会显示


def add_comment(fpath=None, comment=None):
    """ 添加文件夹备注 """
    # 如果提供了文件夹路径，则使用
    if fpath is None and len(sys.argv) > 1:
        fpath = sys.argv[1]
    # 如果没有提供文件夹路径退出
    elif fpath is None:
        return 

    # 判断路径是否存在文件夹
    if not os.path.isdir(fpath):
        return 
    
    setting_file_path = get_setting_file_path(fpath)

    original_comment = ""
    # 如果设置文件已经存在
    if os.path.exists(setting_file_path):
        # 去除保护属性
        run_command('attrib \"' + setting_file_path + '\" -s -h')
        # 获取原备注信息
        original_comment = get_info_tip(setting_file_path)
        
    # 使用图形界面请求用户输入
    comment = get_user_input(fpath, original_comment)
    if not comment:  # 如果用户没有输入，退出函数
        comment = " "
        return
        
    update_folder_comment(fpath, comment)


def get_user_input(fpath, original_comment=""):
    """ 使用tkinter的Text控件获取用户输入, 按下回车自动确认 """
    def on_key_press(event):
        """ 处理按键事件 """
        if event.keysym == 'Return':  # 如果是回车
            submit_text()
            return "break"  # 阻止事件进一步传播

    def submit_text():
        """ 获取文本框内容并销毁窗口 """
        user_input = text.get("1.0", "end-1c")  # 获取文本框的所有内容
        if user_input.strip():  # 如果用户输入非空白字符
            input_var.set(user_input)  # 设置变量为用户输入
        root.destroy()  # 销毁窗口

    root = Tk()
    root.title(f"输入 {Path(fpath).name} 文件夹备注:")
    
    # 设置窗口图标
    root.iconbitmap('logo.ico')
    
    # 创建Text控件用于输入
    text = Text(root,width=40,height=10,font=('宋体',14))
    input_var = tk.StringVar()
    text.grid(row=0,column=0,columnspan=1)
    text.insert("1.0", original_comment)
    
    # 获取当前鼠标位置
    mouse_x = root.winfo_pointerx()
    mouse_y = root.winfo_pointery()
    root.geometry(f"+{mouse_x + 3}+{mouse_y + 5}") # 设置窗口位置
    
    text.bind("<KeyPress-Return>", on_key_press)  # 绑定回车按键事件
    text.focus_set() # 设置焦点到文本框
    root.wait_window(root)  # 等待窗口关闭
    
    return input_var.get()  # 返回用户输入


if __name__ == '__main__':
    if len(sys.argv) == 3:
        add_comment(sys.argv[1], sys.argv[2])
    elif len(sys.argv) <= 2:
        try:
            add_comment()
        except KeyboardInterrupt:
            if DEBUG:
                print(sys_encode(u"感谢使用"))