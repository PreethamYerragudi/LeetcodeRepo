# Problem 901: Online Stock Span
# Difficulty: Medium
class StockSpanner:

    def __init__(self):
        self.stack = [] #define stack here because it will need to exist across all iterations 
        

    def next(self, price: int) -> int:
        counter = 1 #reset counter so it can be used as a default if prev prices are not less than curr
        while self.stack and self.stack[-1][0] <= price: #if stack, check that prices are less 
            #want to run loop as long as the existing top price is less than the curr; only pop when there's a price greater than stack that allows stack price to be encompassed into a span
            counter = self.stack[-1][1] + counter #add counter to the existing span 
            self.stack.pop()
        self.stack.append((price, counter)) #use tuples to store price and associated span
        return counter
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)