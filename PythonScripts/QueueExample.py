# Use deque for fast appends and pops
from collections import deque
queue = deque(["Bob","Adolf"])
print('Queue ', queue)
print('Append St. Michael the Archangel ') 
queue.append("St. Michael the Archangel")
print('Append Doctor Faustus ')
queue.append("Doctor Faustus")
print('Printing queue ... ', queue)
print('popleft ', queue.popleft())
print('popleft again', queue.popleft())
print(queue)


