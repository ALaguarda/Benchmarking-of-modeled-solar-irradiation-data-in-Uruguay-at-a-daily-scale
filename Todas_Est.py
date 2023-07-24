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
cles=['Salto ','le','LE', -31.2827, -57.9181]
DATles=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+cles[1]+"FINAL.csv")
#cppi=['Treinta y tres ','pp','PP', -33.2581, -54.4804]
#DATppi=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+cppi[1]+"FINAL.csv")
crcl= ['Rocha ','rc','RC', -34.4893, -54.3203,]
DATrcl=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+crcl[1]+"FINAL.csv")
ctai= ['Tacuarembo ','ta','TA', -31.7387, -55.9792]
DATtai=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+ctai[1]+"FINAL.csv")
cazt= ['Azotea Fing ','az','AZ', -34.9182, -56.1665]
DATazt=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+cazt[1]+"FINAL.csv")
clbi=['Las Brujas ','lb','LB', -34.6720, -56.3401]
DATlbi=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+clbi[1]+"FINAL.csv")
czue= ['Colonia ','zu','ZU', -34.3380, -57.6904]
DATzue=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+czue[1]+"FINAL.csv")
carm= ['Artigas ','ar','AR', -30.3984, -56.5117]
DATarm=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_les\\"+carm[1]+"FINAL.csv")

lim=30
dMOD  = {'CAMS': ['CAMS'], 
         'MERRA2':["MERRA2"], 
         'NASA': ['NASA'],
         'GL12': ['GL12'], 
         'LCIM': ['LCIM'],
         'NSRDB': ['NSRDB']}
