import tkinter as tk
from tkinter import messagebox
from src.ui.widgets import BalanceWidget, PriceWidget, OrderWidget
from src.ui.graph import GraphWidget
from src.ui.order_history_widget import OrderHistoryWidget
from src.binance_api import get_balance, get_current_price, place_market_order

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Binance Trading Bot")
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")

        # Set up the UI layout
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Binance Trading Bot", font=('Helvetica', 24, 'bold'), fg="white", bg="#2C3E50")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=30)

        # Balance Widget
        self.balance_widget = BalanceWidget(self.root)
        self.balance_widget.grid(row=1, column=0, padx=20, pady=20)

        # Price Widget
        self.price_widget = PriceWidget(self.root)
        self.price_widget.grid(row=1, column=1, padx=20, pady=20)

        # Order Widget
        self.order_widget = OrderWidget(self.root)
        self.order_widget.grid(row=2, column=0, padx=20, pady=20)

        # Order History Widget
        self.order_history_widget = OrderHistoryWidget(self.root)
        self.order_history_widget.grid(row=2, column=1, padx=20, pady=20)

        # Graph Widget
        self.graph_widget = GraphWidget(self.root)
        self.graph_widget.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        # Live price updates
        self.symbol = 'BTCUSDT'
        self.update_price(self.symbol)

    def update_price(self, symbol):
        try:
            price = get_current_price(symbol)
            self.price_widget.update_price(price)
            self.graph_widget.update_graph([price], ["Time1", "Time2", "Time3"])
        except Exception as e:
            messagebox.showerror("Error", str(e))

        self.root.after(1000, self.update_price, symbol)
