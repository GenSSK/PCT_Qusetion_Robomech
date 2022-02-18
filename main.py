# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk
from tkinter import ttk
import ctypes
# import numpy as np
# import pandas as pd
import pickle
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)


        # 初期設定
        self.master.title("アンケート")  # ウィンドウタイトル
        self.master.geometry("1020x1000")
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.Question = [
            "Q1. これはどうでしたか？",
            "Q2. それはどうでしたか？",
            "Q3. あれはどうでしたか？",
            "Q4. それでどうでしたか？",
        ]

        self.data = ['0'] * (1 + 4 + len(self.Question))
        self.first_flag = False

        self.filename = 'answer.bin'

        if os.path.exists(self.filename):
            with open('answer.bin', 'rb') as pk:
                self.read_file = pickle.load(pk)
        else:
            self.first_flag = True

        self.scale_var = []  # スケールの値格納

        frame1 = ttk.Frame(self.master, padding=10)
        frame1.grid()

        name_order = ["自分の名前", "被験者1", "被験者2", "被験者3"]
        name_list = ["g.sasaki",
                     "d.miyamoto",
                     "b.poitrimol",
                     "k.kobayashi",
                     "y.sugano",
                     "t.yumiya",
                     "n.takahashi",
                     "k.tozuka",
                     "h.nakanishi",
                     "y.inoue",
                     "h.nishimura",
                     "y.baba",
                     "y.yoshida",
                     "c.xu",
                     "y.ito",
                     "t.kassai",
                     "ko.kobayashi",
                     "t.shike",
                     "m.suga",
                     "h.tagaya",
                     "d.yamazaki",
                     "t.yamamoto",
                     "s.watanabe",
                     "s.sanuka",
                     "s.tsuchiya",
                     "n.ito",
                     "k.ohya",
                     "t.onogawa",
                     "t.oriuchi",
                     "i.kato",
                     "k.sato",
                     "r.tanaka",
                     "m.nakamura",
                     "y.noguchi",
                     "t.bitoh",
                     "h.mori",
                     "y.yamada"]

        # アンサー
        self.subject = []
        for i in range(len(name_order)):
            answer_text = tk.Label(frame1, text=name_order[i])
            answer_text.grid(row=0, column=i)

            self.subject.append(tk.StringVar())
            cb = ttk.Combobox(
                frame1,
                values=name_list,
                textvariable=self.subject[i],
            )
            # cb.bind('<<ComboboxSelected>>', select_cb)
            cb.set("")
            cb.grid(row=1, column=i)
            cb.grid_configure(padx=5, pady=5)





        frame2 = ttk.Frame(self.master, padding=10)
        frame2.grid()

        # radioウィジェット
        radio_text = tk.Label(frame2, text="実験の選択")
        radio_text.grid(row=0, column=1)

        self.select_var = tk.IntVar()  # ウィジェット変数select_varを作成
        self.select_var.set(0)  # select_var変数に数値をセット

        self.mode = [("normal", 0), ("alone", 1), ("nothing", 2)]  # languagesリストを定義

        for i, val in self.mode:  # ループ開始
            radio = tk.Radiobutton(frame2,
                                   command = self.slider_scroll,
                                   text=i,
                                   value=val,
                                   variable=self.select_var
                                   )  # languagesリストを選択肢とするradio1ウィジェットを生成
            radio.grid(row=1, column=val)  # radio1ウィジェットを配置






        frame3 = ttk.Frame(self.master, padding=10)
        frame3.grid()

        for i in range(len(self.Question)):
            # #文字
            # text = tk.Label(self.master, text=Question[i])
            # text.pack(side="top")

            # 格納する値を追加
            self.scale_var.append(tk.DoubleVar())
            self.scale_var[i].set(50)
            # Scale（オプションをいくつか設定）
            scaleH = tk.Scale(frame3,
                              variable=self.scale_var[i],
                              command=self.slider_scroll,
                              activebackground='skyblue',
                              label=self.Question[i],
                              orient=tk.HORIZONTAL,  # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                              length=1000,  # 全体の長さ
                              width=20,  # 全体の太さ
                              sliderlength=20,  # スライダー（つまみ）の幅
                              from_=0,  # 最小値（開始の値）
                              to=100,  # 最大値（終了の値）
                              resolution=1,  # 変化の分解能(初期値:1)
                              showvalue=False,
                              # tickinterval = 50         # 目盛りの分解能(初期値0で表示なし)
                              )
            scaleH.grid(row=i * 2)

            text = tk.Label(frame3, text="よくない                         "
                                         "                                                             "
                                         ""
                                         ""
                                         "                                                         "
                                         "                                  よい")
            text.grid(row=i * 2 + 1)

        frame4 = ttk.Frame(self.master, padding=10)
        frame4.grid()

        save = tk.Button(
            frame4,
            text='回答',
            command=self.saving,
        )
        save.grid(row=0, column=0)

        clear = tk.Button(
            frame4,
            text='クリア',
            command=self.clearing,
        )
        clear.grid(row=0, column=1)

        frame5 = ttk.Frame(self.master, padding=30)
        frame5.grid()

        self.message = tk.StringVar()
        message_txt = tk.Label(frame5,
                               textvariable=self.message)
        message_txt.grid(padx=5, pady=10)

    def slider_scroll(self, event=None):
        '''スライダーを移動したとき'''
        # print(str(self.scale_var[1].get()))
        self.message.set("")

    def on_closing(self):
        print("Closing!!!")
        self.master.destroy()

    def saving(self):
        print("saving")
        if self.first_flag:
            self.data[0] = str(self.select_var.get())
            self.data[1] = str(self.subject[0].get())
            self.data[2] = str(self.subject[1].get())
            self.data[3] = str(self.subject[2].get())
            self.data[4] = str(self.subject[3].get())
            for i in range(len(self.Question)):
                self.data[5 + i] = str(self.scale_var[i].get())

            write_file = [self.data]
            with open(self.filename, 'wb') as pk:
                pickle.dump(write_file, pk)

            self.message.set("保存しました")
            self.clearing()
            self.first_flag = False
        else:

            if self.data[0] == str(self.select_var.get()) and\
                self.data[1] == str(self.subject[0].get()) and\
                self.data[2] == str(self.subject[1].get()) and\
                self.data[3] == str(self.subject[2].get()):
                self.message.set("同じやん")
            else :
                self.data[0] = str(self.select_var.get())
                self.data[1] = str(self.subject[0].get())
                self.data[2] = str(self.subject[1].get())
                self.data[3] = str(self.subject[2].get())
                self.data[4] = str(self.subject[3].get())
                for i in range(len(self.Question)):
                    self.data[5 + i] = str(self.scale_var[i].get())

                reading_file = []
                with open(self.filename, 'rb') as r:
                    reading_file = pickle.load(r)

                writing_file = []
                with open(self.filename, 'wb') as w:
                    for i in range(len(reading_file)):
                        writing_file.append(reading_file[i])

                    writing_file.append(self.data)
                    pickle.dump(writing_file, w)

                # print(self.data)
                self.message.set("保存しました")
                self.clearing()



    def clearing(self):
        print("clear")
        for i in range(len(self.Question)):
            self.scale_var[i].set(50)


if __name__ == "__main__":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
