"""Encuesta sintética para practicar sin descargar datos reales.

Los datos NO representan a ninguna población real: se generan al azar con una
semilla fija, de modo que todos obtienen exactamente la misma base.

Imita la estructura típica de una encuesta de hogares del INEC:
códigos numéricos, un factor de expansión y algunos valores faltantes o
códigos de "no sabe" que hay que limpiar.
"""

import numpy as np
import pandas as pd

# Códigos de provincia del INEC (se usan las mismas claves que en la cartografía oficial)
PROVINCIAS = {
    1: "Azuay",
    7: "El Oro",
    9: "Guayas",
    13: "Manabí",
    17: "Pichincha",
    18: "Tungurahua",
}

AREAS = {1: "Urbana", 2: "Rural"}
SEXOS = {1: "Hombre", 2: "Mujer"}
NIVELES = {
    1: "Ninguno",
    2: "Educación básica",
    3: "Bachillerato",
    4: "Superior",
}
# En muchas encuestas 99 significa "no sabe / no responde"
CODIGO_NO_SABE = 99


def generar_encuesta(n=2000, semilla=2026):
    """Genera una encuesta sintética de personas.

    Parámetros
    ----------
    n : int
        Número de personas encuestadas.
    semilla : int
        Semilla del generador aleatorio (misma semilla, misma base).

    Devuelve
    --------
    pandas.DataFrame con las columnas:
        id_persona, prov, area, sexo, edad, nivel_instr, ingreso, fexp
    """
    rng = np.random.default_rng(semilla)

    prov = rng.choice(list(PROVINCIAS), size=n, p=[0.12, 0.10, 0.30, 0.18, 0.22, 0.08])
    area = rng.choice(list(AREAS), size=n, p=[0.65, 0.35])
    sexo = rng.choice(list(SEXOS), size=n)
    edad = np.clip(rng.gamma(shape=4.0, scale=9.0, size=n).round(), 15, 90).astype(int)

    # El nivel de instrucción depende un poco del área y de la edad
    p_superior = np.where(area == 1, 0.30, 0.10)
    nivel = np.where(
        rng.random(n) < p_superior,
        4,
        rng.choice([1, 2, 3], size=n, p=[0.08, 0.50, 0.42]),
    )
    nivel = np.where(edad > 60, np.minimum(nivel, rng.choice([1, 2, 3], size=n)), nivel)

    # Ingreso mensual: sube con la instrucción, es más alto en zona urbana
    base = {1: 250, 2: 380, 3: 520, 4: 950}
    media = np.array([base[k] for k in nivel]) * np.where(area == 1, 1.25, 0.85)
    ingreso = rng.lognormal(mean=np.log(media), sigma=0.45).round(2)

    # El factor de expansión cambia según la provincia y el área (diseño no autoponderado)
    fexp = (rng.gamma(shape=6.0, scale=1.0, size=n) * np.where(area == 2, 1.6, 1.0)).round(3)
    fexp = fexp * 150  # escala para que los totales sean del orden de decenas de miles

    df = pd.DataFrame(
        {
            "id_persona": np.arange(1, n + 1),
            "prov": prov,
            "area": area,
            "sexo": sexo,
            "edad": edad,
            "nivel_instr": nivel,
            "ingreso": ingreso,
            "fexp": fexp.round(2),
        }
    )

    # Ensuciar la base a propósito, como ocurre en una encuesta real
    sin_ingreso = rng.random(n) < 0.12
    df.loc[sin_ingreso, "ingreso"] = np.nan

    no_sabe = rng.random(n) < 0.03
    df.loc[no_sabe, "nivel_instr"] = CODIGO_NO_SABE

    return df
