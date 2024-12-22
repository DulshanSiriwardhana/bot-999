import tkinter as tk
from tkinter import ttk
from src.binance_api import place_market_order, place_limit_order, place_stop_limit_order, get_balance

class BalanceWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.balance_label = ttk.Label(self, text="Balance: Not Checked", font=('Helvetica', 16), foreground="white", background="#34495E")
        self.balance_label.pack(pady=10)

        self.check_balance_button = ttk.Button(self, text="Check Balance", command=self.check_balance, width=20)
        self.check_balance_button.pack(pady=10)

    def check_balance(self):
        # Fetch actual balance
        balance = get_balance()
        self.balance_label.config(text=f"Balance: {balance:.2f} USDT")

class PriceWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.price_label = ttk.Label(self, text="Current Price: Not available", font=('Helvetica', 16), foreground="white", background="#34495E")
        self.price_label.pack(pady=10)

    def update_price(self, price):
        self.price_label.config(text=f"Current Price: {price} USDT")

class OrderWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Symbol Selection (Dropdown)
        self.symbol_label = ttk.Label(self, text="Select Symbol", font=('Helvetica', 14), foreground="white", background="#34495E")
        self.symbol_label.pack(pady=5)

        self.symbol_combobox = ttk.Combobox(self, values=["BTCUSDT", "ETHUSDT", "ADAUSDT", "BNBUSDT"], width=20, font=('Helvetica', 12))
        self.symbol_combobox.set("BTCUSDT")  # Default value
        self.symbol_combobox.pack(pady=5)

        # Quantity Entry
        self.quantity_label = ttk.Label(self, text="Enter Quantity", font=('Helvetica', 14), foreground="white", background="#34495E")
        self.quantity_label.pack(pady=5)
        self.quantity_entry = ttk.Entry(self, font=('Helvetica', 12), width=20)
        self.quantity_entry.pack(pady=5)

        # Risk Management: Stop-Loss and Take-Profit
        self.stop_loss_label = ttk.Label(self, text="Stop-Loss Price", font=('Helvetica', 14), foreground="white", background="#34495E")
        self.stop_loss_label.pack(pady=5)
        self.stop_loss_entry = ttk.Entry(self, font=('Helvetica', 12), width=20)
        self.stop_loss_entry.pack(pady=5)

        self.take_profit_label = ttk.Label(self, text="Take-Profit Price", font=('Helvetica', 14), foreground="white", background="#34495E")
        self.take_profit_label.pack(pady=5)
        self.take_profit_entry = ttk.Entry(self, font=('Helvetica', 12), width=20)
        self.take_profit_entry.pack(pady=5)

        # Order Button
        self.place_order_button = ttk.Button(self, text="Place Buy Order", command=self.place_order, width=20)
        self.place_order_button.pack(pady=20)

    def place_order(self):
        symbol = self.symbol_combobox.get()
        quantity = float(self.quantity_entry.get())  # Parse entered quantity
        stop_loss = float(self.stop_loss_entry.get())  # Parse stop-loss
        take_profit = float(self.take_profit_entry.get())  # Parse take-profit

        # Example logic for placing orders
        if stop_loss and take_profit:
            order = place_stop_limit_order(symbol, quantity, stop_loss, take_profit)
        elif stop_loss:
            order = place_limit_order(symbol, quantity, stop_loss)
        else:
            order = place_market_order(symbol, quantity)

        print(order)
