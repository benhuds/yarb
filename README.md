# yarb: Yet Another Redis-backed Bloom filter

Simple Redis-backed Bloom filter in Python.  Implements FNV1 and FNV1a for
hashing (see [here](http://www.isthe.com/chongo/tech/comp/fnv/index.html)), and
comes with a bulk insert function to pipeline multiple inserts to the server.
Inspired by a [similar
implementation](https://github.com/xupeng/bloomfilter-redis).

### Benchmarking insert functions

Inserting 109,582 words from a file of English words (`wordsEn.txt`) into a
1,000,000-bit Bloom filter with 3 hash derivations:

```
Using plain insert: 21.5324678421
Using bulk insert: 9.7206568718
```

