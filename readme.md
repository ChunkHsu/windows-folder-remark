# Windows 下给文件夹添加注释

## 如何使用

本工具提供 exe 版本和 python 源码版本，exe 版本为 dist/remark.exe，可以将文件夹拖到exe，源码版本支持的版本为 Python 3.x

## 使用方式

1. 首先使用管理员打开`addToReg.exe` *目的是添加到注册表*
2. 此时选中一个文件夹右键后弹出的选项会有`添加备注`
3. 两种使用方式
   - 右键点击文件夹即可弹出添加备注窗口
   - 直接将文件夹拖到`remark.exe`上
4. 卸载时需要使用管理员打开`removeReg.exe` *目的是删除之前修改的注册表*，之后再删除`remark.exe`即可

---

## 注意
- 该脚本会修改文件夹下隐藏的 Desktop.ini 文件，并为文件夹修饰系统属性
- 三个exe文件一定放在同一个文件夹内
- 一定不要给exe文件改名
- 添加的注册表有三项
  - `HKEY_CLASSES_ROOT\Directory\Background\shell\AddFolderRemark`    
  - `HKEY_CLASSES_ROOT\Directory\shell\AddFolderRemark`
  - `HKEY_CURRENT_USER\Software\AddFolderRemark\RegistryFlag`