# pyinstall

PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules. PyInstaller supports Python 3.6 or newer, and correctly bundles the major Python packages such as numpy, PyQt, Django, wxPython, and others.

Note: It is not a cross-compiler: to make a Windows app you run PyInstaller in Windows; to make a GNU/Linux app you run it in GNU/Linux, etc. 

Document: [Pyinstaller Homepage](https://pyinstaller.readthedocs.io/en/stable/index.html)

##

在终端将位置切换到python 位置

`pyinstall -F <file name>`

1. 首次打包时直接-F 完成打包
2. 编辑*.spec文件，通过在列表中添加对应元祖信息的方式，追加依赖文件
3. pyinstaller -F *.spec进行二次打包即可追加文件至exe中。

## Spec file
reference: [Using Spec Files](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) 
