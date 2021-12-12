# QuantumBTCMining
Informal research paper and naive implementation of using Grover's Algorithm to mine a Bitcoin Block

# Instructions:
Clone the repo

Use Python 3.7+

```pip install matplotlib, qiskit```

May need to replace pip with pip3

Run ```python main.py $num_qubits $num_grover-iterations```

Try ```python main.py 6 6``` which mines the test block in ```block.py```. You should see a plot in a few seconds with probability of 47 with 99.5% (47 is the nonce)

Note that, the number of leading zeros for a target hash is fixed at 2.
