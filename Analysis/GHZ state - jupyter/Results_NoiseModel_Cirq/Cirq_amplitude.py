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

shots=12000

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
    
    gamma = 0.12 #parameters gamma of amplitude damping
    
    
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
        
    #insert U gate on all qubits
    phi = (pi*j)/(N+1)
    #A  unitary 1-qubit gate U 
    matrix=np.array([[1, 0], [0, np.exp(1.0j*phi)]])
    # matrix=np.array([[np.exp(-1.0j*phi), 1], [1, np.exp(1.0j*phi)]])
    moment_0 = cirq.Moment( cirq.SingleQubitMatrixGate(matrix).on(qubits[q]) for q in range(N) ) 
    # moment_0 = cirq.Moment( cirq.PhasedXPowGate().on(qubits[q]) for q in range(N) ) 
    circuit.append(moment_0)
    
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[3]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[4]))
    
    circuit.append(cirq.CNOT(qubits[3],qubits[4]))
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[2]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[2]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[3]))
    
    circuit.append(cirq.CNOT(qubits[2],qubits[3]))
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[2]))
    
    circuit.append(cirq.CNOT(qubits[1],qubits[2]))
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[1]))
    
    circuit.append(cirq.CNOT(qubits[0],qubits[1]))
    
    circuit.append(cirq.AmplitudeDampingChannel(gamma).on(qubits[0]))
    
    circuit.append(cirq.H(qubits[0]))
    
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
    
        
    #measurement
    circuit.append(cirq.measure(*qubits, key='x'))      
        
    #print(circuit)
    
    return circuit




def simulation(circuit,string,j):

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

        if ( j== 2*N+1):
            f.write('\n\n')
        
        f.close()
def main ():    

    for j in range(2*N+1+1):   # for j in range(2*N+1):
        print('Histogram j = {}'.format(j))
        #simulation(circuit(j, 'NoNoise'), 'NoNoise')
        simulation(circuit(j, 'Noise'), 'Noise',j)
        



if __name__ == '__main__':
    main()
