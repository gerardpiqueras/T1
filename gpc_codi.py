"""
Gerard Piqueras Codina
Tarea T1 APA
"""
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
from numpy.fft import fft     # Importem la funció fft
pi=np.pi  

#Exercici 1
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=4000                             # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide                         
plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 
sd.play(x, fm) 

N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(111)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(112)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics


#Exercici 2
x_r, fm = sf.read('so_exemple1.wav')

plt.figure(2)                             # Nova figura
plt.plot(t[0:Ls], x_r[0:Ls])              # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show() 

N=5000                                    # Dimensió de la transformada discreta
X=fft(x_r[0 : Ls], N)                       # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                            # Vector amb els valors 0≤  k<N

plt.figure(3)                         # Nova figura
plt.subplot(311)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics


#Exercici 3

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
N=5000                               # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)                  # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                       # Vector amb els valors 0≤  k<N

plt.figure(4)                    
x_db=20*np.log10(np.abs(X)/max(np.abs(X)))
f_k = (k[0:N//2+1]/N)*fm
plt.subplot(411)                     
plt.plot(f_k, x_db[0:N//2+1])                 
plt.title(f'Mòdul de la Transformada de Fourier en dB')   
plt.ylabel('db')   
plt.show()      


#Exercici 4
x_raphael, fm = sf.read('RaphaelMigrannoche.wav')

T = 0.025 # 25ms
L=int(fm*T) 
Tm=1/fm 
t=Tm*np.arange(L)
plt.figure(5)  
plt.plot(t[0:L],x_raphael[0:L])
plt.title(f'Mi gran noche') 
plt.xlabel('temps')      
plt.show()

print('La freqüència de mostratge es: ', fm)
print('El nombre de mostres de la senyal es: ', L)
