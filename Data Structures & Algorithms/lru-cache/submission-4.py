
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

        
