from hash_table import HashTable

# Basic smoke tests for modes including double hashing and tombstones
ht = HashTable(size=7, mode='double')
print('Created double hashing table')
print('insert 10:', ht.insert(10))
print('insert 24:', ht.insert(24))
print('search 24:', ht.search(24))
print('delete 10:', ht.delete(10))
print('insert 31:', ht.insert(31))

ht2 = HashTable(size=5, mode='linear')
for k in [1, 6, 11]:
    print('insert linear', k, ht2.insert(k))
print('linear count:', ht2.count)
print('OK')
