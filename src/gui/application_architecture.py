import tkinter as tk


from tkinter import *
from src.gui.displaying_information import TEXT_INFO
from src.logic.crypto_calculator import show_crypto_calculator
from src.logic.crypto_data import show_btc_graph
from src.ai.ai_prediction import update_chart


def application_displays() -> None:

    root = tk.Tk()
    root.title("CryptoPredictor")
    root.geometry("1000x550")
    root.iconbitmap(default="assets/bitcoin.ico")


    def closing_application() -> None:
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", closing_application)
    root.attributes("-alpha", 1)
    root.configure(bg="#282828")


    def update_window(func, *args):
        for widget in root.winfo_children():
            if not isinstance(widget, tk.Button):
                widget.place_forget()

        func(root, *args)


    text_info = tk.Label(root, text = TEXT_INFO, bg="#282828", fg="white", justify="left", wraplength=900)
    text_info.place(x=20, y=40, width=900, height=450)


    btn = tk.Button(root, text="Crypto Data", bg = "#C0C0C0", command=lambda:update_window(show_btc_graph))
    btn.place(x=0, y=0, width=80, height=40)
    btn1 = tk.Button(root, text="AI Prediction", bg = "#C0C0C0", command=lambda:update_window(update_chart))
    btn1.place(x=80, y= 0, width=80, height=40)
    btn2 = tk.Button(root, text="Crypto Calculator", bg = "#C0C0C0", command = lambda:update_window(show_crypto_calculator))
    btn2.place(x=160, y= 0, width=120, height=40)


    root.mainloop()

