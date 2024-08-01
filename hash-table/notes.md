# hash table / set

## when to use

since elements inside a hash table/set aren't linked to one anoteher, lookup is based on hashing the key. this makes it possible for reads to be O(1) and insertions vary from O(1) to O(1 + a).

choice of hashing function directly impacts on compute and collisions, which directly impacts on time complexity.

use hash tables/sets when quick lookup is desired instead of O(n) reads on a linked list.