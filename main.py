# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("Scaleの作成")     # ウィンドウタイトル

        #---------------------------------------------------------------
        # Scaleの作成

        # Scale（デフォルトで作成）
        # scaleV = tk.Scale( self.master)
        # scaleV.pack(side = tk.RIGHT)



        for i in range(3):

            # Scale（オプションをいくつか設定）
            self.scale_var = tk.DoubleVar()
            scaleH = tk.Scale( self.master,
                        variable = self.scale_var,
                        command = self.slider_scroll,
                        orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                        length = 1000,           # 全体の長さ
                        width = 20,             # 全体の太さ
                        sliderlength = 10,      # スライダー（つまみ）の幅
                        from_ = 0,            # 最小値（開始の値）
                        to = 100,               # 最大値（終了の値）
                        resolution= 1,         # 変化の分解能(初期値:1)
                        # tickinterval = 50         # 目盛りの分解能(初期値0で表示なし)
                        )
            scaleH.pack()
        #---------------------------------------------------------------

    def slider_scroll(self, event=None):
        '''スライダーを移動したとき'''
        print(str(self.scale_var.get()))

if __name__ == "__main__":

    Question = [
        "Q1. これはどうでしたか？",
        "Q2. それはどうでしたか？",
        "Q3. あれはどうでしたか？",
        "Q4. それでどうでしたか？",
    ]

    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()