
## Installation

#### 1. Repository klonen
```bash
git clone https://github.com/Saplinging/dufteplots.git
cd dufteplots
```

#### 2. Abhängigkeiten installieren
```bash
poetry install
```

## Beiträge leisten

Bitte halte dich an folgende Richtlinien:

### Fehler melden & Feature Requests
- Nutze [GitHub Issues](https://github.com/Saplinging/dufteplots/issues) für Bugs und Vorschläge.

### Code Style
- Nutze `ruff` und `black` für Formatierung und Linting:
	```bash
	poetry run ruff check .
	poetry run ruff format .
	```

### Tests
- Schreibe und erweitere Tests in `tests/`.
- Führe Tests mit `pytest` aus:
	```bash
	poetry run pytest
	```

### Dokumentation
- Dokumentation befindet sich im `docs/`-Verzeichnis.
- Ergänze relevante Änderungen in der Dokumentation.