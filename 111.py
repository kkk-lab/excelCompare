from tkinter import *
#定义Button的回调函数
def helloButton():
    print('hello button')
root = Tk()
#通过command属性来指定Button的回调函数
Button(root,text = 'Hello Button',command = helloButton).pack()
root.mainloop()
