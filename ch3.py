# """
# Problem 3.1. Three in One: Describe how you could use a single array to implement three stacks

# Consider an array of size 100. 100//3=33. Stack 1 gets index 0 to 32. Stack 2 gets index 33 to 65. Stack 3 gets rest.
# push, pop, top, isEmpty
# Need to pass stack number for all of these methods
# """

# class TripleStack:
#     def __init__(self, arraySize):
#         self.arraySize = arraySize
#         self.STACK0_START = 0
#         self.STACK1_START = arraySize // 3
#         self.STACK2_START = arraySize // 3 * 2
#         self.arr = [None] * arraySize
#         self.stack0_top_index = None
#         self.stack1_top_index = None
#         self.stack2_top_index = None

#     #Just for testing purposes
#     def printTripleStack(self):
#         for i in self.arr:
#             print(i)

#     def push(self, stackNum, val):
#         if stackNum == 0:
#             # print("stack0_top_index", self.stack0_top_index)
#             # print("stack1_start", self.STACK1_START)
#             # print(self.stack0_top_index + 1 < self.STACK1_START)
#             if self.stack0_top_index == None:
#                 self.stack0_top_index = self.STACK0_START
#                 self.arr[self.stack0_top_index] = val
#             elif self.stack0_top_index + 1 < self.STACK1_START:
#                 print()
#                 self.stack0_top_index += 1
#                 self.arr[self.stack0_top_index] = val
#             else:
#                 raise IndexError('Stack 1 Full')
#         elif stackNum == 1:
#             if self.stack1_top_index == None:
#                 self.stack1_top_index = self.STACK1_START
#                 self.arr[self.stack1_top_index] = val
#             elif self.stack1_top_index + 1 < self.STACK2_START:
#                 self.stack1_top_index += 1
#                 self.arr[self.stack1_top_index] = val
#             else:
#                 raise IndexError('Stack 2 Full')
#         elif stackNum == 2:
#             if self.stack2_top_index == None:
#                 self.stack2_top_index = self.STACK2_START
#                 self.arr[self.stack2_top_index] = val
#             elif self.stack2_top_index < self.arraySize:
#                 self.stack2_top_index += 1
#                 self.arr[self.stack2_top_index] = val
#             else:
#                 raise IndexError('Stack 3 Full')


# # tripleStack = TripleStack(6)
# # for i in range(6):
# #     #0 0 1 1
# #     tripleStack.push(i // 2, i)
# # tripleStack.printTripleStack()
# # tripleStack.push(0, 0)
# # print(tripleStack.arr[0])
# # tripleStack.push(0, 1)
# # print(tripleStack.arr[1])
# # tripleStack.push(1, 2)
# # print(tripleStack.arr[2])

"""
Problem 3.1. Three in One: Describe how you could use a single array to implement three stacks

Consider an array of size 100. 100//3=33. Stack 1 gets index 0 to 32. Stack 2 gets index 33 to 65. Stack 3 gets rest.
push, pop, top, isEmpty
Need to pass stack number for all of these methods
"""


class TripleStack:
    def __init__(self, stackSize):
        self._capacity = stackSize
        self._arr = [None] * 3 * stackSize
        self._sizes = [0, 0, 0]

    # def printTripleStack(self):
    #     for i in self._arr:
    #         print(i)

    def computeTopIndex(self, stackNum):
        offset = stackNum * self._capacity
        return offset + self._sizes[stackNum] - 1

    def push(self, stackNum, val):
        if self._sizes[stackNum] >= self._capacity:
            raise IndexError("Stack {} is full".format(stackNum))
        else:
            self._sizes[stackNum] += 1
            topIndex = self.computeTopIndex(stackNum)
            self._arr[topIndex] = val

    def top(self, stackNum):
        if self._sizes[stackNum] == 0:
            raise Exception("Stack Empty")
        else:
            return self.computeTopIndex(stackNum)

    def pop(self, stackNum):
        if self._sizes[stackNum] == 0:
            raise Exception("Stack Empty")
        else:
            self._sizes[stackNum] -= 1


