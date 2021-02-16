import cirq
import numpy as np
from math import pi
#from cirq.ops import gate_operation
from cirq.value import Duration

#libraries to plot histogram
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

#google
from cirq import circuits, ops, sim, study, protocols, optimizers
from cirq.google import convert_to_xmon_gates
from cirq import circuits, ops, sim, study, protocols
from cirq.google import xmon_device

from numpy import linalg as LA

shots=6000

# define the length of the grid.
length = 2

#number of qubits used
N = 2

# define qubits on the grid.
#qubits = [cirq.GridQubit(i, j) for i in range(1) for j in range(length)] #per circuitXMON solo!

qubits = cirq.LineQubit.range(N)

print(qubits)



def circuit(j,string):  
       
    circuit = cirq.Circuit()            
    
    #if(string == 'Noise'):
        #circuit.append(cirq.DepolarizingChannel(0.1).on_each(*qubits))
    
    gamma = j #parameters gamma of amplitude damping
    

    circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[1]))
    circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[1]))
    
    circuit.append(cirq.H(qubits[0]))

    circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[0]))
    
    circuit.append(cirq.CNOT(qubits[0],qubits[1]))

    circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[1]))
    
    return circuit




def simulation(circuit,string):
        
        f = open("counts_Noise.txt","a+")
    #Density simulator
        simulator = cirq.DensityMatrixSimulator()
        results = simulator.simulate(circuit,qubit_order = [qubits[0],qubits[1]]) #per accedere alla matrice densità
        g = results.final_density_matrix
        print(g)  #per accedere alla matrice densità
        print('\n')
        print(g.shape)
        print(g.ndim)
        print('\n')
        
        sigma = [[0, 0,0,-1], [0,0,1,0],[0,1,0,0],[-1,0,0,0]]
        
        print(g.real)
        
        R = np.dot(g.real,sigma)
        R = np.dot(sigma,R)
        
        R = np.dot(R,g.real)
        
        print(R)
        
        w,v = LA.eig(R)
        
        w = np.flip(np.sort(w))
        
        print(w)
        C = np.maximum(0,w[0]-w[1]-w[2]-w[3])
        
        print(C)
#        p00 = R[0,0].real
#        p01 = R[0,1].real
#        p02 = R[0,2].real
#        p03 = R[0,3].real
#
#        p10 = R[1,0].real
#        p11 = R[1,1].real
#        p12 = R[1,2].real
#        p13 = R[1,3].real
#
#        p20 = R[2,0].real
#        p21 = R[2,1].real
#        p22 = R[2,2].real
#        p23 = R[2,3].real
#
#        p30 = R[3,0].real
#        p31 = R[3,1].real
#        p32 = R[3,2].real
#        p33 = R[3,3].real

        
#        f.write('{{')
#        f.write('{},\t{},\t{},\t{}'.format(p00,p01,p02,p03))
#        f.write('},{')
#        f.write('{},\t{},\t{},\t{}'.format(p10,p11,p12,p13))
#        f.write('},{')
#        f.write('{},\t{},\t{},\t{}'.format(p20,p21,p22,p23))
#        f.write('},{')
#        f.write('{},\t{},\t{},\t{}'.format(p30,p31,p32,p33))
#        f.write('}}\n\n')

        f.write('{},'.format(C))
        f.close()


def main ():    

    for j in np.arange(0,1.01,0.01):   # for j in range(2*N+1):
        #simulation(circuit(j, 'NoNoise'), 'NoNoise')
        simulation(circuit(j, 'Noise'), 'Noise')
        



if __name__ == '__main__':
    main()
