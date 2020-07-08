import matplotlib
matplotlib.use('Agg')
import multiprocessing as mp
pool = mp.Pool(mp.cpu_count())
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from qutip import *
import time
from testfun import solvit

start = time.time()

global pi
pi = np.pi 

global Nq, Nm, nth
Nq = 10		#qubits states
Nm = 50		#oscillator states
nth = 0.05	#initial thermal occupation
val = 11    #number of plot points
rAmp = np.logspace(-6, -1, val)   # drive amplitude in GHz units
x = [pool.apply(solvit, args=(Nq, Nm, nth, A)) for A in rAmp]
idname = 'Marios_g=0.001MHz_'+ str(Nq) +'_' + str(Nm) +'_' + str(val)
filname = idname + '_.txt'
np.savetxt(filname, x, delimiter='\n')

tfilname = 'Time_' + filname
end = time.time()
tt = str(end - start)
f = open(tfilname, "w+")
f.write(tt)
f.close()

fig, ax = plt.subplots()
ax.plot(rAmp, x)
ax.set_xscale('log')
ax.set_xlabel("Drive amplitude")
ax.set_ylabel("Oscillator steady state occupation")
plt.grid()
figname='/home/vibhor/' + idname + '_.png'
plt.savefig(figname)
