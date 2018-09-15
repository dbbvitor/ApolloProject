# Calculo solar
import numpy as np

def Declinacao(n):
    "Calcula a declinação solar, onde n é o dia do ano"
    sindec =   -np.sin(np.deg2rad(23.45)) * np.cos(np.deg2rad(360 / 365.25 * (n + 10)))
    dec = np.rad2deg(np.arcsin(sindec))
    return dec

def FatorIrradiancia(n):
    "Calcula o Fator de correção da Irradiancia. Representa a porcentagem da Irradiancia que chega a superficie terrestre. n = dias corridos"
    fi = 1 + 0.033 * np.cos(np.deg2rad(360 / 365.25 * n))
    return fi

def HorasDeSol(lat, dec):
    "Calcula o nascer (nds) e o por (pds) do sol em horas de sol. Recebe os valores de Latitude e Declinação"
    apds = np.rad2deg(np.arccos(-np.tan(np.deg2rad(-20)) * np.tan(np.deg2rad(dec))))
    nhs = 2 / 15 * apds
    nds = 12 - (nhs / 2)
    pds = 12 + (nhs / 2)
    return nds, pds

def AnguloHorario(hs):
    "Converte o horarios solar em angulo horario. Recebe horario solar"
    anh = 15 * (hs - 12)
    return anh

def AnguloIncidencia(dec, lat, incl, az, anh):
    cost1 = np.cos(np.deg2rad(incl)) * np.cos(np.deg2rad(dec)) * np.cos(np.deg2rad(anh)) * np.cos(np.rad2deg(lat))
    cost2 = np.cos(np.deg2rad(incl)) * np.sin(np.deg2rad(dec)) * np.sin(np.deg2rad(lat))
    cost3 = np.sin(np.deg2rad(incl)) * np.sin(np.deg2rad(az)) * np.cos(np.deg2rad(dec)) * np.sin(np.deg2rad(anh))
    cost4 = np.sin(np.deg2rad(incl)) * np.cos(np.deg2rad(az)) * np.cos(np.deg2rad(dec)) * np.cos(np.deg2rad(anh)) * np.sin(np.deg2rad(lat))
    cost5 = np.sin(np.deg2rad(incl)) * np.cos(np.deg2rad(az)) * np.sin(np.deg2rad(dec)) * np.cos(np.deg2rad(lat))
    cost = cost1 + cost2 + cost3 + cost4 - cost5
    t = np.arccos(cost)
    return t

def Irradiancia(fi, t):
    "Calcula a irradiancia. Considera o Fator de Correção da Irradiância (fi) e o Ângulo de Incidencia Solar (t)"
    g = 1367 * fi * np.cos(t)
    return g

lat = float(input("Insira a latitude local: "))
incl = float(input("Insira a inclinção do plano: "))
az = float(input("Insira o desvio azimutal do plano: "))

def IrradianciaAnual(lat, incl, az):
    gtm = []
    gtv = []
    gts = []
    maxg = 0
    gs = 0

    for n in range(1, 367):
        dec = Declinacao(n)
        fi = FatorIrradiancia(n)
        nds, pds = HorasDeSol(lat, dec)

        
        for hs in range(int(nds), int(pds)):
            anh = AnguloHorario(hs)
            t = AnguloIncidencia(dec, lat, incl, az, anh)
            g = Irradiancia(fi, t)
            gtv.append(g)
            gs += g

        if len(gtv) > maxg:
            maxg = len(gtv)

        gs = gs / 24
        gts.append(gs)
        gtm.append(gtv)
        gs = 0
        gtv = []

    gtt = np.sum(gts)
    ga = gtt / 365
    return ga

ga = IrradianciaAnual(lat, incl, az)
#usar transmitância????

print(f"A irradiancia no local é {ga}")
