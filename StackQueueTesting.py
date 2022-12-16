#  Stack Queue Testing

from queues import Stack

print("Testing 1:")
lifo = Stack("1st", "2nd", "3rd")

for element in lifo:
    print(element)

print("\nTesting 2:")
lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print(lifo.pop())
print(lifo.pop())
print(lifo.pop())