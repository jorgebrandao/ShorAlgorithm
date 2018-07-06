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


#############################################################
######### Three qubit Quantum Fourier Transform #############
#############################################################
def qft3(g): 
    Q_program = QuantumProgram()
    qr = Q_program.create_quantum_register("qr", 3)
    cr = Q_program.create_classical_register("cr", 3)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #Entradas
    #qc.h(qr[1])
    qc.h(qr[2])

    #QFT 3
    
    qc.h(qr[2]) #aplica H no 1 qubit

    #S controlada de 0 para 1
    qc.t(qr[2])
    qc.cx(qr[1], qr[2])
    qc.t(qr[1])
    qc.tdg(qr[2])
    qc.cx(qr[1], qr[2])

    #T controlada de 0 para 2
    qc.u1(pi/8, qr[2]) #u1=sqrt(T)
    qc.cx(qr[0], qr[2])
    qc.u1(pi/8, qr[0])
    qc.u1(-pi/8, qr[2])
    qc.cx(qr[0], qr[2])

    qc.h(qr[1]) #aplica H no 2 qubit

    #S controlada de 1 para 2
    qc.t(qr[1])
    qc.cx(qr[0], qr[1])
    qc.t(qr[0])
    qc.tdg(qr[1])
    qc.cx(qr[0], qr[1])

    qc.h(qr[0]) #aplica H no 3 qubit

    qc.swap(qr[2], qr[0]) # troca o 1 e 3 qubit


    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))

    tmp = result.get_data("superposition")
    plot_histogram(tmp['counts'])
                                #####
                                #END#

########################################################################
#############################################################
######### Three qubit Quantum Fourier Transform #############
#############################################################
def qft3u(g):
    Q_program = QuantumProgram()
    qr = Q_program.create_quantum_register("qr", 3)
    cr = Q_program.create_classical_register("cr", 3)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #Entradas
    #qc.h(qr[1])
    qc.h(qr[0])
    #qc.x(qr[0])
    #qc.x(qr[1])
    #qc.x(qr[2])

    #QFT 3
    
    qc.h(qr[2]) #aplica H no 1 qubit

    #S controlada de 2 para 1
    qc.u1(pi/4, qr[2])
    qc.cx(qr[1], qr[2])
    qc.u1(pi/4, qr[1])
    qc.u1(-pi/4, qr[2])
    qc.cx(qr[1], qr[2])

    #T controlada de 0 para 2
    qc.u1(pi/8, qr[2]) #u1=sqrt(T)
    qc.cx(qr[0], qr[2])
    qc.u1(pi/8, qr[0])
    qc.u1(-pi/8, qr[2])
    qc.cx(qr[0], qr[2])

    qc.h(qr[1]) #aplica H no 2 qubit

    #S controlada de 1 para 2
    qc.u1(pi/4, qr[1])
    qc.cx(qr[0], qr[1])
    qc.u1(pi/4, qr[0])
    qc.u1(-pi/4, qr[1])
    qc.cx(qr[0], qr[1])

    qc.h(qr[0]) #aplica H no 3 qubit

    qc.swap(qr[2], qr[0]) # troca o 1 e 3 qubit



    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))

    tmp = result.get_data("superposition")
    plot_histogram(tmp['counts'])
                                #####
                                #END#


########################################################################
#############################################################
###### Three qubit Inverse Quantum Fourier Transform ########
#############################################################
def invqft3(g): 
    Q_program = QuantumProgram()
    qr = Q_program.create_quantum_register("qr", 3)
    cr = Q_program.create_classical_register("cr", 3)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #entradas
    qc.h(qr[1])
    qc.h(qr[2])




    qc.swap(qr[2], qr[0]) # troca o 1 e 3 qubit

    qc.h(qr[0]) 

    qc.tdg(qr[1])
    qc.cx(qr[0], qr[1])
    qc.tdg(qr[0])
    qc.t(qr[1])
    qc.cx(qr[0], qr[1])

    qc.h(qr[1])

    qc.u1(-pi/8, qr[2])
    qc.cx(qr[0], qr[2])
    qc.u1(-pi/8, qr[0])
    qc.u1(pi/8, qr[2])
    qc.cx(qr[0], qr[2])

    qc.tdg(qr[2])
    qc.cx(qr[1], qr[2])
    qc.tdg(qr[1])
    qc.t(qr[2])
    qc.cx(qr[1], qr[2])

    qc.h(qr[2])


    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))

    tmp = result.get_data("superposition")
    plot_histogram(tmp['counts'])
                                #####
                                #END#

