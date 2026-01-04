import tkinter as tk


from tkinter import *
from tkinter import ttk
from binance_api import getting_crypt_currency, prices_crypto


def show_crypto_calculator(root) -> None:
    converting_crypt_into_currency(root)
    converting_currency_into_crypt(root)
    

def converting_crypt_into_currency(root) -> None:

    def converting_crypt_currency(entry, result_entry) -> None:
        try:
            crypto = crypto_combobox.get()
            currency = currency_combobox.get()

            if not crypto or not currency:
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Please select both currencies")
                return

            getting_crypt_currency()
            crypto_currence = f"{crypto}{currency}"
            rate = float(prices_crypto.get(crypto_currence))
            if rate is None:
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Rate not available")
                return
            
            try:
                amount = float(entry.get())
                if amount <= 0:
                        result_entry.delete(0, tk.END)
                        result_entry.insert(0, "Enter a positive amount")
                        return
                result = amount * rate
                result_entry.delete(0, tk.END)
                result_entry.insert(0, str(result))
            except ValueError:
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid input")
        except ValueError:
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid input")
        except Exception as e:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, f"Error: {str(e)}")

    cryptocurrency = ["BTC", "ETH", "DOGE", "BNB"]
    crypto_combobox = ttk.Combobox(root, values=cryptocurrency)
    crypto_combobox.place(x=250, y=150)
    displaying_name_1 = tk.Label(root, text = "Сryptocurrency", bg="#282828", fg= "white") 
    displaying_name_1.place(x = 280, y = 120)

    state_currency = ["USDT", "EUR", "RUB", "GBP"]
    currency_combobox = ttk.Combobox(root, values=state_currency)
    currency_combobox.place(x=150, y=250)
    displaying_name_2 = tk.Label(root, text = "State currency", bg="#282828", fg= "white") 
    displaying_name_2.place(x = 175, y = 220)

    def user_input_numbers_crypto(root) -> None:
        entry = tk.Entry(root)
        entry.place(x=50, y=150)
        displaying_name_1 = tk.Label(root, text = "Enter the number of \n cryptocurrencies", bg="#282828", fg= "white")
        displaying_name_1.place(x = 55, y = 110)
        result_entry = tk.Entry(root)
        result_entry.place(x=50, y=350)
        displaying_name_1 = tk.Label(root, text = "Result", bg="#282828", fg= "white")
        displaying_name_1.place(x = 90, y = 325)

        btn = tk.Button(root, text="Convert", bg = "#C0C0C0",command = lambda: converting_crypt_currency(entry, result_entry))
        btn.place(x=285, y=340, width=80, height=40)

    user_input_numbers_crypto(root)

def converting_currency_into_crypt(root) -> None:

    def converting_currency_crypt(entry, result_entry) -> None:
        try:
            crypto = crypto_combobox.get()
            currency = currency_combobox.get()

            if not crypto or not currency:
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Please select both currencies")
                return

            getting_crypt_currency()
            crypto_currence = f"{crypto}{currency}"
            rate = float(prices_crypto.get(crypto_currence))
            
            if rate is None:
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Rate not available")
                return

            if rate <= 0:
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid rate (cannot divide by zero or negative)")
                return
            
            try:
                amount = float(entry.get())
                if amount <= 0:
                        result_entry.delete(0, tk.END)
                        result_entry.insert(0, "Enter a positive amount")
                        return
                result = amount / rate
                result_entry.delete(0, tk.END)
                result_entry.insert(0, str(result))
            except ValueError:
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid input")
        except ValueError:
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid input")
        except Exception as e:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, f"Error: {str(e)}")

    cryptocurrency = ["BTC", "ETH", "DOGE", "BNB"]
    crypto_combobox = ttk.Combobox(root, values=cryptocurrency)
    crypto_combobox.place(x=680, y=250)
    displaying_name_1 = tk.Label(root, text = "Сryptocurrency", bg="#282828", fg= "white") 
    displaying_name_1.place(x = 710, y = 220)

    state_currency = ["USDT", "EUR", "RUB", "GBP"]
    currency_combobox = ttk.Combobox(root, values=state_currency)
    currency_combobox.place(x=800, y=150)
    displaying_name_2 = tk.Label(root, text = "State currency", bg="#282828", fg= "white") 
    displaying_name_2.place(x = 830, y = 120) 

    def user_input_numbers_crypto(root) -> None:
        entry = tk.Entry(root)
        entry.place(x=600, y=150)
        displaying_name_1 = tk.Label(root, text = "Enter the amount \n of the currency", bg="#282828", fg= "white")
        displaying_name_1.place(x = 605, y = 110)
        result_entry = tk.Entry(root)
        result_entry.place(x=600, y=350)
        displaying_name_1 = tk.Label(root, text = "Result", bg="#282828", fg= "white")
        displaying_name_1.place(x = 645, y = 325)

        btn = tk.Button(root, text="Convert", bg = "#C0C0C0",command = lambda: converting_currency_crypt(entry, result_entry))
        btn.place(x=825, y=340, width=80, height=40)

    user_input_numbers_crypto(root)


