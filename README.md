# excelCompare

aa.spec是pyinstaller的配置文件，使用方法：进入要打包的目录，执行 pyinstaller aa.spec
需要下载windows sdk，并且配置环境变量，其中sdk的配置要和python版本位数一致（tkinter需要用到其中的几个dll，其实不用整个sdk的）
经测试，可以在win10使用，因为sdk就是用的win10的dll。

