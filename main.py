import tkinter as tk
from tkinter import ttk

from zeeshansami_fticonsulting.visualization import *

# Load data once to avoid multiple reads
carshare_data = load_carshare_data()
election_data = load_election_data()
melted_data = melt_election_data(election_data)


def visualize_chart():
    chart_type = chart_combobox.get()
    dataset = dataset_combobox.get()

    if dataset == 'Carshare Data':
        if chart_type == 'Bar Chart':
            fig = barchart_carsharedata()
        elif chart_type == 'Box and Whisker Plot':
            fig = boxandwhiskerplot_carsharedata(carshare_data)
        elif chart_type == 'Dot Plot':
            fig = dotplots_carsharedata(carshare_data)
        elif chart_type == 'Heatmap':
            fig = heatmaps_carsharedata(carshare_data)
        elif chart_type == 'Radar/spider Chart':
            fig = radarspiderchart_carsharedata(carshare_data)
        elif chart_type == 'Treemaps':
            fig = treemaps_carsharedata(carshare_data)
        elif chart_type == 'Waterfall Charts':
            fig = waterfallcharts_carsharedata()
        fig.show()

    else:  # Assuming 'Election Data'
        if chart_type == 'Bar Chart':
            fig = barchart_electiondata(melted_data)
        elif chart_type == 'Box and Whisker Plot':
            fig = boxandwhiskerplot_electiondata('Coderre')
        elif chart_type == 'Dot Plot':
            fig = dotplots_electiondata('Coderre')
        elif chart_type == 'Heatmap':
            fig = heatmaps_electiondata('Coderre')
        elif chart_type == 'Radar/spider Chart':
            fig = radarspiderchart_electiondata('Coderre')
        elif chart_type == 'Treemaps':
            fig = treemaps_electiondata('Coderre')
        elif chart_type == 'Waterfall Charts':
            fig = waterfallcharts_electiondata('Coderre')
        fig.show()


# Creating main window
root = tk.Tk()
root.title("Visualization UI")

# Creating a frame for the combobox and label
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Adding a label
label = ttk.Label(frame, text="Select the type of chart:")
label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

# Combobox for chart selection
chart_combobox = ttk.Combobox(frame, values=['Bar Chart', 'Box and Whisker Plot', 'Dot Plot', 'Heatmap', 'Radar/spider Chart', 'Treemaps', 'Waterfall Charts'])
chart_combobox.grid(column=1, row=0, padx=5, pady=5)
chart_combobox.set('Bar Chart')

# Label and combobox for dataset selection
dataset_label = ttk.Label(frame, text="Select the dataset:")
dataset_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

dataset_combobox = ttk.Combobox(frame, values=['Carshare Data', 'Election Data'])
dataset_combobox.grid(column=1, row=1, padx=5, pady=5)
dataset_combobox.set('Carshare Data')

# Button to visualize the chart
btn_visualize = ttk.Button(frame, text="Visualize", command=visualize_chart)
btn_visualize.grid(column=1, row=2, pady=20)

root.mainloop()
