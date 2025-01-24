import hashlib
import os.path
import tkinter as tk

class copy(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master = master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.l = tk.Label(self)
        self.l.pack()
        self.l1 = tk.Label(self, text='请输入源文件目录')
        self.l1.pack()
        self.i1 = tk.Entry(self, show=None, font=('Arial', 14))
        self.i1.pack()
        self.l2 = tk.Label(self, text='请输入输出目录')
        self.l2.pack()
        self.i2 = tk.Entry(self, show=None, font=('Arial', 14))
        self.i2.pack()
        self.b = tk.Button(self, text='复制', command=self.hit)
        self.b.pack()

    def hit(self):
        source_dir = self.i1.get()
        target_dir = self.i2.get()

        if not os.path.isdir(source_dir) or not os.path.isdir(target_dir):
            self.l['text'] = '请检查路径是否正确'
            return

        mmap = {}
        # 遍历目标目录，获取所有文件的文件名与哈希值
        for file in os.listdir(target_dir):
            file_name = os.path.join(target_dir, file)
            with open(file_name, 'rb') as f:
                content = f.read()
                hash_value = hashlib.md5(content).hexdigest()
                mmap[hash_value] = file_name

        # 遍历源目录，比较每个文件的哈希值与目标目录中已存在的文件哈希值
        for file in os.listdir(source_dir):
            file_name = os.path.join(source_dir, file)
            with open(file_name, 'rb') as f:
                content = f.read()
                hash_value = hashlib.md5(content).hexdigest()
                if hash_value in mmap:
                    print(f'{file_name} 已存在, 跳过')
                    continue
                else:
                    new_file_name = os.path.join(target_dir, file)
                    with open(new_file_name, 'wb') as f:
                        f.write(content)
                        print(f'{file_name} 复制成功')



windows = copy()
windows.master.title("文件复制")
windows.master.geometry("500x300")
windows.mainloop()





