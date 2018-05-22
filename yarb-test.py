import redis
from yarb import BloomFilter
import time

if __name__ == "__main__":

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    bf = BloomFilter(r, 'test', 1000000, 3)

    with open('wordsEn.txt', 'r') as f:
        words = f.readlines()
    words = [x.strip() for x in words]

    start = time.time()
    bf.bulk_insert(words)
    end = time.time()
    print "Bulk insert successful. Duration:", end - start

    start2 = time.time()
    for w in words:
        bf.insert(w)
    end2 = time.time()
    print "Inefficient insert successful. Duration:", end2 - start2

    print "Bloom filter total size:", bf.m
    print "Hash derivations:", bf.k
    print "Occupied offsets after bulk insert:", bf.size()

# Test run 1:
# Bulk insert successful. Duration: 9.5189268589
# Inefficient insert successful. Duration: 21.5237748623

#    print "contains aardvark:", bf.contains('aardvark')
#    print "contains zebra:", bf.contains('zebra')
#    print "contains asdfasdf:", bf.contains('asdfasdf')