modelo=dMOD['LCIM']
mod=modelo[0]
MODles=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+mod+"\\"+cles[1]+mod+".csv")
maskMODles=(MODles.flag==0)*(DATles.flag==0)*(DATles.ipl<lim)
maskDATles=maskMODles
MODrcl=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+mod+"\\"+crcl[1]+mod+".csv")
maskMODrcl=(MODrcl.flag==0)*(DATrcl.flag==0)*(DATrcl.ipl<lim)
maskDATrcl=maskMODrcl
MODtai=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+mod+"\\"+ctai[1]+mod+".csv")
maskMODtai=(MODtai.flag==0)*(DATtai.flag==0)*(DATtai.ipl<lim)
maskDATtai=maskMODtai
MODlbi=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+mod+"\\"+clbi[1]+mod+".csv")
maskMODlbi=(MODlbi.flag==0)*(DATlbi.flag==0)*(DATlbi.ipl<lim)
maskDATlbi=maskMODlbi
MODazt=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+mod+"\\"+cazt[1]+mod+".csv")
maskMODazt=(MODazt.flag==0)*(DATazt.flag==0)*(DATazt.ipl<lim)
maskDATazt=maskMODazt
MODzue=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+mod+"\\"+czue[1]+mod+".csv")
maskMODzue=(MODzue.flag==0)*(DATzue.flag==0)*(DATzue.ipl<lim)
maskDATzue=maskMODzue
MODarm=pd.read_csv(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Datos_Diarios\Acum_"+mod+"\\"+carm[1]+mod+".csv")
maskMODarm=(MODarm.flag==0)*(DATarm.flag==0)*(DATarm.ipl<lim)
maskDATarm=maskMODarm

# NSRDB
#T=(DAT.year>2018)*(DAT.year<2021)
#maskMOD=np.array((DAT.flag[T]==0)*(DAT.ipl[T]<lim))
#maskDAT=(DAT.flag==0)*(DAT.ipl<lim)*(DAT.year>2018)*(DAT.year<2021)


#segun kt
TOAhles=vs.TOAdh(DATles.N[maskDATles],cles[3])/3.6
ktles=DATles.GHI[maskDATles]/TOAhles
xles=np.floor(ktles*10)/10+0.05
difles=MODles.GHI[maskDATles]-DATles.GHI[maskMODles]
meanles=np.mean(difles)
yles=xles*1.0
for i in range(0,8):
    difles[np.floor(ktles*10)==i*1.0]=np.mean(difles[np.floor(ktles*10)==i*1.0])
    yles[np.floor(ktles*10)==i*1.0]=len(xles[np.floor(ktles*10)==i*1.0])

TOAhrcl=vs.TOAdh(DATrcl.N[maskDATrcl],crcl[3])/3.6
ktrcl=DATrcl.GHI[maskDATrcl]/TOAhrcl
xrcl=np.floor(ktrcl*10)/10+0.05
difrcl=MODrcl.GHI[maskDATrcl]-DATrcl.GHI[maskMODrcl]
meanrcl=np.mean(difrcl)
yrcl=xrcl*1.0
for i in range(0,8):
    difrcl[np.floor(ktrcl*10)==i*1.0]=np.mean(difrcl[np.floor(ktrcl*10)==i*1.0])
    yrcl[np.floor(ktrcl*10)==i*1.0]=len(xrcl[np.floor(ktrcl*10)==i*1.0])

TOAhtai=vs.TOAdh(DATtai.N[maskDATtai],ctai[3])/3.6
kttai=DATtai.GHI[maskDATtai]/TOAhtai
xtai=np.floor(kttai*10)/10+0.05
diftai=MODtai.GHI[maskDATtai]-DATtai.GHI[maskMODtai]
meantai=np.mean(diftai)
ytai=xtai*1.0
for i in range(0,8):
    diftai[np.floor(kttai*10)==i*1.0]=np.mean(diftai[np.floor(kttai*10)==i*1.0])
    ytai[np.floor(kttai*10)==i*1.0]=len(xtai[np.floor(kttai*10)==i*1.0])

TOAhazt=vs.TOAdh(DATazt.N[maskDATazt],cazt[3])/3.6
ktazt=DATazt.GHI[maskDATazt]/TOAhazt
xazt=np.floor(ktazt*10)/10+0.05
difazt=MODazt.GHI[maskDATazt]-DATazt.GHI[maskMODazt]
meanazt=np.mean(difazt)
yazt=xazt*1.0
for i in range(0,8):
    difazt[np.floor(ktazt*10)==i*1.0]=np.mean(difazt[np.floor(ktazt*10)==i*1.0])
    yazt[np.floor(ktazt*10)==i*1.0]=len(xazt[np.floor(ktazt*10)==i*1.0])

TOAhlbi=vs.TOAdh(DATlbi.N[maskDATlbi],clbi[3])/3.6
ktlbi=DATlbi.GHI[maskDATlbi]/TOAhlbi
xlbi=np.floor(ktlbi*10)/10+0.05
diflbi=MODlbi.GHI[maskDATlbi]-DATlbi.GHI[maskMODlbi]
meanlbi=np.mean(diflbi)
ylbi=xlbi*1.0
for i in range(0,8):
    diflbi[np.floor(ktlbi*10)==i*1.0]=np.mean(diflbi[np.floor(ktlbi*10)==i*1.0])
    ylbi[np.floor(ktlbi*10)==i*1.0]=len(xlbi[np.floor(ktlbi*10)==i*1.0])
 
 
TOAhzue=vs.TOAdh(DATzue.N[maskDATzue],czue[3])/3.6
ktzue=DATzue.GHI[maskDATzue]/TOAhzue
xzue=np.floor(ktzue*10)/10+0.05
difzue=MODzue.GHI[maskDATzue]-DATzue.GHI[maskMODzue]
meanzue=np.mean(difzue)
yzue=xzue*1.0
for i in range(0,8):
    difzue[np.floor(ktzue*10)==i*1.0]=np.mean(difzue[np.floor(ktzue*10)==i*1.0])
    yzue[np.floor(ktzue*10)==i*1.0]=len(xzue[np.floor(ktzue*10)==i*1.0])
 
TOAharm=vs.TOAdh(DATarm.N[maskDATarm],carm[3])/3.6
ktarm=DATarm.GHI[maskDATarm]/TOAharm
xarm=np.floor(ktarm*10)/10+0.05
difarm=MODarm.GHI[maskDATarm]-DATarm.GHI[maskMODarm]
meanarm=np.mean(difarm)
yarm=xarm*1.0
for i in range(0,8):
    difarm[np.floor(ktarm*10)==i*1.0]=np.mean(difarm[np.floor(ktarm*10)==i*1.0])
    yarm[np.floor(ktarm*10)==i*1.0]=len(xarm[np.floor(ktarm*10)==i*1.0])
 

fig, ax = plt.subplots(figsize = (10, 5)) 
ax2 = ax.twinx() 
ax.bar(xles-0.03,difles, width=0.01,label='Salto') 
ax2.bar(xles-0.03,yles, width=0.0001,color='black') 
ax.bar(xrcl-0.02,difrcl, width=0.01,label='Rocha') 
ax2.bar(xrcl-0.02,yrcl, width=0.0001,color='black') 
ax.bar(xtai-0.01,diftai, width=0.01,label='Tacuarembo') 
ax2.bar(xtai-0.01,ytai, width=0.0001,color='black')
ax.bar(xazt,difazt, width=0.01,label='Azotea Fing') 
ax2.bar(xazt,yazt, width=0.0001,color='black')
ax.bar(xlbi+0.01,diflbi, width=0.01,label='Las Brujas') 
ax2.bar(xlbi+0.01,ylbi, width=0.0001,color='black')
ax.bar(xzue+0.02,difzue, width=0.01,label='Colonia') 
ax2.bar(xzue+0.02,yzue, width=0.0001,color='black')
ax.bar(xarm+0.03,difarm, width=0.01,label='Artigas') 
ax2.bar(xarm+0.03,yarm, width=0.0001,color='black')
ax.set_xlabel(r'$k_t$') 
ax.legend()
ax.set_ylabel('Diferencia [kWh/m2]') 
ax2.set_ylabel('Cantidad de Datos') 
plt.tight_layout() 
#plt.savefig(r"C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Graficos\\"+mod+"\Segunkt\\TodasEST.jpg")
plt.close()

plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12) 
plt.rc('axes', labelsize=14)
plt.figure()
plt.plot()
plt.plot(np.sort(DATarm.ipl[DATarm.flag==0]),np.arange(len(DATarm.ipl[DATarm.flag==0])),label=carm[2],linewidth=2)
plt.plot(np.sort(DATles.ipl[DATles.flag==0]),np.arange(len(DATles.ipl[DATles.flag==0])),label=cles[2],linewidth=2)
plt.plot(np.sort(DATlbi.ipl[DATlbi.flag==0]),np.arange(len(DATlbi.ipl[DATlbi.flag==0])),label=clbi[2],linewidth=2)
plt.plot(np.sort(DATzue.ipl[DATzue.flag==0]),np.arange(len(DATzue.ipl[DATzue.flag==0])),label=czue[2],linewidth=2)
plt.plot(np.sort(DATrcl.ipl[DATrcl.flag==0]),np.arange(len(DATrcl.ipl[DATrcl.flag==0])),label=crcl[2],linewidth=2)
plt.plot(np.sort(DATtai.ipl[DATtai.flag==0]),np.arange(len(DATtai.ipl[DATtai.flag==0])),label=ctai[2],linewidth=2)
plt.plot(np.sort(DATazt.ipl[DATazt.flag==0]),np.arange(len(DATazt.ipl[DATazt.flag==0])),label=cazt[2],linewidth=2)
plt.xlabel('Daily missing data (minutes)')
plt.xlim(-10,120)
plt.ylabel('Available data (days)')
plt.plot((30,30),(0,1500),'--',c='black',linewidth=2)
plt.legend(fontsize=15)
plt.grid()
plt.tight_layout()
plt.savefig(r'C:\Users\juan_\Desktop\Fing\FRS\Pasantia\Paper\Metodologia\Descartasceinver2.jpg')




