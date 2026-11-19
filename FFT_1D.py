# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:18:26 2026

@author: Bechara Aoun!
"""
import numpy as np
import matplotlib.pyplot as plt

fs=500
N=500 # 500/500=1 N/fs=duree de temps

f0=50 #le signal que je connais de 50hz

duree= N/fs #en seconde

t= np.arange(N) / fs # 0 1 2.... 499 /fs pour mesurer a chaque instant

x=np.sin(2*np.pi*f0*t) # 2pi c'est un tour *f0 c'est cb de tour / (t) seconde

plt.figure(figsize=(9,3))

plt.plot(t,x)


plt.xlabel("temps(s)")
plt.ylabel("amplitude")

plt.grid()
plt.show()


X= np.fft.fft(x) # centre de masse de l'enroullement * N de sin(2pif0t a chaque frequence)

print(X.dtype) #donne un nbr complexe vu que le cdm n'est pas seulement celon 1 val

module=np.abs(X/N)

plt.figure(figsize=(9, 3))
plt.plot(module)
plt.xlabel("numero de case k")
plt.ylabel("|X[k]|")
plt.grid()
plt.show()

freqs = np.fft.fftfreq(N, d=1/fs) 

plt.plot(np.fft.fftshift(freqs), np.fft.fftshift(module))


