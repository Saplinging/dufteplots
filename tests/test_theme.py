from plot_dufte.config_theme import tufte_theme


def test_tufte_theme():
    """Teste ob Theme-Funktion ein Theme-Objekt zurückgibt."""
    result = tufte_theme()
    assert result is not None


def test_tufte_theme_custom_base_size():
    """Teste ob Theme custom base_size akzeptiert."""
    result = tufte_theme(base_size=14)
    assert result is not None
