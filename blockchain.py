#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:50:09 2019

@author: wscherer13
"""

"""Implementing a blockchain as a hashed list based off Medium article.
I might include a Merkle tree data structure later if I can figure it out."""

class Blockchain(object):
    
    def __init__(self):
        self.chain = [] #initializing blockchain as a list - update later
        self.current_transactions = []
        
        
    def new_block(self):
        
        #creates a new block and adds it to the chain
        
        pass
    
    def new_transaction(self):
        
        #adds a new transaction to the list of transactions
        
        pass
    
    
    @staticmethod
    def hash(block):
        
        #hashes a block
        
        pass
    
    @property
    def last_block(self):
        #returns the last block in the chan
        
        pass