class MyCircularQueue:

    def __init__(self, k: int):
        self.stack = [None] * k
        self.size = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
            
        self.stack[self.rear] = value
        self.rear = (self.rear + 1) % self.size
            
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
            
        self.stack[self.front] = None
        self.front = (self.front + 1) % self.size
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.stack[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        if self.rear == 0:
            return self.stack[self.size - 1]
        
        return self.stack[self.rear - 1]

    def isEmpty(self) -> bool:
        return not self.stack[self.front] and self.front == self.rear

    def isFull(self) -> bool:
        return self.stack[self.front] and self.front == self.rear


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()