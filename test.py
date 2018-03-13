import tkinter.filedialog
from tkinter import messagebox
import xlrd
import xlwt
import tkinter


class SelectFile():
    def __init__(self):
        self.win=tkinter.Tk(screenName='400x300')
        self.win.title('Excel数据对比工具')
        self.win.resizable(0,0)
        self.win.geometry('720x360')
        self.file_1=tkinter.StringVar()
        self.file_2=tkinter.StringVar()
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_1=tkinter.Label(self.win,text='请选择文件')
        label_1.pack()
        name_1=tkinter.Entry(self.win,width=60,textvariable=self.file_1)
        name_1.pack()
        choose_1=tkinter.Button(self.win,text='Get File',command=self.get_file_1)
        choose_1.pack()
        name_2=tkinter.Entry(self.win,width=60,textvariable=self.file_2)
        name_2.pack()
        choose_2=tkinter.Button(self.win,text='Next File',command=self.get_file_2)
        choose_2.pack()
        confirm=tkinter.Button(self.win,text='对比文件',command=self.excel_cmp)
        confirm.pack()

    def get_file_1(self):
        self.file_1.set(tkinter.filedialog.askopenfilename(title='选择一个文件',filetypes=[('Excel文件','.xls')]))
        # print(self.file_1.get())

    def get_file_2(self):
        self.file_2.set(tkinter.filedialog.askopenfilename(title='选择一个文件',filetypes=[('Excel文件','.xls')]))
        response=messagebox.askretrycancel(title='Nice',message='Please confirm')
        # label_1=tkinter.Label(self.win,text=self.file_2)
        # label_1.pack()
        # print(self.file_2.get())

    def excel_cmp(self):
        if self.file_1.get()==self.file_2.get():
            responses=messagebox.askretrycancel(title='Wrong',message='请不要选择同一个文件！')
        print('confirm')
        pass




try:
    a=SelectFile()
except:
    pass
