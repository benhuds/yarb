# yarb: Yet Another Redis-backed Bloom filter

Simple Redis-backed Bloom filter in Python.  Implements FNV1 and FNV1a for
hashing (see [here](http://www.isthe.com/chongo/tech/comp/fnv/index.html)), and
comes with a bulk insert function to pipeline multiple inserts to the server.
Inspired by a [similar
implementation](https://github.com/xupeng/bloomfilter-redis).

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

