# """
# Problem 3.1. Three in One: Describe how you could use a single array to implement three stacks

# Consider an array of size 100. 100//3=33. Stack 1 gets index 0 to 32. Stack 2 gets index 33 to 65. Stack 3 gets rest.  
# push, pop, peek, isEmpty
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
push, pop, peek, isEmpty
Need to pass stack number for all of these methods 
"""

class TripleStack:
    def __init__(self, stackSize):
        self._capacity = stackSize
        self._arr = [None] * 3 * stackSize
        self._sizes = [0, 0, 0]

    def printTripleStack(self):
        for i in self._arr:
            print(i)

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

    def peek(self, stackNum):
        if self._sizes[stackNum] == 0:
            raise Exception("Stack Empty")
        else:
            return self.computeTopIndex(stackNum)

    def pop(self, stackNum, val):
        if self._sizes[stackNum] == 0:
            raise Exception("Stack Empty")
        else:
            self._sizes[stackNum] -= 1

tripleStack = TripleStack(2)
for i in range(5):
    #0 0 1 1 
    tripleStack.push(i // 2, i)
tripleStack.printTripleStack()
# tripleStack.push(0, 0)
# print(tripleStack._arr[0])
# tripleStack.push(0, 1)
# print(tripleStack._arr[1])
# tripleStack.push(1, 2)
# print(tripleStack._arr[2])
print(tripleStack.peek(2))


