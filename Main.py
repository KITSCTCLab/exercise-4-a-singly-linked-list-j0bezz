from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """
    def __init__(self):
        """
        Initialize the head
        """
        self.head = None
        
    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """
        # Write code here
        new= Node(data,None)
        self.temp=self.head
        if self.temp.next != None:
            self.temp=self.temp.next
        self.temp.next=new.data

    def status(self):
        """
        It prints all the elements of list.
        """
        # write code here
        self.temp=self.head
        while true:
            if(self.temp.next==None):
                print(self.temp.data)
                break
            else:
                print(self.temp.data)
                self.temp=self.temp.next


class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        # Write code here
        self.first=[]
        self.second=[]
        self.result=[]
        for i in first_list:
            self.first.append(i)
        for i in second_list:
            self.second.append(i)
        self.f=self.first[::-1]
        self.l=self.last[::-1]
        for i in range(0,len(self.f)-1):
            temp=self.f[i]+self.l[i]
            self.result.append(temp)
        return self.result
        

# Do not edit the following code      
# Create an instance for LinkedList
first_list = LinkedList()
# Create an another instance for LinkedList
second_list = LinkedList()
# Read data for first list
data_for_first_list = list(map(int, input().strip().split(" ")))
# Add data at the end of first_list
for data in data_for_first_list:
    first_list.insert_at_end(data)
# Read data for second list
data_for_second_list = list(map(int, input().strip().split(" ")))
# Add data at the end of second_list
for data in data_for_second_list:
    second_list.insert_at_end(data)
# Create an instance for Solution
solution = Solution()
# Pass first_list and second_list to addTwoNumbers, which returns a new linked list
new_list = solution.addTwoNumbers(first_list, second_list)
# Display the status of new_list
new_list.status()
