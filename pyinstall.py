from PyInstaller.__main__ import run
if __name__ == '__main__':
    opts = [r'C:\excelCompare\test.py',\
            '-F','-w',r'--distpath=C:\excelCompare',\
            r'--workpath=D:\TEMP',\
            r'--specpath=D:\TEMP\']
    run(opts)
