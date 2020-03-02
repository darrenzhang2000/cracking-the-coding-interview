import random
import queue

# traverse linked list and throw values into a set
# if this item is in the set link prev item to next item (which could be empty)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        cur_ptr = self.head
        while cur_ptr:
            print(cur_ptr.val)
            cur_ptr = cur_ptr.next


def remove_duplicates(llist):
    """
        Problem 2.1: Remove duplicates from an unsorted linked lsit
    """
    memo = set()
    if not llist.head:
        return
    memo.add(llist.head.val)
    prev = llist.head
    cur = llist.head.next
    while(cur):
        # if !cur.next:
        if cur.val in memo:
            # print('prev value is ', prev.val, 'cur value is ', cur.val)
            cur = cur.next
            prev.next = cur
            # print('after removing dup', 'prev value is ', prev.val, 'cur value is ', cur.val)
        else:
            memo.add(cur.val)
            cur = cur.next
            prev = prev.next

    return


x = LinkedList()
x.head = Node(1)
for i in range(5):
    y = Node(i)
    z = Node(i)
    y.next = z
    z.next = x.head
    x.head = y


# remove_duplicates(x)
# x.printList()

def kthToLast(head, k):
    """
    Recursive Solution
    """
    if not head:
        return 0
    index = kthToLast(head.next, k) + 1
    if index == k:
        print(head.val)
    return index


# def kthToLast(head, k):
#     """
#     2.2 Return kth to last element of a singly linked list

#     cur hits nullptr first, prev is exactly k steps behind cur
#     """
#     slow = head
#     fast = head
#     for i in range(k):
#         try:
#             fast = fast.next
#         except AttributeError:
#             print("kth element DNE")

#     while fast:
#         slow = slow.next
#         fast = fast.next
#     return slow.val


b = LinkedList()
b.head = (Node(10))
for i in range(9, 0, -1):
    temp = Node(i)
    temp.next = b.head
    b.head = temp

# print(kthToLast(b.head, 3))
# b.printList()

c = LinkedList()
c.head = (Node(1))
# print(kthToLast(c.head, 10))


def deleteMiddleNode(head: Node):
    """
        Problem 2.3 Delete a node in the middle. 

        If there are an even number of nodes
    """
    fast = head
    slow = Node(None)
    slow.next = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    slow.next = slow.next.next
    return

# deleteMiddleNode(b.head)
# b.printList()

# def partition(head: Node, pivot: int):
#     """
#         Problem 2.4 Partition a linked list around x such that all nodes less than x come before
#         all nodes greater than or equal to x
#     """
#     lower_head = None
#     higher_head = None 
#     cur = head
#     while cur != None:
#         print("current value: ", cur.val)
#         if cur.val < pivot:
#             if lower_head == None:
#                 print("set lower head")
#                 lower_head = cur
#                 cur = cur.next
#                 lower_head.next = None
#                 if(not cur):
#                     print("empty cur after 1")
#             else:
#                 temp = cur
#                 cur = cur.next
#                 temp.next = lower_head
#                 lower_head = temp
#                 print("else 1")
#                 if(not cur):
#                     print("empty cur after 2")
#         else:
#             if higher_head == None:
#                 print("set higher head")
#                 higher_head = cur
#                 cur = cur.next
#                 higher_head.next = None
#                 if(not cur):
#                     print("empty cur after 3")
#             else:
#                 temp = cur
#                 cur = cur.next
#                 temp.next = higher_head
#                 higher_head = temp 
#                 print("else 2")
#                 if(not cur):
#                     print("empty cur after 4")
#     head = lower_head
#     print("end of while loop")
#     while lower_head.next != None:
#         print("infinite")
#         lower_head = lower_head.next
#     lower_head.next = higher_head
#     return head 

def partition(cur: Node, pivot: int):
    """
        Problem 2.4 Partition a linked list around x such that all nodes less than x come before
        all nodes greater than or equal to x
    """
    if not cur:
        return None
    l_h = None
    l_t = None
    h_h = None
    h_t = None
    while cur:
        next = cur.next
        cur.next = None
        if cur.val < pivot:
            if l_h == None:
                l_h = cur
                l_t = cur
            else:
                l_t.next = cur
                l_t = l_t.next
        else:
            if h_h == None:
                h_h = cur 
                h_t = cur 
            else:
                h_t.next = cur
                h_t = h_t.next
        cur = next 
    if not l_h:
        return h_h
    l_t.next = h_h 
    return l_h

mango = LinkedList()
mango.head = Node(49)
z = Node(100)
a = Node(25)
b = Node(75)
c = Node(80)
d = Node(20)
e = Node(90)
f = Node(1)
mango.head.next = a
a.next = z
z.next = b
b.next = c
c.next = d 
d.next = e 
e.next = f

# for i in range(10):
#     temp = Node((int)(random.random() * 100))
#     temp.next = mango.head
#     mango.head = temp

# print("before partition")
# mango.printList()
# print("after partition")
# partition(mango.head, 50)
# mango.printList()

def nodeAdd(n1, n2):
    """
    Problem 2.5. Sum Lists: Adds two numbers and returns as linked list

    7 -> 1 -> 6 + 5 -> 9 -> 2
    yields 912
    """
    start, end = None, None 
    carry, digit = 0, 0
    while n1 and n2:
        digit = (n1.val + n2.val + carry) % 10
        carry = (n1.val + n2.val + carry) // 10
        if not start:
            start = Node(digit)
            end = start 
        else:
            end.next = Node(digit)
            end = end.next
        n1 = n1.next
        n2 = n2.next
    while n1:
        digit = (n1.val + carry) % 10
        carry = (n1.val + carry) // 10
        if not start:
            start = digit
            end = digit
        else:
            end.next = digit
            end = end.next
    while n2:
        digit = (n2.val + carry) % 10
        carry = (n2.val + carry) // 10
        if not start:
            start = digit
            end = digit
        else:
            end.next = digit
            end = end.next
    return start

a5 = Node(6)
b5 = Node(1)
c5 = Node(7)
pineapple = LinkedList()
pineapple.head = c5
c5.next = b5
b5.next = a5

d5 = Node(5)
f5 = Node(9)
g5 = Node(2)
peach = LinkedList()
peach.head = d5 
d5.next = f5 
f5.next = g5

# pineapple.printList()
# peach.printList()

# strawberry = LinkedList()
# strawberry.head = nodeAdd(pineapple.head, peach.head)
# strawberry.printList()

def isPalindrome(head: Node):
    """
    Problem 2.6. Palindrome: check if a linked list is a palindrome
    """
    if head ==  None:
        return True 
    
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next  
    
    if fast != None: #odd length
        slow = slow.next
    
    stack = []
    while slow:
        stack.append(slow.val)
        slow = slow.next

    cur = head
    while len(stack) > 0:
        if stack.pop() != cur.val:
            return False
        cur = cur.next
    return True
    
    
    

# def isPalindrome(head: Node):
#     """
#     Problem 2.6. Palindrome: check if a linked list is a palindrome
#     """
#     if head ==  None:
#         return True 
#     stack = []
#     q = queue.Queue()
#     cur = head
#     while cur:
#         stack.append(cur.val)
#         q.put(cur.val)
#         cur = cur.next
#     while not q.empty():
#         if q.get() != stack.pop():
#             return False
#     return True

a6 = Node(1)
b6 = Node(2)
c6 = Node(3)
d6 = Node(2)
e6 = Node(1)
watermelon = LinkedList()
watermelon.head = a6
a6.next = b6
b6.next = c6
c6.next = d6
d6.next = e6
# print(isPalindrome(watermelon.head))