########################################################################
#############################################################
######### Four qubit Quantum Fourier Transform ##############
#############################################################
def qft4(g):
    Q_program = QuantumProgram()
    qr = Q_program.create_quantum_register("qr", 4)
    cr = Q_program.create_classical_register("cr", 4)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #Entradas
    #qc.h(qr[0])
    qc.h(qr[1])
    #qc.h(qr[2])
    qc.h(qr[3])

    #QFT 4 Qubits

    qc.h(qr[3])

    #Scont
    qc.t(qr[3])
    qc.cx(qr[2], qr[3])
    qc.t(qr[2])
    qc.tdg(qr[3])
    qc.cx(qr[2], qr[3])


    #Tcont
    qc.u1(pi/8, qr[3]) #u1=sqrt(T)
    qc.cx(qr[1], qr[3])
    qc.u1(pi/8, qr[1])
    qc.u1(-pi/8, qr[3])
    qc.cx(qr[1], qr[3])


    #u1cont
    qc.u1(pi/16, qr[3]) #sqrt(sqrt(T))
    qc.cx(qr[0], qr[3])
    qc.u1(pi/16, qr[0])
    qc.u1(-pi/16, qr[3])
    qc.cx(qr[0], qr[3])


    qc.h(qr[2]) 

    #S controlada
    qc.t(qr[2])
    qc.cx(qr[1], qr[2])
    qc.t(qr[1])
    qc.tdg(qr[2])
    qc.cx(qr[1], qr[2])

    #T controlada 
    qc.u1(pi/8, qr[2]) #u1=sqrt(T)
    qc.cx(qr[0], qr[2])
    qc.u1(pi/8, qr[0])
    qc.u1(-pi/8, qr[2])
    qc.cx(qr[0], qr[2])

    qc.h(qr[1]) 

    #S controlada 
    qc.t(qr[1])
    qc.cx(qr[0], qr[1])
    qc.t(qr[0])
    qc.tdg(qr[1])
    qc.cx(qr[0], qr[1])

    qc.h(qr[0])

    qc.swap(qr[2], qr[1])
    qc.swap(qr[3], qr[0])


    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))

    tmp = result.get_data("superposition")
    plot_histogram(tmp['counts'])
                                #####
                                #END#

########################################################################
#############################################################
########## Five qubit Quantum Fourier Transform #############
#############################################################
def qft5(g): #está certa - usei s e t
    Q_program = QuantumProgram()
    qr = Q_program.create_quantum_register("qr", 5)
    cr = Q_program.create_classical_register("cr", 5)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #Entradas
    #qc.h(qr[0])
    qc.h(qr[1])
    qc.h(qr[2])
    qc.h(qr[3])
    qc.h(qr[4])

    #QFT 5 Qubits

    qc.h(qr[4])

    #Scont
    qc.t(qr[4])
    qc.cx(qr[3], qr[4])
    qc.t(qr[3])
    qc.tdg(qr[4])
    qc.cx(qr[3], qr[4])

    #Tcont
    qc.u1(pi/8, qr[4]) #u1=sqrt(T)
    qc.cx(qr[2], qr[4])
    qc.u1(pi/8, qr[2])
    qc.u1(-pi/8, qr[4])
    qc.cx(qr[2], qr[4])


    #sqrt(T)cont
    qc.u1(pi/16, qr[4]) #sqrt(sqrt(T))
    qc.cx(qr[1], qr[4])
    qc.u1(pi/16, qr[1])
    qc.u1(-pi/16, qr[4])
    qc.cx(qr[1], qr[4])


    #T**1/4cont
    qc.u1(pi/32, qr[4]) #sqrt(sqrt(T))
    qc.cx(qr[0], qr[4])
    qc.u1(pi/32, qr[0])
    qc.u1(-pi/32, qr[4])
    qc.cx(qr[0], qr[4])


    qc.h(qr[3])

    #Scont
    qc.t(qr[3])
    qc.cx(qr[2], qr[3])
    qc.t(qr[2])
    qc.tdg(qr[3])
    qc.cx(qr[2], qr[3])


    #Tcont
    qc.u1(pi/8, qr[3]) #u1=sqrt(T)
    qc.cx(qr[1], qr[3])
    qc.u1(pi/8, qr[1])
    qc.u1(-pi/8, qr[3])
    qc.cx(qr[1], qr[3])


    #sqrt(T)cont
    qc.u1(pi/16, qr[3]) #sqrt(sqrt(T))
    qc.cx(qr[0], qr[3])
    qc.u1(pi/16, qr[0])
    qc.u1(-pi/16, qr[3])
    qc.cx(qr[0], qr[3])


    qc.h(qr[2]) 

    #S controlada
    qc.t(qr[2])
    qc.cx(qr[1], qr[2])
    qc.t(qr[1])
    qc.tdg(qr[2])
    qc.cx(qr[1], qr[2])

    #T controlada 
    qc.u1(pi/8, qr[2]) #u1=sqrt(T)
    qc.cx(qr[0], qr[2])
    qc.u1(pi/8, qr[0])
    qc.u1(-pi/8, qr[2])
    qc.cx(qr[0], qr[2])

    qc.h(qr[1]) 

    #S controlada 
    qc.t(qr[1])
    qc.cx(qr[0], qr[1])
    qc.t(qr[0])
    qc.tdg(qr[1])
    qc.cx(qr[0], qr[1])

    qc.h(qr[0])


    qc.swap(qr[4], qr[0])
    qc.swap(qr[3], qr[1])


    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))

    tmp = result.get_data("superposition")
    plot_histogram(tmp['counts'])
                                #####
                                #END#

