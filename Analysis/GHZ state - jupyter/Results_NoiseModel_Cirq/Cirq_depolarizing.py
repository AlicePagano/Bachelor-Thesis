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
    
    m = 10 #number of application of amplitude damping
    gamma = 0.0013125 #parameters gamma of amplitude damping
    
    circuit.append(cirq.H(qubits[0]))

    for i in range(N-1):    
        circuit.append(cirq.CNOT(qubits[i],qubits[i+1]))
        if(string == 'Noise'): 
            if (i==0): 
                y=1
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i]))
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i+1]))
            if (i==1): 
                y=2
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i]))
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i+1]))
            if (i==2): 
                y=3
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i]))
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i+1]))
            if (i==3):
                y=4
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i]))
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i+1]))
        
        
    #insert U gate on all qubits
    phi = (pi*j)/(N+1)
    #A  unitary 1-qubit gate U 
    matrix=np.array([[1, 0], [0, np.exp(1.0j*phi)]])
    # matrix=np.array([[np.exp(-1.0j*phi), 1], [1, np.exp(1.0j*phi)]])
    moment_0 = cirq.Moment( cirq.SingleQubitMatrixGate(matrix).on(qubits[q]) for q in range(N) ) 
    # moment_0 = cirq.Moment( cirq.PhasedXPowGate().on(qubits[q]) for q in range(N) ) 
    circuit.append(moment_0)
    
    
    for i in reversed(range(N-1)):
        if(string == 'Noise'): 
            if (i==3): 
                y=5
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i]))
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i+1]))
            if (i==2): 
                y=6
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i]))
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i+1]))
            if (i==1): 
                y=7
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i]))
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i+1]))
            if (i==0): 
                y=8
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i]))
                for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[i+1]))
            circuit.append(cirq.CNOT(qubits[i],qubits[i+1]))


    y=9                
    for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[0]))
    for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[1]))
    for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[2]))
    for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[3]))
    for k in range(y*m): circuit.append(cirq.DepolarizingChannel(gamma).on(qubits[4]))
        
    circuit.append(cirq.H(qubits[0]))
        
    #measurement
    circuit.append(cirq.measure(*qubits, key='x'))      
        
        #print(circuit)
    
    return circuit




def simulation(circuit,string):

    if(string == 'NoNoise'):
            
        f = open("counts_NoNoise.txt","a+")
        simulator = cirq.Simulator()
        results = simulator.run(circuit, repetitions=shots)
        #results = simulator.simulate(circuit)
        #print(results.dirac_notation())
        h = results.histogram(key='x') 
        #print(results)
        print(1/shots*h[0])

        #f.write('{}'.format(1/shots*h[0]))
        #f.write(',')
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


        results = simulator.run(circuit, repetitions=shots)
        h = results.histogram(key='x')
        print(1/shots*h[0])
        f.write('{}'.format(1/shots*h[0]))
        f.write(',')
        f.close()


def main ():    

    for j in range(2*N+1+1):   # for j in range(2*N+1):
        print('Histogram j = {}'.format(j))
        #simulation(circuit(j, 'NoNoise'), 'NoNoise')
        simulation(circuit(j, 'Noise'), 'Noise')
        



if __name__ == '__main__':
    main()
