PYTHON ?= python

.PHONY: instalar probar lint experimento-ligero limpiar

instalar:
	$(PYTHON) -m pip install -e .

probar:
	pytest

lint:
	$(PYTHON) -m compileall src pruebas scripts

experimento-ligero:
	$(PYTHON) scripts/ejecutar_experimento.py --config configuraciones/sintetico_pequeno.yaml

limpiar:
	rm -rf .pytest_cache __pycache__ resultados/procesados/*
