from ctypes.wintypes import PLARGE_INTEGER
import VARSOL as vs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import fCalculo_indicadores as fc

dEST  = {'les': ['Salto ','le','LE', -31.2827, -57.9181,822], #-31.28	-57.92
         'ppi': ['Treinta y tres ','pp','PP', -33.2581, -54.4804,802], #-33.23	-54.25
         'rcl': ['Rocha ','rc','RC', -34.4893, -54.3203,810],#34.49	-54.31
         'tai': ['Tacuarembo ','ta','TA', -31.7387, -55.9792,805], #-31.7	-55.82
         'azt': ['Azotea Fing ','az','AZ', -34.9182, -56.1665,809], #809	-34.92	-56.17
         'lbi': ['Las Brujas ','lb','LB', -34.6720, -56.3401,808], #-34.67	-56.33
         'zue': ['Colonia ','zu','ZU', -34.3380, -57.6904, 821], #-34.33	-58.68
         'Arm': ['Artigas ','ar','AR', -30.3984, -56.5117,811]} #-30.4	-56.51
dESTdEST  =('les', 'ppi','rcl','tai','azt','lbi','zue','Arm')

AR=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\Globales\GLyNSRDBappart\GLyNSRDBappartar2018-2021.csv",index_col=0)
LE=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\Globales\GLyNSRDBappart\GLyNSRDBappartle2018-2021.csv",index_col=0)
RC=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\Globales\GLyNSRDBappart\GLyNSRDBappartrc2018-2021.csv",index_col=0)
LB=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\Globales\GLyNSRDBappart\GLyNSRDBappartlb2018-2021.csv",index_col=0)
AZ=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\Globales\GLyNSRDBappart\GLyNSRDBappartaz2018-2021.csv",index_col=0)
TA=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\Globales\GLyNSRDBappart\GLyNSRDBappartta2018-2021.csv",index_col=0)
ZU=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\Globales\GLyNSRDBappart\GLyNSRDBappartzu2018-2021.csv",index_col=0)

Prom=(AR+LE+RC+LB+AZ+TA+ZU)/7
Dev=np.sqrt(((AR-Prom)**2+(LE-Prom)**2+(RC-Prom)**2+(LB-Prom)**2+(AZ-Prom)**2+(TA-Prom)**2+(ZU-Prom)**2)/7)

 #para el latex
nombre=('MBD [$\\frac{wh}{m^2}$]&','rMBD ($\%$)&','RMSD [$\\frac{wh}{m^2}$]&','rRMSD ($\%$) &','MAD [$\\frac{wh}{m^2}$]&','rMAD ($\%$)&')
for k in range(0,3):
    print(nombre[2*k+1]+str(round(Prom.LCIM[2*k+1],1))+'$\pm$'+str(round(Dev.LCIM[2*k+1],1))+' & '+str(round(Prom.CAMS[2*k+1],1))+'$\pm$'+str(round(Dev.CAMS[2*k+1],1))+' & '+str(round(Prom.NASA[2*k+1],1))+'$\pm$'+str(round(Dev.NASA[2*k+1],1))+' & '+str(round(Prom.MERRA2[2*k+1],1))+'$\pm$'+str(round(Dev.MERRA2[2*k+1],1))+' & '+str(round(Prom.GL12[2*k+1],1))+'$\pm$'+str(round(Dev.GL12[2*k+1],1))+' & '+str(round(Prom.NSRDB[2*k+1],1))+'$\pm$'+str(round(Dev.NSRDB[2*k+1],1))+'\\'+'\\')

nom=('&rMBD ($\%$)&','&rRMSD ($\%$) &','&rMAD ($\%$)&','&Corr. &','&KSI [$\\frac{Wh}{m^2}$]&')
Modelo=('LCIM','NSRDB','GL1.2','Power','Heliosat-4','Merra 2')
for i in range(0,6):
    print('\\textbf{'+Modelo[i]+'}')
    for k in range(0,3):
        print(nom[k]+str(round(AR.iloc[:,i][2*k+1],1))+'&'+str(round(LE.iloc[:,i][2*k+1],1))+'&'+str(round(TA.iloc[:,i][2*k+1],1))+'&'+str(round(ZU.iloc[:,i][2*k+1],1))+'&'+str(round(LB.iloc[:,i][2*k+1],1))+'&'+str(round(AZ.iloc[:,i][2*k+1],1))+'&'+str(round(RC.iloc[:,i][2*k+1],1))+'&$\mathbf{'+str(round(Prom.iloc[:,i][2*k+1],1))+'}$\\\\')
    print(nom[3]+str(round(AR.iloc[:,i][6],3))+'&'+str(round(LE.iloc[:,i][6],3))+'&'+str(round(TA.iloc[:,i][6],3))+'&'+str(round(ZU.iloc[:,i][6],3))+'&'+str(round(LB.iloc[:,i][6],3))+'&'+str(round(AZ.iloc[:,i][6],3))+'&'+str(round(RC.iloc[:,i][6],3))+'&$\mathbf{'+str(round(Prom.iloc[:,i][6],3))+'}$\\\\')
    print(nom[4]+str(round(AR.iloc[:,i][9]*1000,1))+'&'+str(round(LE.iloc[:,i][9]*1000,1))+'&'+str(round(TA.iloc[:,i][9]*1000,1))+'&'+str(round(ZU.iloc[:,i][9]*1000,1))+'&'+str(round(LB.iloc[:,i][9]*1000,1))+'&'+str(round(AZ.iloc[:,i][9]*1000,1))+'&'+str(round(RC.iloc[:,i][9]*1000,1))+'&$\mathbf{'+str(round(Prom.iloc[:,i][9]*1000,1))+'}$\\\\')
    print('\\\\')


