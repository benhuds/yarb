import redis

# Details on FNV here http://www.isthe.com/chongo/tech/comp/fnv/index.html
def FNV1(key):
    FNV_prime = 16777619
    offset_basis = 2166136261
    res = offset_basis
    for i in key:
        res *= FNV_prime
        res ^= ord(i)
    return res

def FNV1a(key):
    FNV_prime = 16777619
    offset_basis = 2166136261
    res = offset_basis
    for i in key:
        res ^= ord(i)
        res *= FNV_prime
    return res

class BloomFilter:

    def __init__(self, connection, name, m, k):
        self.connection = connection
        self.name = name
        self.m = m # number of bits
        self.k = k # number of hash derivations

    def insert(self, key):
        pipe = self.connection.pipeline()
        for offset in self.calculate_offsets(key):
            pipe.setbit(self.name, offset, 1)
        pipe.execute()

    def bulk_insert(self, keys):
        pipe = self.connection.pipeline()
        for k in keys:
            for offset in self.calculate_offsets(k):
                pipe.setbit(self.name, offset, 1)
        pipe.execute()

    def contains(self, key):
        pipe = self.connection.pipeline()
        for offset in self.calculate_offsets(key):
            pipe.getbit(self.name, offset)
        res = pipe.execute()
        return all(res)

    def size(self):
        pipe = self.connection.pipeline()
        for i in range(self.m):
            pipe.getbit(self.name, i)
        res = pipe.execute()
        return res.count(1)

    # Two hash functions can simulate many:
    # https://www.eecs.harvard.edu/~michaelm/postscripts/tr-02-05.pdf
    def calculate_offsets(self, key):
        h1 = FNV1(key)
        h2 = FNV1a(key)
        offsets = []
        for i in range(self.k):
            offsets.append((h1 + (i * h2)) % self.m)
        return offsets

