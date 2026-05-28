
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/dataset.csv")

df["total"] = df["cantidad"] * df["precio"]

ventas_totales = df["total"].sum()

producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

ventas_por_mes = df.groupby(df["fecha"].str[:7])["total"].sum()

print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

print("Ventas por mes:")

for mes, venta in ventas_por_mes.items():
    print(mes, ":", venta)

ventas_por_mes.plot(kind="bar")

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")

plt.savefig("resultados/grafico_ventas.png")

plt.show()

with open("resultados/resultados.txt", "w") as archivo:
    archivo.write(f"Ventas totales: {ventas_totales}")
    archivo.write(f"Producto más vendido: {producto_mas_vendido}")

    archivo.write("Ventas por mes:")

    for mes, venta in ventas_por_mes.items():
        archivo.write(f"{mes}: {venta}")
