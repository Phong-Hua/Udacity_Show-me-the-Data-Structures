"""
Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and 
how it is connected related to the other blocks in the chain. 
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. 
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

We can break the blockchain down into three main parts.

First is the information hash:
"""
from datetime import datetime
import hashlib


def calc_hash(self):
    sha = hashlib.sha256()
    hash_str = "We are going to encode this string of data!".encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


"""
We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain.

The next main component is the block on the blockchain:
"""


class Block:

  def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

  def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
  
  def get_hash(self):
    return self.hash

"""
Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list.
All of this will help you build up to a simple but full blockchain implementation! 
"""


class Blockchain:
  def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

  def append(self, block):
        if self.is_empty():
            self.head = block
            self.tail = block
        else:
            self.tail = block
        self.size += 1

  def is_empty(self):
        return self.size == 0

  def get_size(self):
        return self.size

def test_case_1():
  """
  """
  print("***********Test_case_1**************")
  blockchain = Blockchain()
  first_block = Block(datetime.now(), 'First block', 0)
  print(blockchain.get_size())
  # 0
  blockchain.append(first_block)
  print(blockchain.get_size())
  # 1
  second_block = Block(datetime.now(), 'Second block', first_block.get_hash())
  blockchain.append(second_block)
  print(blockchain.get_size())
  # 2

def test_case_2():
  """
  Edge test case, with first block is empty string
  """
  print("***********Test_case_2**************")
  blockchain = Blockchain()
  timestamp = datetime.now()
  first_block = Block(timestamp, '', 0)
  print(blockchain.get_size())
  # 0
  blockchain.append(first_block)
  print(blockchain.get_size())
  # 1

def test_case_3():
  """
  Edge test case, with second block has same timestamp with first block
  """
  print("***********Test_case_3**************")
  blockchain = Blockchain()
  timestamp = datetime.now()
  first_block = Block(timestamp, '', 0)
  print(blockchain.get_size())
  # 0
  blockchain.append(first_block)
  print(blockchain.get_size())
  # 1
  second_block = Block(timestamp, 'Second block', first_block.get_hash())
  blockchain.append(second_block)
  print(blockchain.get_size())
  # 2

def test_case_4():
  """
  Edge test case, two blocks have a same data => both hashes should be different
  """
  print("***********Test_case_4**************")
  blockchain = Blockchain()
  first_block = Block(datetime.now(), 'Data', 0)
  print(blockchain.get_size())
  # 0
  blockchain.append(first_block)
  print(blockchain.get_size())
  # 1
  second_block = Block(datetime.now(), 'Data', first_block.get_hash())
  blockchain.append(second_block)
  print(blockchain.get_size())
  # 2
  print(first_block.get_hash() != second_block.get_hash())
  # True

def test_case_5():
  """
  Edge test case, two blocks have a same data, same timestamp => both hashes should be different
  """
  print("***********Test_case_5**************")
  blockchain = Blockchain()
  timestamp = datetime.now()
  first_block = Block(timestamp, 'Data', 0)
  print(blockchain.get_size())
  # 0
  blockchain.append(first_block)
  print(blockchain.get_size())
  # 1
  second_block = Block(timestamp, 'Data', first_block.get_hash())
  blockchain.append(second_block)
  print(blockchain.get_size())
  # 2
  print(first_block.get_hash() != second_block.get_hash())
  # True

test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()