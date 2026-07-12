import queue

q = queue.Queue()   # Create a Queue object

q.put('a')
q.put('s')
q.put(3)

print(q.get())      # a
print(q.get())      # s
print(q.get())      # 3