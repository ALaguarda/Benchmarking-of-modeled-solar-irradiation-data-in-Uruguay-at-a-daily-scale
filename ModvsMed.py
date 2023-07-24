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

dMOD  = {'CAMS': ['CAMS','CAMS'], 
         'MERRA2':["MERRA2",'Merra 2'], 
         'NASA': ['NASA','Power'],
         'GL12': ['GL12','GL 12'], 
         'LCIM': ['LCIM', 'L-CIM'],
         'NSRDB': ['NSRDB','NSRDB']}
dMODmod=('LCIM','NSRDB','GL12','NASA','CAMS', 'MERRA2')

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

        DAT=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+sigla+"FINAL.csv")
        lim=30

        dMOD  = {'CAMS': ['CAMS'], 
                'MERRA2':["MERRA2"], 
                'NASA': ['NASA'],
                'GL12': ['GL12'], 
                'LCIM': ['LCIM'],
                'NSRDB': ['NSRDB']}
        for j in range(0,6):
            
            modelo=dMOD[dMODmod[j]]
            mod=modelo[0]
            MOD=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+mod+"\\"+sigla+mod+".csv")
            mask=(MOD.flag==0)*(DAT.flag==0)*(DAT.ipl<lim)


            TIT=mod +' - '+ siglaMAY

            #########################################################################################################
            #Estaciones del Año
            #modelo
            veranoMOD=(MOD.N>=356)+(MOD.N<81)
            otoñoMOD=(MOD.N>=81)*(MOD.N<173)
            inviernoMOD=(MOD.N>=173)*(MOD.N<265)
            primaveraMOD=(MOD.N>=265)*(MOD.N<356)
            #datos
            veranoDAT=(DAT.N>=356)+(DAT.N<81)
            otoñoDAT=(DAT.N>=81)*(DAT.N<173)
            inviernoDAT=(DAT.N>=173)*(DAT.N<265)
            primaveraDAT=(DAT.N>=265)*(DAT.N<356)

            plt.scatter(DAT.GHI[mask*veranoDAT],MOD.GHI[mask*veranoMOD],s=25,label='Summer',alpha=0.5)
            plt.scatter(DAT.GHI[mask*inviernoDAT],MOD.GHI[mask*inviernoMOD],s=25,label='Winter',alpha=0.5)
            plt.scatter(DAT.GHI[mask*otoñoDAT],MOD.GHI[mask*otoñoMOD],s=25,label='Autumn',alpha=0.5)
            plt.scatter(DAT.GHI[mask*primaveraDAT],MOD.GHI[mask*primaveraMOD],s=25,label='Spring',alpha=0.5)
            plt.legend()
            plt.legend(fontsize=18)
            plt.rc('xtick', labelsize=16)
            plt.rc('ytick', labelsize=16) 
            plt.rc('axes', labelsize=21)
            plt.xlabel('Ground data (kWh/m2)')
            plt.ylabel('Modeled data (kWh/m2)')
            plt.plot((0,10),(0,10),c='black',linewidth=0.5)
            plt.grid()
            plt.tight_layout()
            plt.savefig(r'C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Paper\Mod vs Med (y=x)\\'+mod+' - '+siglaMAY+'.jpg')
            plt.close()
            Desempverano=fc.todas_las_metricas(MOD.GHI[mask*veranoMOD], DAT.GHI[mask*veranoDAT])
            Desempotoño=fc.todas_las_metricas(MOD.GHI[mask*otoñoMOD], DAT.GHI[mask*otoñoDAT])
            Desempinvierno=fc.todas_las_metricas(MOD.GHI[mask*inviernoMOD], DAT.GHI[mask*inviernoDAT])
            Desempprimavera=fc.todas_las_metricas(MOD.GHI[mask*primaveraMOD], DAT.GHI[mask*primaveraDAT])

            DESEMPest=pd.DataFrame()
            DESEMPest.insert(0,'verano',Desempverano)
            DESEMPest.insert(0,'otoño',Desempotoño)
            DESEMPest.insert(0,'invierno',Desempinvierno)
            DESEMPest.insert(0,'primavera',Desempprimavera)
            DESEMPest.to_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\SegunEpoca\\"+mod+'\\'+sigla+'.csv')
            #########################################################################################################

        #########################################################################################################
        #graficos de diferencias
        #GHImod=np.array(MOD.GHI[mask]*1.0)
        #GHIdat=np.array(DAT.GHI[mask]*1.0)
        #plt.plot((MOD.year+MOD.N/365)[mask],GHImod-GHIdat,'.-')
        #plt.grid()
        #plt.title('Modelo - Medidas')
        #plt.ylabel('Diferencia [kWh/m2]')
        #plt.xlabel('Año')
        #plt.savefig(r'C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Graficos\\'+mod+'\MOD-MED\\Resta'+sigla+'.jpg')
        #plt.close()
        #########################################################################################################

        #########################################################################################################
        #segun kt
        #TOAhDAT=vs.TOAdh(DAT.N[mask],lat)/3.6
        #kt=GHIdat/TOAhDAT

        #x=np.floor(kt*10)/10+0.05
        #dif=GHImod-GHIdat
        #mean=np.mean(dif)
        #y=x*1.0
        #for i in range(0,8):
        #    dif[np.floor(kt*10)==i*1.0]=np.mean(dif[np.floor(kt*10)==i*1.0])
        #    y[np.floor(kt*10)==i*1.0]=len(x[np.floor(kt*10)==i*1.0])

        #fig, ax = plt.subplots(figsize = (10, 5)) 
        #ax2 = ax.twinx() 
        #ax.bar(x,dif, width=0.08,color='green',label='Modelo - Medida') 
        #ax2.bar(x,y, width=0.04,color='orange',label='Cantidad de Datos') 
        #ax.set_xlabel(r'$k_t$') 
        #ax.legend()
        #ax2.legend()
        #ax.set_ylabel('Diferencia [kWh/m2]') 
        #ax2.set_ylabel('Cantidad de Datos') 
        #plt.tight_layout() 
        #plt.savefig(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Graficos\\"+mod+"\Segunkt\\"+sigla+'.jpg')
        #plt.close()

        #z1=kt<0.45
        #z2=(0.45<=kt)*(kt<0.65)
        #z3=(0.65<=kt)

        #Desempz1=fc.todas_las_metricas(GHImod[z1],GHIdat[z1])
        #Desempz2=fc.todas_las_metricas(GHImod[z2],GHIdat[z2])
        #Desempz3=fc.todas_las_metricas(GHImod[z3],GHIdat[z3])


        #DESEMPkt=pd.DataFrame()
        #DESEMPkt.insert(0,'kt<0.45',Desempz1)
        #DESEMPkt.insert(0,'0.45<kt<0.65',Desempz2)
        #DESEMPkt.insert(0,'0.65<kt',Desempz3)
        #DESEMPest.to_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Desempeños\SegunKt\\"+mod+'\\'+sigla+'.csv')

        #plt.scatter(kt,GHImod-GHIdat,s=4)
        #plt.title('Modelo - Medidas')
        #plt.ylabel('Diferencia [kWh/m2]')
        #plt.xlabel('kt')
        #plt.savefig(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Graficos\\"+mod+"\Segunkt\\"+sigla+'SCATTER.jpg')
        #plt.close()
