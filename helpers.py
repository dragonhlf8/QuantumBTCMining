import time
from block import block_header
from hash import SHA256

num_leading_zeros = 2
prefix = '0'*num_leading_zeros

'''
    @param fn - a function that returns a base10 value 
    @param n - The number of bits in the input

    @return a Unitary Matrix of size 2^n. With 1 or -1 on the diagonal. -1 marks successful nonces
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


'''
    @param x - Base 10 number. In the context of building the unitary matrix, is it the column number in base 10
    @return (-1)^f(x)
'''
def phase(x):
    return (-1)**f(x)

'''
    @param x - A base 10 number. In the context of Unitary matrices, this is the column number in base 10
    @param n - The size
'''
def f(x):
    nonce = x
    hash = SHA256(block_header, nonce)
    if (hash.startswith(prefix)):
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
    
    
    
        