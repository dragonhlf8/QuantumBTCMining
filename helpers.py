import time
from block import block_header
from hash import SHA256

num_leading_zeros = 2
prefix = '0'*num_leading_zeros

'''
    @fn - a function that returns a base10 value 
    n - The number of bits in the input
'''
def function_to_matrix(fn, n):
    matrix = []
    size = 2**n # matrix size will have 2^n entries
    dim = range(size)

    # Building the Unitary Matrix with 1 or -1 on the diagonal
    for row in dim:
        matrix.append([])
        for col in dim:
            if (col == row):
                matrix[row].append(fn(col))
            else:
                matrix[row].append(0)
    return matrix


def mining_helper(x, n):
    return (-1)**f(x, n)


'''
    @param x - A base 10 number. In the context of Unitary matrices, this is the column number in base 10
    @param n - The size
'''
def f(x):
    nonce = x
    new_hash = SHA256(block_header, nonce)
    if (new_hash.startswith(prefix)):
        return 1
    return 0

'''
    @param qc - A QuantumCircuit Object
    @param vals - A QuantumRegister of the input bits
'''
def input_fragment (qc, input_bits) :
    n = len(input_bits)
    for idx, val in list(enumerate(input_bits)):
        if val == '1' : qc.x((n-idx)-1)
    qc.barrier()
    

'''
    @param qc - A QuantumCircuit Object
    @param input_buts A QuantumRegister of size n that contains the input nonce
    @param n
'''

def BTC_mining_oracle(qc, input_bits, n):
    input_fragment(qc, input_bits)
    fn = lambda x, n : mining_helper(x, n)
    M = function_to_matrix(fn, n)
    qc.unitary(M, range(n))
    
    
        