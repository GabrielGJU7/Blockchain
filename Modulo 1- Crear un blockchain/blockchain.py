#Modulo 1 - Creae una cadena de bloques

# Importar las librerias

import datetime
import hashlib
import json
from flask import Flask, jsonify
from flask.json import JSONDecoder, dump

# Parte 1 - Crear la cadena de Bloques

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
            block = {
                'index': len(self.chain) + 1,
                'timestamp': str(datetime.datetime.now()),
                'proof': proof,
                'previous_hash': previous_hash 
            }
            self.chain.append(block)
            return block

    def getPreviousBlock(self):
        return self.chain[-1]

    def proof_of_word(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256( str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hashlib[:4] == '0000':
                check_proof = True
            else: new_proof  += 1    
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()            
# Parte 2 - Minado de un bloque de la cadena
