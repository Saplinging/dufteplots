# Sparklines

Sparklines sind kleine, inline dargestellte Zeitreihenplots, die Trends oder Muster auf kleinstem Raum zeigen.

---

![Beispiel Sparkline](../images/sparklines.png)

---


## Funktion

```python
def sparklines(
    df: pd.DataFrame,
    category_col: str,
    time_col: str,
    value_col: str,
    title: str = "Sparklines",
    **kwargs,
) -> ggplot:
```

**Parameter:**

- **df** (`pandas.DataFrame`): DataFrame mit den Daten für den Plot.
- **category_col** (`str`): Name der Spalte für die Kategorien (z.B. Aktien).
- **time_col** (`str`): Name der Spalte für die Zeitpunkte.
- **value_col** (`str`): Name der Spalte für die Werte (numerisch).
- **title** (`str`, optional): Titel des Plots.
- **kwargs**: Zusätzliche Argumente für geom_line (z.B. color, alpha).

**Rückgabewert:**

- **plot** (`plotnine.ggplot`): Ein ggplot-Objekt mit den Sparklines.

---


## Anwendungsbeispiel

Der folgende Beispielcode erzeugt den abgebildeten Beispieloutput.

```python
import pandas as pd
import numpy as np
from plot_dufte import sparklines

# Beispieldaten
np.random.seed(42)
def generate_random_walk(start_price, n, volatility=0.01):
    returns = np.random.normal(loc=0.0005, scale=volatility, size=n)
    price_path = start_price * (1 + returns).cumprod()
    return price_path

n_days = 60
currencies = ["EUR/USD", "GBP/USD", "JPY/USD", "CHF/USD", "AUD/USD"]
start_vals = [1.10, 1.30, 0.009, 1.05, 0.70]

spark_data = []
for curr, start in zip(currencies, start_vals):
    values = generate_random_walk(start, n_days, volatility=0.01)
    for t, v in enumerate(values):
        spark_data.append({"Currency": curr, "Day": t, "Rate": v})

df = pd.DataFrame(spark_data)

# Sparklines erstellen
plot = sparklines(
    df,
    category_col="Currency",
    time_col="Day",
    value_col="Rate",
    title="60-Day Currency Trends (Sparklines)"
)

# Plot anzeigen
plot.show()
```