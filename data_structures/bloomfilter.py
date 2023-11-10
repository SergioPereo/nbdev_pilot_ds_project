#Importing the necessary libraries
import hashlib as hl
import numpy as np
import math as mth

class BloomFilter():
  def __init__(self, m=10, k=1):
    self.bits = mth.ceil(mth.log(m,2))
    self.hexa_characters = mth.ceil(self.bits/4) 
    self.MD5proceses = mth.ceil(k*self.hexa_characters/32)
    self.m = m
    self.k = k
    self.bloom = np.zeros(m, dtype = bool)

  def k_positions(self, object: str):
    # Returns 'k' positions in which we´re going to put 'True' in the BloomFilter
    positions = []
    hash = ''
    
    for proceses in range(self.MD5proceses):
      string2 = object +str(proceses)
      hexa = hl.md5(string2.encode('utf-8')).hexdigest()
      hash += hexa
      
    for i in range(0, self.k*self.hexa_characters, self.hexa_characters):
      value = int(hash[i:i + self.hexa_characters], 16) % self.m
      positions.append(value)
      
    return positions

  def insert(self, object: str):
    positions = self.k_positions(object)

    for pos in positions:
      self.bloom[pos] = True

  def search(self, object: str):
    positions = self.k_positions(object)
    i = 0
    found = True
    while i < len(positions) and found:
      found = self.bloom[positions[i]]
      i +=1

    return found