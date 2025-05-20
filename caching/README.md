# Caching

---

Caching (not to be confused with error ca**t**ching) is a way to save data to a
quick-access location like RAM when it will be repeatedly accessed. There are
several eviction policies for cache that determines in what order cached data
is removed when the space for cached data is full. Below are my notes I made 
on the subjet:

**Caching**: Saving data to fast-access memory like RAM to save time when data
is repeatedly accessed, rather than continuing to access it from a slower source
like an API, or (God forbid) re-calculating a static value each time.


**FIFO**: First-In, First-Out
    Chache/stack eviction policy where the oldest data is deleted first when the cache gets full.  
    Example in Python:

```python
from collections import deque

cache = deque(maxlen=3)
cache.append('a')  # First in
cache.append('b')
cache.append('c')
cache.append('d')  # 'a' is removed (first in)
```


**LIFO**: Last-In, Last-Out
    Evicts the most recently added data when the cache/stack gets full, acting like a stack.  
    Example in Python:

```python
stack = ['a', 'b', 'c']
stack.append('d')  # Add new item
stack.pop()        # 'd' is removed (last in)
```


**LRU**: Last Recently Used
    When cache is full, it removes the item that has not been accessed in the
    longest time out of all the items. It's common in real-world caching systems.  
    Example in Python:

```python
from functools import lru_cache

@lru_cache(maxsize=3)
def get_data(x):
    return x * x
```


**MRU**: Most Recently Used
    When cache is full, it removes the item that was last accessed (most recently).  
    No Python example.


**LFU**: Least Frequently Used
    Removes the item that has been accessed the least number of times. To do
    this, it also tracks usage with dictionaries and counters.  
    No Python example.
