#!/usr/bin/env python
# coding: utf-8
'''
Author: Devendra
'''
from logger import LOGGER

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node("Head")

    @property
    def length(self):
        """Get the total length of list."""
        cur = self.head
        count = 0
        while cur.next:
            count += 1
            cur = cur.next
        return count

    def display(self):
        """Display the list."""
        cur = self.head
        while cur.next:
            cur = cur.next
            print(cur.data,end=' ')
        print()

    def insert_begin(self, data):
        """Add a node at the start the list."""
        new_node = Node(data)
        cur = self.head
        new_node.next = cur.next
        cur.next = new_node

    def insert_end(self, data):
        """Add a node at the end of the list."""
        new_node = Node(data)
        cur = self.head
        while cur.next:
            cur =  cur.next
        cur.next = new_node

    def delete(self):
        """Delete a node."""
        cur = self.head
        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None

    def get_at(self, index):
        """Get the value of the node at given index."""
        cur = self.head
        cur_idx = 0
        len_ = self.length
        if index >= len_:
            LOGGER.error(f"Index larger than the length of linked list, {len_}")
            return None
        while cur_idx != index:
            cur_idx += 1
            cur = cur.next
        return cur.next.data

    def insert_at(self, data, index):
        """Add the value of the node at given index."""
        new_node = Node(data)
        cur = self.head
        cur_idx = 0
        len_ = self.length
        if index >= len_:
            LOGGER.error(f"Index larger than the length of linked list, {len_}")
            return None
        while cur_idx != index:
            cur_idx += 1
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

    def delete_at(self, index):
        """Delete the node at given index."""
        cur = self.head
        cur_idx = 0
        len_ = self.length
        if index >= len_:
            LOGGER.error(f"Index larger than the length of linked list, {len_}")
            return None
        while cur_idx != index:
            cur_idx += 1
            cur = cur.next
        cur.next = cur.next.next

    def search(self, data):
        """
        Search for the value.
        @return: False if not present
        """
        cur = self.head
        cur_idx = 0
        while cur.next and cur.next.data != data:
            cur = cur.next
            cur_idx += 1 

        if not cur.next:
            LOGGER.error("Given value is not present.")
            return None
        LOGGER.info(f"Given value present at index-{cur_idx}")
        return True

    def delete_this(self, data):
        """Delete a particular value."""
        cur = self.head
        # self.search(data)
        len_ = self.length
        while cur.next.data != data:
            cur = cur.next 
            len_ -= 1
            if len_ == 0:
                LOGGER.error("Given value is not present.")
                return None
        cur.next = cur.next.next
        return True

    def replace(self, now, new):
        """Repalce the value."""
        cur = self.head
        cur_idx = 0
        while cur.next and cur.next.data != now:
            cur = cur.next
            cur_idx += 1 

        if not cur.next:
            LOGGER.error("Given value not present.")
            return None
        cur.next.data = new
        return True

    def swap(self, data1, data2):
        """Swap the given values."""
        cur = self.head
        while cur.next:
            if cur.next.data == data1:
                cur.next.data = data2
            elif cur.next.data == data2:
                cur.next.data = data1
            cur = cur.next

    def count(self, data):
        """Number of times the given data is present in the list."""
        cur = self.head
        count = 0
        while cur.next:
            if cur.next.data == data:
                count += 1
            cur = cur.next

        return count

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        cur = self.head
        last = cur.next
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        last.next.next = prev
        last.next = None
