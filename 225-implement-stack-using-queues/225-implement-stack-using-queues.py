class MyStack:

    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def push(self, x: int) -> None:
        self.queue_1.append(x)

    def pop(self) -> int:
        if self.queue_1:
            return self.queue_1.pop()

    def top(self) -> int:
        if not self.queue_1:
            return -1
        x = self.queue_1.pop()
        self.queue_1.append(x)
        return x

    def empty(self) -> bool:
        if not self.queue_1:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()