########################################################################
#############################################################
###### Four qubit Inverse Quantum Fourier Transform #########
#############################################################
def invqft4(g):
    Q_program = QuantumProgram()
    qr = Q_program.create_quantum_register("qr", 4)
    cr = Q_program.create_classical_register("cr", 4)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #Entradas
    #qc.h(qr[0])
    #qc.h(qr[1])
    #qc.h(qr[2])
    qc.h(qr[3])



    qc.swap(qr[3], qr[0])
    qc.swap(qr[2], qr[1])

    qc.h(qr[0]) 

    qc.tdg(qr[1])
    qc.cx(qr[0], qr[1])
    qc.tdg(qr[0])
    qc.t(qr[1])
    qc.cx(qr[0], qr[1])

    qc.h(qr[1])

    qc.u1(-pi/8, qr[2]) #u1=sqrt(T)
    qc.cx(qr[0], qr[2])
    qc.u1(-pi/8, qr[0])
    qc.u1(pi/8, qr[2])
    qc.cx(qr[0], qr[2])

    qc.tdg(qr[2])
    qc.cx(qr[1], qr[2])
    qc.tdg(qr[1])
    qc.t(qr[2])
    qc.cx(qr[1], qr[2])

    qc.h(qr[2])

    #u1cont
    qc.u1(-pi/16, qr[3]) #sqrt(sqrt(T))
    qc.cx(qr[0], qr[3])
    qc.u1(-pi/16, qr[0])
    qc.u1(pi/16, qr[3])
    qc.cx(qr[0], qr[3])

    #Tcont
    qc.u1(-pi/8, qr[3]) #u1=sqrt(T)
    qc.cx(qr[1], qr[3])
    qc.u1(-pi/8, qr[1])
    qc.u1(pi/8, qr[3])
    qc.cx(qr[1], qr[3])

    #Scont
    qc.tdg(qr[3])
    qc.cx(qr[2], qr[3])
    qc.tdg(qr[2])
    qc.t(qr[3])
    qc.cx(qr[2], qr[3])

    qc.h(qr[3])


    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))

    tmp = result.get_data("superposition")
    plot_histogram(tmp['counts'])
                                #####
                                #END#

