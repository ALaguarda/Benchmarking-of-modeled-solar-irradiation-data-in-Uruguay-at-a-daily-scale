#Varaibles Solares IÑAKI SARAZOLA 2022 
import numpy as np
import pandas as pd

#gamma
def Fase(n):
    T = 2*np.pi*(n-1)/365
    T =np.float64(T)
    return T     

#correccion orbital
def Fn(n):    
    Fn = 1.000110 + 0.034221*np.cos(Fase(n)) + 0.001280*np.sin(Fase(n)) + 0.000719*np.cos(2*Fase(n)) + 0.000077*np.sin(2*Fase(n))
    return Fn

def Declinacion_solar(n):
    DELTA = 0.006918 - 0.399912*np.cos(Fase(n)) + 0.070257*np.sin(Fase(n)) - 0.006758 *np.cos(2*Fase(n)) + 0.000907 * np.sin(2*Fase(n)) - 0.002697*np.cos(3*Fase(n)) + 0.00148*np.sin(3*Fase(n))
    return DELTA

#angulo cenital min, altura solar max
def CminAmax(n,lat):
    latrad=lat*np.pi/180
    TITAMIN_rad= np.abs(Declinacion_solar(n)-latrad)
    ALPHAMAX_rad = 90-TITAMIN_rad
    return TITAMIN_rad,ALPHAMAX_rad

#Angulo solar max
def w_s(n,lat):
    latrad=lat*np.pi/180
    ws= np.arccos((-1)*np.tan(latrad)*np.tan(Declinacion_solar(n)))
    return ws

#Azimut solar a la puesta del sol
def Azim_puesta(n,lat):
    latrad=lat*np.pi/180
    (TITAMIN,ALPHAMAX)= CminAmax(n,lat)
    gamma=np.sign(w_s(n,lat))*np.abs(np.arccos((np.sin(Declinacion_solar(n))-np.cos(TITAMIN)*np.sin(latrad))/(np.sin(TITAMIN)*np.cos(lat))))
    return gamma
    
#Ecuacion del tiempo
def E(n):
    E = 229.18 * (0.000075 + 0.001868* np.cos(Fase(n)) - 0.032077 *np.sin(Fase(n)) - 0.014615 *np.cos(2*Fase(n)) - 0.04089* np.sin(2*Fase(n)))
    return E

#Cant horas diurnas
def N(n,lat):
    N = 24/np.pi * w_s(n,lat)
    return N

#Irradiacion solar diaria TOAn (MJ/m2)
def TOAdn(n,lat):
    H_0=36*Fn(n)*w_s(n, lat)
    return H_0

#Irradiacion solar diaria TOAn (MJ/m2)
def TOAdh(n,lat):
    latrad=lat*np.pi/180
    H_0h=24/np.pi*4.89*Fn(n)*(np.cos(Declinacion_solar(n))*np.cos(latrad)*np.sin(w_s(n,lat))+w_s(n,lat)*np.sin(Declinacion_solar(n))*np.sin(latrad))
    return H_0h

def Tutcsalidapuesta (n,lat):
    TutcSalida= (12*(1-w_s(n, lat)/(np.pi))+((-45)-(lat))/15-E(n)/60)
    Tutcpuesta= (12*(1+w_s(n, lat)/(np.pi))+((-45)-(lat))/15-E(n)/60)
    return TutcSalida,Tutcpuesta

def datetoordinal(year,month, day):
    esbisiesto=(year%4==0)
    if month==1 : n=day 
    else:
        if month==2 : n=31+day
        else:
            if month==3 : n=31+28+day+esbisiesto
            else:
                if month==4 : n=2*31+28+day+esbisiesto
                else:
                    if month==5 : n=2*31+30+28+day+esbisiesto
                    else:
                        if month==6 : n=2*31+2*30+28+day+esbisiesto
                        else:
                            if month==7 : n=3*31+2*30+28+day+esbisiesto
                            else:
                                if month==8 : n=3*31+3*30+28+day+esbisiesto
                                else:
                                    if month==9 : n=4*31+3*30+28+day+esbisiesto
                                    else:
                                        if month==10 : n=4*31+4*30+28+day+esbisiesto
                                        else:
                                            if month==11 : n=5*31+4*30+28+day+esbisiesto
                                            else: n=5*31+5*30+28+day+esbisiesto
    return n

def RMSD(predictions, targets):
    e=predictions-targets
    media=np.mean(e**2)
    return np.sqrt(media)

def MBD(predictions, targets):
     e=predictions-targets
     return np.mean(e)

def m(csz):
    nom=1.002432 *csz**2+0.148386*csz+0.0096467
    denom=csz**3+0.149864*csz**2+0.0102963*csz+0.00303978
    return nom/denom

def MAD(predictions, targets):
     e=np.abs(predictions-targets)
     return np.mean(e)


def Metricas(predictions,targets):
    MBd=MBD(predictions,targets)
    rMBd=MBd/np.mean(targets)
    RMSd=RMSD(predictions,targets)
    rRMSd=RMSd/np.mean(targets)
    MAd=MAD(predictions,targets)
    rMAD=MAd/np.mean(targets)
    return MBd,rMBd,RMSd,rRMSd,MAd,rMAD


