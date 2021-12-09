from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from bitcoin import BTC_mining_oracle
from grover import diffuser
from qiskit import IBMQ, Aer, assemble, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

import time

def main(n_qubits, num_grovers_iterations):
    n = 6
    input_bits = QuantumRegister(n, name='v')
    cbits = ClassicalRegister(n, name='cbits')
    qc = QuantumCircuit(input_bits, cbits)

 
    # Initialize qubits in state |s>
    qc.h(input_bits)
    qc.barrier()  # for visual separation

    ## First Iteration
    # Apply our oracle
    iterations = 5 # More iterations, the more our target answer is amplified

    for i in range(iterations):
        BTC_mining_oracle(qc, input_bits, n)
        qc.barrier()  # for visual separation
        # Apply our diffuser
        qc.append(diffuser(n), range(n))

    # ## Second Iteration
    # BTC_mining_oracle(qc, input_bits, n)
    # qc.barrier()  # for visual separation
    # # Apply our diffuser
    # qc.append(diffuser(n), range(n))

    # Measure the variable qubits
    qc.measure(input_bits, cbits)

    qc.draw(fold=-1)

    aer_simulator = Aer.get_backend('aer_simulator')
    transpiled_qc = transpile(qc, aer_simulator)
    qobj = assemble(transpiled_qc)
    start = time.time()
    result = aer_simulator.run(qobj).result()
    print(str((time.time() - start)))


    plot_histogram(result.get_counts(), (20,20))
    plt.show()


if __name__ == '__main__':
    main()
    