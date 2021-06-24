"""
Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. 
If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. 
If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. 
After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. 
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. 
For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

    In case of a cache hit, your get() operation should return the appropriate value.
    In case of a cache miss, your get() should return -1.
    While putting an element in the cache, your put() / set() operation must insert the element. 
    If the cache is full, you must write code that removes the least recently used entry first and then insert the element.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enque(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def deque(self):

        if self.is_empty():
            return None
        
        result = self.head.data
        new_head = self.head.next
        self.head.next = None
        self.head = new_head
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return result

    def is_empty(self):
        return self.size == 0;

    def __str__(self) -> str:
        node = self.head
        result = list()
        while node:
            result.append(node.data)
            node = node.next
        return f"{result}"

class Cache:

    def __init__(self, value):
        self.value = value
        self.count = 1
    
    def decrease_count(self):
        if self.count > 0:
            self.count -= 1;
    
    def increase_count(self):
        self.count += 1;
    
    def is_count_reach_zero(self):
        return self.count == 0

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def __str__(self):
        return f"value: {self.value}, count: {self.count}"

class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.cache = {} # cache will map key and (value, count)
        self.capacity = capacity if capacity > 0 else 5
        # we use Queue to keep track of item recently use
        self.tracker = Queue()

    def get_capacity(self):
        return self.capacity;

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # if the item is in cache. we need to update tracking
        cache = self.cache.get(key);
        if not cache:
            return -1
        # TODO: update tracking
        cache.increase_count();
        self.__update_tracking__(key);

        return cache.get_value();

    def set(self, key, value):
        """Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item."""
        if self.capacity == len(self.cache):
            #TODO: Delete oldest item
            self.__remove_oldest_item__();

        # Update the cache
        cache = self.cache.get(key)
        if cache:
            cache.set_value(value)
            cache.increase_count()
        else:
            cache = Cache(value)
            self.cache[key] = cache
        
        # Update tracker
        self.__update_tracking__(key)
    
    def __update_tracking__(self, key):
        """
        Update the tracker by enque the key into the tracker, because key is the most recent used item.
        """
        self.tracker.enque(key)
        

    def __remove_oldest_item__(self):
        """
        Dequeue an item from tracker. 
        Reduce count of that item from the cache. If the count reach 0 => Remove that item from cache.
        If the count of that item does not reach 0 => Repeating the process until we found an item with count is 0 after reduction.
        """
        while not self.tracker.is_empty():
            item = self.tracker.deque();
            cache = self.cache.get(item)
            if cache:
                cache.decrease_count()
                if cache.is_count_reach_zero():
                    self.cache.pop(item, None)
                    return;
    
    def print_tracker(self):
        print(f"tracker {self.tracker}")

    def print_cache(self):
        for key, cache in self.cache.items():
            print(f"key: {key}, cache: {cache}")


def test_case_1():
    print("**********Test_case_1**********")
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print(our_cache.get(1))      
    # returns 1
    print(our_cache.get(2))        
    # returns 2
    print(our_cache.get(9))       
    # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    print(our_cache.get(3))       
    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

def test_case_2():
    """
    Testing edge case with one of the value is None
    """
    print("**********Test_case_2**********")
    our_cache = LRU_Cache(5)
    our_cache.set(1, None);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print(our_cache.get(1))      
    # returns None

def test_case_3():
    """
    Testing default capacity is 5
    """
    print("**********Test_case_3**********")
    our_cache = LRU_Cache()
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    our_cache.set(5, 5);

    print(our_cache.get(1)) 
    # returns 1
    print(our_cache.get(2))      
    # returns 2
    print(our_cache.get(3))     
    # returns 3
    print(our_cache.get(4))      
    # returns 4
    print(our_cache.get(5))     
    # returns 5

    our_cache.set(6, 6);
    
    print(our_cache.get(1)) 
    # return -1, because 1 was deleted
    print(our_cache.get(6)) 
    # return 6


def test_case_4():
    """
    Testing edge case: Getting the same value over and over again to see if the program works
    """
    print("**********Test_case_4**********")
    our_cache = LRU_Cache()
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    our_cache.set(5, 5);

    print(our_cache.get(1)) 
    # returns 1
    print(our_cache.get(1)) 
    # returns 1
    print(our_cache.get(1)) 
    # returns 1
    print(our_cache.get(1)) 
    # returns 1
    print(our_cache.get(1)) 
    # returns 1


def test_case_5():
    """
    Testing edge case: Capacity is negative value
    """
    print("**********Test_case_5**********")
    our_cache = LRU_Cache(-5)
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    our_cache.set(5, 5);

    print(our_cache.get(1)) 
    # returns 1
    print(our_cache.get(2)) 
    # returns 2
    print(our_cache.get(3)) 
    # returns 3
    print(our_cache.get(4)) 
    # returns 4
    print(our_cache.get(5)) 
    # returns 5


def test_case_6():
    """
    Testing edge case: Getting invalid value only
    """
    print("**********Test_case_6**********")
    our_cache = LRU_Cache()
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    our_cache.set(5, 5);

    print(our_cache.get(6)) 
    # returns -1
    print(our_cache.get(7)) 
    # returns -1
    print(our_cache.get(8)) 
    # returns -1
    print(our_cache.get(9)) 
    # returns -1
    print(our_cache.get(10)) 
    # returns -1


def test_case_7():
    """
    Testing edge case: Input is None
    """
    print("**********Test_case_7**********")
    our_cache = LRU_Cache(-5)
    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);
    our_cache.set(5, 5);

    print(our_cache.get(None)) 
    # returns -1
    

test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()
test_case_6()
test_case_7()