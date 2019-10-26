
'''
Implementation of Doubly Linked List by Deshmukh Devendra N.
'''
class Node:
    def __init__(self,data = None):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node("Head")
    
    def display(self):
        cur = self.head
        while cur.next:
            print(cur.next.data,end = " ")
            cur = cur.next
        print()  

    def length(self):
        cur = self.head
        count = 0
        while cur.next:
            count += 1
            cur = cur.next
        return count
            
    def insert_end(self,node):
        new = Node(node)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new
        new.prev = cur

    def insert_begin(self,node):
        new = Node(node)
        cur = self.head
        cur.next.prev = new
        new.next = cur.next
        new.prev = cur
        cur.next = new
            
        
    def delete(self,node):
        cur = self.head
        while cur.next:
            next = cur.next
            if next.data == node:
                cur.next = next.next
                next.prev = cur
                return
            cur = cur.next
        else:
            print("Node not found")
    
    def reverse(self):
        cur = self.head
        prev = cur.prev
        last = cur.next
        while cur:
            next = cur.next
            cur.next = prev
            cur.prev = next
            prev = cur
            cur = next
        self.head.next = prev
        last.next = None
        self.head.prev = None
        self.display()
