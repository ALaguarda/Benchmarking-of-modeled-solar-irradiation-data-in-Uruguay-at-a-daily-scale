from ctypes.wintypes import PLARGE_INTEGER
import VARSOL as vs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import fCalculo_indicadores as fc
import seaborn as sns

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

dMODmod=('CAMS', 'MERRA2','NASA','GL12','LCIM','NSRDB')

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
        maskDAT=(DAT.flag==0)*(DAT.ipl<lim)
        TOAhDAT=vs.TOAdh(DAT.N[maskDAT],lat)/3.6
        ktDAT=DAT.GHI[maskDAT]/TOAhDAT

        for j in range (0,6):
            #j=0
            modelo=dMOD[dMODmod[j]]
            mod=modelo[0]
            modelaso=modelo[1]
            MOD=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+mod+"\\"+sigla+mod+".csv")
            maskMOD=(MOD.flag==0)
            TOAhMOD=vs.TOAdh(MOD.N[maskMOD],lat)/3.6
            ktMOD=MOD.GHI[maskMOD]/TOAhMOD

            plt.plot()
            sns.set_style("white")
            sns.histplot(x=ktDAT, label= 'Ground Data',binrange=(0,0.8),binwidth=0.04,color='black',kde=True,alpha=0.4,stat='density')
            sns.histplot(x=ktMOD, label= mod ,binrange=(0,0.8),binwidth=0.04,alpha=0.35,kde=True,stat='density') #,binrange=(0,0.8),binwidth=0.05
            #plt.title(modelaso+' - '+siglaMAY)
            plt.xlabel(r'$K_t$')
            plt.xlim(0,0.9)
            plt.ylim(0,6)
            #plt.rc('legend', fontsize=16)
    #plt.text(0.25,70,r'Mayor nubosidad $\longleftrightarrow$ Menor nubosidad')
            #plt.legend()
            plt.rc('xtick', labelsize=19)
            plt.rc('ytick', labelsize=19) 
            plt.rc('axes', labelsize=23)
            plt.grid()
            #plt.legend()
            #plt.show()
            plt.tight_layout()
            plt.savefig(r'C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Paper\Predict Nubosidad\\Nub'+mod+sigla+'.jpg')
            plt.close()
        