from logging import error
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from bitcoin import BTC_mining_oracle
from grover import diffuser
from qiskit import IBMQ, Aer, assemble, transpile

# Python
import sys

# Plot
from plot import plot

def main(n_qubits : int, num_grover_iterations: int):
    n = n_qubits
    input_bits = QuantumRegister(n, name='v')
    cbits = ClassicalRegister(n, name='cbits')
    qc = QuantumCircuit(input_bits, cbits)

 
    # Initialize qubits in state |s>
    qc.h(input_bits)
    qc.barrier()  # for visual separation

    # Apply our oracle for the number of iterations specified
    for i in range(num_grover_iterations):
        BTC_mining_oracle(qc, input_bits, n)
        qc.barrier()  # for visual separation
        # Apply our diffuser
        qc.append(diffuser(n), range(n))

    # Measure the variable qubits
    qc.measure(input_bits, cbits)

    qc.draw(fold=-1)

    aer_simulator = Aer.get_backend('aer_simulator')
    transpiled_qc = transpile(qc, aer_simulator)
    qobj = assemble(transpiled_qc)
    result = aer_simulator.run(qobj).result()

    plot(result.get_counts())



if __name__ == '__main__':
    args = sys.argv
    usage = "Usage: python main.py $num_qubits $num_grover_iterations"
    length = len(args)

    if (length != 3):
        raise Exception(usage)
    
    try:
        n_qubits = int(args[1])
        num_grover_iterations = int(args[2])
        main(n_qubits, num_grover_iterations)

    except RuntimeError:
       print("Command Line Arguments should be integers")
       print(usage)