tripleStack = TripleStack(2)
for i in range(6):
    # 0 0 1 1
    tripleStack.push(i // 2, i)
# tripleStack.printTripleStack()
# tripleStack.push(0, 0)
# print(tripleStack._arr[0])
# tripleStack.push(0, 1)
# print(tripleStack._arr[1])
# tripleStack.push(1, 2)
# print(tripleStack._arr[2])
# print(tripleStack.top(2))
# tripleStack.pop(0)
# tripleStack.pop(0)
# print(tripleStack.top(1))


"""
Problem 3.2. Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? 
Push, pop, min should all operate in O(1) time.

Soln 1:
As you push elements onto the stack, check to see if val is smaller than min. If so, let min to val.
After popping elements off the stack, check if the stack is empty. If so, set min to None. 
Bad because we need a way a store the min at each value on the stack

Soln 2:
As you push elements onto the stack, check to see if new element is <= min. If so, push min onto minStack. 
That way, we only push elements onto the minStack only if the minimum changes.
When we pop elements off the original stack, we only pop elements off the minStack if top element of both stacks are equal. 
"""

class Stack:
    """
    A regular stack

    Private:
        Stack<int> _s
        int _size
    Public:
        void push(val)
        void pop()
        int top()
        bool isEmpty()
        int size()
    """
    def __init__(self):
        self._s = []
        self._size = 0
    
    def push(self, val):
        self._size += 1
        self._s.append(val)
        return

    def top(self):
        if self._size == 0:
            raise Exception("Stack empty")
        else:
            return self._s[self._size - 1]

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack already empty")
        else:
            self._s.pop()
            self._size -= 1
            return

    def isEmpty(self):
        return self._size == 0 

    def size(self):
        return self._size

# stack1 = Stack()
# stack1.push(0)
# print(stack1.top())
# stack1.push(1)
# print(stack1.top())
# stack1.pop()
# print(stack1.top())
# print(stack1.isEmpty())
# stack1.pop()
# print(stack1.isEmpty())
# print(stack1.top())

import sys
class StackWithMin(Stack):
    """
    As you push elements onto the stack, check to see if new element is <= min. If so, push min onto minStack. 
    That way, we only push elements onto the minStack only if the minimum changes.
    When we pop elements off the original stack, we only pop elements off the minStack if top element of both stacks are equal.    
    
    private:
        Stack<int> _minS
        int _curMin

        has private variables of base class
    public:
        void push(int)
        void pop()
        int min()

    """
    def __init__(self):
        super().__init__()
        self._minS = Stack()
        self._curMin = sys.maxsize

    def push(self, val):
        if val <= self._curMin:
            self._minS.push(val)
            self._curMin = val
        super().push(val)
        return

    def pop(self):
        if self._minS.top() == super().top():
            self._minS.pop()
            self._curMin = self._minS.top()
        super().pop()
        return

    def min(self):
        if self._minS.isEmpty():
            raise Exception("Stack Empty")
        else:
            return self._minS.top()


stackWithMin1 = StackWithMin()
stackWithMin1.push(4)
stackWithMin1.push(8)
stackWithMin1.push(6)
stackWithMin1.push(2)
stackWithMin1.push(9)
stackWithMin1.push(5)
stackWithMin1.push(3)
stackWithMin1.push(1)
stackWithMin1.push(7)

'''
1
1
2
2
2
2
4
4
4
'''
# for i in range(8):
#     print(stackWithMin1.min())
#     stackWithMin1.pop()
# stackWithMin1.push(0)
# print(stackWithMin1.top())

class StackOfPlates:
    """
    An array of stacks

    Private:
        _capacity
        _stackArray
    Same methods as stack. However, once a stack reaches capacity, the next push creates a new stack
        push(val)
        pop()
        top()
    """
    def __init__(self, capacity):
        self._capacity = capacity
        self._stackArray = []

    def push(self, val):
        if len(self._stackArray) == 0 or len(self._stackArray) >= self._capacity:
            curStack = Stack()
            curStack.push(val)
            self._stackArray.append(curStack)
        else: 
            self._stackArray[-1].push(val)

        
    def pop(self):
        if len(self._stackArray) == 0:
            raise Exception("Stack List Empty")
        else:
            curStack = self._stackArray[-1]
            curStack.pop()
            if curStack.isEmpty():
                self._stackArray.pop()

    def top(self):
        if len(self._stackArray) == 0:
            raise Exception("Stack Empty")
        else:
            curStack = self._stackArray[-1]
            return curStack.top()

# stackOfPlates1 = StackOfPlates(2)
# stackOfPlates1.push(0)
# # print(stackOfPlates1.pop())
# stackOfPlates1.push(1)
# print(stackOfPlates1.top())
# stackOfPlates1.push(2)
# print(stackOfPlates1.top())
# stackOfPlates1.push(3)
# print(stackOfPlates1.top())

"""
Problem 3.3 Follow up: Implement popAt(int index)

Soln 1: One method is have an array sizes that keeps track of all of the stacks in the list. 
We would also have to keep track of the offset, maybe using a helper.
If empty, don't do anything. Else, pop element at specified stack

Pros: Time efficient to remove
Cons: Holes 

Soln 2: Rollover method

public:
    popAt(int index) - Pop top val. If stack exists at index + 1, pop the bottom val and push it to stack at index. 
"""


class MyQueue:
    """
    Problem 3.5. Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks,

    To enqueue just push onto stack1.
    To dequeue, pop everything off stack1 and push onto stack2. When stack1 is empty, pop top off stack2. Then shove everything in stack2 onto stack1.
    """
    def __init__(self):
        self._stack1 = []
        self._stack2 = []
        return

    def put(self, val):
        self._stack1.append(val)
        return

    def get(self):
        while len(self._stack1):
            top = self._stack1.pop()
            self._stack2.append(top)
        first = self._stack2.pop()
        while len(self._stack2):
            top = self._stack2.pop()
            self._stack1.append(top)
        return first 

# myQ1 = MyQueue()
# myQ1.put(1)    
# myQ1.put(2)    
# myQ1.put(3)
# print(myQ1.get())    

"""
Problem 3.5. Sort Stack (smallest on top)

May use a temporary stack but no other data structures
"""

def sortStack(s):
    sorted_ = Stack()
    while not s.isEmpty():
        # print('mango', s.top())
        cur = s.top()
        s.pop()
        counter = 0
        while (not sorted_.isEmpty()) and (cur > sorted_.top()):
            s.push(sorted_.top())
            sorted_.pop()
            counter += 1
        sorted_.push(cur)
        while counter > 0:
            sorted_.push(s.top())
            s.pop()
            counter -= 1
    return sorted_

sortStack1 = Stack()

L = [1, 4, 6, 9, 2, 3, 5, 8]
for e in L:
    sortStack1.push(e)
print(sortStack1.size())
sortStack1 = sortStack(sortStack1)
print(sortStack1.size())

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

class Animal:
    _id = 0
    def __init__(self, animal):
        self._animal = animal
        self._id = Animal._id
        Animal._id += 1

from collections import deque

class AnimalShelter:
    _id = 0
    def __init__(self):
        self._catList = deque([])
        self._dogList = deque([])

    # def enqueue(self, animal):
    #     temp = Node(animal)
    #     if animal._animal == 'cat':
    #         if not self._catList.head:
    #             self._catList.head = temp 
    #             return
    #         cur = self._catList.head 
    #         while cur.next != None:
    #             cur = cur.next
    #         cur.next = temp
    #     elif animal._animal == 'dog':
    #         if not self._dogList.head:
    #             self._dogList.head = temp 
    #             return
    #         cur = self._dogList.head 
    #         while cur.next != None:
    #             cur = cur.next
    #         cur.next = temp
    #     else:
    #         raise Exception("Animal has to be cat or dog")

    def enqueue(self, animal):
        temp = Node(animal)
        if animal._animal == 'cat':
            self._catList.append(temp)
        elif animal._animal == 'dog':
            self._dogList.append(temp)
        else:
            raise Exception("animal not found")
    
    def dequeueCat(self):
        return self._catList.popleft()

    def dequeueDog(self):
        return self._dogList.popleft()

    def dequeueAny(self):
        if not self._dogListL
            return self.dequeueCat
        else:
            return self.dequeueDog
    