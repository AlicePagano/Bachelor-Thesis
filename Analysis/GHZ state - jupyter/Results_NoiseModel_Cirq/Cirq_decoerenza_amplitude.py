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

shots=6000

# define the length of the grid.
length = 5

#number of qubits used
N = 5

# define qubits on the grid.
#qubits = [cirq.GridQubit(i, j) for i in range(1) for j in range(length)] #per circuitXMON solo!

qubits = cirq.LineQubit.range(N)

print(qubits)

def circuit(j,string):
    
    circuit = cirq.Circuit()
    
    #if(string == 'Noise'):
    #circuit.append(cirq.DepolarizingChannel(0.1).on_each(*qubits))
    
    gamma = j #parameters gamma of amplitude damping
    
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[2]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[2]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[2]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[3]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[3]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[3]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[3]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[4]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[4]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[4]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[4]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[4]))
    
    circuit.append(cirq.H(qubits[0]))
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    
    circuit.append(cirq.CNOT(qubits[0],qubits[1]))
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    
    circuit.append(cirq.CNOT(qubits[1],qubits[2]))
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[2]))
    
    circuit.append(cirq.CNOT(qubits[2],qubits[3]))
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[2]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[2]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[3]))
    
    circuit.append(cirq.CNOT(qubits[3],qubits[4]))
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[3]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[4]))
    
    #print(circuit)
    
    return circuit




def simulation(circuit,string):

    if(string == 'NoNoise'):
            
        f = open("counts_NoNoise.txt","a+")
        simulator = cirq.DensityMatrixSimulator()
        results = simulator.simulate(circuit, qubit_order = [qubits[0],qubits[1],qubits[2],qubits[3],qubits[4]]) #per accedere alla matrice densità
        g = results.final_density_matrix
#        print(np.around(g, 3))  #per accedere alla matrice densità
        print(g)  #per accedere alla matrice densità
        print('\n')
        print(g.shape)
        print(g.ndim)
        print('\n')
        p00 = g[0,0].real
        p0N = g[0,31].real
        pN0 = g[31,0].real
        pNN = g[31,31].real
        
        f.write('{}\t{}\t{}\t{}\n'.format(p00,p0N,pN0,pNN))
        f.close()
        
    if(string == 'Noise'):
        
        f = open("counts_Noise.txt","a+")
    #Density simulator
        simulator = cirq.DensityMatrixSimulator()
        
#        pp = []
#
#        for k in range(8):
#            results = simulator.run(circuit, repetitions=shots)
#            h = results.histogram(key='x')
#            pp.append(1/shots*h[0])
#            f.write('{}'.format(1/shots*h[0]))
#
#        pp = np.array(pp)
#        std = np.std(pp, axis=0)
#        f.write(',')
#        f.close()
#
#        gg = open("std_Noise.txt","a+")
#        gg.write('{}'.format(std))
#        gg.write(',')
#        gg.close()


        results = simulator.simulate(circuit,qubit_order = [qubits[0],qubits[1],qubits[2],qubits[3],qubits[4]]) #per accedere alla matrice densità
        g = results.final_density_matrix
        print(np.around(g, 3))  #per accedere alla matrice densità
        print('\n')
        print(g.shape)
        print(g.ndim)
        print('\n')
        p00 = g[0,0].real
        p0N = g[0,31].real
        pN0 = g[31,0].real
        pNN = g[31,31].real
    
        f.write('{},\t{},\t{},\t{},\n'.format(p00,p0N,pN0,pNN))
        f.close()


def main ():    

    for j in np.arange(0,0.04,0.001):   # for j in range(2*N+1):
        #simulation(circuit(j, 'NoNoise'), 'NoNoise')
        simulation(circuit(j, 'Noise'), 'Noise')
        



if __name__ == '__main__':
    main()
