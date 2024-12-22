from tkinter import ttk

class OrderHistoryWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.history_label = ttk.Label(self, text="Order History", font=('Helvetica', 16), foreground="white", background="#34495E")
        self.history_label.pack(pady=10)

        self.history_treeview = ttk.Treeview(self, columns=("Symbol", "Quantity", "Price", "Date"), show="headings")
        self.history_treeview.heading("Symbol", text="Symbol")
        self.history_treeview.heading("Quantity", text="Quantity")
        self.history_treeview.heading("Price", text="Price")
        self.history_treeview.heading("Date", text="Date")
        self.history_treeview.pack(pady=20, fill="both", expand=True)

    def update_history(self, trades):
        for trade in trades:
            self.history_treeview.insert("", "end", values=(trade['symbol'], trade['qty'], trade['price'], trade['time']))
