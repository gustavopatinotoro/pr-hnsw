#!/usr/bin/env python
"""Ejecutor inicial de experimentos PR-HNSW."""
from __future__ import annotations
import argparse
from pathlib import Path
import yaml

def cargar_configuracion(ruta: Path) -> dict:
    """Carga una configuración YAML de experimento."""
    with ruta.open("r", encoding="utf-8") as archivo:
        return yaml.safe_load(archivo)

def main() -> None:
    parser = argparse.ArgumentParser(description="Ejecuta un experimento PR-HNSW.")
    parser.add_argument("--config", required=True, help="Ruta al archivo YAML de configuración.")
    args = parser.parse_args()
    print(cargar_configuracion(Path(args.config)))

if __name__ == "__main__":
    main()