########################################################################
######################### Draper Adder 3+3 #############################
########################################################################
def adder33(g):
    qr = Q_program.create_quantum_register("qr", 7)
    cr = Q_program.create_classical_register("cr", 7)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #Entradas
    #a
    qc.x(qr[0])
    qc.x(qr[1])
    qc.x(qr[2])

    #b
    #qc.x(qr[3])
    #qc.x(qr[4])
    #qc.x(qr[5])

    ####qft4 de b

    qc.h(qr[6])

    #Scont
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])
    qc.t(qr[5])
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])


    #Tcont
    qc.u1(pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(pi/8, qr[4])
    qc.u1(-pi/8, qr[6])
    qc.cx(qr[4], qr[6])


    #u1cont
    qc.u1(pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(pi/16, qr[3])
    qc.u1(-pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    qc.h(qr[5]) #aplica H no 1 qubit

    #S controlada
    qc.u1(pi/4, qr[5])
    qc.cx(qr[4], qr[5])
    qc.u1(pi/4, qr[4])
    qc.u1(-pi/4, qr[5])
    qc.cx(qr[4], qr[5])

    #T controlada
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(pi/8, qr[3])
    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.h(qr[4])

    #S controlada
    qc.u1(pi/4, qr[4])
    qc.cx(qr[3], qr[4])
    qc.u1(pi/4, qr[3])
    qc.u1(-pi/4, qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[3])

    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])


    #ADDER

    #u2 controlada
    qc.u1(pi/4, qr[3])
    qc.cx(qr[2], qr[3])
    qc.u1(pi/4, qr[2])
    qc.u1(-pi/4, qr[3])
    qc.cx(qr[2], qr[3])

    #u3 c
    qc.u1(pi/8, qr[3])
    qc.cx(qr[1], qr[3])
    qc.u1(pi/8, qr[1])
    qc.u1(-pi/8, qr[3])
    qc.cx(qr[1], qr[3])

    #u4 c
    qc.u1(pi/16, qr[3])
    qc.cx(qr[0], qr[3])
    qc.u1(pi/16, qr[0])
    qc.u1(-pi/16, qr[3])    
    qc.cx(qr[0], qr[3])

    #u1 c
    qc.u1(pi/2, qr[4])
    qc.cx(qr[2], qr[4])
    qc.u1(pi/2, qr[2])
    qc.u1(-pi/2, qr[4])
    qc.cx(qr[2], qr[4])

    #u2 c
    qc.u1(pi/4, qr[4])
    qc.cx(qr[1], qr[4])
    qc.u1(pi/4, qr[1])
    qc.u1(-pi/4, qr[4])
    qc.cx(qr[1], qr[4])

    #u3 c
    qc.u1(pi/8, qr[4])
    qc.cx(qr[0], qr[4])
    qc.u1(pi/8, qr[0])
    qc.u1(-pi/8, qr[4])
    qc.cx(qr[0], qr[4])


    #u1 c
    qc.u1(pi/2, qr[5])
    qc.cx(qr[1], qr[5])
    qc.u1(pi/2, qr[1])
    qc.u1(-pi/2, qr[5])
    qc.cx(qr[1], qr[5])

    #u2 c
    qc.u1(pi/4, qr[5])
    qc.cx(qr[0], qr[5])
    qc.u1(pi/4, qr[0])
    qc.u1(-pi/4, qr[5])
    qc.cx(qr[0], qr[5])

    #u1 c
    qc.u1(pi/2, qr[6])
    qc.cx(qr[0], qr[6])
    qc.u1(pi/2, qr[0])
    qc.u1(-pi/2, qr[6])
    qc.cx(qr[0], qr[6])


    
    #   invqft4
    
    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])

    qc.h(qr[3]) 

    qc.tdg(qr[4])
    qc.cx(qr[3], qr[4])
    qc.tdg(qr[3])
    qc.t(qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[4])

    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(-pi/8, qr[3])
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.tdg(qr[5])
    qc.cx(qr[4], qr[5])
    qc.tdg(qr[4])
    qc.t(qr[5])
    qc.cx(qr[4], qr[5])

    qc.h(qr[5])

    #u1cont
    qc.u1(-pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(-pi/16, qr[3])
    qc.u1(pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    #Tcont
    qc.u1(-pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(-pi/8, qr[4])
    qc.u1(pi/8, qr[6])
    qc.cx(qr[4], qr[6])

    #Scont
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])
    qc.tdg(qr[5])
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])

    qc.h(qr[6])


    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))

    tmp = result.get_data("superposition")
    plot_histogram(tmp['counts'])
                                #####
                                #END#

########################################################################
###################### Draper Adder 3+3 mod n ##########################
########################################################################

