import tkinter.filedialog
from tkinter import messagebox
import tkinter
import xlcmp
import xlwt


class SelectFile():
    def __init__(self):
        self.win=tkinter.Tk(screenName='400x300')
        self.win.title('Excel数据对比工具')
        self.win.resizable(0,0)
        self.win.geometry('700x300+350+150')
        self.file_1=tkinter.StringVar()
        self.file_2=tkinter.StringVar()
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        label_1=tkinter.Label(self.win,text='请选择文件')
        # label_1.grid(column=0,row=0)
        label_1.grid(column=0,row=0,sticky='n',padx=10,pady=20)
        name_1=tkinter.Entry(self.win,width=60,textvariable=self.file_1)
        name_1.grid(column=0,row=1,sticky='w',padx=60,pady=10)
        choose_1=tkinter.Button(self.win,text='选择校验文件',command=self.get_file_1)
        choose_1.grid(column=1,row=1,sticky='e',padx=10,pady=10)
        name_2=tkinter.Entry(self.win,width=60,textvariable=self.file_2)
        name_2.grid(column=0,row=5,sticky='sw',padx=60,pady=10)
        choose_2=tkinter.Button(self.win,text='设置基准文件',command=self.get_file_2)
        choose_2.grid(column=1,row=5,sticky='se',padx=10,pady=10)
        confirm=tkinter.Button(self.win,text='对比文件',command=self.excel_cmp)
        confirm.grid(column=0,row=6,sticky='s',padx=10,pady=20)

    def get_file_1(self):
        self.file_1.set(tkinter.filedialog.askopenfilename(title='选择一个文件',filetypes=[('Excel文件','.xls')]))
        # print(self.file_1.get())

    def get_file_2(self):
        self.file_2.set(tkinter.filedialog.askopenfilename(title='选择一个文件',filetypes=[('Excel文件','.xls')]))
        # response=messagebox.askretrycancel(title='Nice',message='Please confirm')
        # label_1=tkinter.Label(self.win,text=self.file_2)
        # label_1.pack()
        # print(self.file_2.get())

    def excel_cmp(self):
        if self.file_1.get()==self.file_2.get():
            responses=messagebox.askretrycancel(title='Wrong',message='请不要选择同一个文件！')
        # print('confirm')
        temp=xlcmp.XlCmp(self.file_1.get(),self.file_2.get())#这里要捕获异常，捕获文件占用的异常，并且弹出警告；其它的异常需要打印出来
        if temp.same:
            pass#表示数据一致
        else:
            print(temp.diff)
            print('different!')

            pass#弹出窗口下载文件

        pass



try:
    a=SelectFile()
except:
    pass
