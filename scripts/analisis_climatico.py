import csv
import matplotlib.pyplot as plt

# Funcion para leer temperaturas desde el archivo CSV
def leer_temperaturas(ruta_archivo):

    anios = []
    temperaturas = []

    with open(ruta_archivo, "r") as archivo:

        lector = csv.reader(archivo)
        next(lector)

        for fila in lector:

            try:

                if fila[0] == "GCAG":

                    anio = int(fila[1])
                    temperatura = float(fila[2])

                    anios.append(anio)
                    temperaturas.append(temperatura)

            except:
                print("Error al leer una fila")

    return anios, temperaturas


# Funcion para calcular estadisticas
def calcular_estadisticas(temperaturas):

    promedio = sum(temperaturas) / len(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)

    return promedio, maxima, minima


# Funcion para guardar resultados
def guardar_resultados(promedio, maxima, minima):

    with open("resultados/resultados.txt", "w") as archivo:

        archivo.write("Resultados del analisis climatico\n")
        archivo.write(f"Temperatura promedio: {promedio}\n")
        archivo.write(f"Temperatura maxima: {maxima}\n")
        archivo.write(f"Temperatura minima: {minima}\n")


# Funcion para generar grafico
def generar_grafico(anios, temperaturas):

    plt.figure(figsize=(10,5))

    plt.plot(anios, temperaturas)

    plt.title("Evolucion de temperaturas")
    plt.xlabel("Anios")
    plt.ylabel("Temperatura")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("resultados/grafico_temperaturas.png")

    print("Grafico guardado correctamente")


# Programa principal

ruta = "datos/annual.csv"

anios, temperaturas = leer_temperaturas(ruta)

promedio, maxima, minima = calcular_estadisticas(temperaturas)

guardar_resultados(promedio, maxima, minima)

generar_grafico(anios, temperaturas)

print("Analisis finalizado")

