
"""
Created on Sat Nov 14 15:51:39 2026

@author: Bechara Aoun
"""
import matplotlib.pyplot as plt
import numpy as np


rng=np.random.default_rng(35) # 35 pour fixer

tableau_blanc= rng.normal(0,1,size=(256,256)) #tab loi de gausse non borne

plt.figure(figsize=(7,7))

plt.imshow(tableau_blanc, cmap='gray')
