import redis
from yarb import BloomFilter
import time

if __name__ == "__main__":

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    bf = BloomFilter(r, 'words-test', 1000000, 3)

# Password insert test

#    with open('10-million-password-list-top-1000000.txt', 'r') as f:
#        passwords = f.readlines()
#    passwords = [x.strip() for x in passwords]

#    start = time.time()
#    bf.bulk_insert(passwords)
#    end = time.time()
#    print "Bulk insert successful. Duration:", end - start

# English words insert test

    with open('wordsEn.txt', 'r') as f:
        words = f.readlines()
    words = [x.strip() for x in words]

    start = time.time()
    bf.bulk_insert(words)
    end = time.time()
    print "Bulk insert successful. Duration:", end - start

#    start2 = time.time()
#    for w in words:
#        bf.insert(w)
#    end2 = time.time()
#    print "Serial insert successful. Duration:", end2 - start2

#    print "Capacity after insert:", str((float(bf.size()) / bf.m) * 100)+"%"

    print "\nContains \'aardvark\' test:"
    start = time.time()
    bf.contains('aardvark')
    end = time.time()
    print bf.contains('aardvark')
    print "Duration:", end - start

    print "\nContains \'zebra\' test:"
    start = time.time()
    bf.contains('zebra')
    end = time.time()
    print bf.contains('zebra')
    print "Duration:", end - start

    print "\nContains \'asdfasdf\' test:"
    start = time.time()
    bf.contains('asdfasdf')
    end = time.time()
    print bf.contains('asdfasdf')
    print "Duration:", end - start

