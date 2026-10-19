"""Verifica que el entorno tenga lo necesario para el seminario.

Uso, desde la raíz del proyecto:

    python scripts/verificar_entorno.py

Sale con código 0 si todo lo esencial está instalado y con 1 si falta algo
de lo necesario para las primeras sesiones.
"""

import importlib
import sys

# (nombre del paquete en pip, módulo que se importa, desde qué semana se usa)
ESENCIALES = [
    ("pandas", "pandas", "1"),
    ("numpy", "numpy", "1"),
    ("matplotlib", "matplotlib", "3"),
    ("seaborn", "seaborn", "3"),
    ("jupyterlab", "jupyterlab", "1"),
    ("ipykernel", "ipykernel", "1"),
]

POSTERIORES = [
    ("polars", "polars", "7"),
    ("pyarrow", "pyarrow", "7"),
    ("pyreadstat", "pyreadstat", "7"),
    ("scipy", "scipy", "8"),
    ("statsmodels", "statsmodels", "8"),
    ("geopandas", "geopandas", "12"),
    ("shapely", "shapely", "12"),
    ("pyogrio", "pyogrio", "12"),
    ("mapclassify", "mapclassify", "12"),
    ("folium", "folium", "13"),
    ("plotly", "plotly", "13"),
    ("altair", "altair", "13"),
    ("libpysal", "libpysal", "14"),
    ("esda", "esda", "14"),
    ("spreg", "spreg", "14"),
    ("streamlit", "streamlit", "15"),
]

VERSION_MINIMA = (3, 10)


def revisar(paquetes):
    """Devuelve la lista de paquetes que no se pudieron importar."""
    faltantes = []
    for pip_nombre, modulo, semana in paquetes:
        try:
            mod = importlib.import_module(modulo)
            version = getattr(mod, "__version__", "")
            print(f"  [ok]    {pip_nombre:<12} {version}")
        except Exception:  # noqa: BLE001 - cualquier fallo de importación cuenta
            print(f"  [falta] {pip_nombre:<12} (se usa desde la semana {semana})")
            faltantes.append(pip_nombre)
    return faltantes


def main():
    print(f"Python {sys.version.split()[0]}")
    if sys.version_info < VERSION_MINIMA:
        print(f"Se necesita Python {VERSION_MINIMA[0]}.{VERSION_MINIMA[1]} o superior.")
        return 1

    print("\nEsenciales (semanas 1 a 6):")
    faltan_esenciales = revisar(ESENCIALES)

    print("\nPara las semanas siguientes:")
    faltan_posteriores = revisar(POSTERIORES)

    print()
    if faltan_esenciales:
        print("Faltan paquetes esenciales: " + ", ".join(faltan_esenciales))
        print("Instálalos con: pip install " + " ".join(faltan_esenciales))
        return 1

    if faltan_posteriores:
        print("Lo esencial está listo. Faltan paquetes para semanas posteriores:")
        print("  " + ", ".join(faltan_posteriores))
        print("Es normal si usas el entorno mínimo: se instalan antes de la semana 7 con el entorno completo:")
        print("  conda env update -f environment-completo.yml")
        print("  (o, con pip: pip install -r requirements-completo.txt)")
    else:
        print("Todo listo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
