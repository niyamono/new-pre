import tkinter as tk

def on_scroll(*args):
    text.yview(*args)

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Weite chocolate")

# てきぼ
text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text.grid(row=0, column=0)

# 垂直方向のスクロールバー
scrollbar = tk.Scrollbar(root, command=on_scroll)
scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)

text.config(yscrollcommand=scrollbar.set)

# テキストボックスに初期テキストを追加
initial_text = "このソフトウェアは開発中です。\nいかなる理由があっても制作者は責任を負いません。\nまた、当ソフトの無断配布は固く禁止する。\n当ソフトを悪用しないこと\ncopy&light2024 Niya_nay 2024 2.16" 
text.insert(tk.END, initial_text)

# ボタンの作成
button = tk.Button(root, text="以上に同意した上で実行", width=50, command=close_window)
button.grid(row=1, column=0, columnspan=2)
#ウィンドウを消した。
#その後他のexeを呼び出す。はず
root.mainloop()