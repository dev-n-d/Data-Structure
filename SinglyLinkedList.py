#!/usr/bin/env python
# coding: utf-8
'''
Implementation of Singly Linked List by Deshmukh Devendra N.
'''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node("Head")

    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count

    def display(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data,end=' ')
        print()

    def insert_begin(self,data):
        new_node = node(data)
        cur = self.head
        new_node.next = cur.next
        cur.next = new_node

    def insert_end(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur =  cur.next
        cur.next = new_node

    def delete(self):
        cur = self.head
        while cur.next != None:
            prev = cur
            cur = cur.next
        prev.next = None

    def getAt(self,index):
        cur = self.head
        cur_idx = 0
        if index >= self.length():
            print("ERROR! Index out of bounds")
            return None
        while cur_idx != index:
            cur_idx += 1
            cur = cur.next
        print(cur.next.data)

    def insertAt(self,data,index):
        new_node = node(data)
        cur = self.head
        cur_idx = 0
        while cur_idx != index:
            cur_idx += 1
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

    def deleteAt(self,index):
        cur = self.head
        cur_idx = 0
        while cur_idx != index:
            cur_idx += 1
            cur = cur.next
        cur.next = cur.next.next

    def search(self,data):
        cur = self.head
        cur_idx = 0
        while cur.next != None and cur.next.data != data:
            cur = cur.next
            cur_idx += 1 

        if cur.next == None:
            print("No data found")
            return None
        else:
            print("given data at index = ",cur_idx)
            return True

    def deleteThis(self,data):
        cur = self.head
        # self.search(data)
        l = self.length()
        while cur.next.data != data:
            cur = cur.next 
            l -= 1
            if l == 0:
                print("No data found")
                return None
        cur.next = cur.next.next

    def replace(self,now,new):
        cur = self.head
        cur_idx = 0
        while cur.next != None and cur.next.data != now:
            cur = cur.next
            cur_idx += 1 

        if cur.next == None:
            print("No data found")
            return None
        else:
            cur.next.data = new
            return None

    def swap(self,data1,data2):
        cur = self.head
        while cur.next != None:
            if cur.next.data == data1:
                cur.next.data = data2
            elif cur.next.data == data2:
                cur.next.data = data1
            cur = cur.next

    def count(self,data):
        cur = self.head
        count = 0
        while cur.next != None:
            if cur.next.data == data:
                count += 1
            cur = cur.next
        if count:
            print(count)
            return count
        else:
            print("No data found")
            return None

    def reverse(self):
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
            