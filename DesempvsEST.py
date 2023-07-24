from ctypes.wintypes import PLARGE_INTEGER
from tkinter import Y
from unittest.case import DIFF_OMITTED
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


dMOD  = {'CAMS': ['CAMS','Heliosat-4'], 
         'MERRA2':["MERRA2",'MERRA2'], 
         'NASA': ['NASA','CERES'],
         'GL12': ['GL12','GL1.2'], 
         'LCIM': ['LCIM', 'LCIM'],
         'NSRDB': ['NSRDB','NSRDB']}
dMODmod=('LCIM','NSRDB','GL12','NASA','CAMS', 'MERRA2')

promLCIM=0
promNSRDB=0
promGL12=0
promNASA=0
promCAMS=0
promMERRA2=0
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

        lim=30
        DAT=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+sigla+"FINAL.csv")
        LCIM=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+ dMOD[dMODmod[0]][0] +"\\"+sigla+dMOD[dMODmod[0]][0]+".csv")
        NSRDB=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+ dMOD[dMODmod[1]][0] +"\\"+sigla+dMOD[dMODmod[1]][0]+".csv")
        GL12=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+ dMOD[dMODmod[2]][0] +"\\"+sigla+dMOD[dMODmod[2]][0]+".csv")
        NASA=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+ dMOD[dMODmod[3]][0] +"\\"+sigla+dMOD[dMODmod[3]][0]+".csv")
        CAMS=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+ dMOD[dMODmod[4]][0] +"\\"+sigla+dMOD[dMODmod[4]][0]+".csv")
        MERRA2=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+ dMOD[dMODmod[5]][0] +"\\"+sigla+dMOD[dMODmod[5]][0]+".csv")

        mask=(DAT.flag==0)*(DAT.ipl<lim)*(CAMS.flag==0)*(LCIM.flag==0)*(NASA.flag==0)
        maskNSRDB=(NSRDB.flag==0)*(DAT.flag==0)*(DAT.ipl<lim)
        maskGL12=(GL12.flag==0)*(DAT.flag==0)*(DAT.ipl<lim)

        Est=pd.DataFrame(columns=('Verano', 'Otoño', 'Invierno', 'Primavera'))
    
        EstNSRDB=Est*1.0
        EstNSRDB.Verano,EstNSRDB.Otoño,EstNSRDB.Invierno,EstNSRDB.Primavera=(DAT.N[maskNSRDB]>=356)+(DAT.N[maskNSRDB]<81),(DAT.N[maskNSRDB]>=81)*(DAT.N[maskNSRDB]<173),(DAT.N[maskNSRDB]>=173)*(DAT.N[maskNSRDB]<265),(DAT.N[maskNSRDB]>=265)*(DAT.N[maskNSRDB]<356)
        EstGL12=Est*1.0
        EstGL12.Verano,EstGL12.Otoño,EstGL12.Invierno,EstGL12.Primavera=(DAT.N[maskGL12]>=356)+(DAT.N[maskGL12]<81),(DAT.N[maskGL12]>=81)*(DAT.N[maskGL12]<173),(DAT.N[maskGL12]>=173)*(DAT.N[maskGL12]<265),(DAT.N[maskGL12]>=265)*(DAT.N[maskGL12]<356)
        
        Est.Verano,Est.Otoño,Est.Invierno,Est.Primavera=(DAT.N[mask]>=356)+(DAT.N[mask]<81),(DAT.N[mask]>=81)*(DAT.N[mask]<173),(DAT.N[mask]>=173)*(DAT.N[mask]<265),(DAT.N[mask]>=265)*(DAT.N[mask]<356)
        
        y=pd.DataFrame(columns=('rRMSD','rMBD','rMAD'))
        W=np.arange(0,4)*1.0
        y.rRMSD,y.rMBD,y.rMAD=W*1.0,W*1.0,W*1.0
        yLCIM=y*1.0
        yNSRDB=y*1.0
        yGL12=y*1.0
        yNASA=y*1.0
        yCAMS=y*1.0
        yMERRA2=y*1.0
        
        yprom=pd.DataFrame(columns=('prom','promGL12','promNSRDB'))
        yprom.prom,yprom.promGL12,yprom.promNSRDB=W*1.0,W*1.0,W*1.0

        for k in range(0,4):
            
            yLCIM.iloc[k,:]=fc.calculo_MBD_RMS_MAD(LCIM.GHI[mask][Est.iloc[:,k]],DAT.GHI[mask][Est.iloc[:,k]])
            yNSRDB.iloc[k,:]=fc.calculo_MBD_RMS_MAD(NSRDB.GHI[maskNSRDB][EstNSRDB.iloc[:,k]],DAT.GHI[maskNSRDB][EstNSRDB.iloc[:,k]])
            yGL12.iloc[k,:]=fc.calculo_MBD_RMS_MAD(GL12.GHI[maskGL12][EstGL12.iloc[:,k]],DAT.GHI[maskGL12][EstGL12.iloc[:,k]])
            yNASA.iloc[k,:]=fc.calculo_MBD_RMS_MAD(NASA.GHI[mask][Est.iloc[:,k]],DAT.GHI[mask][Est.iloc[:,k]])
            yCAMS.iloc[k,:]=fc.calculo_MBD_RMS_MAD(CAMS.GHI[mask][Est.iloc[:,k]],DAT.GHI[mask][Est.iloc[:,k]])
            yMERRA2.iloc[k,:]=fc.calculo_MBD_RMS_MAD(MERRA2.GHI[mask][Est.iloc[:,k]],DAT.GHI[mask][Est.iloc[:,k]])
            yprom.iloc[k,:]=[np.mean(DAT.GHI[mask][Est.iloc[:,k]]),np.mean(DAT.GHI[maskGL12][EstGL12.iloc[:,k]]),np.mean(DAT.GHI[maskNSRDB][EstNSRDB.iloc[:,k]])]
        promLCIM=promLCIM+yLCIM
        promNSRDB=promNSRDB+yNSRDB
        promGL12=promGL12+yGL12
        promNASA=promNASA+yNASA
        promCAMS=promCAMS+yCAMS
        promMERRA2=promMERRA2+yMERRA2
        prom=prom+yprom

