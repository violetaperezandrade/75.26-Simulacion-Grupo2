# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random as rn


def generateNormalAcceptanceRejection(n, mu, sigma):
    deltax = 0.5 * mu
    xmin, xmax = mu - deltax, mu + deltax
    ymax = max(stats.norm.pdf(np.arange(xmin, xmax), mu, sigma))
    numbers = np.array([])
    acceptedN = 0
    while acceptedN < n:
        x = np.random.uniform(xmin, xmax)
        y = np.random.uniform(0.0, ymax)
        fx = stats.norm.pdf(x, mu, sigma)

        if y < fx:
            numbers = np.append(numbers, x)
            acceptedN += 1
            continue

    return numbers


def drawHistogram(numbers, show):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(numbers, weights=np.zeros_like(numbers) + 1.0 / numbers.size, bins=20)
    ax.set_xlabel("Numbers range")
    ax.set_ylabel("Relative frequency")
    if show:
        plt.show()


def drawNormalDistribution(mu, sigma, show):
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), "-r")
    if show:
        plt.show()


def main():
    # Aplicando el algoritmo de Aceptación y rechazo se pide:
    # a) Generar 100.000 número aleatorios con distribución Normal de media 25 y desvío estándar 2 .
    n, mu, sigma = 1000000, 25, 2
    numbers = generateNormalAcceptanceRejection(n, mu, sigma)

    # b) Realizar un histograma de frecuencias relativas con todos los valores obtenidos.
    drawHistogram(numbers, True)

    # c) Comparar, en el mismo gráfico, el histograma realizado en el punto anterior con la función de densidad de
    # probabilidad brindada por el lenguaje elegido (para esta última distribución utilizar un gráfico de línea).
    drawHistogram(numbers, False)
    drawNormalDistribution(mu, sigma, True)

    # d) Calcular la media y la varianza de la distribución obtenida y compararlos con los valores teóricos
    print("Valores teóricos:")
    print("Media:", mu)
    print("Varianza:", sigma ** 2)

    print("Valores prácticos:")
    print("Media:", np.average(numbers))
    print("Varianza:", np.var(numbers))


if __name__ == "__main__":
    main()
