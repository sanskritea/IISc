import numpy as np
from qutip import *

global pi
pi = np.pi

global wq, wm, a, g, dm, dq
wq = 2 * pi  * 6                     
wm = 2 * pi  * 6 * 1e-3     #1e-3 = MHz
dm = 2 * pi  * 100 * 1e-9   #1e-9 = Hz
dq = 2 * pi  * 200 * 1e-6   # 1e-6 = kHz
ah = 2 * pi  * 300 * 1e-3 
g =  2 * pi  * 0.001  * 1e-3


#print('Cooperativity = '+ str(g**2/dq/dm))
#print('Calculating...')

def solvit(Nq, Nm, nth, amp):
    # Operators
    global aq, am, Xq, Xm, numq, numm, Ident
    aq = tensor(destroy(Nq), qeye(Nm))      # qubit annihilation operator
    am = tensor(qeye(Nq), destroy(Nm))      # oscillator annihilation operator
    Xq = aq + aq.dag()      # qubit X
    Xm = am + am.dag()      # oscillator X
    numq = aq.dag() * aq    # qubit number operator
    numm = am.dag() * am    # oscillator number operator

    Hq = wm * numq - (ah * 0.5 * aq.dag() * aq.dag() * aq * aq)   # anharmonic qubit
    Hm = wm * numm                                  # bare oscillator
    Hqmz = g * numq * Xm                            # z-x coupling
    Hnet = Hq + Hm + Hqmz                           # time-independent hamiltonian
    Hd = amp * 2 * pi * Xq                          # qubit drive
    qcol = np.sqrt(dq) * aq                         # qubit state leakage
    bathp = np.sqrt(dm * (nth+1)) * am              # bath decrement
    bathm = np.sqrt(dm * nth) * am.dag()            # bath increment
    cops = [qcol, bathm, bathp]     # collapse operator
    H = Hnet + Hd
   # print('computing using ', amp)

    soln = steadystate(H, cops, tol=1e-13)
    mstate = expect(numm, soln)
   # qstate = expect(numq, soln)
    return mstate#, qstate
