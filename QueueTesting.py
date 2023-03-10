# Queue Testing 

from queues import Queue

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print("Testing 1:")
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())

print("\nTesting 2:")
fifo = Queue("1st", "2nd", "3rd")
print("Initial length:",len(fifo))

for element in fifo:
    print(element)

print("Final length:",len(fifo))
