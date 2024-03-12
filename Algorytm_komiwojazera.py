import numpy as np
import math
import matplotlib.collections as mc
import matplotlib.pylab as pl


random_seed = 1729
np.random.seed(random_seed)

N = 40
x = np.random.rand(N)
y = np.random.rand(N)

points = zip(x, y)
cities = list(points)

itinerary = list(range(0, N))


def genlines(cities, itinerary):
    lines = []
    for j in range(0, len(itinerary) - 1):
        lines.append([cities[itinerary[j]], cities[itinerary[j + 1]]])
    return lines


def howfar(lines):
    distance = 0
    for j in range(0, len(lines)):
        distance += math.sqrt((lines[j][1][0] - lines[j][0][0])**2 + (lines[j][1][1] - lines[j][0][1])**2)
    return distance


def draw_trail(cities, itin, plottitle, thename):
    lc = mc.LineCollection(genlines(cities, itin), linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.scatter(x, y)
    pl.title(plottitle)
    pl.xlabel("Wspolrzedna X")
    pl.ylabel("Wspolrzedna Y")
    pl.savefig(str(thename) + '.png')
    pl.close()


totaldistance = howfar(genlines(cities, itinerary))

draw_trail(cities, itinerary, "Problem komiwojazera", "rysunek2")

print(totaldistance)

