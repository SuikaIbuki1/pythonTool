import tkinter as tk
from pathlib import Path
import os
import shutil

class copy(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master = master)
        self.pack()
        self.createWidgets()

    # 创建界面
    def createWidgets(self):
        self.l = tk.Label(self)
        self.l.pack()
        self.l1 = tk.Label(self, text = '请输入源文件目录')
        self.l1.pack()
        self.i1 = tk.Entry(self, show=None, font=('Arial', 14))
        self.i1.pack()
        self.l2 = tk.Label(self, text = '请输入输出目录')
        self.l2.pack()
        self.i2 = tk.Entry(self, show=None, font=('Arial', 14))
        self.i2.pack()
        self.l3 = tk.Label(self, text = '请输入文件后缀')
        self.l3.pack()
        self.i3 = tk.Entry(self, show=None, font=('Arial', 14))
        self.i3.pack()
        self.b = tk.Button(self, text = '复制', command = self.hit)
        self.b.pack()

    # 点击事件
    def hit(self):
        op = self.i1.get()
        np = self.i2.get()
        axios = self.i3.get()
        self.copytree(op, np, axios)
        print("完成")

    # 递归检查文件夹并复制文件
    def copytree(self, src, dst, axios, symlinks=False):
        names = os.listdir(src)
        print(names)
        # os.makedirs(dst)
        errors = []
        for name in names:
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                if os.path.isdir(srcname):
                    self.copytree(srcname, dst, axios, symlinks)
                else:
                    if srcname == srcname.split(axios)[0]:
                        continue
                    shutil.copy2(srcname, dstname)
            except OSError as why:
                errors.append((srcname, dstname, str(why)))
            except shutil.Error as err:
                errors.extend(err.args[0])

windows = copy()
windows.master.title("文件复制")
windows.master.geometry("500x300")
windows.mainloop()

