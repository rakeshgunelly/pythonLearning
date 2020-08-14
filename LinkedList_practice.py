'''
https://github.com/codebasics/py/blob/master/DataStructures/3_LinkedList/3_linked_list.py
https://github.com/codebasics/py/blob/master/DataStructures/3_LinkedList/Solution/singly_linked_list_exercise.py
above is the reference of the below code
'''

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        if self.head==None:
            print('Linkedlist is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr :
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr =  self.head
        while itr.next:
            itr = itr.next
    
        itr.next = Node (data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        
        return count
        
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
    
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next


''' # this was written by me
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        count = 1
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count, data_to_insert)
                
            itr = itr.next
            count +=1

    def remove_by_value(self, data):
    # Remove first node that contains data
        count = 0
        itr = self.head
        
        while itr:
            if itr.data == data:
                self.remove_at(count)

            itr = itr.next
            count += 1 
'''

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value("apple")
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()
