from helpers import input_fragment, function_to_matrix, mining_helper

def BTC_mining_oracle(qc, input_bits, n):
    input_fragment(qc, input_bits)
    fn = lambda x, n : mining_helper(x, n)
    M = function_to_matrix(fn, n)
    qc.unitary(M, range(n))