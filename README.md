# yarb: Yet Another Redis-backed Bloom filter

Simple Redis-backed Bloom filter in Python.  Inspired by a [similar
implementation](https://github.com/xupeng/bloomfilter-redis). Implements FNV1
and FNV1a for hashing (see
[here](http://www.isthe.com/chongo/tech/comp/fnv/index.html)), and also
comes with a bulk insert function to pipeline multiple inserts to the server.

### Usage

Prerequisites: [redis](https://redis.io/download) and
[redis-py](https://github.com/andymccurdy/redis-py) (the Redis Python client)

If you're running `redis-server` locally, you can try something like

``` python
import redis
from yarb import BloomFilter

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Filter is set to 1000000 bits with 3 hash derivations but feel free to experiment
bf = BloomFilter(r, 'filter-name-here', 1000000, 3)

bf.insert('foo')
bf.insert('bar')
bf.insert('baz')

bf.contains('bar')
bf.contains('qux')
```

### Benchmarking inserts

Inserting [109,582 English
words](https://github.com/benhuds/yarb/blob/master/wordsEn.txt) into a
1,000,000-bit Bloom filter with 3 hash derivations:

```
Using serial insert: 21.5324678421s
Using bulk insert: 9.7206568718s
```

Inserting [1,000,000 bad
passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords)
into a 1,000,000,000-bit Bloom filter with 3 hash derivations:

```
Using bulk insert: 95.7611479759s
```

