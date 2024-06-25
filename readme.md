# Windows 下给文件夹添加备注

## 说明

本工具可以在 Windows 下给文件夹添加备注，源码版本支持的版本为 Python 3.x

## 使用方式
下载`release`下面的`remark`压缩包
1. 需要先打开文件夹的备注标签
   
   ![image](https://github.com/ChunkHsu/windows-folder-remark/assets/92206375/f3d7308e-0713-441d-a514-209dc34a5936)
   ![image](https://github.com/ChunkHsu/windows-folder-remark/assets/92206375/10f718ee-f7cb-4832-b1b7-d07a159c122d)
2. 将下载的压缩包解压到存放软件的位置(目录中最好不要有中文字符)
3. 进入刚刚解压的文件夹，使用管理员方式打开`addToReg.exe` *目的是将软件exe路径添加到注册表*
4. 此时任意选中一个文件夹右键后弹出的选项会有`添加备注`选项
5. 一共两种使用方式
   - 右键点击文件夹即可弹出添加备注窗口
   - 直接将文件夹拖到`remark.exe`上
  
在弹出的添加备注窗口中输入备注后回车即可
   ![image](https://github.com/ChunkHsu/windows-folder-remark/assets/92206375/df8c0167-e63a-47c4-bf35-0c8f3d4757fa) 
   
等待一会儿后文件夹的备注栏中会显示刚刚的备注信息
   ![image](https://github.com/ChunkHsu/windows-folder-remark/assets/92206375/47ab90e2-7179-4d3d-af9f-7861d4048329)

6. 卸载时需要使用管理员打开`removeReg.exe` *目的是删除之前修改的注册表*，之后再删除`remark.exe`即可

---

## 注意
- 该脚本会修改文件夹下隐藏的 Desktop.ini 文件，并为文件夹修饰系统属性
- 三个exe文件一定放在同一个文件夹内
- 一定不要给exe文件改名
- addToReg.exe添加的注册表有三项
  - `HKEY_CLASSES_ROOT\Directory\Background\shell\AddFolderRemark`    
  - `HKEY_CLASSES_ROOT\Directory\shell\AddFolderRemark`
  - `HKEY_CURRENT_USER\Software\AddFolderRemark\RegistryFlag`
