import os
import subprocess

print(os.getppid())
# procesid = os.fork()
# print(procesid)
print('-------------------------------------')

# r = subprocess.call(['nslookup'])
# print('Exit code:', r)

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hellnolabel = Label(self, 'Hello,world!')
        self.hellnolabel.pack()
        self.hellnobutton = Button(self, 'Quit', command=self.quit())
        self.hellnobutton.pack()


app = Application()
app.master.title("我是标题")
# 主消息循环
app.mainloop()
