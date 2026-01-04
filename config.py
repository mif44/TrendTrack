import os


from dotenv import load_dotenv


load_dotenv()
BINANCE_URL = os.getenv("URL_BINANCE")
BINANCE_URL_SCHEDULE = os.getenv("BINANCE_URL_SCHEDULE")