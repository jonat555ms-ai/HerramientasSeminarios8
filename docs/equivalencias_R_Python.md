# Equivalencias R ↔ Python

Guía rápida para quienes vienen de R (tidyverse). Se asume `import pandas as pd`, `import numpy as np` y un data frame llamado `df`.

## Diferencias de fondo

| Tema | R | Python |
| --- | --- | --- |
| Primer índice | 1 | **0** |
| Rangos | `x[1:3]` incluye los dos extremos | `x[0:3]` **excluye** el extremo final |
| Estructura de bloques | llaves `{ }` | **sangría** (indentación) |
| Pipe | `%>%` o `\|>` | encadenar métodos con `.` y paréntesis |
| Instalar paquetes | `install.packages("x")` | `pip install x` (en la terminal) |
| Entornos | `renv` | `venv` o `conda` |
| Editor habitual | RStudio | JupyterLab o VS Code |
| Valores faltantes | `NA` | `NaN` (numéricos) o `pd.NA` |
| Asignar | `x <- 1` | `x = 1` |

## Manejo de datos (dplyr ↔ pandas)

| Tarea | R (tidyverse) | Python (pandas) |
| --- | --- | --- |
| Leer CSV | `read.csv("a.csv")` | `pd.read_csv("a.csv")` |
| Leer SPSS | `haven::read_sav("a.sav")` | `pd.read_spss("a.sav")` o `pyreadstat.read_sav("a.sav")` |
| Primeras filas | `head(df)` | `df.head()` |
| Estructura | `str(df)` | `df.info()` |
| Resumen | `summary(df)` | `df.describe(include="all")` |
| Dimensiones | `dim(df)` | `df.shape` |
| Nombres de columnas | `names(df)` | `df.columns` |
| Una columna | `df$x` | `df["x"]` |
| Varias columnas | `select(df, a, b)` | `df[["a", "b"]]` |
| Filtrar filas | `filter(df, x > 5)` | `df[df["x"] > 5]` o `df.query("x > 5")` |
| Crear columna | `mutate(df, z = x + y)` | `df.assign(z=df["x"] + df["y"])` |
| Ordenar | `arrange(df, x)` | `df.sort_values("x")` |
| Renombrar | `rename(df, nuevo = viejo)` | `df.rename(columns={"viejo": "nuevo"})` |
| Resumir por grupo | `group_by(g) %>% summarise(m = mean(x))` | `df.groupby("g").agg(m=("x", "mean"))` |
| Conteos | `count(df, g)` | `df["g"].value_counts()` |
| Unir tablas | `left_join(a, b, by = "k")` | `a.merge(b, on="k", how="left")` |
| Apilar tablas | `bind_rows(a, b)` | `pd.concat([a, b])` |
| Ancho a largo | `pivot_longer()` | `df.melt()` |
| Largo a ancho | `pivot_wider()` | `df.pivot_table()` |
| Detectar NA | `is.na(x)` | `df["x"].isna()` |
| Eliminar NA | `drop_na(df)` | `df.dropna()` |
| Condicional múltiple | `case_when()` | `np.select(condiciones, valores)` |
| Factor | `factor(x, levels = ...)` | `pd.Categorical(x, categories=..., ordered=True)` |
| Media ponderada | `weighted.mean(x, w)` | `np.average(x, weights=w)` |

## Visualización

| R | Python |
| --- | --- |
| `ggplot2` | `matplotlib` (base), `seaborn` (estadística), `plotly` y `altair` (interactivos) |
| `geom_histogram()` | `sns.histplot()` o `df["x"].plot.hist()` |
| `geom_bar()` | `sns.countplot()` o `df["x"].value_counts().plot.bar()` |
| `geom_point()` | `sns.scatterplot()` |
| `facet_wrap()` | `sns.FacetGrid()` o `col=` en las funciones de seaborn |

## Datos geográficos (se usan desde la semana 4)

| R | Python |
| --- | --- |
| `sf::st_read("a.shp")` | `geopandas.read_file("a.shp")` |
| `sf::st_transform(x, crs)` | `gdf.to_crs(crs)` |
| `left_join()` sobre un objeto `sf` | `gdf.merge(df, on="codigo")` |
| `tmap`, `ggplot2::geom_sf()` | `gdf.plot()`, `folium`, `plotly` |

## Un ejemplo completo

Media del ingreso por provincia, solo para personas con ingreso:

```r
df %>%
  filter(!is.na(ingreso)) %>%
  group_by(provincia) %>%
  summarise(media = mean(ingreso)) %>%
  arrange(desc(media))
```

```python
(
    df.dropna(subset=["ingreso"])
      .groupby("provincia")
      .agg(media=("ingreso", "mean"))
      .sort_values("media", ascending=False)
)
```
