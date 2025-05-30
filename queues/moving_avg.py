"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
"""

from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = deque(maxlen=size)

        self.window_sum = 0
        self.count = 0

    def next(self, val):
        self.count += 1
        self.queue.append(val)

        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)
