class MyHashSet:
    items={-1}
    def __init__(self):
        self.items={-1}

    def add(self, key: int) -> None:
        self.items.add(key)

    def remove(self, key: int) -> None:
        self.items.discard(key)

    def contains(self, key: int) -> bool:
        if key in self.items:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)