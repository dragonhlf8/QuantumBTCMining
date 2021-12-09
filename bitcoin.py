from helpers import input_fragment, function_to_matrix, phase

'''
    @param qc - A QuantumCircuit Object
    @param input_buts A QuantumRegister of size n that contains the input nonce
    @param n
'''
def BTC_mining_oracle(qc, input_bits, n):
    input_fragment(qc, input_bits)
    fn = lambda x : phase(x)
    M = function_to_matrix(fn, n)
    qc.unitary(M, range(n))