def add33(g):
    Q_program = QuantumProgram()
    qr = Q_program.create_quantum_register("qr", 7)
    cr = Q_program.create_classical_register("cr", 7)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #Entradas
    #x
    #qc.x(qr[0])
    #qc.x(qr[1])
    #qc.x(qr[2])

    #b
    qc.x(qr[3])
    #qc.x(qr[4])
    #qc.x(qr[5])

    ####qft4 de b

    qc.h(qr[6])

    #Scont
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])
    qc.t(qr[5])
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])


    #Tcont
    qc.u1(pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(pi/8, qr[4])
    qc.u1(-pi/8, qr[6])
    qc.cx(qr[4], qr[6])


    #u1cont
    qc.u1(pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(pi/16, qr[3])
    qc.u1(-pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    qc.h(qr[5]) #aplica H no 1 qubit

    #S controlada
    qc.u1(pi/4, qr[5])
    qc.cx(qr[4], qr[5])
    qc.u1(pi/4, qr[4])
    qc.u1(-pi/4, qr[5])
    qc.cx(qr[4], qr[5])

    #T controlada
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(pi/8, qr[3])
    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.h(qr[4])

    #S controlada
    qc.u1(pi/4, qr[4])
    qc.cx(qr[3], qr[4])
    qc.u1(pi/4, qr[3])
    qc.u1(-pi/4, qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[3])

    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])


    #       ADDER (começa do menos significativo da transformada para o mais significativo do a)
    #vamos admitir a=101 = 5
    #u2+u4
    #qc.u1(pi/2, qr[3])
    #qc.u1(pi/8, qr[3])
    qc.u1(5*pi/8, qr[3]) # é o mesmo que ter os dois de cima (pi/2+pi/8=5*pi/8)

    #u1+u3
    #qc.u1(pi, qr[4])
    #qc.u1(pi/4, qr[4])
    qc.u1(5*pi/4, qr[4])# é o mesmo que ter os dois de cima (pi+pi/4=5*pi/4)

    #u2
    qc.u1(pi/2, qr[5])

    #u1
    qc.u1(pi, qr[6])
    #nota, só o adder funcionou com as fases mas agora precisa-se do adder controlado
 
    # cmult vamos multiplicar a= 101 por x
    
    #   invqft4
    
    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])

    qc.h(qr[3]) 

    qc.tdg(qr[4])
    qc.cx(qr[3], qr[4])
    qc.tdg(qr[3])
    qc.t(qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[4])

    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(-pi/8, qr[3])
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.tdg(qr[5])
    qc.cx(qr[4], qr[5])
    qc.tdg(qr[4])
    qc.t(qr[5])
    qc.cx(qr[4], qr[5])

    qc.h(qr[5])

    #u1cont
    qc.u1(-pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(-pi/16, qr[3])
    qc.u1(pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    #Tcont
    qc.u1(-pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(-pi/8, qr[4])
    qc.u1(pi/8, qr[6])
    qc.cx(qr[4], qr[6])

    #Scont
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])
    qc.tdg(qr[5])
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])

    qc.h(qr[6])


    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))

    #tmp = result.get_data("superposition")
    #plot_histogram(tmp['counts'])
                                #####
                                #END#


