from collections import deque

queue = deque()
queue.appendleft(1)
queue.appendleft(2) # enqueue

item = queue.pop() #dequeue
# print(item)

# print(queue)


stack = []
stack.append(1) # push
stack.append(5)

item = stack.pop()
print(item)
print(stack)