# Seminario de Herramientas Estadísticas de Actualidad

Plantilla de repositorio para el análisis de encuestas con Python: manejo de datos, mapas, visualización enlazada, tableros y reportes reproducibles.

Carrera de Estadística, Universidad Central del Ecuador. Periodo 2026-2027.

## Cómo empezar: Google Colab (camino principal)

En los laboratorios todo lo que se instala se borra, así que el curso se trabaja en **Google Colab**, sin instalar nada.

1. Entra a colab.research.google.com con tu cuenta de Google (en los laboratorios, usa una ventana de incógnito y cierra sesión al terminar).
2. Abre el notebook de la clase con el enlace que comparte el docente.
3. Ejecuta primero la **celda de arranque**: trae la carpeta `src/` y los datos de práctica a tu sesión.
4. Guarda una copia del notebook en tu Drive (`Archivo > Guardar una copia en Drive`).

Colab ya trae pandas, numpy, matplotlib, seaborn, scipy, statsmodels, geopandas, folium, plotly y altair. Faltan `pyreadstat`, `streamlit` y `quarto`; se instalan con `pip install -q` en la celda de arranque cuando se necesiten.

Al cerrar la sesión se pierde lo que está en memoria y en `/content`; se conserva lo que guardes en tu Drive.

## Opcional: instalación en tu computador personal

Sirve para trabajar en casa. Requiere permisos de instalación, por lo que no se puede hacer en los laboratorios.

1. Descarga y descomprime esta plantilla.
2. Instala Miniforge (elige «Just Me») y abre «Miniforge Prompt».
3. Desde la carpeta de la plantilla:

   ```bash
   conda env create -f environment.yml
   conda activate seminario-encuestas
   python scripts/verificar_entorno.py
   jupyter lab
   ```

   Alternativa con pip: `python -m venv .venv`, activar, `pip install -r requirements.txt`.

## Entorno mínimo y completo

| Archivo | Para qué | Cuándo |
| --- | --- | --- |
| `environment.yml` y `requirements.txt` | Jupyter, pandas, matplotlib y seaborn | Semanas 1 a 6 |
| `environment-completo.yml` y `requirements-completo.txt` | Archivos, estadística, mapas, tableros y reportes | Desde la semana 7 |

El día 1 se instala solo el mínimo porque es liviano. Antes de la semana 7 se actualiza el mismo entorno:

```bash
conda env update -f environment-completo.yml
```

Con pip: `pip install -r requirements-completo.txt`.

## Estructura

| Carpeta | Contenido |
| --- | --- |
| `data/raw/` | Bases originales de la encuesta. No se modifican nunca. |
| `data/external/` | Cartografía oficial (INEC) y otros insumos externos. |
| `data/processed/` | Bases limpias y resultados intermedios generados por el código. |
| `notebooks/` | Un notebook por sesión o taller. |
| `src/` | Funciones reutilizables (módulos `.py`). |
| `scripts/` | Utilidades de línea de comandos, como el verificador del entorno. |
| `docs/` | Documentación, incluida la tabla de equivalencias R ↔ Python. |
| `outputs/` | Mapas, figuras, tableros y reportes finales. |

Las bases y los resultados no se suben a Git (ver `.gitignore`): cada persona descarga los datos desde la fuente oficial.

## Reglas de trabajo

- Las rutas son relativas a la raíz del proyecto, nunca absolutas.
- Los datos originales en `data/raw/` no se editan: toda limpieza se hace con código y se guarda en `data/processed/`.
- Un cambio importante, un commit con mensaje claro.
- Antes de entregar, reinicia el kernel y ejecuta el notebook completo de principio a fin (`Kernel > Restart & Run All`; en Colab, `Entorno de ejecución > Reiniciar sesión y ejecutar todo`).

## Datos de práctica

El notebook `01_entorno_y_pandas.ipynb` y la semana 2 usan una encuesta **sintética** (`src/datos_sinteticos.py`) para que cualquiera pueda ejecutarlos sin descargar nada. No representa a ninguna población real. Para el proyecto integrador cada estudiante usa una encuesta oficial real (por ejemplo ENEMDU o ENSANUT del INEC) con su factor de expansión.

El notebook `01_entorno_y_pandas.ipynb` trabaja pandas y se usa en las semanas 4 y 5.

## Equivalencias R ↔ Python

Ver `docs/equivalencias_R_Python.md`.
