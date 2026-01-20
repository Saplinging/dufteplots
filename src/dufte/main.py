import pandas as pd
from dufte.plots.line import plot_line 

def main():
    data = pd.DataFrame({
        'jahr': ['2020', '2021', '2020', '2021'],
        'wert': [10, 15, 20, 18],
        'kategorie': ['A', 'A', 'B', 'B']
    })

    chart = plot_line(data)

    print(chart)
    chart.save("output/line_plot.png", dpi=300)

if __name__ == "__main__":
    main()