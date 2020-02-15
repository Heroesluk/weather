def matlibb(root, data):
    import numpy as np
    import tkinter as tk
    import matplotlib
    matplotlib.use('TkAgg')

    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt

    plt.style.use('seaborn-bright')
    fig = plt.figure(1, figsize=[9.1, 4.8])
    fig.tight_layout()
    fig.clf()

    hours = data.hour_normal_times
    temperature = data.hour_temperatures
    plt.plot(hours, temperature)

    canvas = FigureCanvasTkAgg(fig, master=root)
    plot_widget = canvas.get_tk_widget()

    plot_widget.pack(expand=1, fill=tk.X)

