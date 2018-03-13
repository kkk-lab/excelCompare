# import Tkinter
# from Tkinter import *
import win32ui

dlg=win32ui.CreateFileDialog(1)
dlg.SetOFNInitialDir('D:/')
dlg.DoModal()
filename=dlg.GetPathName()
print(filename)

def test():
    print('It works!')

# root=Tk()
# root.title('Test')
# root.geometry('400x200')

# btn=Button(root,text='Click here',command=test)
# btn.pack()
# mainloop()
