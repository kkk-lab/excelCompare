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
        try:
            temp=xlcmp.XlCmp(self.file_1.get(),self.file_2.get())#这里要捕获异常，捕获文件占用的异常，并且弹出警告；其它的异常需要打印出来
            if temp.same:
                response=messagebox.showinfo(title='Nice',message='数据一致！')
                pass#表示数据一致
            else:
                print(temp.diff)
                print('different!')
                workbook = xlwt.Workbook()
                pattern = xlwt.Pattern()  # Create the Pattern
                pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
                pattern.pattern_fore_colour = 5  # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
                style = xlwt.XFStyle()  # Create the Pattern
                style.pattern = pattern  # Add Pattern to Style
                for k,v in temp.diff.items():
                    worksheet = workbook.add_sheet(k)
                    for i in v:
                        worksheet.write(i[0], i[1], i[2], style)

                download=messagebox.askyesno(title='下载',message='是否下载校验结果？')
                if download:
                    here=tkinter.filedialog.asksaveasfilename(filetypes=[('Excel文件','.xls')])#获取保存地址
                    here=here+'.xls'
                    # print(here)
                    workbook.save(here)#保存文件
                pass#弹出窗口下载文件
        except Exception as e:
            errors=messagebox.showerror(title='Wrong',message='请选择格式一致的文件！\n'+str(e))

        pass



try:
    a=SelectFile()
except:
    pass