promLCIM=promLCIM/7
promNSRDB=promNSRDB/7
promGL12=promGL12/7
promNASA=promNASA/7
promCAMS=promCAMS/7
promMERRA2=promMERRA2/7
prom=prom/7

X =['Summer', 'Autumn', 'Winter', 'Spring']
X_axis = np.arange(len(X))
retardin=(-0.375,-0.225,-0.075,0.075,0.225,0.375)

Indicador=('rRMSD','rMBD','rMAD')
for j in range(0,3):
    plt.rc('xtick', labelsize=15)
    plt.rc('ytick', labelsize=14) 
    plt.rc('axes', labelsize=15)
    plt.rc('legend', fontsize=13)
    plt.bar(X_axis-0.375,promLCIM.iloc[:,j], width=0.15,label=dMOD[dMODmod[0]][1]) 
    plt.bar(X_axis-0.225,promNSRDB.iloc[:,j], width=0.15,label=dMOD[dMODmod[1]][1]) 
    plt.bar(X_axis-0.075,promGL12.iloc[:,j], width=0.15,label=dMOD[dMODmod[2]][1]) 
    plt.bar(X_axis+0.075,promNASA.iloc[:,j], width=0.15,label=dMOD[dMODmod[3]][1]) 
    plt.bar(X_axis+0.225,promCAMS.iloc[:,j], width=0.15,label=dMOD[dMODmod[4]][1]) 
    plt.bar(X_axis+0.375,promMERRA2.iloc[:,j], width=0.15,label=dMOD[dMODmod[5]][1]) 
    plt.grid()
    plt.xticks(X_axis, X)
    plt.ylabel(Indicador[j]+' (%)')
    #plt.legend(fontsize=30)
    #plt.title("Desempeño estacional de los modelos Promediado espacialmente ")
    plt.legend()
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(r'C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Paper\Desemp Estacional\\'+Indicador[j]+'PromEspacial.jpg')
    plt.close()


plt.grid()
plt.bar(X_axis,prom.iloc[:,0], width=0.8,label='Mean') 
#plt.bar(X_axis,prom.iloc[:,1], width=0.3,label='Mean GL1.2') 
#plt.bar(X_axis+0.3,prom.iloc[:,2], width=0.3,label='Mean NSRDB') 
plt.xticks(X_axis, X)
plt.legend()
plt.ylabel("[kWh/m2]")
plt.savefig(r'C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Paper\Desemp Estacional\\MeansPromEspacial.jpg')
