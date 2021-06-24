"""
Union and Intersection of Two Linked Lists

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, 
in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. 
Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def contains(self, value):
        """
        Check if this linkedList contains this value
        """
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    result = LinkedList()
    def append_lists(node):
        if node:
            result.append(node)
            node = node.next
            append_lists(node)

    node = llist_1.head
    append_lists(node)

    node = llist_2.head
    append_lists(node)

    return result

    

def intersection(llist_1, llist_2):
    intersection_list = LinkedList()
    
    def create_set(llist):
        """
        Create a set of unique element from llist
        """
        result = set()
        node = llist.head
        while node:
            result.add(node.value)
            node = node.next
        return result

    def traverse(node, another_set):
        """
        Recursively checking if a node is in another_set, if it is add to intersection_list.
        """
        if node:
            if node.value in another_set:
                intersection_list.append(node.value)
            node = node.next
            traverse(node, another_set)
    
    set_1 = create_set(llist_1)
    set_2 = create_set(llist_2)

    traverse(llist_1.head, set_2)
    traverse(llist_2.head, set_1)
    
    return intersection_list

# Test case 1
def test_case_1():
    """
    Normal test case
    """
    print("**************Test_case_1*****************")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(f"llist1: {linked_list_1}")
    print(f"llist2: {linked_list_2}")

    print (f"union result: {union(linked_list_1,linked_list_2)}")
    print (f"intersection result: {intersection(linked_list_1,linked_list_2)}")

# Test case 2
def test_case_2():
    """
    Normal test case
    """
    print("**************Test_case_2*****************")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(f"llist1: {linked_list_1}")
    print(f"llist2: {linked_list_2}")

    print (f"union result: {union(linked_list_1,linked_list_2)}")
    print (f"intersection result: {intersection(linked_list_1,linked_list_2)}")

# Test case 3
def test_case_3():
    """
    Edge test case. list1 is empty
    """
    print("**************Test_case_3*****************")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = []
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(f"llist1: {linked_list_1}")
    print(f"llist2: {linked_list_2}")

    print (f"union result: {union(linked_list_1,linked_list_2)}")
    print (f"intersection result: {intersection(linked_list_1,linked_list_2)}")

# Test case 4
def test_case_4():
    """
    Edge test case. both lists are empty
    """
    print("**************Test_case_4*****************")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(f"llist1: {linked_list_1}")
    print(f"llist2: {linked_list_2}")

    print (f"union result: {union(linked_list_1,linked_list_2)}")
    print (f"intersection result: {intersection(linked_list_1,linked_list_2)}")

test_case_1()
test_case_2()
test_case_3()
test_case_4()