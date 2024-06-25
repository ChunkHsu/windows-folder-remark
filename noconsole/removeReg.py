""" 从注册表中删除添加的内容  """

import winreg as reg
import tkinter as tk
from tkinter import messagebox

DEBUG=0

def show_message(title, message):
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo(title, message) if title == "Success" else messagebox.showerror(title, message)
    root.destroy()


def remove_from_registry():
    """ 从注册表中删除添加的内容 """
    # 注册表路径
    reg_path_background = r"Directory\Background\shell\AddFolderRemark"
    back_command_key = reg_path_background + r"\command"
    
    reg_path_folder = r"Directory\shell\AddFolderRemark"
    folder_command_key = reg_path_folder + r"\command"
    
    flag_key_path = r"Software\AddFolderRemark\RegistryFlag"

    try:
        # 删除 back command 键
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, back_command_key)
        if DEBUG:
            print(f"Successfully deleted {back_command_key}.")

        # 删除 back AddFolderRemark 键
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, reg_path_background)
        if DEBUG:
            print(f"Successfully deleted {reg_path_background}.")

        # 删除 folder command 键
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, folder_command_key)
        if DEBUG:
            print(f"Successfully deleted {folder_command_key}.")

        # 删除 folder AddFolderRemark 键
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, reg_path_folder)
        if DEBUG:
            print(f"Successfully deleted {reg_path_folder}.")


        # 删除 flag_key_path 键
        reg.DeleteKey(reg.HKEY_CURRENT_USER, flag_key_path)
        if DEBUG:
            print(f"Successfully deleted {flag_key_path}.")
        
        show_message("Success", "Successfully removed from registry.")

    except FileNotFoundError as e:
        if DEBUG:
            print(f"Registry key not found: {e}")
        show_message("Error", f"Registry key not found: {e}")
        
    except Exception as e:
        if DEBUG:
            print(f"Failed to delete registry key: {e}")
        show_message("Error", f"Failed to delete registry key: {e}")

if __name__ == "__main__":
    remove_from_registry()
