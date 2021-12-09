import matplotlib.pyplot as plt
import numpy as np
import itertools

# importing Qiskit
from qiskit import IBMQ, Aer, assemble, transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.ibmq import least_busy
from qiskit.visualization import plot_histogram

# Other imports
from bitcoin import BTC_mining_oracle

def diffuser(nqubits):
    qc = QuantumCircuit(nqubits)
    # Apply transformation |s> -> |00..0> (H-gates)
    for qubit in range(nqubits):
        qc.h(qubit)
    # Apply transformation |00..0> -> |11..1> (X-gates)
    for qubit in range(nqubits):
        qc.x(qubit)
    # Do multi-controlled-Z gate
    qc.h(nqubits-1)
    qc.mct(list(range(nqubits-1)), nqubits-1)  # multi-controlled-toffoli
    qc.h(nqubits-1)
    # Apply transformation |11..1> -> |00..0>
    for qubit in range(nqubits):
        qc.x(qubit)
    # Apply transformation |00..0> -> |s>
    for qubit in range(nqubits):
        qc.h(qubit)
    # We will return the diffuser as a gate
    U_s = qc.to_gate()
    U_s.name = "U$_s$"
    return U_s

def main():
    n = 6
    var_qubits = QuantumRegister(n, name='v')
    #clause_qubits = QuantumRegister(n, name='c')
    #output_qubit = QuantumRegister(1, name='out')
    cbits = ClassicalRegister(n, name='cbits')
    qc = QuantumCircuit(var_qubits, cbits)
    #qc = QuantumCircuit(var_qubits, output_qubit, cbits)

    # Initialize 'out0' in state |->
    #qc.initialize([1, -1]/np.sqrt(2), output_qubit)

    # Initialize qubits in state |s>
    qc.h(var_qubits)
    qc.barrier()  # for visual separation

    ## First Iteration
    # Apply our oracle
    BTC_mining_oracle(qc, var_qubits, n)
    qc.barrier()  # for visual separation
    # Apply our diffuser
    qc.append(diffuser(4), [0,1,2,3])

    ## Second Iteration
    BTC_mining_oracle(qc, var_qubits, n)
    qc.barrier()  # for visual separation
    # Apply our diffuser
    qc.append(diffuser(4), [0,1,2,3])

    # Measure the variable qubits
    qc.measure(var_qubits, cbits)

    qc.draw(fold=-1)

if __name__ == '__main__':
    main()
    