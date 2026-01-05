import requests
import tkinter as tk


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
from src.utils.config import BINANCE_URL_SCHEDULE


def fetch_btc_usdt(interval="1h", limit="200") -> tuple[list[datetime], list[float]]:
    try:
        values = requests.get(BINANCE_URL_SCHEDULE, 
                    params={"symbol": "BTCUSDT", "interval": interval, "limit": limit},
                    timeout=10)
        values.raise_for_status()
        klines = values.json()

        times = [datetime.fromtimestamp(k[0] / 1000) for k in klines]
        closes = [float(k[4]) for k in klines]
        return times, closes
    
    except requests.exceptions.RequestException as e:
        print("Ошибка при запросе данных:", e)
        return [], []


def show_btc_graph(root) -> None:
    for widget in root.winfo_children():
        if isinstance(widget, tk.Widget) and widget.winfo_y() > 50:
            widget.destroy()

    times, closes = fetch_btc_usdt()

    if not times or not closes:
        print("There is no data to display!")
        return
    
    fig = Figure(figsize=(7,3), dpi= 100)
    ax = fig.add_subplot(111)

    ax.plot(times, closes, label=closes[-1])
    ax.set_title("Bitcoin rate (BTC/USDT)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Price (USDT)")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=10, y=60, width=980, height=480)
    canvas.draw()


