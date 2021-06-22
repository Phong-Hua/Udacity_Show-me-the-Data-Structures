"""
Min Heap Implementation
Code from https://www.geeksforgeeks.org/binary-heap/
"""
# A Python program to demonstrate common binary heap operations
  
# Import the heap functions from python library
from heapq import heappush, heappop, heapify
  
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time
  
# A class for Min Heap
class MinHeap:

    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 
  
    def parent(self, i):
        return (i-1)/2
      
    # Inserts a new key 'k'
    def insert_key(self, k, node):
        heappush(self.heap, (k, node))
  
    # Decrease value of key at index 'i' to new_key
    # It is assumed that new_key is smaller than heap[i]
    def decrease_key(self, i, new_key):
        current_element = self.heap[i]
        self.heap[i]  = (new_key, current_element[1])
        temp = int(self.parent(i))

        while(i != 0 and self.heap[temp][0] > self.heap[i][0]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[temp] = (
            self.heap[temp], self.heap[i])
              
    # Method to remove minium element from min heap
    def extract_min(self):
        if len(self.heap) > 0:
            return heappop(self.heap)
        return None
  
    # This functon deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()
  
    # Get the minimum element from the heap
    def get_min(self):
        return self.heap[0]

    def get_size(self):
        return len(self.heap);


    def get_value(self, i):
        if i < len(self.heap):
            return self.heap[i]
        return None
  
# Driver pgoratm to test above function
# heapObj = MinHeap()

# heapObj.insert_key(3, 'B')
# heapObj.insert_key(2, 'D')

# heapObj.delete_key(1)

# heapObj.insert_key(6, 'E')
# heapObj.insert_key(7, 'A')
# heapObj.insert_key(7, 'C')
# heapObj.insert_key(1, 'F')

# print("Print all")
# heapObj.print_all()

# print("Extract min")
# print(heapObj.extract_min())

# print("Extract min")
# print(heapObj.extract_min())

# print("Extract min")
# print(heapObj.extract_min())

# print("Extract min")
# print(heapObj.extract_min())
# print(f"value at index 2 {heapObj.get_value(2)}")
# heapObj.decrease_key(2, 1)
# print(f"value at index 2 {heapObj.get_value(2)}")
# print(heapObj.get_min())

"""
Node implementation
"""
class Node:
    def __init__(self, character, priority):
        """
        Constructor:
        If this node is not character node, character is None.
        """
        self.character = character
        self.priority = priority
        self.left = None
        self.right = None
    
    def get_character(self):
        return self.character;

    def get_priority(self):
        return self.priority

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, Node)):
            return False
        return self.priority == other.priority

class HuffmanNode:
    def __init__(self, binary_code, node):
        self.binary_code = binary_code;
        self.node = node;

    def get_binary_code(self):
        return self.binary_code
    
    def get_node(self):
        return self.node

from queue import Queue

def extract_char_frequence(data):
    """
    Extract character and frequence into a dictionary
    """
    char_frequency = dict()
    for char in data:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency

def create_priority_queue(char_frequency_dict):
    """
    From a dictionary of charater and its frequency, create a priority queue using MinHeap data structure.
    Return priority queue at the end.
    """
    heap = MinHeap()
    for char, frequency in char_frequency_dict.items():
        char_node = Node(char, frequency)
        heap.insert_key(frequency, char_node)
    return heap

def build_tree(priority_queue):
    """
    From a priority_queue build a tree and return root node
    """
    while priority_queue.get_size() > 1:
        left = priority_queue.extract_min()
        right = priority_queue.extract_min()
        sum_priority = left[0] + right[0]
        node = Node(None, sum_priority)
        node.set_left(left[1])
        node.set_right(right[1])
        priority_queue.insert_key(sum_priority, node)
    root = priority_queue.extract_min()[1]
    return root

def huffman_encoding(data):

    def traverse(root):
        
        """
        Traverse the tree and return a dictionary of huffman code of all characters
        """

        def extract_huffman_node(huffman_node):
            """
            From a huffman_node, return a tuple of left_huffman_node and right_huffman_node
            """
            node = huffman_node.get_node()
            binary_code = huffman_node.get_binary_code()
            left_node = node.get_left()
            right_node = node.get_right()
            
            left_node_binary_code = binary_code + '0' if binary_code else '0'
            right_node_binary_code = binary_code + '1' if binary_code else '1'

            left_huffman_node = HuffmanNode(left_node_binary_code, left_node)
            right_huffman_node = HuffmanNode(right_node_binary_code, right_node)

            return (left_huffman_node, right_huffman_node)

        def traverse_recursive(huffman_queue, huffman_dict):
            if not huffman_queue.empty():
                huffman_node = huffman_queue.get()
                character = huffman_node.get_node().get_character()
                
                if character:
                    huffman_dict[character] = huffman_node.get_binary_code() if huffman_node.get_binary_code() else '0'
                else:
                    left_huffman_node, right_huffman_node = extract_huffman_node(huffman_node)
                    
                    queue.put(left_huffman_node)
                    queue.put(right_huffman_node)

                traverse_recursive(queue, huffman_dict)

        queue = Queue()
        huffman_root = HuffmanNode(None, root)
        queue.put(huffman_root)
        huffman_dict = dict()
        traverse_recursive(queue, huffman_dict)
        return huffman_dict

    def encode_data(data, encode_dict = dict):
        """
        Create an encode_data string after map each character in data to relate encode.
        """
        result = ""
        for char in data:
            result += encode_dict.get(char, 0)
        return result

    char_frequency_dict = extract_char_frequence(data)
    priority_queue = create_priority_queue(char_frequency_dict)
    root = build_tree(priority_queue)
    huffman_dict = traverse(root)
    encode_data = encode_data(data, huffman_dict)
    return encode_data, root
    

def huffman_decoding(data,tree):
    if data == '' or not tree:
        return ""

    decoded_data = ""
    node = tree
    for i in range(len(data)):

        if node == tree and node.get_character():
            decoded_data += node.get_character()
            node = tree
        else:
            if data[i] == '0':
                node = node.get_left()
            elif data[i] == '1':
                node = node.get_right()
            if node.get_character():    # found a character match
                decoded_data += node.get_character()
                node = tree

    return decoded_data

import sys

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The world is big"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


