import yfinance as yf
import joblib
import matplotlib.pyplot as plt
import pandas as pd


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


model = joblib.load('btc_model.pkl')
features = joblib.load('features.pkl')


def get_live_forecast() -> tuple[pd.DataFrame, float, float]:
    data = yf.download("BTC-USD", period="60d", interval="1d")
    data["MA7"] = data["Close"].rolling(window=7).mean()
    data["MA30"] = data["Close"].rolling(window=30).mean()
    data["Diff"] = data["Close"].diff()
    data["Gain"] = data["Diff"].clip(lower=0)
    data["Loss"] = data["Diff"].clip(upper=0).abs()
    data["Avg_Gain"] = data["Gain"].ewm(alpha=1/14, adjust=False).mean()
    data["Avg_Loss"] = data["Loss"].ewm(alpha=1/14, adjust=False).mean()
    data["RS"] = data["Avg_Gain"] / data["Avg_Loss"]
    data["RSI"] = 100 - (100 / (1 + data["RS"]))
    data["Actual_Return"] = data["Close"].pct_change()

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.dropna(inplace=True)

    data["Model_Prediction"] = model.predict(data[features])
    data["Predicted_Price"] = data["Close"] * (1 + data["Model_Prediction"])
    last_close = float(data["Close"].iloc[-1])
    last_pred = float(data["Model_Prediction"].iloc[-1])
    
    return data, last_close, last_pred


def update_chart(root) -> None:
    fig, ax = plt.subplots(figsize=(7, 3))
    data, last_close, last_pred = get_live_forecast()
    predicted_price = last_close * (1 + last_pred)
    ax.clear()
    plot_data = data.tail(30)
    ax.plot(data.index[-30:], data["Close"].tail(30), label='Reality', color='royalblue', lw=2)
    ax.plot(data.index[-30:], data["Predicted_Price"].tail(30), label='AI Forecast', color='crimson', ls='--')
    local_min = min(plot_data['Close'].min(), plot_data['Predicted_Price'].min())
    local_max = max(plot_data['Close'].max(), plot_data['Predicted_Price'].max())
    ax.set_ylim(local_min * 0.98, local_max * 1.02)
    ax.axhline(0, color='black', lw=1, alpha=0.3)
    info_text = (f"Price: ${last_close:,.2f}\n"
                 f"Predict: ${predicted_price:,.2f}\n"
                 f"Change: {last_pred*100:+.2f}%")
    
    ax.text(0.02, 0.95, info_text, transform=ax.transAxes, 
            fontsize=10, fontweight='bold', verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    ax.set_title("Forecast accuracy (last 30 days)", color='Black')
    ax.tick_params(colors='black')
    ax.legend()
    ax.grid(True, alpha=0.2)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=10, y=60, width=980, height=480)
    canvas.draw()

