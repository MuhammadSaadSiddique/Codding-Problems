class MyHashSet:
    items=[]
    def __init__(self):
        self.items=[]

    def add(self, key: int) -> None:
        self.items.append(key)

    def remove(self, key: int) -> None:
        self.items=list(filter((key).__ne__, self.items))
        # while key in self.items:
        #     self.items.remove(key)

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