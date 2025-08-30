# Problem 1472: Design Browser History
# Difficulty: Medium
class BrowserHistory:
    history = []
    i = 0
    def __init__(self, homepage: str):
        self.history.clear()
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        if self.i + 1 >= len(self.history):
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
            self.history = self.history[:self.i + 2]
        self.i += 1

    def back(self, steps: int) -> str:
        if self.i - steps < 0:
            self.i = 0
        else:
            self.i = self.i - steps
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        if self.i + steps >= len(self.history):
            self.i = len(self.history) - 1
        else:
            self.i = self.i + steps
        return self.history[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)