import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class GraphWidget(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack()

    def update_graph(self, price_data, time_labels):

        self.ax.clear()

        self.ax.plot(time_labels, price_data, marker='o', color='b')

        self.ax.set_title("Price Over Time")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Price (USDT)")
        self.canvas.draw()
