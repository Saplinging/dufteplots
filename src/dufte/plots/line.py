from plotnine import ggplot, aes, geom_line, geom_point, labs
from dufte.config_theme import tufte_theme


def plot_line(data):
    """
    Erstellt ein Liniendiagramm mit dem Tufte-Theme.

    Parameter:
    data (DataFrame): Ein Pandas DataFrame mit den Spalten 'jahr', 'wert' und 'kategorie'.

    Rückgabe:
    plotnine.ggplot: Ein Liniendiagramm im Tufte-Stil.
    """
    chart = (
        ggplot(data, aes(x='jahr', y='wert', color='kategorie', group='kategorie'))
        + geom_line(size=1.2)
        + geom_point(size=3)
        + labs(
            title='Liniendiagramm im Tufte-Stil',
            x='Jahr',
            y='Wert',
            color='Kategorie'
        )
        + tufte_theme()
    )
    return chart