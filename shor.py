import sys
sys.path.append('qiskit-sdk-py-master')

from qiskit import QuantumProgram
from math import*
from qiskit.tools.visualization import plot_histogram


#####################COMO USAR AS DIFERENTES GATES######################

    #.x(qr[0])      #applying  x gate to the first qubit
    #.y(qr[0])      #applying  y gate to the first qubit
    #.z(qr[0])      #applying  z gate to the first qubit
    #.iden(qr[0])       #identity gate on the first qubit
    #.u1(lambd, qr[0])      #applying a u1 gate to the first qubit
    #.u2(phi, lambd, qr[0])         #applying a u2 gate to the first qubit
    #.u3(theta, phi, lambd, qr[0])      #applying a u3 gate to the first qubit
    #.h(qr[0])      #applying h gate to the first qubit
    #.s(qr[0])      #applying s gate to the first qubit
    #.sdg(qr[0])        #applying sdg gate to the first qubit
    #.t(qr[0])      #applying t gate to the first qubit
    #.tdg(qr[0])        #applying tdg gate to the first qubit
    #.rx(theta, qr[0])      #applying rotation around x-axis gate to the first qubit
    #.ry(theta, qr[0])      #applying rotation around y-axis gate to the first qubit
    #.rz(phi, qr[0])        #applying rotation around z-axis gate to the first qubit
    #.cx(qr[0], qr[1])      #applying cnot gate (do 1 para o 0 (testar melhor...))
    #.cy(qr[0], qr[1])      #controlled-y
    #.cz(qr[0], qr[1])      #controlled-z
    #.ch(qr[0], qr[1])      #controlled-h
    #.crz(lambd, qr[0], qr[1])      #controlled rotation around-Z
    #.cu1(lambd, qr[0], qr[1])      #controlled u1
    #.cu3(theta, phi, lambd, qr[0], qr[1])      #controlled u3
    #.swap(qr[0], qr[1])        #swapping the first and second qubits
    #.ccx(qr[0], qr[1], qr[2])        #Toffoli gate
    #.cswap(qr[0], qr[1], qr[2])        #swapping the second and third qubits controlled by the first qubit

