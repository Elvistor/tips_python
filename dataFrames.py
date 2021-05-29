import numpy as np
import pandas as pd

#Se crea un rango de 10 días desde la fecha indicada
days = pd.date_range("2020-01-01", periods=10, freq="D")

#Se crean tablas usando "days" de columna, asignando a una letra
#y generando 10 números aleatorios entre 100 y 200
A = pd.DataFrame({"date": days,
                  "store": "A",
                  "sales": np.random.randint(100, 200, size=10)})

B = pd.DataFrame({"date": days,
                  "store": "B",
                  "sales": np.random.randint(100, 200, size=10)})

C = pd.DataFrame({"date": days,
                  "store": "C",
                  "sales": np.random.randint(100, 200, size=10)})

#Se unen las tres tablas usando concat, y se ordena por fecha
df = pd.concat([A, B, C]).sort_values(by="date")

#Se genera una columna llamada rank, donde se le asigna un ránking 
df["rank"] = df.groupby("date")["sales"]\
               .rank(ascending=False).astype("int")

#Se agrupan por las columnas store y rank, y se contabiliza cuantas ventas se hicieron
df.groupby(["store","rank"]).count()[["sales"]]

#Para renombrar la nueva columna se usa el método agg
df_store_sales = df.groupby(["store","rank"]).agg(rank_count = ("rank", "count"))

#Se redefine df, ordenado por fecha, pero reseteando los índices.
df = pd.concat([A, B, C])\
       .sort_values(by="date").reset_index(drop=True)
       
#Si al ordenar los valores, le decimos que ignore los índices, no hay necesidad de resetearlos
df = pd.concat([A, B, C]).sort_values(by="date", ignore_index=True)
print(df.head())

