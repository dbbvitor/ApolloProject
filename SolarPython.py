# Calculo Solar
import numpy as np
import math

def Declinacao(n):
    "Calcula a declinação solar, onde n é o dia do ano"
    dec = 23.5 * np.sin(np.deg2rad(360 * (284 + n) / 365))
    return dec

def AnguloHorario(n, fuso, tl, hv, lonl):
    "Calcula o Angulo Horario, onde n é o dia do ano, fuso é o fuso horario, tl é o horario legal, hv é o horario de verão e lonl é a longitude local"
    b = (360 * (n - 81)) / 365
    #E é a diferença entra o tempo solar verdadeiro e o tempo solar medio
    e = 9.87 * np.sin(np.deg2rad(2 * b)) - 7.53 * np.cos(np.deg2rad(b)) - 1.5 * np.sin(np.deg2rad(b))
    #TSV é o tempo solar verdadeiro
    #TL é o tempo legal
    #HV é o horario de verão e assume o valor de 1 ou 0
    #LONL é a longitude local
    #LONR é a longitude de referência
    lonr = 15 * fuso
    tsv = tl - hv + (4 * (lonl - lonr) + e) / 60
    anh = 15 * (tsv - 12)
    return anh

def AnguloIncidencia(dec, lat, incl, az, anh):
    cost = np.sin(np.deg2rad(dec)) * (np.sin(np.deg2rad(lat)) * np.cos(np.deg2rad(incl)) + np.cos(np.deg2rad(lat)) * np.sin(np.deg2rad(incl)) * np.cos(np.deg2rad(az))) + np.cos(np.deg2rad(dec)) * np.cos(np.deg2rad(anh)) * (np.cos(np.deg2rad(lat)) * np.cos(np.deg2rad(incl)) - np.sin(np.deg2rad(lat)) * np.sin(np.deg2rad(incl)) * np.cos(np.deg2rad(az))) - np.cos(np.deg2rad(dec)) * np.sin(np.deg2rad(incl)) * np.sin(np.deg2rad(az)) * np.sin(np.deg2rad(anh))
    t = np.arccos(cost)
    return t

def Irradiancia(t):
    "Calcula a irradiancia segundo o angulo de incidencia solar (t)"
    g = 1000 * np.cos(t)
    return g

n = float(input("Insira o dia do ano em valor absoluto: "))
fuso = float(input("Insira o fuso horario local: "))
tl = float(input("Insira o horario: "))
hv = float(input("Insira 1 caso seja horario de verão, 0 caso contrario: "))
lonl = float(input("Insira a longitude local: "))
lat = float(input("Insira a latitude local: "))
incl = float(input("Insira a inclinção do plano: "))
az = float(input("Insira o desvio azimutal do plano: "))

dec = Declinacao(n)
anh = AnguloHorario(n, fuso, tl, hv, lonl)
t = AnguloIncidencia(dec, lat, incl, az, anh)
g = Irradiancia(t)
print(f"A irradiancia no local é {g}")