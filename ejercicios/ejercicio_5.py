#!/usr/bin/python
# coding: latin-1
#5- Escribir un algoritmo que imprima el m�nimo, el m�ximo y la media de tres n�meros.

def min_max_med(vector_valores):
    # Ordenamos.
    vector_valores.sort()

    # Obtenemos m�ximo y m�nimo.
    minimo = numeros[0]
    maximo = numeros[2]

    # Obtenemos la media aritm�tica.
    media = round((numeros[0] + numeros[1] + numeros[2]) / float(3),3)

    # Visualizamos resultados.
    cadena = u'M�nimo: %d, M�ximo: %d, Media: %f' % (minimo, maximo, media)
    print cadena


# Obtenemos n�meros.
numeros = []
for i in ['primer', 'segundo','tercer']:
    texto = u'Introduce el %s n�mero: ' % (i)
    numeros.append(float(raw_input(texto)))

min_max_med(numeros)


