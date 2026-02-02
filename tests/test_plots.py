import pandas as pd
import pytest
from plotnine import ggplot

from dufteplots.plots.dot_dash_plot import dot_dash_plot
from dufteplots.plots.layered_focus import layered_focus
from dufteplots.plots.range_frame import range_frame
from dufteplots.plots.slopegraph import slopegraph
from dufteplots.plots.small_multiples import small_multiples
from dufteplots.plots.sparklines import sparklines
from dufteplots.plots.time_series import time_series

# ============ Data ============


@pytest.fixture
def scatter_data():
    return pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [2, 4, 3, 5, 4]})


@pytest.fixture
def categorical_data():
    return pd.DataFrame(
        {"category": ["A", "A", "A", "B", "B", "B"], "value": [10, 12, 11, 20, 22, 21]}
    )


@pytest.fixture
def slope_data():
    return pd.DataFrame(
        {
            "country": ["Germany", "France", "Germany", "France"],
            "year": [2020, 2020, 2024, 2024],
            "value": [100, 80, 120, 95],
        }
    )


@pytest.fixture
def multi_series_data():
    return pd.DataFrame(
        {
            "category": ["A", "A", "A", "B", "B", "B"],
            "time": [1, 2, 3, 1, 2, 3],
            "value": [10, 15, 12, 20, 25, 22],
        }
    )


# ============ Tests ============


def test_dot_dash_plot(scatter_data):
    result = dot_dash_plot(scatter_data, "x", "y")
    assert isinstance(result, ggplot)


def test_range_frame(categorical_data):
    result = range_frame(categorical_data, "category", "value")
    assert isinstance(result, ggplot)


def test_slopegraph(slope_data):
    result = slopegraph(slope_data, "country", "year", "value")
    assert isinstance(result, ggplot)


def test_time_series(scatter_data):
    result = time_series(scatter_data, "x", "y")
    assert isinstance(result, ggplot)


def test_small_multiples(multi_series_data):
    result = small_multiples(multi_series_data, "time", "value", "category")
    assert isinstance(result, ggplot)


def test_layered_focus(multi_series_data):
    result = layered_focus(multi_series_data, "time", "value", "category", "A")
    assert isinstance(result, ggplot)


def test_sparklines(multi_series_data):
    result = sparklines(multi_series_data, "category", "time", "value")
    assert isinstance(result, ggplot)
