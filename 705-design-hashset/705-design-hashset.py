class MyHashSet:

    data = []
    
    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.data.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)