def addmod(g):
    Q_program = QuantumProgram()
    qr = Q_program.create_quantum_register("qr", 8)
    cr = Q_program.create_classical_register("cr", 8)
    qc = Q_program.create_circuit("superposition", [qr], [cr])

    #Entradas
    #n
    #qc.x(qr[0])
    #qc.x(qr[1])
    #qc.x(qr[2])



    #b
    qc.x(qr[3])
    #qc.x(qr[4])
    qc.x(qr[5])

    ####qft4 de b

    qc.h(qr[6])

    #Scont
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])
    qc.t(qr[5])
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])


    #Tcont
    qc.u1(pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(pi/8, qr[4])
    qc.u1(-pi/8, qr[6])
    qc.cx(qr[4], qr[6])


    #u1cont
    qc.u1(pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(pi/16, qr[3])
    qc.u1(-pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    qc.h(qr[5]) #aplica H no 1 qubit

    #S controlada
    qc.u1(pi/4, qr[5])
    qc.cx(qr[4], qr[5])
    qc.u1(pi/4, qr[4])
    qc.u1(-pi/4, qr[5])
    qc.cx(qr[4], qr[5])

    #T controlada
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(pi/8, qr[3])
    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.h(qr[4])

    #S controlada
    qc.u1(pi/4, qr[4])
    qc.cx(qr[3], qr[4])
    qc.u1(pi/4, qr[3])
    qc.u1(-pi/4, qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[3])

    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])

    #add a
    #       ADDER (começa do menos significativo da transformada para o mais significativo do a)
    #vamos admitir a=101 = 5
    #u2+u4
    #qc.u1(pi/2, qr[3])
    #qc.u1(pi/8, qr[3])
    qc.u1(5*pi/8, qr[3]) # é o mesmo que ter os dois de cima (pi/2+pi/8=5*pi/8)
    #u1+u3
    #qc.u1(pi, qr[4])
    #qc.u1(pi/4, qr[4])
    qc.u1(5*pi/4, qr[4])# é o mesmo que ter os dois de cima (pi+pi/4=5*pi/4)
    #u2
    qc.u1(pi/2, qr[5])
    #u1
    qc.u1(pi, qr[6])
    
    #subtrai n
    #vamos admitir n=011 = 3 logo subtrair n é fazer conjugado
    #u3+u4
    #qc.u1(pi/4, qr[3])
    #qc.u1(pi/8, qr[3])
    qc.u1(-3*pi/8, qr[3])
    #u2+u3
    #qc.u1(pi/2, qr[4])
    #qc.u1(pi/4, qr[4])
    qc.u1(-3*pi/4, qr[4])# é o mesmo que ter os dois de cima (pi+pi/4=5*pi/4)
    #u1+u2
    qc.u1(-3*pi/2, qr[5])
    #u1
    qc.u1(-pi, qr[6])    

    #   invqft4
    
    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])

    qc.h(qr[3]) 

    qc.tdg(qr[4])
    qc.cx(qr[3], qr[4])
    qc.tdg(qr[3])
    qc.t(qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[4])

    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(-pi/8, qr[3])
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.tdg(qr[5])
    qc.cx(qr[4], qr[5])
    qc.tdg(qr[4])
    qc.t(qr[5])
    qc.cx(qr[4], qr[5])

    qc.h(qr[5])

    #u1cont
    qc.u1(-pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(-pi/16, qr[3])
    qc.u1(pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    #Tcont
    qc.u1(-pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(-pi/8, qr[4])
    qc.u1(pi/8, qr[6])
    qc.cx(qr[4], qr[6])

    #Scont
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])
    qc.tdg(qr[5])
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])

    qc.h(qr[6])

    #cnot do ultimo bit da qft para um |0>
    qc.cx(qr[6], qr[7])

    #qft novamente
    qc.h(qr[6])

    #Scont
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])
    qc.t(qr[5])
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])


    #Tcont
    qc.u1(pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(pi/8, qr[4])
    qc.u1(-pi/8, qr[6])
    qc.cx(qr[4], qr[6])


    #u1cont
    qc.u1(pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(pi/16, qr[3])
    qc.u1(-pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    qc.h(qr[5]) #aplica H no 1 qubit

    #S controlada
    qc.u1(pi/4, qr[5])
    qc.cx(qr[4], qr[5])
    qc.u1(pi/4, qr[4])
    qc.u1(-pi/4, qr[5])
    qc.cx(qr[4], qr[5])

    #T controlada
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(pi/8, qr[3])
    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.h(qr[4])

    #S controlada
    qc.u1(pi/4, qr[4])
    qc.cx(qr[3], qr[4])
    qc.u1(pi/4, qr[3])
    qc.u1(-pi/4, qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[3])

    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])

    #add n controlado por 7
    qc.u1(3*pi/8, qr[3])
    qc.cx(qr[7], qr[3])
    qc.u1(3*pi/8, qr[7])
    qc.u1(-3*pi/8, qr[3])
    qc.cx(qr[7], qr[3])


    qc.u1(3*pi/4, qr[4])
    qc.cx(qr[7], qr[4])
    qc.u1(3*pi/4, qr[7])
    qc.u1(-3*pi/4, qr[4])
    qc.cx(qr[7], qr[4])

    qc.u1(3*pi/2, qr[5])
    qc.cx(qr[7], qr[5])
    qc.u1(3*pi/2, qr[7])
    qc.u1(-3*pi/2, qr[5])
    qc.cx(qr[7], qr[5])


    qc.u1(pi, qr[6])
    qc.cx(qr[7], qr[6])
    qc.u1(pi, qr[7])
    qc.u1(-pi, qr[6])
    qc.cx(qr[7], qr[6])


    #subtrai a
    qc.u1(-5*pi/8, qr[3])
    qc.u1(-5*pi/4, qr[4])
    qc.u1(-pi/2, qr[5])
    qc.u1(-pi, qr[6])

    #qft-1
    
    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])

    qc.h(qr[3]) 

    qc.tdg(qr[4])
    qc.cx(qr[3], qr[4])
    qc.tdg(qr[3])
    qc.t(qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[4])

    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(-pi/8, qr[3])
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.tdg(qr[5])
    qc.cx(qr[4], qr[5])
    qc.tdg(qr[4])
    qc.t(qr[5])
    qc.cx(qr[4], qr[5])

    qc.h(qr[5])

    #u1cont
    qc.u1(-pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(-pi/16, qr[3])
    qc.u1(pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    #Tcont
    qc.u1(-pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(-pi/8, qr[4])
    qc.u1(pi/8, qr[6])
    qc.cx(qr[4], qr[6])

    #Scont
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])
    qc.tdg(qr[5])
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])

    qc.h(qr[6])

    #x cnot x
    qc.x(qr[6])
    qc.cx(qr[7], qr[6])
    qc.x(qr[6])

    #qft
    qc.h(qr[6])

    #Scont
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])
    qc.t(qr[5])
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])


    #Tcont
    qc.u1(pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(pi/8, qr[4])
    qc.u1(-pi/8, qr[6])
    qc.cx(qr[4], qr[6])


    #u1cont
    qc.u1(pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(pi/16, qr[3])
    qc.u1(-pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    qc.h(qr[5]) #aplica H no 1 qubit

    #S controlada
    qc.u1(pi/4, qr[5])
    qc.cx(qr[4], qr[5])
    qc.u1(pi/4, qr[4])
    qc.u1(-pi/4, qr[5])
    qc.cx(qr[4], qr[5])

    #T controlada
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(pi/8, qr[3])
    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.h(qr[4])

    #S controlada
    qc.u1(pi/4, qr[4])
    qc.cx(qr[3], qr[4])
    qc.u1(pi/4, qr[3])
    qc.u1(-pi/4, qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[3])

    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])

    #add a
    qc.u1(5*pi/8, qr[3])
    qc.u1(5*pi/4, qr[4])
    qc.u1(pi/2, qr[5])
    qc.u1(pi, qr[6])

    #inv qft
    qc.swap(qr[6], qr[3])
    qc.swap(qr[5], qr[4])

    qc.h(qr[3]) 

    qc.tdg(qr[4])
    qc.cx(qr[3], qr[4])
    qc.tdg(qr[3])
    qc.t(qr[4])
    qc.cx(qr[3], qr[4])

    qc.h(qr[4])

    qc.u1(-pi/8, qr[5])
    qc.cx(qr[3], qr[5])
    qc.u1(-pi/8, qr[3])
    qc.u1(pi/8, qr[5])
    qc.cx(qr[3], qr[5])

    qc.tdg(qr[5])
    qc.cx(qr[4], qr[5])
    qc.tdg(qr[4])
    qc.t(qr[5])
    qc.cx(qr[4], qr[5])

    qc.h(qr[5])

    #u1cont
    qc.u1(-pi/16, qr[6]) #sqrt(sqrt(T))
    qc.cx(qr[3], qr[6])
    qc.u1(-pi/16, qr[3])
    qc.u1(pi/16, qr[6])
    qc.cx(qr[3], qr[6])

    #Tcont
    qc.u1(-pi/8, qr[6]) #u1=sqrt(T)
    qc.cx(qr[4], qr[6])
    qc.u1(-pi/8, qr[4])
    qc.u1(pi/8, qr[6])
    qc.cx(qr[4], qr[6])

    #Scont
    qc.tdg(qr[6])
    qc.cx(qr[5], qr[6])
    qc.tdg(qr[5])
    qc.t(qr[6])
    qc.cx(qr[5], qr[6])

    qc.h(qr[6])

    qc.measure(qr, cr)
    result = Q_program.execute(["superposition"], backend='local_qasm_simulator', shots=g)
    print(result)
    print(result.get_data("superposition"))

    #tmp = result.get_data("superposition")
    #plot_histogram(tmp['counts'])
                                #####
                                #END#