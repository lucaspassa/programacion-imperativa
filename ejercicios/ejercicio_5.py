#!/usr/bin/python
# coding: latin-1
#5- Escribir un algoritmo que imprima el mínimo, el máximo y la media de tres números.

def min_max_med(vector_valores):
    # Ordenamos.
    vector_valores.sort()

    # Obtenemos máximo y mínimo.
    minimo = numeros[0]
    maximo = numeros[2]

    # Obtenemos la media aritmética.
    media = round((numeros[0] + numeros[1] + numeros[2]) / float(3),3)

    # Visualizamos resultados.
    cadena = u'Mínimo: %d, Máximo: %d, Media: %f' % (minimo, maximo, media)
    print cadena


# Obtenemos números.
numeros = []
for i in ['primer', 'segundo','tercer']:
    texto = u'Introduce el %s número: ' % (i)
    numeros.append(float(raw_input(texto)))

min_max_med(numeros)


