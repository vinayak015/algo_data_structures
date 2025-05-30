"""
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.
"""

from collections import deque

class StockSpanner:

    def __init__(self):
        self.stack = deque()

    def next_(self, price: int) -> int:
        self.queue.append(price)
        stack = deque()
        for num in self.queue:
            while stack and stack[-1] > price:
                stack.popleft()
            stack.append(num)
        return len(stack)

    def next(self, price):
        ans = 1
        while self.stack and self.stack[-1][0] < price:
            ans += self.stack.pop()[1]
        self.stack.append([price, ans])
        return ans



if __name__ == "__main__":
    # Your StockSpanner object will be instantiated and called as such:
    obj = StockSpanner()
    print(obj.next(100))
    print(obj.next(80))
    print(obj.next(60))
    print(obj.next(70))
    print(obj.next(60))
    print(obj.next(75))
    print(obj.next(85))