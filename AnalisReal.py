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
dESTdEST  =('Arm', 'ppi','les','tai','zue','lbi','azt','rcl')
prom=0
for i in range (0,8):
    if i!=1:
        EST=dEST[dESTdEST[i]]
        COD=EST[5]
        estacion= EST[0]
        sigla=EST[1]
        siglaMAY=EST[2]

        lat=EST[3]
        latrad=lat*np.pi/180
        long=EST[4]


        CAMS=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_CAMS\\"+sigla+"CAMS.csv")
        GL12=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_GL12\\"+sigla+"GL12.csv")
        LCIM=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_LCIM\\"+sigla+"LCIM.csv")
        DAT=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+sigla+"FINAL.csv")
        NASA=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_NASA\\"+sigla+"NASA.csv")
        NSRDB=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_NSRDB\\"+sigla+"NSRDB.csv")
        MERRA2=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_MERRA2\\"+sigla+"MERRA2.csv")


        lim=30
        #mask TOTAL
        mask=(DAT.flag==0)*(DAT.ipl<lim)*(CAMS.flag==0)*(LCIM.flag==0)*(NASA.flag==0)
        maskNSRDB=(NSRDB.flag==0)*(DAT.flag==0)*(DAT.ipl<lim)
        maskGL12=(GL12.flag==0)*(DAT.flag==0)*(DAT.ipl<lim)

        DesempMERRA2=fc.todas_las_metricas(MERRA2.GHI[mask], DAT.GHI[mask])
        DesempCAMS=fc.todas_las_metricas(CAMS.GHI[mask], DAT.GHI[mask])
        DesempLCIM=fc.todas_las_metricas(LCIM.GHI[mask], DAT.GHI[mask])
        DesempNASA=fc.todas_las_metricas(NASA.GHI[mask], DAT.GHI[mask])
        DesempGL12=fc.todas_las_metricas(GL12.GHI[maskGL12],DAT.GHI[maskGL12])
        DesempNSRDB=fc.todas_las_metricas(NSRDB.GHI[maskNSRDB], DAT.GHI[maskNSRDB])

        DESEMP=pd.DataFrame()
        DESEMP.insert(0,'LCIM',DesempLCIM)
        DESEMP.insert(1,'MERRA2',DesempMERRA2)
        DESEMP.insert(1,'CAMS',DesempCAMS)
        DESEMP.insert(1,'NASA',DesempNASA)
        DESEMP.insert(1,'GL12',DesempGL12)
        DESEMP.insert(1,'NSRDB',DesempNSRDB)
        
        prom=prom+DESEMP
        #print('&'+np.str0(round(np.mean(DAT.GHI[mask]),1)))
        #prom=prom+np.mean(DAT.GHI[mask])
        #print('&'+np.str0(round(np.mean(DAT.GHI[maskGL12]),1))+'$\\vert$'+np.str0(round(np.mean(DAT.GHI[maskNSRDB]),1)))
        #prom=prom+np.mean(DAT.GHI[maskNSRDB])

        #para el latex
        #print(dESTdEST[i])
        #nombre=('MBD [$\\frac{wh}{m^2}$]&','rMBD ($\%$)&','RMSD [$\\frac{wh}{m^2}$]&','rRMSD ($\%$) &','MAD [$\\frac{wh}{m^2}$]&','rMAD ($\%$)&')
        #for k in range(0,6):
        #3    if k%2==0: c=1000
        #    else: c=1
        #    print(nombre[k]+str(round(DESEMP.LCIM[k]*c,1))+' & '+str(round(DESEMP.CAMS[k]*c,1))+' & '+str(round(DESEMP.NASA[k]*c,1))+' & '+str(round(DESEMP.MERRA2[k]*c,1))+' & '+str(round(DESEMP.GL12[k]*c,1))+' & '+str(round(DESEMP.NSRDB[k]*c,1))+'\\'+'\\')
        
        #cant datos
        #print('&'+np.str0(len(DAT.GHI[mask])))

        #media de las medidas
        #print('&'+np.str0(round(np.mean(DAT.GHI[mask]),1)))

        #cant datos  gl\\nsrdb
        #print('&'+np.str0(len(DAT.GHI[maskGL12]))+'$\\vert$'+np.str0(len(DAT.GHI[maskNSRDB])))

        #media   gl\\nsrdb
        #print('&'+np.str0(round(np.mean(DAT.GHI[maskGL12]),1))+'$\\vert$'+np.str0(round(np.mean(DAT.GHI[maskGL12]),1)))

        DESEMP.to_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\Globales\GLyNSRDBappart\\GLyNSRDBappart"+sigla+"2018-2021.csv")
#print(np.str0(prom/7))