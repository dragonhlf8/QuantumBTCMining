from hashlib import sha256
import json

'''
    @param block_header - The block header object found in block.py
    @param nonce - The nonce/input guess to use

    @return The sha256 hash in hexadecimal
'''
def SHA256(block_header, nonce):
    block_header['nNonce'] = nonce;
    return sha256(json.dumps(block_header).encode('utf-8')).hexdigest()