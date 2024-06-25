""" 添加到注册表  """
import os
import sys
import winreg as reg

import tkinter as tk
from tkinter import messagebox

def show_message(title, message):
    """ 显示消息框 """
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo(title, message) if title == "Success" else messagebox.showerror(title, message)
    root.destroy()


def check_and_add_to_registry():
    """ 检查是否已经添加到注册表，如果没有则添加 """
    # 获取当前执行的 exe 文件所在的路径
    exe_path = sys.executable  # 获取当前执行的 exe 文件路径
    current_dir = os.path.dirname(exe_path)  # 获取 exe 文件所在的目录
    exe_path = os.path.join(current_dir, 'remark.exe')
    
    # 注册表路径
    reg_path_background = r"Directory\Background\shell\AddFolderRemark"
    back_command_key = reg_path_background + r"\command"
    
    reg_path_folder = r"Directory\shell\AddFolderRemark"
    folder_command_key = reg_path_folder + r"\command"
    
    flag_key_path = r"Software\AddFolderRemark\RegistryFlag" # \HKEY_CURRENT_USER\SOFTWARE\

    try:
        # 打开或创建用于记录标志的注册表键
        flag_key = reg.CreateKey(reg.HKEY_CURRENT_USER, flag_key_path)
        flag_value, _ = reg.QueryValueEx(flag_key, 'IsRegistered')

        # 如果标志存在且为True，说明已经注册过，直接返回
        if flag_value:
            return

    except FileNotFoundError:
        # 如果标志键不存在，则继续执行添加注册表的操作
        pass

    try:
        ## 1. 创建注册表键 background
        reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, reg_path_background)
        reg.SetValue(reg_key, '', reg.REG_SZ, '添加备注')
        reg.SetValueEx(reg_key, 'Icon', 0, reg.REG_SZ, exe_path)  # 设置 Icon 值
        reg.CloseKey(reg_key)

        # 创建 command 键
        back_command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, back_command_key)
        reg.SetValue(back_command_key, '', reg.REG_SZ, f'"{exe_path}" "%V"')
        reg.CloseKey(back_command_key)
        
        ## 2. 创建注册表键 folder 
        reg_key_folder = reg.CreateKey(reg.HKEY_CLASSES_ROOT, reg_path_folder)
        reg.SetValue(reg_key_folder, '', reg.REG_SZ, '添加备注')
        reg.SetValueEx(reg_key_folder, 'Icon', 0, reg.REG_SZ, exe_path)  # 设置 Icon 值
        reg.CloseKey(reg_key_folder)

        # 创建 command 键
        folder_command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, folder_command_key)
        reg.SetValue(folder_command_key, '', reg.REG_SZ, f'"{exe_path}" "%1"')
        reg.CloseKey(folder_command_key)

        # 设置标志为True，表示已经完成注册表修改
        reg.SetValueEx(flag_key, 'IsRegistered', 0, reg.REG_SZ, "True")
        reg.CloseKey(flag_key)
        
        show_message("Success", "Successfully added to registry.")
    
    except Exception as e:
        show_message("Error", f"Failed to add to registry: {e}")
        
        
if __name__ == "__main__":
    check_and_add_to_registry()