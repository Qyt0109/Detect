from datetime import datetime
import queue

class QueueEvent():
    def __init__(self, event, time:str = None) -> None:
        self.time = time if time else datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.event = event

class MaxSizeQueue(queue.Queue):
    def __init__(self, max_size=10):
        super().__init__(maxsize=max_size)

    def put(self, item, block=True, timeout=None):
        # If the queue is full, remove the oldest item before putting a new one
        if self.full():
            self.get_nowait()
        super().put(item, block, timeout)

"""Exaple
my_queue = MaxSizeQueue(max_size=10)

for i in range(15):
    my_queue.put(i)
    print(f"Put: {i}, Queue Size: {my_queue.qsize()}")

# The queue will only have the last 10 elements due to the maximum size restriction
while not my_queue.empty():
    print(f"Get: {my_queue.get()}, Queue Size: {my_queue.qsize()}")
"""