def sh(g):
    Q_program = QuantumProgram()
    qr = Q_program.create_quantum_register("qr", 12)
    cr = Q_program.create_classical_register("cr", 12)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #x (0,1)
    #y (2,3,4,5,6)
    #b///adder (7,8,9,10,11)
    # auxiliar (12)

    #a=4  = 0 1 0 0
    #N=15 = 1 1 1 1


    #a %N = 4*a**2 =      4 = 0 1 0 0
    #2*a %N =             8 = 1 0 0 0
    #4*a %N == a**2 %N =  1 = 0 0 0 1
    #2*a**2 %N =          2 = 0 0 1 0

    #########fases
    ###N

    #u2+u3+u4+u5 = 15*pi/16
    #u1+u2+u3+u4 = 15*pi/8
    #u1+u2+u3 = 7*pi/4
    #u1+u2 = 3*pi/2
    #u1 = pi

    ###a
    #u3 = pi/4
    #u2 = pi/2
    #u1 = pi



    ###############begin###########
    #entradas
    qc.h(qr[0])
    qc.h(qr[1])
    #qc.x(qr[0])
    #qc.x(qr[1])
    qc.x(qr[2])



    ########qft5 (7-11)

    qc.h(qr[11])

    qc.u1(pi/4, qr[11]) 
    qc.cx(qr[10], qr[11])
    qc.u1(pi/4, qr[10])
    qc.u1(-pi/4, qr[11])
    qc.cx(qr[10], qr[11])

    qc.u1(pi/8, qr[11])
    qc.cx(qr[9], qr[11])
    qc.u1(pi/8, qr[9])
    qc.u1(-pi/8, qr[11])
    qc.cx(qr[9], qr[11])

    qc.u1(pi/16, qr[11])
    qc.cx(qr[8], qr[11])
    qc.u1(pi/16, qr[8])
    qc.u1(-pi/16, qr[11])
    qc.cx(qr[8], qr[11])

    qc.u1(pi/32, qr[11])
    qc.cx(qr[7], qr[11])
    qc.u1(pi/32, qr[7])
    qc.u1(-pi/32, qr[11])
    qc.cx(qr[7], qr[11])

    qc.h(qr[10])

    qc.u1(pi/4, qr[10])
    qc.cx(qr[9], qr[10])
    qc.u1(pi/4, qr[9])
    qc.u1(-pi/4, qr[10])
    qc.cx(qr[9], qr[10])

    qc.u1(pi/8, qr[10]) 
    qc.cx(qr[8], qr[10])
    qc.u1(pi/8, qr[8])
    qc.u1(-pi/8, qr[10])
    qc.cx(qr[8], qr[10])

    qc.u1(pi/16, qr[10]) 
    qc.cx(qr[7], qr[10])
    qc.u1(pi/16, qr[7])
    qc.u1(-pi/16, qr[10])
    qc.cx(qr[7], qr[10])


    qc.h(qr[9])

    qc.u1(pi/4, qr[9])
    qc.cx(qr[8], qr[9])
    qc.u1(pi/4, qr[8])
    qc.u1(-pi/4, qr[9])
    qc.cx(qr[8], qr[9])

    qc.u1(pi/8, qr[9]) 
    qc.cx(qr[7], qr[9])
    qc.u1(pi/8, qr[7])
    qc.u1(-pi/8, qr[9])
    qc.cx(qr[7], qr[9])


    qc.h(qr[8]) 

    qc.u1(pi/4, qr[8])
    qc.cx(qr[7], qr[8])
    qc.u1(pi/4, qr[7])
    qc.u1(-pi/4, qr[8])
    qc.cx(qr[7], qr[8])

    qc.h(qr[7]) 

    qc.swap(qr[11], qr[7])
    qc.swap(qr[10], qr[8])
    ##########################################
    #add a mod N controlado em 0 e 2
    #qc.u1(pi/4, qr[7])
    #qc.u1(pi/2, qr[8])
    #qc.u1(pi, qr[9])


    qc.u1(pi/8, qr[7])
    qc.ccx(qr[0], qr[2], qr[7])
    qc.u1(pi/8, qr[2])
    qc.u1(pi/8, qr[0])
    qc.u1(-pi/8, qr[7])
    qc.ccx(qr[0], qr[2], qr[7])


    qc.u1(pi/4, qr[8])
    qc.ccx(qr[0], qr[2], qr[8])
    qc.u1(pi/4, qr[2])
    qc.u1(pi/4, qr[0])
    qc.u1(-pi/4, qr[8])
    qc.ccx(qr[0], qr[2], qr[8])


    qc.u1(pi/2, qr[9])
    qc.ccx(qr[0], qr[2], qr[9])
    qc.u1(pi/2, qr[2])
    qc.u1(pi/2, qr[0])
    qc.u1(-pi/2, qr[9])
    qc.ccx(qr[0], qr[2], qr[9])

 
    ##########################################
    ###invqft5
    qc.swap(qr[11], qr[7])
    qc.swap(qr[10], qr[8])

    qc.h(qr[7])

    qc.u1(-pi/4, qr[8])
    qc.cx(qr[7], qr[8])
    qc.u1(-pi/4, qr[7])
    qc.u1(pi/4, qr[8])
    qc.cx(qr[7], qr[8])

    qc.h(qr[8])

    qc.u1(-pi/8, qr[9]) 
    qc.cx(qr[7], qr[9])
    qc.u1(-pi/8, qr[7])
    qc.u1(pi/8, qr[9])
    qc.cx(qr[7], qr[9])

    qc.u1(-pi/4, qr[9])
    qc.cx(qr[8], qr[9])
    qc.u1(-pi/4, qr[8])
    qc.u1(pi/4, qr[9])
    qc.cx(qr[8], qr[9])

    qc.h(qr[9])

    qc.u1(-pi/16, qr[10]) 
    qc.cx(qr[7], qr[10])
    qc.u1(-pi/16, qr[7])
    qc.u1(pi/16, qr[10])
    qc.cx(qr[7], qr[10])

    qc.u1(-pi/8, qr[10]) 
    qc.cx(qr[8], qr[10])
    qc.u1(-pi/8, qr[8])
    qc.u1(pi/8, qr[10])
    qc.cx(qr[8], qr[10])

    qc.u1(-pi/4, qr[10])
    qc.cx(qr[9], qr[10])
    qc.u1(-pi/4, qr[9])
    qc.u1(pi/4, qr[10])
    qc.cx(qr[9], qr[10])

    qc.h(qr[10])

    qc.u1(-pi/32, qr[11])
    qc.cx(qr[7], qr[11])
    qc.u1(-pi/32, qr[7])
    qc.u1(pi/32, qr[11])
    qc.cx(qr[7], qr[11])

    qc.u1(-pi/16, qr[11])
    qc.cx(qr[8], qr[11])
    qc.u1(-pi/16, qr[8])
    qc.u1(pi/16, qr[11])
    qc.cx(qr[8], qr[11])

    qc.u1(-pi/8, qr[11])
    qc.cx(qr[9], qr[11])
    qc.u1(-pi/8, qr[9])
    qc.u1(pi/8, qr[11])
    qc.cx(qr[9], qr[11])

    qc.u1(-pi/4, qr[11]) 
    qc.cx(qr[10], qr[11])
    qc.u1(-pi/4, qr[10])
    qc.u1(pi/4, qr[11])
    qc.cx(qr[10], qr[11])

    qc.h(qr[11])

 
    ################################
    #swap controlado
    qc.ccx(qr[0], qr[2], qr[7])
    qc.ccx(qr[0], qr[7], qr[2])
    qc.ccx(qr[0], qr[2], qr[7])

    qc.ccx(qr[0], qr[3], qr[8])
    qc.ccx(qr[0], qr[8], qr[3])
    qc.ccx(qr[0], qr[3], qr[8])

    qc.ccx(qr[0], qr[4], qr[9])
    qc.ccx(qr[0], qr[9], qr[4])
    qc.ccx(qr[0], qr[4], qr[9])

    qc.ccx(qr[0], qr[5], qr[10])
    qc.ccx(qr[0], qr[10], qr[5])
    qc.ccx(qr[0], qr[5], qr[10])

    qc.ccx(qr[0], qr[6], qr[11])
    qc.ccx(qr[0], qr[11], qr[6])
    qc.ccx(qr[0], qr[6], qr[11])

    ################################
    
    #cnot em 7
    qc.cx(qr[0], qr[7])

    ################################

    ########qft5 (7-11)

    qc.h(qr[11])

    qc.u1(pi/4, qr[11]) 
    qc.cx(qr[10], qr[11])
    qc.u1(pi/4, qr[10])
    qc.u1(-pi/4, qr[11])
    qc.cx(qr[10], qr[11])

    qc.u1(pi/8, qr[11])
    qc.cx(qr[9], qr[11])
    qc.u1(pi/8, qr[9])
    qc.u1(-pi/8, qr[11])
    qc.cx(qr[9], qr[11])

    qc.u1(pi/16, qr[11])
    qc.cx(qr[8], qr[11])
    qc.u1(pi/16, qr[8])
    qc.u1(-pi/16, qr[11])
    qc.cx(qr[8], qr[11])

    qc.u1(pi/32, qr[11])
    qc.cx(qr[7], qr[11])
    qc.u1(pi/32, qr[7])
    qc.u1(-pi/32, qr[11])
    qc.cx(qr[7], qr[11])

    qc.h(qr[10])

    qc.u1(pi/4, qr[10])
    qc.cx(qr[9], qr[10])
    qc.u1(pi/4, qr[9])
    qc.u1(-pi/4, qr[10])
    qc.cx(qr[9], qr[10])

    qc.u1(pi/8, qr[10]) 
    qc.cx(qr[8], qr[10])
    qc.u1(pi/8, qr[8])
    qc.u1(-pi/8, qr[10])
    qc.cx(qr[8], qr[10])

    qc.u1(pi/16, qr[10]) 
    qc.cx(qr[7], qr[10])
    qc.u1(pi/16, qr[7])
    qc.u1(-pi/16, qr[10])
    qc.cx(qr[7], qr[10])


    qc.h(qr[9])

    qc.u1(pi/4, qr[9])
    qc.cx(qr[8], qr[9])
    qc.u1(pi/4, qr[8])
    qc.u1(-pi/4, qr[9])
    qc.cx(qr[8], qr[9])

    qc.u1(pi/8, qr[9]) 
    qc.cx(qr[7], qr[9])
    qc.u1(pi/8, qr[7])
    qc.u1(-pi/8, qr[9])
    qc.cx(qr[7], qr[9])


    qc.h(qr[8]) 

    qc.u1(pi/4, qr[8])
    qc.cx(qr[7], qr[8])
    qc.u1(pi/4, qr[7])
    qc.u1(-pi/4, qr[8])
    qc.cx(qr[7], qr[8])

    qc.h(qr[7]) 

    qc.swap(qr[11], qr[7])
    qc.swap(qr[10], qr[8])


    #######################################

    #add a**2%N=1
    #qc.u1(pi/16, qr[7])
    #qc.u1(pi/8, qr[8])
    #qc.u1(pi/4, qr[9])
    #qc.u1(pi/2, qr[10])
    #qc.u1(pi, qr[11])

    qc.u1(pi/32, qr[7])
    qc.ccx(qr[1], qr[2], qr[7])
    qc.u1(pi/32, qr[2])
    qc.u1(pi/32, qr[1])
    qc.u1(-pi/32, qr[7])
    qc.ccx(qr[1], qr[2], qr[7])


    qc.u1(pi/16, qr[8])
    qc.ccx(qr[1], qr[2], qr[8])
    qc.u1(pi/16, qr[2])
    qc.u1(pi/16, qr[1])
    qc.u1(-pi/16, qr[8])
    qc.ccx(qr[1], qr[2], qr[8])


    qc.u1(pi/8, qr[9])
    qc.ccx(qr[1], qr[2], qr[9])
    qc.u1(pi/8, qr[2])
    qc.u1(pi/8, qr[1])
    qc.u1(-pi/8, qr[9])
    qc.ccx(qr[1], qr[2], qr[9])


    qc.u1(pi/4, qr[10])
    qc.ccx(qr[1], qr[2], qr[10])
    qc.u1(pi/4, qr[2])
    qc.u1(pi/4, qr[1])
    qc.u1(-pi/4, qr[10])
    qc.ccx(qr[1], qr[2], qr[10])

    qc.u1(pi/2, qr[11])
    qc.ccx(qr[1], qr[2], qr[11])
    qc.u1(pi/2, qr[2])
    qc.u1(pi/2, qr[1])
    qc.u1(-pi/2, qr[11])
    qc.ccx(qr[1], qr[2], qr[11])

    #add 2a**2 modN

    #add 4a**2 modN = 4
    #qc.u1(pi/4, qr[7])
    #qc.u1(pi/2, qr[8])
    #qc.u1(pi, qr[9])

    qc.u1(pi/8, qr[7])
    qc.ccx(qr[1], qr[4], qr[7])
    qc.u1(pi/8, qr[4])
    qc.u1(pi/8, qr[1])
    qc.u1(-pi/8, qr[7])
    qc.ccx(qr[1], qr[4], qr[7])

    qc.u1(pi/4, qr[8])
    qc.ccx(qr[1], qr[4], qr[8])
    qc.u1(pi/4, qr[4])
    qc.u1(pi/4, qr[1])
    qc.u1(-pi/4, qr[8])
    qc.ccx(qr[1], qr[4], qr[8])

    qc.u1(pi/2, qr[9])
    qc.ccx(qr[1], qr[4], qr[9])
    qc.u1(pi/2, qr[4])
    qc.u1(pi/2, qr[1])
    qc.u1(-pi/2, qr[9])
    qc.ccx(qr[1], qr[4], qr[9])


    ##########################################

    ###invqft5
    qc.swap(qr[11], qr[7])
    qc.swap(qr[10], qr[8])

    qc.h(qr[7])

    qc.u1(-pi/4, qr[8])
    qc.cx(qr[7], qr[8])
    qc.u1(-pi/4, qr[7])
    qc.u1(pi/4, qr[8])
    qc.cx(qr[7], qr[8])

    qc.h(qr[8])

    qc.u1(-pi/8, qr[9]) 
    qc.cx(qr[7], qr[9])
    qc.u1(-pi/8, qr[7])
    qc.u1(pi/8, qr[9])
    qc.cx(qr[7], qr[9])

    qc.u1(-pi/4, qr[9])
    qc.cx(qr[8], qr[9])
    qc.u1(-pi/4, qr[8])
    qc.u1(pi/4, qr[9])
    qc.cx(qr[8], qr[9])

    qc.h(qr[9])

    qc.u1(-pi/16, qr[10]) 
    qc.cx(qr[7], qr[10])
    qc.u1(-pi/16, qr[7])
    qc.u1(pi/16, qr[10])
    qc.cx(qr[7], qr[10])

    qc.u1(-pi/8, qr[10]) 
    qc.cx(qr[8], qr[10])
    qc.u1(-pi/8, qr[8])
    qc.u1(pi/8, qr[10])
    qc.cx(qr[8], qr[10])

    qc.u1(-pi/4, qr[10])
    qc.cx(qr[9], qr[10])
    qc.u1(-pi/4, qr[9])
    qc.u1(pi/4, qr[10])
    qc.cx(qr[9], qr[10])

    qc.h(qr[10])

    qc.u1(-pi/32, qr[11])
    qc.cx(qr[7], qr[11])
    qc.u1(-pi/32, qr[7])
    qc.u1(pi/32, qr[11])
    qc.cx(qr[7], qr[11])

    qc.u1(-pi/16, qr[11])
    qc.cx(qr[8], qr[11])
    qc.u1(-pi/16, qr[8])
    qc.u1(pi/16, qr[11])
    qc.cx(qr[8], qr[11])

    qc.u1(-pi/8, qr[11])
    qc.cx(qr[9], qr[11])
    qc.u1(-pi/8, qr[9])
    qc.u1(pi/8, qr[11])
    qc.cx(qr[9], qr[11])

    qc.u1(-pi/4, qr[11]) 
    qc.cx(qr[10], qr[11])
    qc.u1(-pi/4, qr[10])
    qc.u1(pi/4, qr[11])
    qc.cx(qr[10], qr[11])

    qc.h(qr[11])

    ################################
    #swap controlado
    qc.ccx(qr[1], qr[2], qr[7])
    qc.ccx(qr[1], qr[7], qr[2])
    qc.ccx(qr[1], qr[2], qr[7])

    qc.ccx(qr[1], qr[3], qr[8])
    qc.ccx(qr[1], qr[8], qr[3])
    qc.ccx(qr[1], qr[3], qr[8])

    qc.ccx(qr[1], qr[4], qr[9])
    qc.ccx(qr[1], qr[9], qr[4])
    qc.ccx(qr[1], qr[4], qr[9])

    qc.ccx(qr[1], qr[5], qr[10])
    qc.ccx(qr[1], qr[10], qr[5])
    qc.ccx(qr[1], qr[5], qr[10])

    qc.ccx(qr[1], qr[6], qr[11])
    qc.ccx(qr[1], qr[11], qr[6])
    qc.ccx(qr[1], qr[6], qr[11])

    ################################
    ########qft5 (7-11)

    qc.h(qr[11])

    qc.u1(pi/4, qr[11]) 
    qc.cx(qr[10], qr[11])
    qc.u1(pi/4, qr[10])
    qc.u1(-pi/4, qr[11])
    qc.cx(qr[10], qr[11])

    qc.u1(pi/8, qr[11])
    qc.cx(qr[9], qr[11])
    qc.u1(pi/8, qr[9])
    qc.u1(-pi/8, qr[11])
    qc.cx(qr[9], qr[11])

    qc.u1(pi/16, qr[11])
    qc.cx(qr[8], qr[11])
    qc.u1(pi/16, qr[8])
    qc.u1(-pi/16, qr[11])
    qc.cx(qr[8], qr[11])

    qc.u1(pi/32, qr[11])
    qc.cx(qr[7], qr[11])
    qc.u1(pi/32, qr[7])
    qc.u1(-pi/32, qr[11])
    qc.cx(qr[7], qr[11])

    qc.h(qr[10])

    qc.u1(pi/4, qr[10])
    qc.cx(qr[9], qr[10])
    qc.u1(pi/4, qr[9])
    qc.u1(-pi/4, qr[10])
    qc.cx(qr[9], qr[10])

    qc.u1(pi/8, qr[10]) 
    qc.cx(qr[8], qr[10])
    qc.u1(pi/8, qr[8])
    qc.u1(-pi/8, qr[10])
    qc.cx(qr[8], qr[10])

    qc.u1(pi/16, qr[10]) 
    qc.cx(qr[7], qr[10])
    qc.u1(pi/16, qr[7])
    qc.u1(-pi/16, qr[10])
    qc.cx(qr[7], qr[10])


    qc.h(qr[9])

    qc.u1(pi/4, qr[9])
    qc.cx(qr[8], qr[9])
    qc.u1(pi/4, qr[8])
    qc.u1(-pi/4, qr[9])
    qc.cx(qr[8], qr[9])

    qc.u1(pi/8, qr[9]) 
    qc.cx(qr[7], qr[9])
    qc.u1(pi/8, qr[7])
    qc.u1(-pi/8, qr[9])
    qc.cx(qr[7], qr[9])


    qc.h(qr[8]) 

    qc.u1(pi/4, qr[8])
    qc.cx(qr[7], qr[8])
    qc.u1(pi/4, qr[7])
    qc.u1(-pi/4, qr[8])
    qc.cx(qr[7], qr[8])

    qc.h(qr[7]) 

    qc.swap(qr[11], qr[7])
    qc.swap(qr[10], qr[8])


    ################################
    #add a**2%N=1
    #qc.u1(pi/16, qr[7])
    #qc.u1(pi/8, qr[8])
    #qc.u1(pi/4, qr[9])
    #qc.u1(pi/2, qr[10])
    #qc.u1(pi, qr[11])

    qc.u1(-pi/32, qr[7])
    qc.ccx(qr[1], qr[2], qr[7])
    qc.u1(-pi/32, qr[2])
    qc.u1(-pi/32, qr[1])
    qc.u1(pi/32, qr[7])
    qc.ccx(qr[1], qr[2], qr[7])


    qc.u1(-pi/16, qr[8])
    qc.ccx(qr[1], qr[2], qr[8])
    qc.u1(-pi/16, qr[2])
    qc.u1(-pi/16, qr[1])
    qc.u1(pi/16, qr[8])
    qc.ccx(qr[1], qr[2], qr[8])


    qc.u1(-pi/8, qr[9])
    qc.ccx(qr[1], qr[2], qr[9])
    qc.u1(-pi/8, qr[2])
    qc.u1(-pi/8, qr[1])
    qc.u1(pi/8, qr[9])
    qc.ccx(qr[1], qr[2], qr[9])


    qc.u1(-pi/4, qr[10])
    qc.ccx(qr[1], qr[2], qr[10])
    qc.u1(-pi/4, qr[2])
    qc.u1(-pi/4, qr[1])
    qc.u1(pi/4, qr[10])
    qc.ccx(qr[1], qr[2], qr[10])

    qc.u1(-pi/2, qr[11])
    qc.ccx(qr[1], qr[2], qr[11])
    qc.u1(-pi/2, qr[2])
    qc.u1(-pi/2, qr[1])
    qc.u1(pi/2, qr[11])
    qc.ccx(qr[1], qr[2], qr[11])


    ################################
    #sub a mod N controlado em 1 e 4
    #qc.u1(pi/4, qr[7])
    #qc.u1(pi/2, qr[8])
    #qc.u1(pi, qr[9])


    qc.u1(-pi/8, qr[7])
    qc.ccx(qr[1], qr[4], qr[7])
    qc.u1(-pi/8, qr[4])
    qc.u1(-pi/8, qr[1])
    qc.u1(pi/8, qr[7])
    qc.ccx(qr[1], qr[4], qr[7])


    qc.u1(-pi/4, qr[8])
    qc.ccx(qr[1], qr[4], qr[8])
    qc.u1(-pi/4, qr[4])
    qc.u1(-pi/4, qr[1])
    qc.u1(pi/4, qr[8])
    qc.ccx(qr[1], qr[4], qr[8])


    qc.u1(-pi/2, qr[9])
    qc.ccx(qr[1], qr[4], qr[9])
    qc.u1(-pi/2, qr[4])
    qc.u1(-pi/2, qr[1])
    qc.u1(pi/2, qr[9])
    qc.ccx(qr[1], qr[4], qr[9])

    ################################
    ###invqft5
    qc.swap(qr[11], qr[7])
    qc.swap(qr[10], qr[8])

    qc.h(qr[7])

    qc.u1(-pi/4, qr[8])
    qc.cx(qr[7], qr[8])
    qc.u1(-pi/4, qr[7])
    qc.u1(pi/4, qr[8])
    qc.cx(qr[7], qr[8])

    qc.h(qr[8])

    qc.u1(-pi/8, qr[9]) 
    qc.cx(qr[7], qr[9])
    qc.u1(-pi/8, qr[7])
    qc.u1(pi/8, qr[9])
    qc.cx(qr[7], qr[9])

    qc.u1(-pi/4, qr[9])
    qc.cx(qr[8], qr[9])
    qc.u1(-pi/4, qr[8])
    qc.u1(pi/4, qr[9])
    qc.cx(qr[8], qr[9])

    qc.h(qr[9])

    qc.u1(-pi/16, qr[10]) 
    qc.cx(qr[7], qr[10])
    qc.u1(-pi/16, qr[7])
    qc.u1(pi/16, qr[10])
    qc.cx(qr[7], qr[10])

    qc.u1(-pi/8, qr[10]) 
    qc.cx(qr[8], qr[10])
    qc.u1(-pi/8, qr[8])
    qc.u1(pi/8, qr[10])
    qc.cx(qr[8], qr[10])

    qc.u1(-pi/4, qr[10])
    qc.cx(qr[9], qr[10])
    qc.u1(-pi/4, qr[9])
    qc.u1(pi/4, qr[10])
    qc.cx(qr[9], qr[10])

    qc.h(qr[10])

    qc.u1(-pi/32, qr[11])
    qc.cx(qr[7], qr[11])
    qc.u1(-pi/32, qr[7])
    qc.u1(pi/32, qr[11])
    qc.cx(qr[7], qr[11])

    qc.u1(-pi/16, qr[11])
    qc.cx(qr[8], qr[11])
    qc.u1(-pi/16, qr[8])
    qc.u1(pi/16, qr[11])
    qc.cx(qr[8], qr[11])

    qc.u1(-pi/8, qr[11])
    qc.cx(qr[9], qr[11])
    qc.u1(-pi/8, qr[9])
    qc.u1(pi/8, qr[11])
    qc.cx(qr[9], qr[11])

    qc.u1(-pi/4, qr[11]) 
    qc.cx(qr[10], qr[11])
    qc.u1(-pi/4, qr[10])
    qc.u1(pi/4, qr[11])
    qc.cx(qr[10], qr[11])

    qc.h(qr[11])
    ################################
    #qft-1 em 0 e 1

    qc.swap(qr[0], qr[1])

    qc.h(qr[0])

    qc.u1(-pi/4, qr[1])
    qc.cx(qr[0], qr[1])
    qc.u1(-pi/4, qr[0])
    qc.u1(pi/4, qr[1])
    qc.cx(qr[0], qr[1])

    qc.h(qr[1])
    
    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))