#
#plt.plot(np.sort(DATarm.ipl[DATarm.flag==0]),np.arange(len(DATarm.ipl[DATarm.flag==0])),label=carm[2],linewidth=1.5)
#plt.plot(np.sort(DATles.ipl[DATles.flag==0]),np.arange(len(DATles.ipl[DATles.flag==0])),label=cles[2],linewidth=1.5)
##plt.plot(np.sort(DATlbi.ipl[DATlbi.flag==0]),np.arange(len(DATlbi.ipl[DATlbi.flag==0])),label=clbi[2],linewidth=1.5)
#plt.plot(np.sort(DATzue.ipl[DATzue.flag==0]),np.arange(len(DATzue.ipl[DATzue.flag==0])),label=czue[2],linewidth=1.5)
#plt.plot(np.sort(DATrcl.ipl[DATrcl.flag==0]),np.arange(len(DATrcl.ipl[DATrcl.flag==0])),label=crcl[2],linewidth=1.5)
#plt.plot(np.sort(DATtai.ipl[DATtai.flag==0]),np.arange(len(DATtai.ipl[DATtai.flag==0])),label=ctai[2],linewidth=1.5)
#plt.plot(np.sort(DATazt.ipl[DATazt.flag==0]),np.arange(len(DATazt.ipl[DATazt.flag==0])),label=cazt[2],linewidth=1.5)