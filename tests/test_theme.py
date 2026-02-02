from dufteplots.config_theme import tufte_theme


def test_tufte_theme():
    """Teste ob Theme-Funktion ein Theme-Objekt zurückgibt."""
    result = tufte_theme()
    assert result is not None
