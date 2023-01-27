# -*- coding: utf-8 -*-
"""
Created on Fri May 27 16:40:44 2022

@author: n.patsalidis
"""


import sys
from matplotlib import pyplot as plt

sys.path.insert(0, '/Users/n.patsalidis/Desktop/PHD/REPOSITORIES/MDanalysis')

import md_analysis as mda  
import numpy as np
##### Setup ####



trajf = '../trr/PRwhbench.trr'
conftype = 'zdir'
binl=0.025 ; dmax =5 
results = mda.Analysis_Confined(trajf,['../itp/topol_UA_PB30.itp','../itp/alu_to.itp'],
                        conftype, 
                        topol_file ='../gro/alupb.gro',
                        particle='ALU',polymer='PB')

topol_vector = 4 # gets all 1-4 vectors
conf = 'free'
results.read_file()


P2 = results.calc_P2(binl,dmax,topol_vector,option=conf,dads=1.025)

figsize=(3.3,3.3)
dpi=300
fig =plt.figure(figsize=figsize,dpi=dpi)
plt.title(conf)
plt.minorticks_on()
plt.tick_params(direction='in', which='minor',length=5)
plt.tick_params(direction='in', which='major',length=10)
plt.xlim([0,dmax])

plt.plot(P2['d'],P2['P2'],
        ls='none',marker='o',fillstyle='none',
        markersize=4,color='k',lw=1.5)

plt.xlabel(r'd $(nm)$')
plt.ylabel(r'$P_2(\theta)$')
plt.legend(frameon=False)
plt.savefig('P2_{}.png'.format(conf),bbox_inches='tight')
plt.show()