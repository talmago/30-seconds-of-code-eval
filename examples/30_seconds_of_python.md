### index_of_all (task/1)

#### canonical solution
```python
def index_of_all(lst, value):  return [i for i, x in enumerate(lst) if x == value]
```

#### solution 0
```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+
+    return [i for i, x in enumerate(lst) if x == value]
+
+if __name__ == '__main__':
+    main()
```

#### solution 1
```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+
+    return [i for i, v in enumerate(lst) if v == value]
+
+
+def make_simulated_path(size, *args):
+    """
+    make_simulated_path(size,
```

#### solution 2
```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+
+    """Returns a list of indexes in which value can be found in lst.
+
+    >>> index_of_all([2, 3, 5, 3], 3)
+    [1, 3]
+    """
+    indexes
```

#### solution 3
```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+
+    '''Finds the indexes of all occurences of value in lst'''
+    return [i for i, x in enumerate(lst) if x == value]
+
+def read_seq(filename):
```

#### solution 4
```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+
+    res = []
+    for i, x in enumerate(lst):
+        if x == value:
+            res.append(i)
+    return res
+
+def find_sub_list(sl,l):
```

### head (task/2)

#### canonical solution
```python
def head(lst):  return lst[0]
```

#### solution 0
```diff
-def head(lst):
+def head(lst):
+
+    return lst[0]
+
+def tail(lst):
+    return lst[1:]
+
+def transpose(lst):
+    return list(map(list, zip(*lst)))
+
+def
```

#### solution 1
```diff
-def head(lst):
+def head(lst):
+
+    return lst[0]
+
+def tail(lst):
+    return lst[1:]
+
+def empty(lst):
+    return lst == []
+
+def sum_list(lst):
```

#### solution 2
```diff
-def head(lst):
+def head(lst):
+
+    """Returns the first element of a list."""
+    return lst[0]
+
+
+def tail(lst):
+    """Returns the last element of a list."""
+    return lst[-1]
+
```

#### solution 3
```diff
-def head(lst):
+def head(lst):
+
+    return lst[0]
+
+def tail(lst):
+    return lst[1:]
+
+def init(lst):
+    return lst[:-1]
+
+def last(lst):
```

#### solution 4
```diff
-def head(lst):
+def head(lst):
+
+    return lst[0]
+
+def tail(lst):
+    return lst[1:]
+
+def is_empty(lst):
+    return not lst
+
+def length(lst):
+   
```

### max_n (task/3)

#### canonical solution
```python
def max_n(lst, n = 1):  return sorted(lst, reverse = True)[:n]
```

#### solution 0
```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+
+    """Returns the n maximum elements from the provided list. 
+    If n is greater than or equal to the provided list's length, 
+    then return the original list (sorted in descending order).
+    """
+   
```

#### solution 1
```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+
+    '''
+    return the n max elements in a list
+    Parameters:
+        lst: list
+            list of numerical values
+        n: int
+            number of max elements to return
+    '''
+    return
```

#### solution 2
```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+
+    """Returns the n maximum elements from the provided list. 
+
+    Keyword arguments:
+    lst -- the list to check
+    n -- the number of elements to return (default 1)
+    """
+    return heap
```

#### solution 3
```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+
+    """
+    >>> max_n([1,2,3,4,5])
+    5
+    >>> max_n([1,2,3,4,5], 2)
+    5
+    >>> max_
```

#### solution 4
```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+
+    max_n = []
+    for i in range(0, n):
+        max_n.append(max(lst))
+        lst.remove(max(lst))
+    return max_n
```

### to_iso_date (task/4)

#### canonical solution
```python
from datetime import datetime

def to_iso_date(d):  return d.isoformat()
```

#### solution 0
```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    return datetime.strftime(d, "%Y-%m-%d")
+
+def get_soup(url):
+    # Fetch url
+    print(f"Fetching: {url}")
```

#### solution 1
```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    """Convert the given date to the ISO 8601 format, unless it is None, in
+    which case None is returned."""
+    if d is None:
+        return None
+    else:
+        return d.
```

#### solution 2
```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    return datetime.strftime(d, "%Y-%m-%d")
+
+def get_link(link):
+    return link.split('"')[1]
+
+def get_content(link):
```

#### solution 3
```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    return d.strftime('%Y-%m-%d')
+
+def from_iso_date(s):
+    return datetime.strptime(s, '%Y-%m-%d')
```

#### solution 4
```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    if not d:
+        return None
+    if d == 'None':
+        return None
+    try:
+        return datetime.strptime(d, '%Y-%m-%d').date()
```

### median (task/5)

#### canonical solution
```python
def median(list):  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

#### solution 0
```diff
-def median(list):
+def median(list):
+
+    list = sorted(list)
+    if len(list)%2 == 0:
+        return (list[len(list)/2]+list[len(list)/2-1])/2.0
+    else:
```

#### solution 1
```diff
-def median(list):
+def median(list):
+
+    sortedList = sorted(list)
+    listLen = len(list)
+    index = (listLen - 1) // 2
+
+    if (listLen % 2):
+        return sortedList[index]
+    else
```

#### solution 2
```diff
-def median(list):
+def median(list):
+
+    """
+    Args: list (list): list of numbers.
+    Returns: median value (float)
+    """
+    # sort the list
+    list.sort()
+    # check for even list length and calculate
```

#### solution 3
```diff
-def median(list):
+def median(list):
+
+    median = 0
+    length = len(list)
+    if (length % 2 == 0):
+        index_odd = length / 2
+        index_even = index_odd - 1
+        median = (list[
```

#### solution 4
```diff
-def median(list):
+def median(list):
+
+    list.sort()
+    if len(list) % 2 == 0:
+        return (list[len(list)//2] + list[len(list)//2 - 1]) / 2
+    else:
```

### longest_item (task/6)

#### canonical solution
```python
def longest_item(*args):  return max(args, key = len)
```

#### solution 0
```diff
-def longest_item(*args):
+def longest_item(*args):
+
+    longest = 0
+    for i in args:
+        if len(i) > longest:
+            longest = len(i)
+    return longest
+
+def longest_item_re(*args):
+    return max(
```

#### solution 1
```diff
-def longest_item(*args):
+def longest_item(*args):
+
+    longest = ""
+    for i in args:
+        if len(i) > len(longest):
+            longest = i
+    return longest
+
+print(longest_item("one", "two", "three
```

#### solution 2
```diff
-def longest_item(*args):
+def longest_item(*args):
+
+    res = []
+    for arg in args:
+        res.append(len(arg))
+    return res
+
+# >>> longest_item("one", "two", "three")
+# [3, 3, 5
```

#### solution 3
```diff
-def longest_item(*args):
+def longest_item(*args):
+
+    """
+    :param args:
+    :return:
+    """
+    return max(args, key=len)
+
+
+def get_common_part(a, b):
+    """
+    :param a:
```

#### solution 4
```diff
-def longest_item(*args):
+def longest_item(*args):
+
+    print(max(args, key=len))
+longest_item('this', 'is', 'a', 'test', 'case')
+# another solution
+def longest_item(*args):
+    return max(args
```

### powerset (task/7)

#### canonical solution
```python
from itertools import chain, combinations

def powerset(iterable):  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
```

#### solution 0
```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    s = list(iterable)
+    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
+
+a = input().split()
+b = list(
```

#### solution 1
```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
+    s = list
```

#### solution 2
```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    s = list(iterable)
+    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
+
+#print(list(powerset(['a','
```

#### solution 3
```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    s = list(iterable)
+    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
+
+def main():
+    N = input()
+   
```

#### solution 4
```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    s = list(iterable)
+    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
+
+def select_from_list(l, n):
```

### find_index_of_all (task/8)

#### canonical solution
```python
def find_index_of_all(lst, fn):  return [i for i, x in enumerate(lst) if fn(x)]
```

#### solution 0
```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    """Finds the indices of all elements in lst where fn is True."""
+    indices = []
+    for i, elem in enumerate(lst):
+        if fn(elem):
+            indices.
```

#### solution 1
```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    """Return the indices of all items in lst where fn(item) is True."""
+    return [i for i, x in enumerate(lst) if fn(x)]
+
+
+def find_index_of
```

#### solution 2
```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    """
+    Find the index of all items in the list
+    that satisfies the given predicate.
+    """
+    return [i for i, e in enumerate(lst) if fn(e)]
+
+
+def all
```

#### solution 3
```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    """Finds all indices in a list where a predicate is true.
+
+    Args:
+        lst: A list.
+        fn: A function taking an element and returning a bool.
+
+    Returns:
+        A
```

#### solution 4
```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    idx = []
+    for i, x in enumerate(lst):
+        if fn(x):
+            idx.append(i)
+    return idx
+
+def iif(condition, true_
```

### take (task/9)

#### canonical solution
```python
def take(itr, n = 1):  return itr[:n]
```

#### solution 0
```diff
-def take(itr, n = 1):
+def take(itr, n = 1):
+
+    return list(islice(itr, n))
+
+def take_nth(itr, n = 1):
+    return list(islice(itr, 0, None, n))
+
+def tabulate
```

#### solution 1
```diff
-def take(itr, n = 1):
+def take(itr, n = 1):
+
+    """
+    This function returns the first n elements of an iterator as a list.
+    :param itr: The iterator.
+    :param n: The number of elements to return.
+    :return: The first n
```

#### solution 2
```diff
-def take(itr, n = 1):
+def take(itr, n = 1):
+
+    return itr[0:n]
+
+def read_int(file):
+    return int(file.readline())
+
+def read_int_array(file, sep = ' '):
+    return [int
```

#### solution 3
```diff
-def take(itr, n = 1):
+def take(itr, n = 1):
+
+    if n < 0:
+        raise ValueError('Cannot take a negative number of elements from the iterable')
+    return itr[:n]
+
+def take_nth(itr, n = 1):
```

#### solution 4
```diff
-def take(itr, n = 1):
+def take(itr, n = 1):
+
+    for i in range(n):
+        yield next(itr)
+
+def get(itr, k = 0):
+    return next(take(itr, k))
+
+def nth(itr,
```

### last (task/10)

#### canonical solution
```python
def last(lst):  return lst[-1]
```

#### solution 0
```diff
-def last(lst):
+def last(lst):
+
+    return lst[-1]
+
+
+def subsets(lst):
+    return [[]] if len(lst) == 0 else (
+        [lst] + [lst[:k] + lst
```

#### solution 1
```diff
-def last(lst):
+def last(lst):
+
+    if lst:
+        return lst[-1]
+    else:
+        return None
+
+def merge(result, op):
+    def insert(key, value):
+        if not result.has_key
```

#### solution 2
```diff
-def last(lst):
+def last(lst):
+
+    if lst == []:
+        return None
+    else:
+        return lst[-1]
+
+def assign(x, y):
+    globals()[x] = y
+
+def isa(
```

#### solution 3
```diff
-def last(lst):
+def last(lst):
+
+    return lst[-1]
+
+def second(lst):
+    return lst[1]
+
+def key(lst):
+    return last(lst)
+
+def is_number(x):
```

#### solution 4
```diff
-def last(lst):
+def last(lst):
+
+    """Returns the last element of a list"""
+    return lst[-1]
+
+
+def before_last(lst):
+    """Returns the element before the last of a list"""
+    return lst[-
```

### delay (task/11)

#### canonical solution
```python
from time import sleep

def delay(fn, ms, *args):  sleep(ms / 1000)
  return fn(*args)
```

#### solution 0
```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    t = Thread(target=fn, args=args)
+    t.start()
+    sleep(ms/1000)
+    return t
+
+def _get_device_by_port(port):
+    for d
```

#### solution 1
```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    """
+    This function allows you to delay the execution of a function.
+
+    :param fn: The function to be delayed.
+    :param ms: The number of milliseconds to delay the function by.
+    :param args
```

#### solution 2
```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    def wrapper():
+        sleep(ms/1000)
+        return fn(*args)
+    return wrapper
+
+@delay
+def hello(name):
+    print("Hello, {}!".format(name))
+
+# hello
```

#### solution 3
```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    def wrap(*args):
+        sleep(ms/1000)
+        return fn(*args)
+    return wrap
+
+def my_decorator(func):
+    def wrapper():
+        print("Something is happening before
```

#### solution 4
```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    sleep(ms / 1000)
+    return fn(*args)
+
+def get_key_value(item):
+    return item[1]
+
+def sort_dict(d):
+    return sorted(d.items
```

### curry (task/12)

#### canonical solution
```python
from functools import partial

def curry(fn, *args):  return partial(fn, *args)
```

#### solution 0
```diff
-from functools import partial
-
-def curry(fn, *args):
+from functools import partial
+
+def curry(fn, *args):
+
+    def _fn(*_args):
+        return fn(*(args + _args))
+    return _fn
+
+class Tee:
+    def __init__(self, file):
+        self.file = file
+   
```

#### solution 1
```diff
-from functools import partial
-
-def curry(fn, *args):
+from functools import partial
+
+def curry(fn, *args):
+
+    return partial(fn, *args)
+
+
+class Person:
+    def __init__(self, name, age):
+        self.name = name
+        self.age = age
+
+    def __repr__(
```

#### solution 2
```diff
-from functools import partial
-
-def curry(fn, *args):
+from functools import partial
+
+def curry(fn, *args):
+
+    def curried(*more_args):
+        return fn(*(args + more_args))
+    return curried
+
+def uppercase(s):
+    return s.upper()
+
+def test():
+   
```

#### solution 3
```diff
-from functools import partial
-
-def curry(fn, *args):
+from functools import partial
+
+def curry(fn, *args):
+
+    def curried(*more_args):
+        return fn(*(args + more_args))
+    return curried
+
+# curry = lambda fn, *args: lambda *more_args: fn(*(args + more
```

#### solution 4
```diff
-from functools import partial
-
-def curry(fn, *args):
+from functools import partial
+
+def curry(fn, *args):
+
+    """
+    Return a curried version of the given function,
+    in the style of `functools.partial`
+
+    Example
+    -------
+    def add(x, y):
+        return x + y
+
```

### find (task/13)

#### canonical solution
```python
def find(lst, fn):  return next(x for x in lst if fn(x))
```

#### solution 0
```diff
-def find(lst, fn):
+def find(lst, fn):
+
+    for l in lst:
+        if fn(l):
+            return l
+    return None
+
+def get_thread_id(i3con):
+    tree = i3con.get_tree()
+   
```

#### solution 1
```diff
-def find(lst, fn):
+def find(lst, fn):
+
+    """
+    Return the first item in lst that returns True in fn.
+    """
+    for item in lst:
+        if fn(item):
+            return item
+    return None
+
+def rev(l
```

#### solution 2
```diff
-def find(lst, fn):
+def find(lst, fn):
+
+    for item in lst:
+        if fn(item):
+            return item
+    return None
+
+def main():
+    results = []
+    for case in xrange(input()):
+        C, D,
```

#### solution 3
```diff
-def find(lst, fn):
+def find(lst, fn):
+
+    for l in lst:
+        if fn(l):
+            return l
+    return None
+
+def isValid(p):
+    if p.parachute:
+        return True
+    elif p.
```

#### solution 4
```diff
-def find(lst, fn):
+def find(lst, fn):
+
+    for el in lst:
+        if fn(el):
+            return el
+    return None
+
+def find_index(lst, fn):
+    for i, el in enumerate(lst):
+       
```

### capitalize_every_word (task/14)

#### canonical solution
```python
def capitalize_every_word(s):  return s.title()
```

#### solution 0
```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+
+    return ' '.join([word.capitalize() for word in s.split(' ')])
+
+def levenshtein(s1, s2):
+    if len(s1) < len(s2):
```

#### solution 1
```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+
+    return ' '.join([x.capitalize() for x in s.split(' ')])
+
+class Command(BaseCommand):
+    help = 'Imports a text file of RepoCommits into the database'
+
```

#### solution 2
```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+
+    s = s.split(' ')
+    s = map(lambda x: x.capitalize(), s)
+    return ' '.join(s)
+
+class User(object):
+    def __init__(self
```

#### solution 3
```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+
+    return ' '.join([w.capitalize() for w in s.split(' ')])
+
+
+def capitalize_initial_letters(s):
+    return ' '.join([w[0].upper() + w[1
```

#### solution 4
```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+
+    return ' '.join([w.capitalize() for w in s.split(' ')])
+
+def is_same_full_name(name1, name2):
+    return normalize_full_name(name
```

### is_prime (task/15)

#### canonical solution
```python
from math import sqrt

def is_prime(n):  if n <= 1 or (n % 2 == 0 and n > 2): 
    return False
  return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
```

#### solution 0
```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    for i in range(2, int(sqrt(n))+1):
+        if n % i == 0:
+            return False
+    return True
+
+def get_primes(max_number):
+   
```

#### solution 1
```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    if n % 2 == 0 and n > 2: 
+        return False
+    for i in range(3, int(sqrt(n)) + 1, 2):
+        if n % i == 0:
+           
```

#### solution 2
```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    if n < 2:
+        return False
+    if n == 2:
+        return True
+    limit = int(sqrt(n))
+    i = 2
+    while i <= limit:
+        if n %
```

#### solution 3
```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    for i in range(2, int(sqrt(n)) + 1):
+        if n % i == 0:
+            return False
+    return True
+
+def find_prime_factors(n):
+   
```

#### solution 4
```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    if n < 2:
+        return False
+    for i in range(2, int(sqrt(n)) + 1):
+        if n % i == 0:
+            return False
+    return True
+
+print
```

### includes_all (task/16)

#### canonical solution
```python
def includes_all(lst, values):  for v in values:
    if v not in lst:
      return False
  return True
```

#### solution 0
```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+
+    for value in values:
+        if value not in lst:
+            return False
+    return True
+
+
+@register.filter
+def append_to_list(lst, value):
+    if value not in l
```

#### solution 1
```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+
+    for value in values:
+        if value not in lst:
+            return False
+    return True
+
+
+def plot_gene_means(data, gene, bins=50, ax=None, plot_mean
```

#### solution 2
```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+
+    """Returns true if all of the strings in values are in lst."""
+    for v in values:
+        if v not in lst:
+            return False
+    return True
+
+
+def includes_any(l
```

#### solution 3
```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+
+    """Check that the list contains all the values."""
+    for value in values:
+        if value not in lst:
+            return False
+    return True
+
+
+def validate_args(args):
+    """Check
```

#### solution 4
```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+
+    return all(item in lst for item in values)
+
+
+def get_version():
+    from .__init__ import __version__
+    return __version__
+
+
+def get_name():
+    from .__
```

### is_weekend (task/17)

#### canonical solution
```python
from datetime import datetime

def is_weekend(d = datetime.today()):  return d.weekday() > 4
```

#### solution 0
```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    if d.weekday() == 5 or d.weekday() == 6:
+        return True
+    else:
+        return False
+
+def get_last_date(filename):
+    df = pd.read
```

#### solution 1
```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    if d.weekday() == 5 or d.weekday() == 6:
+        return True
+    else:
+        return False
+
+def is_workday(d = datetime.today()):
+    if
```

#### solution 2
```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    return d.weekday() in [5, 6]
+
+def is_weekday(d = datetime.today()):
+    return d.weekday() in [0, 1, 2, 3, 4]
```

#### solution 3
```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    if d.weekday() == 5 or d.weekday() == 6:
+        return True
+    else:
+        return False
+
+if __name__ == '__main__':
+    print(is_week
```

#### solution 4
```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    if d.weekday() == 5 or d.weekday() == 6:
+        return True
+    else:
+        return False
+
+def is_leap(year):
+    if (year % 4 == 0
```

### spread (task/18)

#### canonical solution
```python
def spread(arg):  ret = []
  for i in arg:
    ret.extend(i) if isinstance(i, list) else ret.append(i)
  return ret
```

#### solution 0
```diff
-def spread(arg):
+def spread(arg):
+
+    return 'spread({})'.format(arg)
+
+
+def cached_item(arg):
+    return 'cached_item({})'.format(arg)
+
+
+def cached_item_call(arg):
+    return
```

#### solution 1
```diff
-def spread(arg):
+def spread(arg):
+
+    return abs(min(arg)) + max(arg)
+
+def flatten(lst):
+    return [item for sublist in lst for item in sublist]
+
+def args_to_lists(args
```

#### solution 2
```diff
-def spread(arg):
+def spread(arg):
+
+    """spread(iterable) -> iterator
+
+    Runs the iterable and executes every returned value as a function argument
+    in the same way.
+
+    :param iterable: Input iterable
+    :return: The iterable
```

#### solution 3
```diff
-def spread(arg):
+def spread(arg):
+
+    """
+    Given a string of a Gimp color palette file, it will return a list
+    of the colors in that file.
+
+    Gimp color palette files are RGB color definitions of the form:
+
+    # Comments
```

#### solution 4
```diff
-def spread(arg):
+def spread(arg):
+
+    '''
+    Return the aggregation by spreading values of the given sequence.
+    '''
+    _args = []
+    prev = None
+    for i in arg:
+        if prev is None:
+            prev =
```

### reverse_number (task/19)

#### canonical solution
```python
from math import copysign

def reverse_number(n):  return copysign(float(str(n)[::-1].replace('-', '')), n)
```

#### solution 0
```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    return int(str(n)[::-1])
+
+def is_palindrome(n):
+    return n == reverse_number(n)
+
+def is_lychrel(n):
+    for i
```

#### solution 1
```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    return int(str(n)[::-1])
+
+def is_palindrome(n):
+    return n == reverse_number(n)
+
+def is_lychrel(n):
+    for i
```

#### solution 2
```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    return int(str(n)[::-1])
+
+def is_lychrel(n):
+    for i in range(0, 50):
+        n += reverse_number(n)
+        if n ==
```

#### solution 3
```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    return int(str(n)[::-1])
+
+def is_palindrome(n):
+    if reverse_number(n) == n:
+        return True
+    else:
+        return False
+
```

#### solution 4
```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    return int(str(n)[::-1])
+
+def reverse_signed_number(n):
+    return copysign(reverse_number(abs(n)), n)
+
+def test_reverse_number():
```

### words (task/20)

#### canonical solution
```python
import re

def words(s, pattern = '[a-zA-Z-]+'):  return re.findall(pattern, s)
```

#### solution 0
```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    for word in re.findall(pattern, s):
+        yield word
+
+def lines(s, pattern = '\n'):
+    for line in re.findall(pattern, s):
+        yield line
```

#### solution 1
```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    return re.findall(pattern, s)
+
+def phone_number(s):
+    number = re.findall('[0-9]+', s)
+    return (number[0], number[1])
```

#### solution 2
```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    return re.findall(pattern, s)
+
+def phone_number(s):
+    phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4
```

#### solution 3
```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    return re.findall(pattern, s)
+
+def phone_number(s):
+    pattern = '^\s*(?:\+?(\d{1,3}))?[-. (]*(\
```

#### solution 4
```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    for word in re.findall(pattern, s):
+        yield word.lower()
+
+def articles(s, pattern = '\s+([a-zA-Z]+\s*){1,3}
```

### sample (task/21)

#### canonical solution
```python
from random import choice

def sample(lst):  return choice(lst)
```

#### solution 0
```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    return choice(lst)
+
+def get_index(lst, word):
+    return lst.index(word)
+
+def get_index_sequence(lst, word_list):
+    index_
```

#### solution 1
```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    return choice(lst)
+
+def generate_model(cfdist, word, num=15):
+    for i in range(num):
+        print(word, end=' ')
+        word = sample(cf
```

#### solution 2
```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    """
+    Sample one element from the list.
+    """
+    return choice(lst)
+
+
+def gen_sentence(word1, word2, max_len):
+    """
+    Generate a sentence
```

#### solution 3
```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    return choice(lst)
+
+def calculate_frequency(list, word):
+    return list.count(word)
+
+def calculate_degree(list):
+    return (len(list) - 1)
+
```

#### solution 4
```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    return choice(lst)
+
+def shuffle(lst):
+    new_lst = []
+    for n in range(len(lst)):
+        new_lst.append(sample(lst
```

### days_ago (task/22)

#### canonical solution
```python
from datetime import timedelta, date

def days_ago(n):  return date.today() - timedelta(n)
```

#### solution 0
```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    return date.today() - timedelta(days=n)
+
+class Command(BaseCommand):
+    help = 'Closes the specified poll for voting'
+
+    def add_arguments(self, parser):
+       
```

#### solution 1
```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    return date.today() - timedelta(days=n)
+
+# default
+default_args = {
+    'owner': 'airflow',
+    'depends_on_past': False,
+    'start
```

#### solution 2
```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    return date.today() - timedelta(days=n)
+
+print(days_ago(5))
+#2018-11-29
+
+"""
+可见，如果
```

#### solution 3
```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    return date.today() - timedelta(days=n)
+
+def argparse_date(date_string):
+    """ Convert datetime string to datetime object.
+
+    Arguments:
+        date_string {
```

#### solution 4
```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    return date.today() - timedelta(days=n)
+
+def build_query(lst):
+    return (lst)
+
+def assign_trending(post):
+    from django.db
```

### key_in_dict (task/23)

#### canonical solution
```python
def key_in_dict(d, key):  return (key in d)
```

#### solution 0
```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    return key in d.keys()
+
+
+def has_same_shape(d, dicts):
+    for dict in dicts:
+        for key in d.keys():
+            if key not in dict.keys():
```

#### solution 1
```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    return key in d and d[key] is not None
+
+
+def check_to_insert(cur, tid, user_name, movie_id, rating, timestamp):
+    cur.execute(
+        "SELECT *
```

#### solution 2
```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    """
+    Check if key is in dict, but do not raise error
+    """
+    if key in d:
+        return True
+    else:
+        return False
+
+
+def read_dict_data(path):
```

#### solution 3
```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    if key in d:
+        return True
+    else:
+        return False
+    
+def dict_to_list(d):
+    l = []
+    for item in d:
+        l.append(item
```

#### solution 4
```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    return key in d and d[key] is not None
+
+
+def is_running_on_server():
+    return key_in_dict(os.environ, 'SERVER_SOFTWARE') and not os.
```

### factorial (task/24)

#### canonical solution
```python
def factorial(num):  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)
```

#### solution 0
```diff
-def factorial(num):
+def factorial(num):
+
+    if num == 0:
+        return 1
+    else:
+        return num * factorial(num - 1)
+
+if __name__ == '__main__':
+    num = int(input("Enter a number
```

#### solution 1
```diff
-def factorial(num):
+def factorial(num):
+
+    return 1 if num == 1 else num * factorial(num - 1)
+
+
+n = int(input())
+print(factorial(n))
```

#### solution 2
```diff
-def factorial(num):
+def factorial(num):
+
+    if num == 1:
+        return 1
+    else:
+        return num * factorial(num - 1)
+
+print(factorial(5))
```

#### solution 3
```diff
-def factorial(num):
+def factorial(num):
+
+    if num == 0:
+        return 1
+    else:
+        return num * factorial(num - 1)
+
+user_input = int(input("Enter a number: "))
+print(factorial(user
```

#### solution 4
```diff
-def factorial(num):
+def factorial(num):
+
+    if num == 1:
+        return 1
+    else:
+        return num * factorial(num - 1)
+
+def countPaths(m, n):
+    return factorial(m + n) / (
```

### initial (task/25)

#### canonical solution
```python
def initial(lst):  return lst[:-1]
```

#### solution 0
```diff
-def initial(lst):
+def initial(lst):
+
+    for i in range(len(lst)):
+        for j in range(len(lst[i])):
+            lst[i][j] = random.randint(0, 1)
+    return
```

#### solution 1
```diff
-def initial(lst):
+def initial(lst):
+
+    for i in range(0,len(lst)):
+        lst[i] = " "
+    return lst
+
+def clear_screen():
+    os.system('cls' if os.name
```

#### solution 2
```diff
-def initial(lst):
+def initial(lst):
+
+    for i in range(len(lst)):
+        lst[i] = 0
+        
+def add_vectors(u, v):
+    """
+    >>> add_vectors([1, 0],
```

#### solution 3
```diff
-def initial(lst):
+def initial(lst):
+
+    """
+    Returns the initial of a string.
+    """
+    lst[-1] = lst[-1].replace('.', '')
+    return lst[-1][0].upper()
+
```

#### solution 4
```diff
-def initial(lst):
+def initial(lst):
+
+    for i in range(1, len(lst)):
+        temp = lst[i]
+        j = i - 1
+        while j >= 0 and temp < lst[j]:
+            lst[
```

### pad (task/26)

#### canonical solution
```python
from math import floor

def pad(s, length, char = ' '):  return s.rjust(floor((len(s) + length)/2), char).ljust(length, char)
```

#### solution 0
```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+    return s + (char * (length - len(s)))
+
+def main():
+    """
+    Cracking the Safe
+    There is a box protected by a password. The password is n digits, where each letter can
```

#### solution 1
```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+    assert(length >= len(s))
+    r = length - len(s)
+    return s + (char * r)
+
+def strip_pad(s, length, char = ' '):
+    assert(
```

#### solution 2
```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+    if length <= len(s):
+        return s
+    return s + (char * (length - len(s)))
+
+def align(s, length, alignment = 'left'):
+    if alignment == 'left
```

#### solution 3
```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+	while len(s) < length:
+		s = s + char
+	return s
+
+def hex_dump(data, length = 16):
+	'''
+	Dump data in hex format.
+
+	
```

#### solution 4
```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+	if len(s) < length:
+		return s + (char * (length - len(s)))
+	else:
+		return s
+
+def bar(value, length = 10, min = 0,
```

### degrees_to_rads (task/27)

#### canonical solution
```python
from math import pi

def degrees_to_rads(deg):  return (deg * pi) / 180.0
```

#### solution 0
```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return deg*pi/180
+
+def polygon_area(n, side_length):
+    return ((n*side_length**2)/(4*tan(pi/n)))
+
+n = int(input
```

#### solution 1
```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return deg * pi / 180
+
+def log(msg):
+    print("\n" + msg)
+
+def build_distance_matrix(locations):
+    """
+    This method calculates the great circle distance
```

#### solution 2
```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return deg*pi/180
+
+def distance(lat1, lat2, lon1, lon2):
+    '''
+    https://stackoverflow.com/questions/19412462/getting-
```

#### solution 3
```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return deg*pi/180
+
+def rads_to_degrees(rads):
+    return rads*180/pi
+
+def get_ref_ellipsoid_vector():
+    return (6
```

#### solution 4
```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return deg * pi / 180
+
+def main():
+    degrees = float(input("Enter degrees: "))
+    rads = degrees_to_rads(degrees)
+    print("{} degrees is {}
```

### lcm (task/28)

#### canonical solution
```python
from functools import reduce
from math import gcd

def lcm(numbers):  return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)
```

#### solution 0
```diff
-from functools import reduce
-from math import gcd
-
-def lcm(numbers):
+from functools import reduce
+from math import gcd
+
+def lcm(numbers):
+
+    return reduce(lambda x, y: (x*y)//gcd(x,y), numbers, 1)
+
+def answer(dimensions, captain_position, badguy_position, distance):
+    w,
```

#### solution 1
```diff
-from functools import reduce
-from math import gcd
-
-def lcm(numbers):
+from functools import reduce
+from math import gcd
+
+def lcm(numbers):
+
+    return reduce(lambda x, y: (x*y)//gcd(x,y), numbers, 1)
+
+def gcd_list(L):
+    v = L[0]
+
+    for i in
```

#### solution 2
```diff
-from functools import reduce
-from math import gcd
-
-def lcm(numbers):
+from functools import reduce
+from math import gcd
+
+def lcm(numbers):
+
+    return reduce(lambda x, y: (x*y)//gcd(x,y), numbers, 1)
+
+print(lcm([3, 6, 8]))
```

#### solution 3
```diff
-from functools import reduce
-from math import gcd
-
-def lcm(numbers):
+from functools import reduce
+from math import gcd
+
+def lcm(numbers):
+
+    return reduce(lambda x, y: (x*y)//gcd(x,y), numbers, 1)
+
+def find_in_grid(grid, pattern):
+    size = len(pattern)
+   
```

#### solution 4
```diff
-from functools import reduce
-from math import gcd
-
-def lcm(numbers):
+from functools import reduce
+from math import gcd
+
+def lcm(numbers):
+
+    return reduce(lambda x, y: (x*y)//gcd(x,y), numbers, 1)
+
+def lcm_for_range(start, end):
+    return lcm(range(start
```

### most_frequent (task/29)

#### canonical solution
```python
def most_frequent(lst):  return max(set(lst), key = lst.count)
```

#### solution 0
```diff
-def most_frequent(lst):
+def most_frequent(lst):
+
+    return max(set(lst), key=lst.count)
+    
+    
+def random_subset(lst,m):
+    return random.sample(lst,m)
+
+def random_
```

#### solution 1
```diff
-def most_frequent(lst):
+def most_frequent(lst):
+
+    """
+    Returns the element of the list that is the most frequent.
+    """
+    return max(set(lst), key=lst.count)
+
+
+def main():
+    """
+    Main program.
```

#### solution 2
```diff
-def most_frequent(lst):
+def most_frequent(lst):
+
+    return max(set(lst), key=lst.count)
+
+def get_center(area):
+    return np.array([area[0] + (area[2] - area[0]) / 2
```

#### solution 3
```diff
-def most_frequent(lst):
+def most_frequent(lst):
+
+    """
+    Find the most frequent element in a list.
+    """
+    return max(set(lst), key=lst.count)
+    
+    
+def get_q_table(mdp, states
```

#### solution 4
```diff
-def most_frequent(lst):
+def most_frequent(lst):
+
+    """
+    :param lst: list of integers
+    :return: integer - the most frequent number in the list
+    """
+    return max(set(lst), key=lst.count)
+
+
+def
```

### rads_to_degrees (task/30)

#### canonical solution
```python
from math import pi

def rads_to_degrees(rad):  return (rad * 180.0) / pi
```

#### solution 0
```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    return rad*180/pi
+
+def main():
+    degree = rads_to_degrees(pi/2)
+    print(degree)
+
+if __name__ == "__main__":
+    main
```

#### solution 1
```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    return (rad * 180) / pi
+
+def degrees_to_rads(deg):
+    return (deg * pi) / 180
+
+class Vechicle():
+    def __init__(self, x,
```

#### solution 2
```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    return rad * 180.0 / pi
+
+def degrees_to_rads(deg):
+    return deg * pi / 180.0
+
+class Vector:
+    def __init__(self, x=0,
```

#### solution 3
```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    return rad * 180.0 / pi
+
+def degrees_to_rads(deg):
+    return deg * pi / 180.0
+
+def get_sim_time_seconds(s):
+    return s.
```

#### solution 4
```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    return rad * 180 / pi
+
+def degrees_to_rads(deg):
+    return deg * pi / 180
+
+def tuple_to_list(points):
+    return [[i[0], i[1
```

### n_times_string (task/31)

#### canonical solution
```python
def n_times_string(s, n):  return (s * n)
```

#### solution 0
```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    s_n = s * n
+    return s_n
+
+print(n_times_string('123', 4))
```

#### solution 1
```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    return s * n
+
+print(n_times_string('ja', 2))
+print(n_times_string('ja', 0))
+
+# Optional arguments
+# 
+# Arguments can be made optional by
```

#### solution 2
```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    return s * n
+
+print(n_times_string('abc', 3))
+
+# See the second argument to the function call?
+# We can give `n_times_string` a different argument name (like
```

#### solution 3
```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    return s * n
+
+def print_string(s):
+    print(s)
+
+def print_sum(a, b):
+    print(a + b)
+
+def repeat_string(s, n
```

#### solution 4
```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    return n * s
+
+# # 3.2
+def list_length(l):
+    length = 0
+    for i in l:
+        length += 1
+    return length
+
+# # 3.3
```

### map_values (task/32)

#### canonical solution
```python
def map_values(obj, fn):  return dict((k, fn(v)) for k, v in obj.items())
```

#### solution 0
```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+
+    for key, value in obj.items():
+        obj[key] = fn(value)
+    return obj
+
+
+def get_path_class(path):
+    if path in ALL_CLASSES:
+        return
```

#### solution 1
```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+
+    """Map values of an object to new values using a function.
+
+    Args:
+        obj (dict):
+        fn (function): Function to map with.
+
+    Returns:
+        obj (dict):
+    """
```

#### solution 2
```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+
+    if isinstance(obj, dict):
+        return {key: map_values(value, fn) for key, value in obj.items()}
+    if isinstance(obj, list):
+        return [map_
```

#### solution 3
```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+
+    """
+    Maps all values in a collection using a given function
+    """
+    if type(obj) is dict:
+        return {key: fn(val) for key, val in obj.items()}
+   
```

#### solution 4
```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+
+    """
+    Apply a function to every element in an object
+
+    The function must take one argument and return one value. The object can be any
+    type that can be indexed with a number, string, or tuple of numbers or
```

### hex_to_rgb (task/33)

#### canonical solution
```python
def hex_to_rgb(hex):  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
```

#### solution 0
```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    return [int(hex[i:i+2], 16) for i in range(1,6,2)]
+
+def rgb_to_hex(rgb):
+    return "#"+"".join(["
```

#### solution 1
```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
+
+def get_dominant_color(image):
+    image = image.convert('RGBA
```

#### solution 2
```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    hex = hex.lstrip('#')
+    hlen = len(hex)
+    return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen,
```

#### solution 3
```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    h = hex.lstrip('#')
+    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
+
+def rgb_to_hex(rgb):
```

#### solution 4
```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    hex = hex.lstrip('#')
+    hlen = len(hex)
+    return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen,
```

### shuffle (task/34)

#### canonical solution
```python
from copy import deepcopy
from random import randint

def shuffle(lst):  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
```

#### solution 0
```diff
-from copy import deepcopy
-from random import randint
-
-def shuffle(lst):
+from copy import deepcopy
+from random import randint
+
+def shuffle(lst):
+
+    for i in range(len(lst)):
+        r = randint(0, i)
+        tmp = lst[i]
+        lst[i] = lst[r]
+        lst
```

#### solution 1
```diff
-from copy import deepcopy
-from random import randint
-
-def shuffle(lst):
+from copy import deepcopy
+from random import randint
+
+def shuffle(lst):
+
+    """Returns a copy of lst that has been shuffled.
+    shuffle(list) -> list
+    """
+    if not lst:
+        return []
+    else:
+        lst = deepcopy(l
```

#### solution 2
```diff
-from copy import deepcopy
-from random import randint
-
-def shuffle(lst):
+from copy import deepcopy
+from random import randint
+
+def shuffle(lst):
+
+    """
+    Shuffles a list in random order
+    """
+    lst = deepcopy(lst)
+    shuffled = []
+    while len(lst) > 0:
+        index = randint
```

#### solution 3
```diff
-from copy import deepcopy
-from random import randint
-
-def shuffle(lst):
+from copy import deepcopy
+from random import randint
+
+def shuffle(lst):
+
+    """
+    Returns a randomly shuffled copy of a list.
+    """
+    shf = deepcopy(lst)
+    n = len(shf)
+    for i in range(n):
+        j
```

#### solution 4
```diff
-from copy import deepcopy
-from random import randint
-
-def shuffle(lst):
+from copy import deepcopy
+from random import randint
+
+def shuffle(lst):
+
+    new_lst = deepcopy(lst)
+    for i in range(0, len(new_lst)):
+        while new_lst[i] != i + 1:
+            new_l
```

### find_index (task/35)

#### canonical solution
```python
def find_index(lst, fn):  return next(i for i, x in enumerate(lst) if fn(x))
```

#### solution 0
```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+
+    for i, e in enumerate(lst):
+        if fn(e):
+            return i
+    return None
+
+class Dictionary:
+    def __init__(self, words):
+        self.by_
```

#### solution 1
```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+
+    for i, e in enumerate(lst):
+        if fn(e):
+            return i
+    return None
+
+def load_images():
+    res = {}
+    for path in glob.glob(
```

#### solution 2
```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+
+    for i, value in enumerate(lst):
+        if fn(value):
+            return i
+    return None
+
+def first_true(lst, pred):
+    for value in lst:
+       
```

#### solution 3
```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+
+    for i, value in enumerate(lst):
+        if fn(value):
+            return i
+    return None
+
+def find_index_left(lst, fn):
+    for i, value in enumer
```

#### solution 4
```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+
+    for i, value in enumerate(lst):
+        if fn(value):
+            return i
+    return None
+
+def load_data(file_name):
+    with open(file_name, 'r
```

### num_to_range (task/36)

#### canonical solution
```python
def num_to_range(num, inMin, inMax, outMin, outMax):  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

#### solution 0
```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    return (num - inMin) * (outMax - outMin) / (inMax - inMin) + outMin
+
+def _handle_led_all(option):
+    global LED_COUNT
+    if
```

#### solution 1
```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    """
+    Convert a number from one range to another.
+    See: http://arduino.cc/en/Reference/Map
+    """
+    return (num - inMin) * (outMax - outMin
```

#### solution 2
```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    return (num - inMin) * (outMax - outMin) / (inMax - inMin) + outMin
+
+def map_range(value, from_min, from_max, to_min, to
```

#### solution 3
```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    return (num - inMin) * (outMax - outMin) / (inMax - inMin) + outMin;
+
+def clamp(num, min, max):
+    if num < min:
+        return
```

#### solution 4
```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    return (num - inMin) * (outMax - outMin) / (inMax - inMin) + outMin
+
+# def read_temp_raw():
+#     f = open(device_file, '
```

### transpose (task/37)

#### canonical solution
```python
def transpose(lst):  return list(zip(*lst))
```

#### solution 0
```diff
-def transpose(lst):
+def transpose(lst):
+
+    return [list(x) for x in zip(*lst)]
+
+def main():
+    tests = [
+        [[1,2,3],[4,5,6],[7,8,9]],
+       
```

#### solution 1
```diff
-def transpose(lst):
+def transpose(lst):
+
+    """Swap the rows and columns in a list of lists representing a 2D matrix.
+
+    Args:
+        lst: list of lists representing a 2D matrix
+
+    Returns:
+        transposed list of lists
```

#### solution 2
```diff
-def transpose(lst):
+def transpose(lst):
+
+    for i in range(len(lst)):
+        for j in range(i):
+            if len(lst[i]) <= len(lst[j]):
+                break
+            else:
+               
```

#### solution 3
```diff
-def transpose(lst):
+def transpose(lst):
+
+    lst = list(lst)
+    lst = [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]
+   
```

#### solution 4
```diff
-def transpose(lst):
+def transpose(lst):
+
+    return list(map(list, zip(*lst)))
+
+def multiple_matrix_multiply(matrix_lst):
+    lst = transpose(matrix_lst)
+    return list
```

### is_even (task/38)

#### canonical solution
```python
def is_even(num):  return num % 2 == 0
```

#### solution 0
```diff
-def is_even(num):
+def is_even(num):
+
+    if num % 2 == 0:
+        return True
+    else:
+        return False
+
+if __name__ == "__main__":
+    number = int(input("Enter a number to check if it is even
```

#### solution 1
```diff
-def is_even(num):
+def is_even(num):
+
+    return num % 2 == 0
+#filter will pass only the values that returns true from the function.
+nums = [3,2,6,8,4,6,2,9]
+evens = list(
```

#### solution 2
```diff
-def is_even(num):
+def is_even(num):
+
+    return num % 2 == 0
+
+def print_string(txt):
+    print(txt)
+
+def return_true():
+    return True
+
+print(is_even(5))
+print(is_even
```

#### solution 3
```diff
-def is_even(num):
+def is_even(num):
+
+    if num % 2 == 0:
+        return True
+    else:
+        return False
+def is_odd(num):
+    if num % 2 == 1:
+        return True
+    else:
+        return False
```

#### solution 4
```diff
-def is_even(num):
+def is_even(num):
+
+    if num % 2 == 0:
+        return True
+    else:
+        return False
+
+# 2. Write a function that accepts a number as an argument and returns a Boolean indicating whether the number is odd.
+def is
```

### max_element_index (task/39)

#### canonical solution
```python
def max_element_index(arr):  return arr.index(max(arr))
```

#### solution 0
```diff
-def max_element_index(arr):
+def max_element_index(arr):
+
+    max_val = arr[0]
+    max_idx = 0
+    for i in range(1, len(arr)):
+        if arr[i] > max_val:
+            max_val =
```

#### solution 1
```diff
-def max_element_index(arr):
+def max_element_index(arr):
+
+    if len(arr) == 0:
+        return None
+    current_max = arr[0]
+    current_max_index = 0
+    for i in range(1, len(arr)):
+        if
```

#### solution 2
```diff
-def max_element_index(arr):
+def max_element_index(arr):
+
+    max_element = arr[0]
+    max_index = 0
+    for i in range(1, len(arr)):
+        if arr[i] > max_element:
+            max_element = arr
```

#### solution 3
```diff
-def max_element_index(arr):
+def max_element_index(arr):
+
+    max_index = 0
+    max_value = arr[0]
+    for i in range(1, len(arr)):
+        if arr[i] > max_value:
+            max_value = arr
```

#### solution 4
```diff
-def max_element_index(arr):
+def max_element_index(arr):
+
+    max_element = arr[0]
+    max_index = 0
+    for i in range(1, len(arr)):
+        if arr[i] > max_element:
+            max_element = arr
```

### min_n (task/40)

#### canonical solution
```python
def min_n(lst, n = 1):  return sorted(lst, reverse = False)[:n]
```

#### solution 0
```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+
+    lst = list(set(lst))
+    lst.sort()
+    return lst[:n]
+
+def max_n(lst, n = 1):
+    lst = list(set
```

#### solution 1
```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+
+    min = lst[0]
+    for x in range(1, n):
+        if min > lst[x]:
+            min = lst[x]
+    return min
+
+def max_n(
```

#### solution 2
```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+
+    if len(lst) < n:
+        return lst
+    lst.sort()
+    return lst[:n]
+
+def med_n(lst, n = 1):
+    if len
```

#### solution 3
```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+
+    return heapq.nsmallest(n, lst)
+
+def max_n(lst, n = 1):
+    return heapq.nlargest(n, lst)
+
+def add_to_
```

#### solution 4
```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+
+    if lst == []:
+        return None
+    for i in range(n):
+        min_val = lst[0]
+        for j in range(len(lst)):
+            if lst
```

### take_right (task/41)

#### canonical solution
```python
def take_right(itr, n = 1):  return itr[-n:]
```

#### solution 0
```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+
+    """ 
+    Return the last n elements of an iterator. 
+    """
+    return itr[-n:]
+
+def take_left(itr, n = 1):
+    """ 
+    Return the
```

#### solution 1
```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+
+    '''returns the last n elements from the iterable'''
+    #TODO: use itertools.islice
+    assert n >= 0
+    itr = iter(itr)
+    for _
```

#### solution 2
```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+
+    '''
+    itr : iterator to take right
+    n : number of elements to take
+    '''
+    for _ in range(n):
+        itr, _ = itertools.tee(it
```

#### solution 3
```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+
+    if n < 1:
+        raise ValueError("The number of elements to return must be > 0")
+    return itr[-n:]
+
+def take_left(itr, n = 1):
+    if
```

#### solution 4
```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+
+    """
+    This function takes the right side of an iterable and returns
+    it as a new iterable.
+    """
+    return itr[-n:]
+
+
+# -----------------------------------------------------------------------------
+# TESTING
+# ----------------------------------------------------------------
```

### filter_unique (task/42)

#### canonical solution
```python
from collections import Counter

def filter_unique(lst):  return [item for item, count in Counter(lst).items() if count > 1]
```

#### solution 0
```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    return [l for l, _ in Counter(lst).most_common()]
+
+class Controller:
+    def __init__(self, interfaces):
+        self.interfaces = interfaces
+        self.datap
```

#### solution 1
```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    seen = set()
+    seen_add = seen.add
+    return [x for x in lst if not (x in seen or seen_add(x))]
+
+def load_vocab(vocab_
```

#### solution 2
```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    """
+    filter out non-unique elements in the list, order of elements should not change
+    :param lst: List[Int]
+    :return: List[Int]
+    """
+    return [x for
```

#### solution 3
```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    return [item for item, count in Counter(lst).items() if count == 1]
+
+def filter_non_unique(lst):
+    return [item for item, count in Counter(lst).items
```

#### solution 4
```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    counts = Counter(lst)
+    return [x for x in lst if counts[x] == 1]
+
+def calculate_table(lst):
+    lst.sort()
+    return lst[
```

### arithmetic_progression (task/43)

#### canonical solution
```python
def arithmetic_progression(n, lim):  return list(range(n, lim + 1, n))
```

#### solution 0
```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+
+    if n == 1:
+        return lim
+    return lim + (n - 1) * lim
+
+def get_nth_triangular_number(n):
+    return arithmetic_progression(n, 1)
```

#### solution 1
```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+
+    last = 0
+    cur = 1
+    yield 0
+    while last + cur < lim:
+        yield last + cur
+        last, cur = cur, last + cur
+    yield lim
+
+
+def pentagonal_
```

#### solution 2
```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+
+    for i in range(1, lim+1):
+        if n % i == 0:
+            print(i)
+
+arithmetic_progression(n, lim)
```

#### solution 3
```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+
+    # 公差
+    d = (lim - n) / (n - 1)
+    # 等差数列
+    a = n - 1
+    return a, d
+
+
```

#### solution 4
```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+
+    ls = []
+    start = 1
+    while start <= lim:
+        ls.append(start)
+        start += n
+    return ls
+
+
+def geometric_progression(n, lim):
+    ls =
```

### merge_dictionaries (task/44)

#### canonical solution
```python
def merge_dictionaries(*dicts):  res = dict()
  for d in dicts:
    res.update(d)
  return res
```

#### solution 0
```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+
+    """
+    Return a new dictionary that contains all the keys and values of the
+    dictionaries passed as arguments. In case of conflicts, values
+    from dictionaries to the right have precedence over those to the
+    left.
```

#### solution 1
```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+
+    '''
+    Merge the input dictionaries.
+    Only the first layer will be merged and the deep copy will be returned.
+    '''
+    result = {}
+    for d in dicts:
+        result.
```

#### solution 2
```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+
+    """Merge dictionaries into a new dictionary"""
+    merged = {}
+    for dict in dicts:
+        merged.update(dict)
+    return merged
+
+
+def generate_password(password_length=20):
```

#### solution 3
```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+
+    return dict(chain(*[d.iteritems() for d in dicts]))
+
+
+def finalize_evaluation(evaluation, do_print=True):
+    evaluation.update({
+        'model': {
```

#### solution 4
```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+
+    """
+    Merges dictionaries in *dicts argument into one
+    """
+    result = {}
+    for dictionary in dicts:
+        result.update(dictionary)
+    return result
+
+
+def random_
```

### sort_by_indexes (task/45)

#### canonical solution
```python
def sort_by_indexes(lst, indexes, reverse=False):  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]
```

#### solution 0
```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+
+    indexes_map = {idx: i for i, idx in enumerate(indexes)}
+    return sorted(lst, key=lambda x: indexes_map[x], reverse=reverse)
+
+
+def chunks
```

#### solution 1
```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+
+    return [lst[i] for i in indexes]
+
+def sort_lists_by_first_list(lists, reverse=False):
+    sorted_lists = []
+    ordered_indexes = sorted(range
```

#### solution 2
```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+
+    return [lst[i] for i in indexes]
+
+
+def sort_by_scores(lst, scores, reverse=False):
+    return sort_by_indexes(lst,
+                           [
```

#### solution 3
```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+
+    '''
+    Sort the list `lst` by indexes in the list `indexes`
+    '''
+    pairs = [(lst[i], i) for i in indexes]
+    pairs.sort(reverse
```

#### solution 4
```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+
+    return [x for _, x in sorted(zip(indexes, lst), reverse=reverse)]
+
+
+def convert_to_js_timestamp(timestamp):
+    return int(timestamp * 1000)
+
```

### get (task/46)

#### canonical solution
```python
from functools import reduce 
from operator import getitem

def get(d, selectors):  return reduce(getitem, selectors, d)
```

#### solution 0
```diff
-from functools import reduce 
-from operator import getitem
-
-def get(d, selectors):
+from functools import reduce 
+from operator import getitem
+
+def get(d, selectors):
+
+    if not isinstance(selectors, list):
+        selectors = [selectors]
+    return reduce(getitem, selectors, d)
+
+def set(d, selectors, value):
+    get(
```

#### solution 1
```diff
-from functools import reduce 
-from operator import getitem
-
-def get(d, selectors):
+from functools import reduce 
+from operator import getitem
+
+def get(d, selectors):
+
+    return reduce(getitem, selectors, d)
+
+def set(d, selectors, value):
+    get(d, selectors[:-1])[selectors[-1]] = value
+
+def load
```

#### solution 2
```diff
-from functools import reduce 
-from operator import getitem
-
-def get(d, selectors):
+from functools import reduce 
+from operator import getitem
+
+def get(d, selectors):
+
+    return reduce(getitem, selectors, d)
+
+def set(d, selectors, value):
+    get(d, selectors[:-1])[selectors[-1]] = value
+
+def main
```

#### solution 3
```diff
-from functools import reduce 
-from operator import getitem
-
-def get(d, selectors):
+from functools import reduce 
+from operator import getitem
+
+def get(d, selectors):
+
+    """
+    >>> d = {1: {2: {3: {4: {5: 6}}}}}
+    >>> get(d, [1, 2, 3, 4, 5])
+    6
+    """
```

#### solution 4
```diff
-from functools import reduce 
-from operator import getitem
-
-def get(d, selectors):
+from functools import reduce 
+from operator import getitem
+
+def get(d, selectors):
+
+    """
+    Return a value from a nested dict.
+
+    This function is an alternative to the dict method `get`.
+    `get` returns a default value if a key is not found.
+
+    Parameters
+    ----------
```

### bifurcate_by (task/47)

#### canonical solution
```python
def bifurcate_by(lst, fn):  return [
    [x for x in lst if fn(x)],
    [x for x in lst if not fn(x)]
  ]
```

#### solution 0
```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+
+    return [
+        [x for x in lst if fn(x)],
+        [x for x in lst if not fn(x)]
+    ]
+
+
+def bifurcate(lst, fn
```

#### solution 1
```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+
+    return [
+        [x for x in lst if fn(x)],
+        [x for x in lst if not fn(x)]
+    ]
+
+def flatten(l):
+    return [item
```

#### solution 2
```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+
+    return [
+        [x for x in lst if fn(x)],
+        [x for x in lst if not fn(x)]
+    ]
+
+def partition_by(lst, fn):
```

#### solution 3
```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+
+    return [
+        [x for x in lst if fn(x)],
+        [x for x in lst if not fn(x)]
+    ]
+
+# ------------------------------------------------------------------------------
+# Working with files
+# ----------------------------------------------------------------
```

#### solution 4
```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+
+    return [
+        [x for x in lst if fn(x)],
+        [x for x in lst if not fn(x)]
+    ]
+
+# A representation of a single Node in the network.
```

### fibonacci (task/48)

#### canonical solution
```python
def fibonacci(n):  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence
```

#### solution 0
```diff
-def fibonacci(n):
+def fibonacci(n):
+
+    if n == 0:
+        return 0
+    elif n == 1:
+        return 1
+    else:
+        return fibonacci(n-1) + fibonacci(n-2)
+
+print
```

#### solution 1
```diff
-def fibonacci(n):
+def fibonacci(n):
+
+    if n <= 1:
+        return n
+    else:
+        return fibonacci(n-1) + fibonacci(n-2)
+
+def ejercicio_7():
+    n = int
```

#### solution 2
```diff
-def fibonacci(n):
+def fibonacci(n):
+
+    """Fibonacci series."""
+    if n == 0:
+        return 0
+    elif n == 1:
+        return 1
+    else:
+        return fibonacci(n-1) + fib
```

#### solution 3
```diff
-def fibonacci(n):
+def fibonacci(n):
+
+    a = 0
+    b = 1
+    for i in range(n):
+        temp = a
+        a = b
+        b = temp + b
+    return a
+
+# Driver Program
+
+print(f
```

#### solution 4
```diff
-def fibonacci(n):
+def fibonacci(n):
+
+    a, b = 0, 1
+    while a < n:
+        print(a, end=' ')
+        a, b = b, a+b
+    print()
+
+fibonacci(2000)
```

### invert_dictionary (task/49)

#### canonical solution
```python
def invert_dictionary(obj):  return { value: key for key, value in obj.items() }
```

#### solution 0
```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+
+    out = {}
+    for k, v in obj.items():
+        out[v] = k
+    return out
+
+
+def string_to_array(string):
+    return np.array(string.split('
```

#### solution 1
```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+
+    """
+    Inverts a dictionary that maps keys to sets.
+
+    `obj` must map each key to a set of keys. The returned
+    dictionary maps each key in the sets to a set of keys from
+    the
```

#### solution 2
```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+
+    """
+    Inverts a dictionary object.
+
+    :param obj: Dictionary to invert.
+    :return: Dictionary with the keys and values swapped.
+    """
+    return {v: k for k, v in
```

#### solution 3
```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+
+    """
+    Inverts a dictionary.
+
+    :param obj: Dictionary to invert.
+    :return: Reversed dictionary.
+    """
+    return {v: k for k, v in obj.items()
```

#### solution 4
```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+
+    """
+    Inverts a dictionary.
+
+    Parameters
+    ----------
+    obj : dict
+        Dictionary to invert.
+
+    Returns
+    -------
+    dict
+        Inverted dictionary.
+    """
+    return
```

### camel (task/50)

#### canonical solution
```python
from re import sub

def camel(s):  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])
```

#### solution 0
```diff
-from re import sub
-
-def camel(s):
+from re import sub
+
+def camel(s):
+
+    a = sub('(.)([A-Z][a-z]+)', r'\1 \2', s)
+    return sub('([a-z0-9])([A-Z])', r'
```

#### solution 1
```diff
-from re import sub
-
-def camel(s):
+from re import sub
+
+def camel(s):
+
+    return sub(r'(?:^|_)(.)', lambda m: m.group(1).upper(), s)
+
+def dasherize(s):
+    return sub(r'([A-Z])',
```

#### solution 2
```diff
-from re import sub
-
-def camel(s):
+from re import sub
+
+def camel(s):
+
+    # Replace dash with space and then capitalize the first letter of each word.
+    # If the first letter is a number capitalize that as well.
+    # Remove dashes and slashes.
+    # This function is used to
```

#### solution 3
```diff
-from re import sub
-
-def camel(s):
+from re import sub
+
+def camel(s):
+
+    '''
+    Convert string to camelCase
+    s: string
+    '''
+    return sub(r'\s', '', sub(r'\W+', '', s)).lower()
```

#### solution 4
```diff
-from re import sub
-
-def camel(s):
+from re import sub
+
+def camel(s):
+
+    return sub(r'([^A-Z])([A-Z])', r'\1_\2', s).lower()
+
+def setup(app):
+    app.connect('autodoc-process
```

### key_of_min (task/51)

#### canonical solution
```python
def key_of_min(d):  return min(d, key = d.get)
```

#### solution 0
```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    v = list(d.values())
+    k = list(d.keys())
+    return k[v.index(min(v))]
+
+# 读取文件
+def readfile
```

#### solution 1
```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    """
+    Returns the key of the minimum value of a dictionary
+
+    Parameters
+    ----------
+    d : dict
+        Dictionary of numerical values
+
+    Returns
+    -------
+    key : hashable
+        The key of
```

#### solution 2
```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    d_copy = d.copy()
+    m = min(d_copy.values())
+    for k in d_copy:
+        if d_copy[k] == m:
+            return k
+
+def
```

#### solution 3
```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    v = list(d.values())
+    k = list(d.keys())
+    return k[v.index(min(v))]
+
+#Function to find the key of max dict value
+def key_
```

#### solution 4
```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    """Return key of a dict d that corresponds to its minimum value.
+    Assumes that d has at least one value.
+    """
+    min_key = None
+    min_val = None
+    for key,
```

### capitalize (task/52)

#### canonical solution
```python
def capitalize(s, lower_rest = False):  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

#### solution 0
```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+
+    """Capitalize a string, optionally leaving the rest of the string alone"""
+    return s[:1].upper() + (s[1:].lower() if lower_rest else s[1:])
+
+def clean
```

#### solution 1
```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+
+    return s[:1].upper() + (s[1:].lower() if lower_rest else s[1:])
+
+def full_folder_path(local_path):
+    return os.path.join
```

#### solution 2
```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+
+    return s[:1].upper() + (s[1:].lower() if lower_rest else s[1:])
+
+def check_isinstance(obj, cls):
+    """Checks that obj is
```

#### solution 3
```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+
+    return s[:1].upper() + (s[1:].lower() if lower_rest else s[1:])
+
+def get_readme_dev_changed_files():
+    changed_files = sub
```

#### solution 4
```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+
+    return s[:1].upper() + (s[1:].lower() if lower_rest else s[1:])
+
+def get_class( kls ):
+    parts = kls.split('.')
```

### celsius_to_fahrenheit (task/53)

#### canonical solution
```python
def celsius_to_fahrenheit(degrees):  return ((degrees * 1.8) + 32)
```

#### solution 0
```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+
+    """Convert celsius to fahrenheit."""
+    return degrees * 9.0 / 5 + 32
+
+
+class Thermostat(object):
+    """Class to represent a thermostat."""
+
+    def __
```

#### solution 1
```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+
+    return degrees * 1.8 + 32
+
+if __name__ == '__main__':
+    print("Testing function celsius_to_fahrenheit()...")
+    test(celsius_to_f
```

#### solution 2
```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+
+    return degrees * 9 / 5 + 32
+
+# converts fahrenheit to celsius
+def fahrenheit_to_celsius(degrees):
+    return (degrees - 32) * 5 / 9
```

#### solution 3
```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+
+    return degrees * 1.8 + 32
+
+
+def fahrenheit_to_celsius(degrees):
+    return (degrees - 32) / 1.8
+
+
+def main():
+    user_input =
```

#### solution 4
```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+
+    '''Returns the input temperature in degrees Fahrenheit
+
+    Takes a temperature in degrees Celsius, converts it to degrees Fahrenheit,
+    and returns the result.
+    '''
+    return degrees * 1.8 + 32.0
+
```

### every_nth (task/54)

#### canonical solution
```python
def every_nth(lst, nth):  return lst[nth - 1::nth]
```

#### solution 0
```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+
+    return [lst[i] for i in range(0, len(lst), nth)]
+
+def make_sublattice_z(atom_type, atom_x, atom_y, data_
```

#### solution 1
```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+
+    return lst[::nth]
+every_nth([1,2,3,4,5,6,7,8,9], 2)
+def every_nth(lst, nth):
```

#### solution 2
```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+
+    """Return every nth item in list"""
+    return lst[::nth]
+
+
+def every_second(lst):
+    """Return every second item in list"""
+    return lst[::2]
```

#### solution 3
```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+
+    out = []
+    i = 0
+    while i < len(lst):
+        out.append(lst[i])
+        i += nth
+    return out
+
+# Slicing
+# 
```

#### solution 4
```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+
+    """
+    >>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
+    >>> every_nth(lst, 3)
+    [3, 6,
```

### union (task/55)

#### canonical solution
```python
def union(a, b):  return list(set(a + b))
```

#### solution 0
```diff
-def union(a, b):
+def union(a, b):
+
+    """ return the union of two lists """
+    return list(set(a) | set(b))
+
+def get_file_name_from_dates(date_from, date_to, publisher=None, extension
```

#### solution 1
```diff
-def union(a, b):
+def union(a, b):
+
+    return max(a[0], b[0]), min(a[1], b[1])
+
+
+def intersect(a, b):
+    return min(a[0], b[0]), max(a[1
```

#### solution 2
```diff
-def union(a, b):
+def union(a, b):
+
+    return [e for e in a] + [e for e in b if e not in a]
+
+# To do a union we just need to use the function union that we defined above.
+union(first, second)
```

#### solution 3
```diff
-def union(a, b):
+def union(a, b):
+
+    a = np.asarray(a)
+    b = np.asarray(b)
+    c = np.unique(np.concatenate((a, b)))
+    return c
+
+
+def intersection(
```

#### solution 4
```diff
-def union(a, b):
+def union(a, b):
+
+    return a | b
+
+
+def intersection(a, b):
+    return a & b
+
+
+def difference(a, b):
+    return a - b
+
+
+def symmetric_difference(a, b):
```

### drop (task/56)

#### canonical solution
```python
def drop(a, n = 1):  return a[n:]
```

#### solution 0
```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+
+    return a[n:]
+
+def bind(f, *args):
+    return lambda x: f(x, *args)
+
+def compose(f, g):
+    return lambda x: f(g(x
```

#### solution 1
```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+
+    return a[n:]
+
+def cut(a, n = 1):
+    return a[:-n]
+
+def rev(a):
+    return a[::-1]
+
+def lwr(a):
```

#### solution 2
```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+
+    for _ in range(n):
+        a.pop()
+    return a
+
+def roll(a, n = 1):
+    for _ in range(n):
+        b = a.pop()
+        a
```

#### solution 3
```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+
+    """Return the rest of the elements of a sequence when n elements are removed."""
+    for i in range(n):
+        a.pop(0)
+    return a
+
+def drop_right(a, n
```

#### solution 4
```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+
+    a = list(a)
+    return a[n:] + a[:n]
+
+def mod(a, b):
+    return a % b
+
+def gcd(a, b):
+    while b
```

### frequencies (task/57)

#### canonical solution
```python
from collections import defaultdict

def frequencies(lst):  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq)
```

#### solution 0
```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    freq = defaultdict(int)
+    for v in lst:
+        freq[v] += 1
+    return freq
+
+def combinadic(n):
+    return [(x,y) for
```

#### solution 1
```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    d = defaultdict(int)
+    for el in lst:
+        d[el] += 1
+    return d
+
+
+def main():
+    input_file = sys.argv[1]
+    output
```

#### solution 2
```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    freq = defaultdict(int)
+    for elem in lst:
+        freq[elem] += 1
+    return freq
+
+def most_frequent(lst):
+    freq =
```

#### solution 3
```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    d = defaultdict(int)
+    for x in lst:
+        d[x] += 1
+    return d
+
+def main():
+    parser = argparse.ArgumentParser()
+    parser.add
```

#### solution 4
```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    freq = defaultdict(int)
+    for l in lst:
+        freq[l] += 1
+    return freq
+
+class Tree:
+    def __init__(self, freq, left
```

### initialize_list_with_range (task/58)

#### canonical solution
```python
def initialize_list_with_range(end, start = 0, step = 1):  return list(range(start, end + 1, step))
```

#### solution 0
```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+
+    """Return a list that has the value of start and goes up to the number
+    before end in increments of step."""
+    l = []
+    while start < end:
+        l.append(start)
+       
```

#### solution 1
```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+
+    """
+    Initialize a list with a given range
+
+    :param end:
+    :param start:
+    :param step:
+    :return:
+    """
+    my_list = []
+    while start
```

#### solution 2
```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+
+    """
+    Function to initialize a list from a range.
+    :param end: The upper bound of the range
+    :param start: The lower bound of the range. Default is 0
+    :param step: The step
```

#### solution 3
```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+
+    l = []
+    for i in range(start, end, step):
+        l.append(i)
+    return l
+
+print initialize_list_with_range(20)
+print initialize_list_with
```

#### solution 4
```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+
+    list = []
+    i = start
+    while i < end:
+        list.append(i)
+        i += step
+    return list
+
+def initialize_dict_with_pairs(pairs):
```

### cumsum (task/59)

#### canonical solution
```python
from itertools import accumulate

def cumsum(lst):  return list(accumulate(lst))
```

#### solution 0
```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    return list(accumulate(lst))
+
+def cumsum2(lst):
+    return [sum(lst[:i+1]) for i in range(len(lst))]
+
```

#### solution 1
```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    return list(accumulate(lst))
+
+N = int(input())
+
+div = 10**9 + 7
+
+# 文字列をリスト化する
+a = list
```

#### solution 2
```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    accum = 0
+    for i in lst:
+        accum += i
+        yield accum
+
+def chunk(lst, n):
+    for i in range(0, len(lst), n):
+       
```

#### solution 3
```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    return list(accumulate(lst))
+
+def main():
+    n = int(input())
+    x = list(map(int, input().split()))
+    y = list(map(int,
```

#### solution 4
```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    return [0] + list(accumulate(lst))
+
+lst = [0,1,2,3,4,5,6,7,8,9]
+print(cumsum(l
```

### months_diff (task/60)

#### canonical solution
```python
from math import ceil

def months_diff(start, end):  return ceil((end - start).days / 30)
```

#### solution 0
```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    """
+    Number of months between two dates.
+    :param start: Start date
+    :param end: End date
+    :return: Int with number of months
+    """
+    # TODO: implement
+   
```

#### solution 1
```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    if start == end:
+        return 0
+    if start[0] == end[0]:
+        return 0
+    if start[1] == end[1]:
+        return 0
+    return 12 * (end
```

#### solution 2
```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    result = end.year - start.year
+    if end.month < start.month:
+        result -= 1
+    elif end.month == start.month and end.day < start.day:
+        result
```

#### solution 3
```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    """
+    Number of months between two dates
+    """
+    # copy dates so don't mutate the originals
+    start = start.replace(hour=0, minute=0, second=0, microsecond=0
```

#### solution 4
```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    return (end.year - start.year) * 12 + end.month - start.month + 1
+
+def main():
+    loan_amount = int(input())
+    down_payment = int(input())
```

### collect_dictionary (task/61)

#### canonical solution
```python
from collections import defaultdict

def collect_dictionary(obj):  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)
```

#### solution 0
```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    words = set()
+    word_freq = defaultdict(int)
+    def do_collect(obj):
+        if obj.type in ['string', 'html']:
+            text = obj.as_html
```

#### solution 1
```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    if isinstance(obj, list):
+        return collect_dictionary_list(obj)
+    elif isinstance(obj, dict):
+        return collect_dictionary_dict(obj)
+    else:
```

#### solution 2
```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    return {key: value for key, value in obj.__dict__.items() if not key.startswith('__')}
+
+def make_action_list(action_list):
+    return [collect_
```

#### solution 3
```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    """
+    Given a dictionary or list of dictionaries, this method flattens it to a
+    single dictionary. This method will also sort the keys in the dictionary.
+    """
+    # If it's a dictionary, just
```

#### solution 4
```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    """Collect attributes and methods for object.
+
+    Args:
+        obj (:obj:`object`): object from which the attributes and methods will be collected.
+
+    Returns:
+        :obj:`dict` of
```

### binomial_coefficient (task/62)

#### canonical solution
```python
from math import comb

def binomial_coefficient(n, k):  return comb(n, k)
```

#### solution 0
```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    return comb(n, k, exact=True)
+
+# binomial_coefficient(5, 2)
+# Out[108]: 10
+
+# We can use this function to implement the nCk function as follows
```

#### solution 1
```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    return comb(n, k, exact=True)
+
+def pascals_triangle(rows):
+    result = []
+    for count in range(rows):
+        row = []
+        for element in range
```

#### solution 2
```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    return comb(n, k, exact=True)
+
+n = 5
+k = 2
+print(binomial_coefficient(n, k))
```

#### solution 3
```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    return comb(n, k, exact=True)
+
+n = [100, 1000, 10000, 100000, 1000000]
+for i in n:
+    print(i, binomial_coefficient(i,
```

#### solution 4
```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    return comb(n, k, exact=True)
+
+n = int(input())
+for _ in range(n):
+    print(binomial_coefficient(*map(int, input().split())))
```

### find_keys (task/63)

#### canonical solution
```python
def find_keys(dict, val):  return list(key for key, value in dict.items() if value == val)
```

#### solution 0
```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    return [k for k, v in dict.items() if v == val]
+
+
+def _get_n_params(model):
+    pp = 0
+    for p in list(model.parameters()):
```

#### solution 1
```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    """
+    Returns the key of the dict element with the given value.
+
+    If the given value is not in the dict, returns an empty array.
+    """
+    return [k for k, v in dict.items
```

#### solution 2
```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    """Return list of keys where the value is val."""
+    return [k for k, v in dict.items() if v == val]
+
+
+def is_ascii(s):
+    """Check whether the
```

#### solution 3
```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    """return the key of dictionary dic given the value"""
+    try:
+        return [k for k, v in dict.iteritems() if v == val][0]
+    except KeyError:
+        return None
```

#### solution 4
```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    """return the key of dictionary dic given the value"""
+    return [k for k, v in dict.iteritems() if v == val]
+
+# methods for obtaining 
+def get_gene_name(
```

### when (task/64)

#### canonical solution
```python
def when(predicate, when_true):  return lambda x: when_true(x) if predicate(x) else x
```

#### solution 0
```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+
+    return lambda x: when_true(x) if predicate(x) else x
+
+def nested_when(predicate, list_of_when_true):
+    return lambda x: list_of_when_true
```

#### solution 1
```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+
+    def wrapper(fn):
+        def inner(*args, **kwargs):
+            if predicate(*args, **kwargs):
+                return when_true(*args, **kwargs)
+            else:
+                return fn
```

#### solution 2
```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+
+    """
+    This function is like :meth:`itertools.compress()` where *when_true* is
+    the selector sequence and *predicate* filters the values.
+    The difference is that *
```

#### solution 3
```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+
+    return when_true() if predicate else None
+
+
+def unless(predicate, when_false):
+    return when_false() if not predicate else None
+
+
+def is_char(data):
+    """
+    Return
```

#### solution 4
```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+
+    if predicate():
+        return when_true()
+    return None
+
+# @when(menu_choice == 'p', prepare_meal)
+
+def menu_choice():
+    return input("""
+    What would
```

### chunk_into_n (task/65)

#### canonical solution
```python
from math import ceil

def chunk_into_n(lst, n):  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )
```

#### solution 0
```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    """
+    Yield successive n-sized chunks from lst.
+    """
+    for i in range(0, len(lst), n):
+        yield lst[i:i + n]
+
+def
```

#### solution 1
```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    return [lst[i:i + n] for i in range(0, len(lst), n)]
+
+def crop_to_n(lst, n):
+    return lst[:n]
```

#### solution 2
```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    '''
+    Splits a list into n sublists.
+    '''
+    return [lst[i::n] for i in range(n)]
+
+def flatten(lst):
+    '''
```

#### solution 3
```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    return [lst[i:i + n] for i in range(0, len(lst), n)]
+
+def list_to_str(lst):
+    return '\n'.join(map(
```

#### solution 4
```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    """
+    Splits a list into n smaller lists of roughly equal size.
+    Returns a list of lists.
+    """
+    n = int(n)
+    n = max(1, n)
+    return
```

### km_to_miles (task/66)

#### canonical solution
```python
def km_to_miles(km):  return km * 0.621371
```

#### solution 0
```diff
-def km_to_miles(km):
+def km_to_miles(km):
+
+    return km * 0.621371
+
+def main():
+    km = float(input("Enter the distance in kilometers: "))
+    miles = km_to_miles(km)
+    print("The distance
```

#### solution 1
```diff
-def km_to_miles(km):
+def km_to_miles(km):
+
+    return km * 0.621371192
+
+
+def miles_to_km(miles):
+    return miles / 0.621371192
+
+
+def lbs_to_kg(lbs):
+    return lbs *
```

#### solution 2
```diff
-def km_to_miles(km):
+def km_to_miles(km):
+
+    """
+    Function that converts km to miles
+    :param km:
+    :return:
+    """
+    miles = km / 1.609
+    return miles
+
+
+def miles_to_km(miles):
```

#### solution 3
```diff
-def km_to_miles(km):
+def km_to_miles(km):
+
+    return km * 0.621371
+
+def miles_to_km(miles):
+    return miles / 0.621371
+
+def kmh_to_ms(kmh):
+    return kmh
```

#### solution 4
```diff
-def km_to_miles(km):
+def km_to_miles(km):
+
+    return km * 0.621371
+
+if __name__ == '__main__':
+    print(km_to_miles(5))
```

### max_by (task/67)

#### canonical solution
```python
def max_by(lst, fn):  return max(map(fn, lst))
```

#### solution 0
```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+
+    max_result = None
+    max_value = None
+    for i in lst:
+        # TODO: find the element e where fn(e) has the highest value
+        if max_result == None or
```

#### solution 1
```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+
+    if lst == []:
+        return None
+    return_val = lst[0]
+    for item in lst:
+        if fn(item) > fn(return_val):
+            return_val
```

#### solution 2
```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+
+    """
+    Return the largest item in an iterable or the largest of two or more args.
+    """
+    try:
+        return reduce(lambda a, b: a if fn(a) > fn(b)
```

#### solution 3
```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+
+    """Return the element of a list that gives the maximum value from a function.
+
+    >>> square = lambda x: x * x
+    >>> max_by([2, 4, 9, 3, 2], square)
+   
```

#### solution 4
```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+
+    """
+    returns the maximum element of a list,
+    determined by a function.
+    """
+    return reduce(lambda x, y: x if fn(x) > fn(y) else y, lst)
```

### min_element_index (task/68)

#### canonical solution
```python
def min_element_index(arr):  return arr.index(min(arr))
```

#### solution 0
```diff
-def min_element_index(arr):
+def min_element_index(arr):
+
+    min_index = 0
+    for i in range(1, len(arr)):
+        if arr[i] < arr[min_index]:
+            min_index = i
+    return min_index
+
+
```

#### solution 1
```diff
-def min_element_index(arr):
+def min_element_index(arr):
+
+    min_index = 0
+    for i in range(1, len(arr)):
+        if arr[i] < arr[min_index]:
+            min_index = i
+    return min_index
+
+
```

#### solution 2
```diff
-def min_element_index(arr):
+def min_element_index(arr):
+
+    min_idx = 0
+    for i in range(1, len(arr)):
+        if arr[i] < arr[min_idx]:
+            min_idx = i
+    return min_
```

#### solution 3
```diff
-def min_element_index(arr):
+def min_element_index(arr):
+
+    min_elem = arr[0]
+    min_index = 0
+    for i in range(1, len(arr)):
+        if arr[i] < min_elem:
+            min_e
```

#### solution 4
```diff
-def min_element_index(arr):
+def min_element_index(arr):
+
+    """Find minimum value in array"""
+    min_index = 0
+    for i in range(1, len(arr)):
+        if arr[i] < arr[min_index]:
+            min_index =
```

### initialize_2d_list (task/69)

#### canonical solution
```python
def initialize_2d_list(w, h, val = None):  return [[val for x in range(w)] for y in range(h)]
```

#### solution 0
```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    if val == None:
+        val = []
+    return [[val for x in range(w)] for y in range(h)]
+
+def initialize_3d_list(w, h, d, val = None
```

#### solution 1
```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    list = [[val for x in range(w)] for y in range(h)]
+    return list
+
+def create_grid(w, h, val = None):
+    grid = initialize_2d_list(
```

#### solution 2
```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    l = []
+    for i in range(h):
+        l.append([val] * w)
+    return l
+
+#-----------------------------------------------------------------------
+#
+#   get_chunks_indexes_to_remove
```

#### solution 3
```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    return [[val for i in range(w)] for j in range(h)]
+
+def initialize_2d_array(w, h, val = None):
+    return np.full((h, w), val)
```

#### solution 4
```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    """
+    Returns a 2d list of width w and height h, initialized with value val
+    """
+    if val == None:
+        val = 0
+    # Default value is 0
+    ans = []
+   
```

### dict_to_list (task/70)

#### canonical solution
```python
def dict_to_list(d):  return list(d.items())
```

#### solution 0
```diff
-def dict_to_list(d):
+def dict_to_list(d):
+
+    return sorted(d.items(), key=lambda x: x[1], reverse=True)
+
+
+# This class attempts to parse the given character as an integer.
+# If it fails, the value -1 is returned.
```

#### solution 1
```diff
-def dict_to_list(d):
+def dict_to_list(d):
+
+    ''' Return a list of (key, value) tuples, sorted by key '''
+    return sorted(d.items(), key=lambda x: x[0])
+
+
+def dict_to_args(d):
```

#### solution 2
```diff
-def dict_to_list(d):
+def dict_to_list(d):
+
+    return [v for _, v in d.items()]
+
+
+def sum_dicts(dicts):
+    sum_dict = defaultdict(float)
+    for d in dicts:
+        for k,
```

#### solution 3
```diff
-def dict_to_list(d):
+def dict_to_list(d):
+
+    l = []
+    for i in d:
+        l.append((i, d[i]))
+    return l
+
+def get_reg_ex(string):
+    reg_ex = r'^%
```

#### solution 4
```diff
-def dict_to_list(d):
+def dict_to_list(d):
+
+    ret = []
+    for k, v in d.items():
+        ret.append(v)
+    return ret
+
+
+# In[ ]:
+
+
+def list_to_dict(l):
+    ret =
```

### average (task/71)

#### canonical solution
```python
def average(*args):  return sum(args, 0.0) / len(args)
```

#### solution 0
```diff
-def average(*args):
+def average(*args):
+
+    """
+    A function that takes an arbitrary number of arguments and returns their average.
+    """
+    return sum(args) / len(args)
+
+
+def square_root(n):
+    """
+    A function
```

#### solution 1
```diff
-def average(*args):
+def average(*args):
+
+    sum = 0
+    for i in args:
+        sum += i
+    return sum / len(args)
+
+
+print(average(1, 2, 3, 4, 5))
+print(average(1, 2
```

#### solution 2
```diff
-def average(*args):
+def average(*args):
+
+    '''
+    Returns the average of args
+    '''
+    return sum(args) / len(args)
+
+print(average(1, 2, 3, 4))
+
+# If a function does not explicitly
```

#### solution 3
```diff
-def average(*args):
+def average(*args):
+
+    return sum(args) / len(args)
+
+def absolute_value(x):
+    return abs(x)
+
+def squre(x):
+    return x ** 2
+
+print(average(1,
```

#### solution 4
```diff
-def average(*args):
+def average(*args):
+
+    a = 0
+    b = 0
+    n = 0
+    for arg in args:
+        a += arg[0]
+        b += arg[1]
+        n += 1
+    return a/n,
```

### intersection (task/72)

#### canonical solution
```python
def intersection(a, b):  _a, _b = set(a), set(b)
  return list(_a & _b)
```

#### solution 0
```diff
-def intersection(a, b):
+def intersection(a, b):
+
+    return list(set(a) & set(b))
+
+# Which of the following two arrays contains all the unique values?
+a = np.array([[1,2,3],[4,5,6],[7
```

#### solution 1
```diff
-def intersection(a, b):
+def intersection(a, b):
+
+    if a.x > b.x:
+        a, b = b, a
+    return (b.x-a.x)*(a.y-b.y)/(a.y*b.x-
```

#### solution 2
```diff
-def intersection(a, b):
+def intersection(a, b):
+
+    """Determine the intersection of two rectangles"""
+    # Return a dictionary with the keys lo, hi
+    lo = max(a['lo'], b['lo'])
+    hi = min(a['hi
```

#### solution 3
```diff
-def intersection(a, b):
+def intersection(a, b):
+
+    """
+    Determine if two rectangles intersect and return the intersecting rectangle.
+    """
+    r1_start, r1_end = a[0], a[1]
+    r2_start, r
```

#### solution 4
```diff
-def intersection(a, b):
+def intersection(a, b):
+
+    return list(set(a) & set(b))
+
+def getData(filenames):
+    """
+    获取原始数据
+    :param filenames
```

### hamming_distance (task/73)

#### canonical solution
```python
def hamming_distance(a, b):  return bin(a ^ b).count('1')
```

#### solution 0
```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+
+    return sum(c1 != c2 for c1, c2 in zip(a, b))
+
+def decrypt(ciphertext, key):
+    plaintext = ""
+    for i in range(len(c
```

#### solution 1
```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+
+    assert len(a) == len(b)
+    return sum(c1 != c2 for c1, c2 in zip(a, b))
+
+# return percentage of symbols that match the reference
+def get_
```

#### solution 2
```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+
+    '''
+    Calculate the hamming distance of two equal-length strings.
+    The strings should be the same length, or bad things will happen.
+    '''
+    return sum(a[i] != b
```

#### solution 3
```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+
+    return np.sum(a != b)
+
+
+def train_test_split(X, y, test_size=0.2, random_state=None):
+    """split the given data into train and test sets
```

#### solution 4
```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+
+    ''' Return the Hamming distance between equal-length sequences '''
+    if len(a) != len(b):
+        raise ValueError("Undefined for sequences of unequal length")
+    return sum(ch1 !=
```

### digitize (task/74)

#### canonical solution
```python
def digitize(n):  return list(map(int, str(n)))
```

#### solution 0
```diff
-def digitize(n):
+def digitize(n):
+
+    if n <= 9:
+        return n
+    else:
+        n = n % 9
+        if n == 0:
+            return 9
+        else:
+            return n
+
+if __name__ == '__
```

#### solution 1
```diff
-def digitize(n):
+def digitize(n):
+
+    if (n <= 9):
+        return n
+    digit = 1
+    while(n>= 10):
+        n = n/10
+        digit += 1
+    return digit
+
+def get_sum_of
```

#### solution 2
```diff
-def digitize(n):
+def digitize(n):
+
+    digits = []
+    while n > 0:
+        digits.append(n % 10)
+        n = n // 10
+    return digits
+
+# Solution
+
+def persistence(n):
+    s = 0
```

#### solution 3
```diff
-def digitize(n):
+def digitize(n):
+
+    return map(int, str(n))
+
+
+def unfold_list(list_of_list):
+    """
+    >>> from random import randint
+    >>> l = [[randint(1,10) for i
```

#### solution 4
```diff
-def digitize(n):
+def digitize(n):
+
+    n = str(n)
+    n = n[::-1]
+    n = list(n)
+    for i in range(len(n)):
+        n[i] = int(n[i
```

### roll (task/75)

#### canonical solution
```python
def roll(lst, offset):  return lst[-offset:] + lst[:-offset]
```

#### solution 0
```diff
-def roll(lst, offset):
+def roll(lst, offset):
+
+    return lst[offset:] + lst[:offset]
+
+def create_new_deck():
+    return (range(1, 53) + range(1, 53))[::-1]
+
+def deal
```

#### solution 1
```diff
-def roll(lst, offset):
+def roll(lst, offset):
+
+    """Returns a copy of lst rolled forward by offset elements"""
+    return lst[offset:] + lst[:offset]
+
+def eval_at_offset(sess, env, offset):
+    """E
```

#### solution 2
```diff
-def roll(lst, offset):
+def roll(lst, offset):
+
+    return lst[offset:] + lst[:offset]
+
+def rotate(lst, offset):
+    offset = offset % len(lst)
+    rotated = roll(lst, offset)
+    return
```

#### solution 3
```diff
-def roll(lst, offset):
+def roll(lst, offset):
+
+    return lst[offset:] + lst[:offset]
+
+# print(roll([1,2,3,4,5], 2))
+
+def roll_rec(lst, offset):
+    if offset
```

#### solution 4
```diff
-def roll(lst, offset):
+def roll(lst, offset):
+
+    return lst[offset:] + lst[:offset]
+
+#Returns the ID of the given chip
+def id(chip):
+    return chip >> 2
+
+#Returns the floor number of the given chip
+def
```

### some (task/76)

#### canonical solution
```python
def some(lst, fn = lambda x: x):  return any(map(fn, lst))
```

#### solution 0
```diff
-def some(lst, fn = lambda x: x):
+def some(lst, fn = lambda x: x):
+
+    i = 0
+    while i < len(lst):
+        if fn(lst[i]):
+            return True
+        i += 1
+    return False
+
+def every(lst, fn = lambda
```

#### solution 1
```diff
-def some(lst, fn = lambda x: x):
+def some(lst, fn = lambda x: x):
+
+    """
+    Returns a predicate that returns true iff fn(x) is true for some element
+    in lst.
+
+    >>> some([0, False, None, [], (), 42])
+    lambda x: x
```

#### solution 2
```diff
-def some(lst, fn = lambda x: x):
+def some(lst, fn = lambda x: x):
+
+    filtered = filter(fn, lst)
+    return len(filtered) > 0
+
+# map/reduce style
+def any_match(lst, fn = lambda x: x):
+    return some(
```

#### solution 3
```diff
-def some(lst, fn = lambda x: x):
+def some(lst, fn = lambda x: x):
+
+    for x in lst:
+        if fn(x):
+            return x
+    return None
+
+class App:
+    def __init__(self, stdscr):
+        self.wc = Wc
```

#### solution 4
```diff
-def some(lst, fn = lambda x: x):
+def some(lst, fn = lambda x: x):
+
+    return [x for x in lst if fn(x)]
+
+def any(lst, fn = lambda x: x):
+    return len(some(lst, fn)) > 0
+
+def without(l
```

### combine_values (task/77)

#### canonical solution
```python
from collections import defaultdict

def combine_values(*dicts):  res = defaultdict(list)
  for d in dicts:
    for key in d:
      res[key].append(d[key])
  return dict(res)
```

#### solution 0
```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    if len(dicts) == 0:
+        return {}
+    if len(dicts) == 1:
+        return dicts[0]
+    if len(dicts) == 2:
+        return combine_
```

#### solution 1
```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    """
+    Combine values of multiple dictionaries
+    """
+    d = defaultdict(list)
+    for dd in dicts:
+        for k, v in dd.items():
+            d[k].append(
```

#### solution 2
```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    """
+    Combines multiple values into a single dictionary.
+    """
+    return {k: [v] if v is not None else [] for k, v in reduce(lambda x, y: x + y, [
```

#### solution 3
```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    result = defaultdict(list)
+    for dictionary in dicts:
+        for key, value in dictionary.items():
+            result[key].append(value)
+    return result
+
+#dictionaries = [
```

#### solution 4
```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    """Combine the given dictionaries into a single dictionary.
+
+    Each given dictionary will either overwrite or be added to the
+    return dictionary.
+    """
+    ret = {}
+    for d in dicts:
+       
```

### flatten (task/78)

#### canonical solution
```python
def flatten(lst):  return [x for y in lst for x in y]
```

#### solution 0
```diff
-def flatten(lst):
+def flatten(lst):
+
+    for el in lst:
+        if isinstance(el, Iterable) and not isinstance(el, str):
+            yield from flatten(el)
+        else:
+            yield el
+
+def flatten
```

#### solution 1
```diff
-def flatten(lst):
+def flatten(lst):
+
+    return sum(([x] if not isinstance(x, list) else flatten(x) for x in lst), [])
+
+def p_system(p):
+    '''system : SYSTEM WORD
```

#### solution 2
```diff
-def flatten(lst):
+def flatten(lst):
+
+    '''Takes a list of lists and returns a list of the elements'''
+    new_list = []
+    for i in lst:
+        for j in i:
+            new_list.append(j
```

#### solution 3
```diff
-def flatten(lst):
+def flatten(lst):
+
+    """Returns a flattened version of lst.
+
+    >>> flatten([1, 2, 3])     # normal list
+    [1, 2, 3]
+    >>> x = [1, [2, 3], 4
```

#### solution 4
```diff
-def flatten(lst):
+def flatten(lst):
+
+    for x in lst:
+        if isinstance(x, Iterable) and not isinstance(x, str):
+            for y in flatten(x):
+                yield y
+        else:
+            yield x
```

### symmetric_difference_by (task/79)

#### canonical solution
```python
def symmetric_difference_by(a, b, fn):  (_a, _b) = (set(map(fn, a)), set(map(fn, b)))
  return [item for item in a if fn(item) not in _b] + [item
          for item in b if fn(item) not in _a]
```

#### solution 0
```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    pass
+
+def symmetric_difference_with(a, b, fn):
+    pass
+
+def tail(a):
+    pass
+
+def take(a, n):
+    pass
+
+def take_
```

#### solution 1
```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    diff1 = difference_by(a, b, fn)
+    diff2 = difference_by(b, a, fn)
+    return diff1.concat(diff2)
+
+def symmetric_difference
```

#### solution 2
```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    diff1 = difference_by(a, b, fn)
+    diff2 = difference_by(b, a, fn)
+    return concat([diff1, diff2])
+
+def symmetric_difference
```

#### solution 3
```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    """
+    Returns a new set with elements in either the set or
+    the second set but not both.
+    """
+    b = set(map(fn, b))
+    return symmetric_difference(a
```

#### solution 4
```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    return symmetric_difference(a, b).sort_by(fn)
+
+def symmetric_difference_with(a, b, fn):
+    return symmetric_difference(a, b).sort
```

### find_last_index (task/80)

#### canonical solution
```python
def find_last_index(lst, fn):  return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))
```

#### solution 0
```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+
+    """
+    like list.find() but return the index of the last item found
+    """
+    res = None
+    for i, v in enumerate(lst):
+        if fn(v):
+            res
```

#### solution 1
```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+
+    last_index = 0
+    for i, val in enumerate(lst):
+        if fn(val):
+            last_index = i
+    return last_index
+
+
+def find_last_number(l
```

#### solution 2
```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+
+    for idx, val in enumerate(reversed(lst)):
+        if fn(val):
+            return len(lst) - idx - 1
+    return None
+
+
+def get_parser():
```

#### solution 3
```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+
+    last_index = -1
+    result = False
+    while True:
+        try:
+            index = lst.index(fn, last_index + 1)
+        except ValueError:
+            break
+       
```

#### solution 4
```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+
+    reversed_list = lst[::-1]
+    return len(lst) - 1 - reversed_list.index(fn)
+
+
+def find_last(lst, fn):
+    return lst[
```

### weighted_average (task/81)

#### canonical solution
```python
def weighted_average(nums, weights):  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
```

#### solution 0
```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+
+    return (sum(nums * weights) / sum(weights))
+
+def lmap(func, *iterables):
+    return list(map(func, *iterables))
+
+def iterate(func, start
```

#### solution 1
```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+
+    assert len(nums) == len(weights)
+    return sum(num * weight for num, weight in zip(nums, weights)) / sum(weights)
+
+average = weighted_average([1, 2,
```

#### solution 2
```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+
+    assert len(nums) == len(weights)
+    return sum(num * weight for num, weight in zip(nums, weights)) / sum(weights)
+
+def highest_frequency(nums):
+   
```

#### solution 3
```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+
+    return sum(n * w for n, w in zip(nums, weights)) / sum(weights)
+
+def get_error(ans, pred):
+    return sum(abs(a - p) for a,
```

#### solution 4
```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+
+    numerator = sum([nums[i] * weights[i] for i in range(len(nums))])
+    denominator = sum(weights)
+    return numerator / denominator
+
+def get_
```

### bifurcate (task/82)

#### canonical solution
```python
def bifurcate(lst, filter):  return [
    [x for x, flag in zip(lst, filter) if flag],
    [x for x, flag in zip(lst, filter) if not flag]
  ]
```

#### solution 0
```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    return [
+        [x for i, x in enumerate(lst) if filter[i] == True],
+        [x for i, x in enumerate(lst) if filter[i] == False]
```

#### solution 1
```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    return [
+        [x for i, x in enumerate(lst) if filter[i] == True],
+        [x for i, x in enumerate(lst) if filter[i] == False]
```

#### solution 2
```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    """
+    Bifurcate list based on filter
+    :param lst:
+    :param filter:
+    :return:
+    """
+    return [
+        [x for i, x in enumerate
```

#### solution 3
```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    return [
+        [x for i, x in enumerate(lst) if filter[i] == True],
+        [x for i, x in enumerate(lst) if filter[i] == False]
```

#### solution 4
```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    return [
+        [x for i, x in enumerate(lst) if filter[i] == True],
+        [x for i, x in enumerate(lst) if filter[i] == False]
```

### all_equal (task/83)

#### canonical solution
```python
def all_equal(lst):  return len(set(lst)) == 1
```

#### solution 0
```diff
-def all_equal(lst):
+def all_equal(lst):
+
+    return all(elem == lst[0] for elem in lst)
+def get_mask_from_range_list(ranges):
+    """
+    example:
+    ranges: [[0, 1
```

#### solution 1
```diff
-def all_equal(lst):
+def all_equal(lst):
+
+    return not lst or lst.count(lst[0]) == len(lst)
+
+def all_unique(lst):
+    return len(lst) == len(set(lst))
```

#### solution 2
```diff
-def all_equal(lst):
+def all_equal(lst):
+
+    return all(x == lst[0] for x in lst)
+
+# If a singleton is requested, try to return the first value from the iterator,
+# unless the iterator is empty in which case return the
```

#### solution 3
```diff
-def all_equal(lst):
+def all_equal(lst):
+
+    return all(x == lst[0] for x in lst)
+
+def concat_bits(list_of_bit_list):
+    '''
+    concat_bits takes a list of bit lists
```

#### solution 4
```diff
-def all_equal(lst):
+def all_equal(lst):
+
+    return lst[1:] == lst[:-1]
+
+def all_same(lst):
+    return len(set(lst)) == 1
+
+# Refine Data
+
+# Drop rows with missing
```

### difference (task/84)

#### canonical solution
```python
def difference(a, b):  _b = set(b)
  return [item for item in a if item not in _b]
```

#### solution 0
```diff
-def difference(a, b):
+def difference(a, b):
+
+    return [item for item in a if item not in b]
+
+# -- end code --
```

#### solution 1
```diff
-def difference(a, b):
+def difference(a, b):
+
+    return list(set(a) - set(b))
+
+
+@app.route('/')
+def index():
+    return render_template('index.html')
+
+
+@app.route('/', methods=['
```

#### solution 2
```diff
-def difference(a, b):
+def difference(a, b):
+
+    return min(a, b)
+
+
+def get_difference(array):
+    n = len(array)
+    # Initialize result
+    res = 0
+    i = 0
+    while i < n -
```

#### solution 3
```diff
-def difference(a, b):
+def difference(a, b):
+
+    c = []
+    for i in a:
+        if i not in b:
+            c.append(i)
+    return c
+
+print(difference([1,2,3], [1,2,
```

#### solution 4
```diff
-def difference(a, b):
+def difference(a, b):
+
+    return abs(a - b)
+
+# F1-score
+def f1_score(prediction, actual):
+    try:
+        prediction = prediction.astype(int)
+        prediction = np.array
```

### kebab (task/85)

#### canonical solution
```python
from re import sub

def kebab(s):  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
```

#### solution 0
```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    return sub(r"(\s|_|-)+","-",
+               sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\
```

#### solution 1
```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    # your code here
+    return ''.join(x.lower() if i == 0 else ('-' + x.lower() if x.isupper() else x) for i, x in enumerate(sub('[A
```

#### solution 2
```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    s = sub(r"(\s|_|-)+","-",s)
+    s = sub(r"[A-Z]",lambda m: "_" + m.group(0).lower(),s)
```

#### solution 3
```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    return sub(r"(\s|_|-)+","-",sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|
```

#### solution 4
```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    if isinstance(s, basestring):
+        s = sub(r'[^a-zA-Z0-9]+', '-', s)
+        s = sub(r'\-+', '
```

### miles_to_km (task/86)

#### canonical solution
```python
def miles_to_km(miles):  return miles * 1.609344
```

#### solution 0
```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+
+    km = 1.6 * miles
+    return km
+
+miles = 10
+km = miles_to_km(miles)
+print(miles, 'miles equals', km, 'km')
+
+m
```

#### solution 1
```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+
+    km = miles * 1.60934
+    return km
+
+def km_to_miles(km):
+    miles = km / 1.60934
+    return miles
```

#### solution 2
```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+
+    return miles * 1.609
+
+print(miles_to_km(10))
+
+print(miles_to_km(0))
+
+print(miles_to_km(13))
+
+print
```

#### solution 3
```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+
+    km = miles * 1.60934
+    return km
+
+print(miles_to_km(12))
+
+#OUTPUT:
+#18.619788802909413
```

#### solution 4
```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+
+    km = 1.6 * miles
+    return km
+
+# km to miles function
+def km_to_miles(km):
+    miles = km / 1.6
+    return miles
+
+# convert function
```

### sum_of_powers (task/87)

#### canonical solution
```python
def sum_of_powers(end, power = 2, start = 1):  return sum([(i) ** power for i in range(start, end + 1)])
```

#### solution 0
```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+
+    """
+    This function takes an end and start value and returns the sum of
+    powers of 'power' that are between start and end.
+
+    sum_of_powers(end, power, start)
+
+    end:
```

#### solution 1
```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+
+    '''
+    This function sums all numbers between start and end that
+    are some power of two. For example, if start is 1 and end is 8,
+    the function should return 14, because the powers of two between
```

#### solution 2
```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+
+    return sum(map(lambda x: x**power, range(start, end+1)))
+
+# no need to actually go over all numbers for this, but the option to go over the entire set is there
+# limit
```

#### solution 3
```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+
+    """Return the sum of all numbers less than end which are a power of start
+    """
+    return sum(i for i in range(start, end) if i**power == start)
+
+
+def sum_of_
```

#### solution 4
```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+
+    if (start <= end):
+        if (start == end):
+            return start ** power
+        else:
+            return start ** power + sum_of_powers(end, power, start + 1)
+    else
```

### compose (task/88)

#### canonical solution
```python
from functools import reduce

def compose(*fns):  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
```

#### solution 0
```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    def inner(arg):
+        return reduce(lambda acc, f: f(acc), reversed(fns), arg)
+    return inner
+
+import numpy as np
+
+def load_image(fp):
+   
```

#### solution 1
```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    if len(fns) == 0:
+        return lambda x: x
+    elif len(fns) == 1:
+        return fns[0]
+    else:
+        return reduce(lambda f,
```

#### solution 2
```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    if len(fns) == 0:
+        return lambda x: x
+    elif len(fns) == 1:
+        return fns[0]
+    else:
+        return reduce(lambda f,
```

#### solution 3
```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    return reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)
+
+from functools import partial
+
+def add1(x):
+    return x + 1
```

#### solution 4
```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    if len(fns) == 0:
+        return lambda x: x
+    elif len(fns) == 1:
+        return fns[0]
+    else:
+        return reduce(lambda f,
```

### similarity (task/89)

#### canonical solution
```python
def similarity(a, b):  return [item for item in a if item in b]
```

#### solution 0
```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    return dot(a, b) / (norm(a) * norm(b))
+
+# X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1],
```

#### solution 1
```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    return SequenceMatcher(None, a, b).ratio()
+
+if __name__ == '__main__':
+    main()
```

#### solution 2
```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    return len(a & b) / len(a | b)
+
+assert similarity({'x', 'y', 'z'}, {'w', 'x', 'y', 'z'}) == 1.0
```

#### solution 3
```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    return SequenceMatcher(None, a, b).ratio()
+
+# Download image and show contour
+def download_image(url):
+    req = requests.get(url, stream=True)
+    filename
```

#### solution 4
```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
+
+def similarity_cosine(a, b):
+    return np
```

### have_same_contents (task/90)

#### canonical solution
```python
def have_same_contents(a, b):  for v in set(a + b):
    if a.count(v) != b.count(v):
      return False
  return True
```

#### solution 0
```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    """
+    Check that two files have the same contents
+    """
+    return open(a, "rb").read() == open(b, "rb").read()
+
+
+def random_bytes(size):
+    """
```

#### solution 1
```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    """
+    Return True if two files have the same contents.
+    """
+    try:
+        with open(a, 'rb') as f:
+            contents_a = f.read()
+    except FileNot
```

#### solution 2
```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    return a == b
+
+def make_immutable(value):
+    if isinstance(value, list):
+        return tuple(make_immutable(item) for item in value)
+    else:
+        return
```

#### solution 3
```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    """Returns true if two files have the same contents."""
+    try:
+        return filecmp.cmp(a, b, shallow=False)
+    except OSError:
+        return False
+
+
+def _
```

#### solution 4
```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    return open(a, 'rb').read() == open(b, 'rb').read()
+
+def is_iterable(x):
+    try:
+        iter(x)
+        return True
+    except Type
```

### days_from_now (task/91)

#### canonical solution
```python
from datetime import timedelta, date

def days_from_now(n):  return date.today() + timedelta(n)
```

#### solution 0
```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    d = date.today() + timedelta(days=n)
+    return d.strftime("%Y-%m-%d")
```

#### solution 1
```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    return date.today() + timedelta(days=n)
```

#### solution 2
```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    return date.today() + timedelta(days=n)
```

#### solution 3
```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    return date.today() + timedelta(days=n)
+
+# In case you need dates that fall on a particular weekday in the next n days, replace the timedelta with a TimeDelta that uses one of the constants in
```

#### solution 4
```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    d = date.today() + timedelta(days=n)
+    return d.strftime("%Y-%m-%d")
+
+def days_ago(n):
+    d = date.today()
```

### cast_list (task/92)

#### canonical solution
```python
def cast_list(val):  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
```

#### solution 0
```diff
-def cast_list(val):
+def cast_list(val):
+
+    if isinstance(val, list):
+        return val
+    return [val]
+
+
+def _open_for_csv(path):
+    """
+    Open a file with flags suitable for csv.reader.
+
```

#### solution 1
```diff
-def cast_list(val):
+def cast_list(val):
+
+    return val if isinstance(val, list) else [val]
+
+
+def _check_files(files):
+    success = True
+    for filename in files:
+        if not path.exists(filename):
```

#### solution 2
```diff
-def cast_list(val):
+def cast_list(val):
+
+    if ',' in val:
+        val = val.split(',')
+    else:
+        val = [val]
+    return val
+
+
+def cast_bool(val):
+    if isinstance(val,
```

#### solution 3
```diff
-def cast_list(val):
+def cast_list(val):
+
+    if not val:
+        return None
+    else:
+        return [val]
+
+
+def _convert_str(val):
+    if val is None:
+        return None
+    return str(val)
+
```

#### solution 4
```diff
-def cast_list(val):
+def cast_list(val):
+
+    return [v.strip() for v in val.split(',')]
+
+def gen_secret(length=32):
+    secret = ''
+    for _ in range(length):
+        secret += choice(SEC
```

### sort_dict_by_value (task/93)

#### canonical solution
```python
def sort_dict_by_value(d, reverse = False):  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
```

#### solution 0
```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+
+    """Return list of key-value pairs in d, sorted by values"""
+    kv_list = d.items()
+    sort_kv_list = sorted(kv_list, key = lambda kv:
```

#### solution 1
```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+
+    sorted_keys = sorted(d, key = d.get, reverse = reverse)
+    return sorted_keys
+
+def sort_dict_by_value_as_string(d, reverse = False):
+    sorted
```

#### solution 2
```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+
+    return sorted(d.items(), key = lambda x: x[1], reverse = reverse)
+
+def sort_dict_by_key(d, reverse = False):
+    return sorted(d.items(), key =
```

#### solution 3
```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+
+    """
+    Sort a dict by value.
+    """
+    return sorted(d.items(), key = operator.itemgetter(1), reverse = reverse)
+
+def sort_dict_by_key(d,
```

#### solution 4
```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+
+    '''
+    Sorts a dictionary by value
+    '''
+    sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse = reverse)
+    return sorted_d
+
```

### slugify (task/94)

#### canonical solution
```python
import re

def slugify(s):  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s
```

#### solution 0
```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    return re.sub('[^a-zA-Z0-9]+', '-', s)
+
+def add_link(doc, rel, url, title=None, mimetype=None):
+   
```

#### solution 1
```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    s = s.lower()
+    for c in [' ', '-', '.', '/']:
+        s = s.replace(c, '_')
+    s = re.sub('\W', '',
```

#### solution 2
```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    """Generates an ASCII-only slug."""
+    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
+    s =
```

#### solution 3
```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    return re.sub('[^a-zA-Z0-9_\-]+', '-', s)
+
+def safe_string(s):
+    return s.replace('"', '\\"')
```

#### solution 4
```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    s = re.sub('[^a-zA-Z0-9_\.]', '', s)
+    s = re.sub(' ', '_', s)
+    return s
+
+def find_
```

### to_roman_numeral (task/95)

#### canonical solution
```python
def to_roman_numeral(num):  lookup = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
  ]
  res = ''
  for (n, roman) in lookup:
    (d, num) = divmod(num, n)
    res += roman * d
  return res
```

#### solution 0
```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+
+    """
+    Converts integer to Roman numeral.
+    :param num: integer
+    :return: Roman numeral string
+    """
+    ints = (1000, 900, 500, 400, 100, 90,
```

#### solution 1
```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+
+    numerals = {
+        1000: 'M',
+        900: 'CM',
+        500: 'D',
+        400: 'CD',
+        100: 'C',
+        90: 'XC',
```

#### solution 2
```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+
+    arabic_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
+    roman_list = ["M", "CM", "D
```

#### solution 3
```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+
+    '''Returns the Roman numeral version of an integer'''
+    if num <= 0 or num >= 4000:
+        raise OutOfRangeError('number out of range (must be less than 4000)')
+    if not
```

#### solution 4
```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+
+    """
+    Convert an integer to a Roman numeral.
+    """
+    roman_numeral = ""
+    for (arabic, roman) in MAPPING:
+        (factor, num) =
```

### check_prop (task/96)

#### canonical solution
```python
def check_prop(fn, prop):  return lambda obj: fn(obj[prop])
```

#### solution 0
```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+
+    def f(self, *args, **kwargs):
+        if prop not in self.__dict__:
+            raise ValueError('%s is not defined on %s' % (prop, self.__class__
```

#### solution 1
```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+
+    if prop is None:
+        return True
+    if not fn in prop:
+        return False
+    return True
+
+def check_labels(fn, labels):
+    if labels is None:
+        return True
```

#### solution 2
```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+
+    if fn.endswith('.dts'):
+        expr = prop.tokens[1].value
+        val = prop.tokens[3].value
+        if val.startswith('0
```

#### solution 3
```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+
+    """Return the value of a property for the given function
+    """
+    for p in fn.props:
+        if p.prop == prop:
+            return p.value
+    return None
+
+
+def check_
```

#### solution 4
```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+
+    for i in range(0, 10):
+        r = random.randint(0, 1024)
+        fn(r)
+        assert r in prop
+
+def test_set_prop():
+    prop = set
```

### count_occurrences (task/97)

#### canonical solution
```python
def count_occurrences(lst, val):  return lst.count(val)
```

#### solution 0
```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+
+    """ (list, object) -> int
+
+    Return the number of times val occurs in lst.
+
+    >>> count_occurrences([2, 3, 3, 3, 2], 2)
+    2
+    >>>
```

#### solution 1
```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+
+    count = 0
+    for item in lst:
+        if item == val:
+            count += 1
+    return count
+
+def max_occurrences(lst):
+    counts = []
+    for item
```

#### solution 2
```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+
+    ''' (list, object) -> int
+
+    Return the number of times val occurs in lst.
+
+    >>> count_occurrences([2, 3, 3, 3, 2, 4, 2], 2)
```

#### solution 3
```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+
+    if lst is None:
+        return 0
+    return count_occurrences_rec(lst, val)
+
+def count_occurrences_rec(lst, val):
+    if lst is
```

#### solution 4
```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+
+    # Your code here
+    return lst.count(val)
+
+# Should be 3
+print(count_occurrences([True, False, True, True], True))
+
+# Should be 1
+print(
```

### find_parity_outliers (task/98)

#### canonical solution
```python
from collections import Counter

def find_parity_outliers(nums):  return [
    x for x in nums
    if x % 2 != Counter([n % 2 for n in nums]).most_common()[0][0]
  ]
```

#### solution 0
```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    counts = Counter(nums)
+    return [x for x in counts if counts[x] % 2 == 1]
+
+def find_parity_outliers_sets(nums):
+    parity = {
```

#### solution 1
```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    """Given list of ints, return list of values at odd indices"""
+    out = []
+    for i in range(len(nums)):
+        if i % 2 == 1:
+            out.append(
```

#### solution 2
```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    # first find the mode
+    # if mode is even, return all elements that are odd
+    # if mode is odd, return all elements that are even
+    c = Counter(nums)
+    mode = c.
```

#### solution 3
```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    c = Counter(nums)
+    return [k for k, v in c.items() if v % 2 != 0]
```

#### solution 4
```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    parity = [i % 2 for i in nums]
+    return [nums[i] for i in range(len(nums)) if parity[i] != parity[0]]
+
+def find_outl
```

### to_dictionary (task/99)

#### canonical solution
```python
def to_dictionary(keys, values):  return dict(zip(keys, values))
```

#### solution 0
```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+
+    """
+    :param keys: a list of strings
+    :param values: a list of ints
+    :return: dictionary with keys and values
+    """
+    dictionary = {}
+    for i in range(len
```

#### solution 1
```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+
+    """
+    Return a dictionary of keys and values
+
+    Args:
+        keys (list): keys to be returned in dictionary
+        values (list): values to be returned in dictionary
+
+    Returns:
+        dict: dictionary
```

#### solution 2
```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+
+    """
+    takes a list of keys and a list of values, and makes a dictionary out of them
+    :param keys: list of keys
+    :param values: list of values
+    :return: dictionary
+    """
```

#### solution 3
```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+
+    """
+    Given a list of keys and a list of values, make a dictionary matching these keys to these values.
+
+    >>> to_dictionary(['one', 'two', 'three'], [1, 2, 3
```

#### solution 4
```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+
+    return dict(zip(keys, values))
+
+
+def main():
+    keys = ['name', 'age', 'height']
+    values = ['John', '24', '5.5']
+    print(to_
```

### geometric_progression (task/100)

#### canonical solution
```python
from math import floor, log

def geometric_progression(end, start=1, step=2):  return [start * step ** i for i in range(floor(log(end / start)
          / log(step)) + 1)]
```

#### solution 0
```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    return [start * step ** k for k in range(0, floor(log(end, step)) + 1)]
```

#### solution 1
```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    n = floor(log(end + 1 - start, step))
+    return int(step ** n) - 1
+
+def solution(m):
+    # Your code here
+    return geometric_progression(m)
```

#### solution 2
```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    # return a geometric progression with the specified starting value and step
+    return [start * (step ** n) for n in range(0, floor(log(end, step)) + 1)]
```

#### solution 3
```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    i = start
+    while i < end:
+        yield i
+        i *= step
+
+def is_prime(n):
+    if n == 2:
+        return True
+    elif n < 2 or
```

#### solution 4
```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    if not isinstance(end, int):
+        raise ValueError('Geometric Progression must end with an integer.')
+    return int(floor(log(end) / log(step))) + 1
+
+def triangular
```

### find_last (task/101)

#### canonical solution
```python
def find_last(lst, fn):  return next(x for x in lst[::-1] if fn(x))
```

#### solution 0
```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    return next(iter(reversed(list(filter(fn, lst)))))
+
+def find_first(lst, fn):
+    return next(iter(list(filter(fn, lst))))
```

#### solution 1
```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    """Find the last item in a list that satisfies a predicate.
+
+    Returns the item and the next index in the list where the item occurs.
+
+    """
+    idx = len(lst) - 1
+    while
```

#### solution 2
```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    return next(reversed(filter(fn, reversed(lst))))
+
+
+def find_last_index(lst, fn):
+    return len(lst) - 1 - next(i for i, e
```

#### solution 3
```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    last = None
+    for val in lst:
+        if fn(val):
+            last = val
+    return last
+
+
+def find_first(lst, fn):
+    first = None
+    for val
```

#### solution 4
```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    for x in reversed(lst):
+        if fn(x):
+            return x
+    return None
+
+def prepend_line(filepath, line):
+    """Rewrite a file adding a line to its
```

### sort_dict_by_key (task/102)

#### canonical solution
```python
def sort_dict_by_key(d, reverse = False):  return dict(sorted(d.items(), reverse = reverse))
```

#### solution 0
```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    sorted_keys = sorted(d.keys(), reverse = reverse)
+    return [(key, d[key]) for key in sorted_keys]
+
+
+def sort_dict_by_value(d, reverse = False):
```

#### solution 1
```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    return sorted(d.items(), key=operator.itemgetter(0), reverse = reverse)
+
+def sort_dict_by_value(d, reverse = False):
+    return sorted(d.items(), key
```

#### solution 2
```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    """
+    Given a dictionary, return sorted (key, value) list.
+    """
+    sorted_tuple = sorted(d.items(), key = lambda x: x[0], reverse = reverse)
+    return
```

#### solution 3
```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    return sorted(d.items(), key=lambda x: x[0], reverse=reverse)
+
+def sort_dict_by_value(d, reverse = False):
+    return sorted(d.items(), key=
```

#### solution 4
```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    return sorted(d.items(), key=lambda item: item[0], reverse=reverse)
+
+def sort_dict_by_value(d, reverse = False):
+    return sorted(d.items(), key=
```

### split_lines (task/103)

#### canonical solution
```python
def split_lines(s):  return s.split('\n')
```

#### solution 0
```diff
-def split_lines(s):
+def split_lines(s):
+
+    """
+    split s in lines, dealing correctly with parentheses
+    """
+    result = []
+    parens = 0
+    start = 0
+    for i, c in enumerate(s):
+        if c
```

#### solution 1
```diff
-def split_lines(s):
+def split_lines(s):
+
+    """Split lines in a multiline string.
+
+    This is the counter part of join_lines.
+    """
+    return [line for line in s.splitlines() if line]
+
+
+def remove_whites
```

#### solution 2
```diff
-def split_lines(s):
+def split_lines(s):
+
+    s = s.strip()
+    lines = []
+    while len(s) > 0:
+        found = False
+        for i in range(1, len(s)):
+            if s[i] ==
```

#### solution 3
```diff
-def split_lines(s):
+def split_lines(s):
+
+    return re.split(r'[\r\n]+', s)
+
+
+class HelpFormatter(object):
+    """Formatter for generating usage messages and argument help strings.
+
+    Only the name of this class is
```

#### solution 4
```diff
-def split_lines(s):
+def split_lines(s):
+
+    """Split a block of text into lines.
+
+    This method is smart about trimming whitespace from the right hand side of
+    each line.  It is also smart about retaining the newline characters on a
+    line that
```

### includes_any (task/104)

#### canonical solution
```python
def includes_any(lst, values):  for v in values:
    if v in lst:
      return True
  return False
```

#### solution 0
```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+
+    for value in values:
+        if value in lst:
+            return True
+    return False
+
+
+def get_cols(field_names, include_serial=True):
+    cols = ['"%s
```

#### solution 1
```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+
+    for v in values:
+        if v in lst:
+            return True
+    return False
+
+
+class DjangoUtilsTest(TestCase):
+    def test_read_file(self):
+        self.assert
```

#### solution 2
```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+
+    """Returns true if any value in lst is in values.
+
+    :param lst: list of values
+    :param values: list of values
+    :returns: True if any value in lst is in values
```

#### solution 3
```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+
+    for value in values:
+        if value in lst:
+            return True
+    return False
+
+
+def includes_all(lst, values):
+    for value in values:
+        if value not in lst
```

#### solution 4
```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+
+    for value in values:
+        if value in lst:
+            return True
+    return False
+
+
+@user_passes_test(lambda u: u.is_superuser)
+def index(request):
```

### merge (task/105)

#### canonical solution
```python
def merge(*args, fill_value = None):  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

#### solution 0
```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+
+    new_data = {}
+    for data in args:
+        for key, value in data.items():
+            if key in new_data:
+                new_data[key].append(value)
+            else:
```

#### solution 1
```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+
+    lengths = [len(i) for i in args]
+    min_length = min(lengths)
+    max_length = max(lengths)
+    if min_length != max_length:
+        raise
```

#### solution 2
```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+
+    """
+    Merge together values that were separated by a groupby operation
+
+    .. versionadded:: 0.16.1
+
+    Parameters
+    ----------
+    *args : DataFrames
+        DataFrames that you want to merge
```

#### solution 3
```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+
+    """
+    Merge dataframes column-wise. 
+    Uses union of all indices in order to merge.
+    """
+    args = list(args)
+    base = args.pop(0)
+    for df
```

#### solution 4
```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+
+    if len(args) == 1:
+        return args[0]
+    if len(args) == 2:
+        a, b = args
+        if a is None:
+            return b
+        if b is
```

### min_by (task/106)

#### canonical solution
```python
def min_by(lst, fn):  return min(map(fn, lst))
```

#### solution 0
```diff
-def min_by(lst, fn):
+def min_by(lst, fn):
+
+    return reduce(lambda x, y: x if fn(x) < fn(y) else y, lst)
+
+def max_by(lst, fn):
+    return reduce(lambda x, y: x
```

#### solution 1
```diff
-def min_by(lst, fn):
+def min_by(lst, fn):
+
+    if not lst:
+        return None
+    fn = maybe_unary(fn)
+    return reduce(lambda a, b: a if fn(a) < fn(b) else b, lst)
+
```

#### solution 2
```diff
-def min_by(lst, fn):
+def min_by(lst, fn):
+
+    return min(lst, key=fn)
+
+def min_index_by(lst, fn):
+    return min(range(len(lst)), key=lambda i: fn(lst[i]
```

#### solution 3
```diff
-def min_by(lst, fn):
+def min_by(lst, fn):
+
+    min_fn = None
+    min_val = None
+    for e in lst:
+        v = fn(e)
+        if min_val is None or v < min_val:
+            min_val
```

#### solution 4
```diff
-def min_by(lst, fn):
+def min_by(lst, fn):
+
+    """
+    Returns the element in the list that gives the minimum value when passed to the function.
+    """
+    return min(lst, key=fn)
+
+
+def inverse_signal(signal):
+   
```

### add_days (task/107)

#### canonical solution
```python
from datetime import datetime, timedelta

def add_days(n, d = datetime.today()):  return d + timedelta(n)
```

#### solution 0
```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    return d + timedelta(days = n)
+
+def add_years(n, d = datetime.today()):
+    return d + timedelta(days = n * 365)
+
+def add_hours(
```

#### solution 1
```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    return d + timedelta(days = n)
+
+def format_date(d):
+    return d.strftime('%m/%d/%Y')
+
+def format_date_time(d):
```

#### solution 2
```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    return d + timedelta(days = n)
+
+def list_to_dict(li):
+    return { i : li[i] for i in range(len(li)) }
+
+def get_input():
```

#### solution 3
```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    return d + timedelta(days = n)
+
+def sub_days(n, d = datetime.today()):
+    return d - timedelta(days = n)
+
+def string_to_datetime
```

#### solution 4
```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    delta = timedelta(days = n)
+    d += delta
+    return d
+
+def find_nth(haystack, needle, n):
+    start = haystack.find(needle)
+   
```

### palindrome (task/108)

#### canonical solution
```python
from re import sub

def palindrome(s):  s = sub('[\W_]', '', s.lower())
  return s == s[::-1]
```

#### solution 0
```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+    s = sub('[^A-Za-z]', '', s).lower()
+    return s == s[::-1]
+
+"""
+import re
+
+def palindrome(s):
+   
```

#### solution 1
```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+	s = sub(r'[^A-Za-z]', '', s).lower()
+	return s == s[::-1]
+
+print(palindrome("Dammit, I'm mad!"
```

#### solution 2
```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+    s = sub('[^A-Za-z]', '', s).lower()
+    return s == s[::-1]
+
+if __name__ == '__main__':
+    s = input
```

#### solution 3
```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+    s = sub('[^A-Za-z]', '', s).lower()
+    return s == s[::-1]
+
+print(palindrome("Test 5:1, a s!nt
```

#### solution 4
```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+    s = sub('[^A-Za-z]', '', s.lower())
+    return s == s[::-1]
+
+print(palindrome("A man, a plan, a canal:
```

### none (task/109)

#### canonical solution
```python
def none(lst, fn = lambda x: x):  return all(not fn(x) for x in lst)
```

#### solution 0
```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+
+    for i in lst:
+        if fn(i):
+            return False
+    return True
+
+def find_optimal_move(board, player):
+    t_start = time.time()
+    moves
```

#### solution 1
```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+
+    """
+    Passes over an iterator exactly once.
+
+    This is a more efficient version of [fn(x) for x in lst].
+
+    :param lst: The list to pass over.
+    :param
```

#### solution 2
```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+
+    return [fn(x) for x in lst if x != None]
+
+def one(lst, fn = lambda x: x):
+    return [fn(x) for x in lst if x == 1
```

#### solution 3
```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+
+    return [fn(x) for x in lst if x is not None]
+
+def all_none(lst):
+    return not any(lst)
+
+def all_not_none(lst):
```

#### solution 4
```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+
+    for x in lst:
+        if fn(x):
+            return False
+    return True
+
+def one(lst, fn = lambda x: x):
+    cnt = 0
+    for x in l
```

### tail (task/110)

#### canonical solution
```python
def tail(lst):  return lst[1:] if len(lst) > 1 else lst
```

#### solution 0
```diff
-def tail(lst):
+def tail(lst):
+
+    return lst[1:]
+
+# Some tests.
+from doctest import run_docstring_examples as dtest
+dtest(tail, globals(), verbose=True)
+
+# The implementation of **
```

#### solution 1
```diff
-def tail(lst):
+def tail(lst):
+
+    return lst[1:]
+
+def nth(lst, n):
+    return lst[n]
+
+def init(lst):
+    return lst[:-1]
+
+def last(l
```

#### solution 2
```diff
-def tail(lst):
+def tail(lst):
+
+    return lst[1:]
+
+def last(lst):
+    return lst[-1]
+
+def init(lst):
+    return lst[:-1]
+
+def reverse(lst):
```

#### solution 3
```diff
-def tail(lst):
+def tail(lst):
+
+    return lst[1:]
+
+def last(lst):
+    return lst[-1]
+
+def first(lst):
+    return lst[0]
+
+def drop(lst, n
```

#### solution 4
```diff
-def tail(lst):
+def tail(lst):
+
+    return lst[1:]
+
+def last(lst):
+    return lst[-1]
+
+def init(lst):
+    return lst[:-1]
+
+def reverse(lst):
```

### has_duplicates (task/111)

#### canonical solution
```python
def has_duplicates(lst):  return len(lst) != len(set(lst))
```

#### solution 0
```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+
+    return len(lst) != len(set(lst))
+
+def has_duplicates2(lst):
+    seen = []
+    for i in lst:
+        if i in seen:
```

#### solution 1
```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+
+    """Returns True if there is any element that appears more than once.
+
+    >>> has_duplicates([1, 2, 3, 4, 5])
+    False
+    >>> has_duplicates([1, 2
```

#### solution 2
```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+
+    for i in range(len(lst)):
+        for j in range(i+1, len(lst)):
+            if lst[i] == lst[j]:
+                return True
+   
```

#### solution 3
```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+
+    """ Return True if lst has any duplicates, False if it does not.
+    """
+    # replace the pass below with your code
+    dup_lst = []
+    for i in lst:
+       
```

#### solution 4
```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+
+    ''' (list) -> bool
+    Return True iff the items in lst are not unique
+    '''
+    # make a copy of lst and sort it
+    sorted_list = lst[:]
```

### map_dictionary (task/112)

#### canonical solution
```python
def map_dictionary(itr, fn):  return dict(zip(itr, map(fn, itr)))
```

#### solution 0
```diff
-def map_dictionary(itr, fn):
+def map_dictionary(itr, fn):
+
+    return {fn(x): x for x in itr}
+
+
+def map_to_array(itr, fn):
+    return np.array([fn(x) for x in itr])
+
+
+def to
```

#### solution 1
```diff
-def map_dictionary(itr, fn):
+def map_dictionary(itr, fn):
+
+    return dict(map(lambda item: (item[0], fn(item[1])), itr))
+
+
+class RunResult(object):
+    def __init__(self, result_dict, retval, duration
```

#### solution 2
```diff
-def map_dictionary(itr, fn):
+def map_dictionary(itr, fn):
+
+    """
+    Maps a dictionary of iterables by applying a function to each element
+    of the iterable and collecting the results in a dictionary.
+
+    This is what you would usually use on a dictionary comprehension.
+
+    :param
```

#### solution 3
```diff
-def map_dictionary(itr, fn):
+def map_dictionary(itr, fn):
+
+    d = {}
+    for k, v in itr:
+        d[k] = fn(v)
+    return d
+
+def zip_dictionary(dict_a, dict_b):
+    d =
```

#### solution 4
```diff
-def map_dictionary(itr, fn):
+def map_dictionary(itr, fn):
+
+    return {key: fn(value) for key, value in itr}
+
+
+def _mock_model_list(count=1):
+    for x in range(count):
+        yield _mock_model
```

### count_by (task/113)

#### canonical solution
```python
from collections import defaultdict

def count_by(lst, fn = lambda x: x):  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)
```

#### solution 0
```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+    counter = defaultdict(int)
+    for item in lst:
+        counter[fn(item)] += 1
+    return counter
+
+# Recursion
+
+# Introduction
+
+# Recursion happens when a function calls
```

#### solution 1
```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+    counts = defaultdict(int)
+    for item in lst:
+        counts[fn(item)] += 1
+    return counts
+
+count_by([1,2,3,4,5], lambda x:
```

#### solution 2
```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+	counts = defaultdict(int)
+	for v in lst:
+		counts[fn(v)] += 1
+	return counts
+
+def count_list(lst, fn = lambda x: x
```

#### solution 3
```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+    out = defaultdict(int)
+    for x in lst:
+        out[fn(x)] += 1
+    return out
+
+def set_by(lst, fn = lambda x: x):
+   
```

#### solution 4
```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+    d = defaultdict(int)
+    for item in lst:
+        key = fn(item)
+        d[key] += 1
+    return d
+
+def create_fn(name, args, body):
```

### difference_by (task/114)

#### canonical solution
```python
def difference_by(a, b, fn):  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]
```

#### solution 0
```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+
+    b = set(map(fn, b))
+    return [item for item in a if fn(item) not in b]
+
+
+print(difference_by([2.1, 1.2], [2.
```

#### solution 1
```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+
+    b = set(map(fn, b))
+    return [item for item in a if fn(item) not in b]
+
+assert difference_by([2.1, 1.2], [2.3,
```

#### solution 2
```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+
+    b = set(map(fn, b))
+    return [item for item in a if fn(item) not in b]
+
+
+# The difference_of_squares function returns the difference between the square of the sum
```

#### solution 3
```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+
+    """
+    a - b, after applying fn to keys of b
+    """
+    b = {fn(k): v for (k, v) in b.items()}
+    return {k: a[k
```

#### solution 4
```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+
+    """Returns the difference of both lists (A - B)"""
+    return [item for item in a if fn(item) not in map(fn, b)]
+
+
+def difference(a, b):
+    """Returns
```

### from_iso_date (task/115)

#### canonical solution
```python
from datetime import datetime

def from_iso_date(d):  return datetime.fromisoformat(d)
```

#### solution 0
```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    return datetime.strptime(d, "%Y-%m-%d")
+
+def to_iso_date(d):
+    return d.strftime("%Y-%m-%d")
```

#### solution 1
```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    return datetime.strptime(d, "%Y-%m-%d")
+
+def from_iso_time(t):
+    return datetime.strptime(t, "%H:%M:
```

#### solution 2
```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    return datetime.strptime(d, "%Y-%m-%d")
+
+def to_iso_date(d):
+    return d.strftime("%Y-%m-%d")
```

#### solution 3
```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    """Convert an ISO-8601 date string to a datetime object.
+    """
+    return datetime.strptime(d, "%Y-%m-%d")
```

#### solution 4
```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    return datetime.strptime(d, "%Y-%m-%d")
```

### filter_non_unique (task/116)

#### canonical solution
```python
from collections import Counter

def filter_non_unique(lst):  return [item for item, count in Counter(lst).items() if count == 1]
```

#### solution 0
```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    counts = Counter(lst)
+    return [x for x in lst if counts[x] == 1]
+
+def main():
+    lst = [3,3,3,2,2,2,
```

#### solution 1
```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    c = Counter(lst)
+    return [x for x in lst if c[x] == 1]
+
+"""
+Given a list of integers, find the highest product you can get from three of the integers.
```

#### solution 2
```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    return list(set(lst))
+
+def collect_data(lst):
+    counter = Counter(lst)
+    out = []
+    for key,value in counter.items():
+        out.append
```

#### solution 3
```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    """ Function that removes duplicate elements from a list.
+    Args:
+        lst: The list that we want to filter.
+    Returns:
+        A new list with only unique elements.
+    """
+    return
```

#### solution 4
```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    duplicates = []
+    for item in lst:
+        if lst.count(item) > 1:
+            duplicates.append(item)
+    return duplicates
+
+def count_unique(lst
```

### symmetric_difference (task/117)

#### canonical solution
```python
def symmetric_difference(a, b):  (_a, _b) = (set(a), set(b))
  return [item for item in a if item not in _b] + [item for item in b
          if item not in _a]
```

#### solution 0
```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+
+    """The difference between the two iterables a and b, making sure that no
+    duplicates are returned. This is the set version of the binary XOR operator.
+    """
+    if not isinstance(b, Iter
```

#### solution 1
```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+
+    return a ^ b
+
+def symmetric_difference_update(a, b):
+    a ^= b
+
+def union(a, b):
+    return a | b
+
+def update(a, b
```

#### solution 2
```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+
+    return a ^ b
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
+    
```

#### solution 3
```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+
+    '''(set, set) -> set
+    Return a new set that contains all the elements that are in exactly
+    one of the sets a and b.
+    '''
+    # Make an empty set.
+   
```

#### solution 4
```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+
+    return a ^ b
+
+
+def _get_bin(op):
+    if isinstance(op, str):
+        op = op.encode()
+    return base64.b16decode(op)
+
+
```

### snake (task/118)

#### canonical solution
```python
from re import sub

def snake(s):  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()
```

#### solution 0
```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    return sub(r'(.)([A-Z][a-z]+)', r'\1_\2', s).lower()
+
+def camel(s):
+    return sub(r'(?:^|
```

#### solution 1
```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    return sub(r'(.)([A-Z][a-z]+)', r'\1_\2', s).lower()
+
+def lcamel(s):
+    return sub(r'(.)
```

#### solution 2
```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    return sub(r'([A-Z])', r'_\1', s).lower()
+
+def pascal(s):
+    return sub(r'_([a-z])', lambda m: m.
```

#### solution 3
```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    return sub(r'([A-Z])', r'_\1', s).lower()
+
+def get_key(dictionary, val):
+    """return the key of dictionary given the value"""
+    return
```

#### solution 4
```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    return sub(r'[A-Z][a-z]*',
+               lambda mo: mo.group(0).lower(),
+               s)
+
+if __name__ == '__main__':
+    print
```

### keys_only (task/119)

#### canonical solution
```python
def keys_only(flat_dict):  return list(flat_dict.keys())
```

#### solution 0
```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+
+    return flat_dict.keys()
+
+
+@field_filter_fn
+def get_names(flat_dict):
+    return [flat_dict[k].name for k in flat_dict]
+
+
+@field_
```

#### solution 1
```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+
+    """Returns only the keys of a flat dictionary.
+
+    Args:
+        flat_dict (dict): the flat dictionary to get the keys of.
+
+    Returns:
+        list: the keys of the dictionary.
+   
```

#### solution 2
```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+
+    if not isinstance(flat_dict, dict):
+        return flat_dict
+    else:
+        return flat_dict.keys()
+
+def values_only(flat_dict):
+    if not isinstance(
```

#### solution 3
```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+
+    """
+    Returns a tuple of all the keys of the dictionary
+    :param flat_dict: dictionary
+    :return: Tuple of all the keys of the dictionary
+    """
+    if not isinstance(flat_
```

#### solution 4
```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+
+    for key, val in flat_dict.items():
+        if isinstance(val, dict):
+            keys_only(val)
+        else:
+            flat_dict[key] = key
+    return flat_
```

### is_odd (task/120)

#### canonical solution
```python
def is_odd(num):  return num % 2 != 0
```

#### solution 0
```diff
-def is_odd(num):
+def is_odd(num):
+
+    if num % 2 == 0:
+        return False
+    else:
+        return True
+
+def fib_num(n):
+    if n == 0:
+        return 0
+    elif n == 1:
```

#### solution 1
```diff
-def is_odd(num):
+def is_odd(num):
+
+    return num % 2 == 1
+
+def is_even(num):
+    return num % 2 == 0
+
+def is_prime(num):
+    for divisor in range(2, int(math.sq
```

#### solution 2
```diff
-def is_odd(num):
+def is_odd(num):
+
+    if num % 2 == 0:
+        return False
+    else:
+        return True
+
+def remove_odd(lst):
+    lst1 = []
+    for i in lst:
+        if is
```

#### solution 3
```diff
-def is_odd(num):
+def is_odd(num):
+
+    if num % 2 == 0:
+        return True
+    else:
+        return False
+
+print(is_odd(5))
+
+# 定义函数，判断
```

#### solution 4
```diff
-def is_odd(num):
+def is_odd(num):
+
+    return num % 2 == 1
+
+def sum_odd_numbers(numbers):
+    total = 0
+    for num in numbers:
+        if is_odd(num):
+            total += num
+    return
```

### group_by (task/121)

#### canonical solution
```python
from collections import defaultdict

def group_by(lst, fn):  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
```

#### solution 0
```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    d = defaultdict(list)
+    for e in lst:
+        d[fn(e)].append(e)
+    return d
+
+def try_except(fn):
+    try:
+        return fn
```

#### solution 1
```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    groups = defaultdict(list)
+    for x in lst:
+        groups[fn(x)].append(x)
+    return groups
+
+def test_group_by():
+    animals = [{'species
```

#### solution 2
```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    grouped = defaultdict(list)
+    for l in lst:
+        grouped[fn(l)].append(l)
+    return grouped
+
+def group_by_key(lst, key):
+    return
```

#### solution 3
```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    d = defaultdict(list)
+    for x in lst:
+        d[fn(x)].append(x)
+    return d
+
+def group_by_centroid(restaurants, centroids
```

#### solution 4
```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    groups = defaultdict(list)
+    for el in lst:
+        key = fn(el)
+        groups[key].append(el)
+    return groups
+
+def test_group_by():
+   
```

### to_binary (task/122)

#### canonical solution
```python
def to_binary(n):  return bin(n)
```

#### solution 0
```diff
-def to_binary(n):
+def to_binary(n):
+
+    s = ''
+    while n > 0:
+        s = str(n % 2) + s
+        n = n // 2
+    return s
+
+def to_base(n, b):
+    s =
```

#### solution 1
```diff
-def to_binary(n):
+def to_binary(n):
+
+    if n > 1:
+        to_binary(n//2)
+    print(n % 2, end = '')
+
+to_binary(10)
+print()
+
+#%%
+# 2.1.
```

#### solution 2
```diff
-def to_binary(n):
+def to_binary(n):
+
+    #returns binary string of n, MSB first
+    #for example, to_binary(14) returns '1110'
+    string = ''
+    while n > 0:
+        string = str(n %
```

#### solution 3
```diff
-def to_binary(n):
+def to_binary(n):
+
+    return "{0:b}".format(n)
+
+def sum_weights(weights):
+    return sum(weights)
+
+def trim_zeros(s):
+    return s.lstrip('0')
```

#### solution 4
```diff
-def to_binary(n):
+def to_binary(n):
+
+    return [int(i) for i in list(bin(n)[2:])]
+
+def generate_numbers(n, m):
+    return [to_binary(i) for i in range(n,
```

### compact (task/123)

#### canonical solution
```python
def compact(lst):  return list(filter(None, lst))
```

#### solution 0
```diff
-def compact(lst):
+def compact(lst):
+
+    return [item for item in lst if item]
+
+def check_if_installed(cmd):
+    """
+    :param cmd: Command to execute to check if software is installed.
+    :type cmd: str
```

#### solution 1
```diff
-def compact(lst):
+def compact(lst):
+
+    if len(lst) <= 1:
+        return lst
+    if lst[0] == lst[1]:
+        return compact(lst[1:])
+    return [lst[0]]
```

#### solution 2
```diff
-def compact(lst):
+def compact(lst):
+
+    """Return a copy of lst with non-true elements removed.
+
+        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
+        [1, 2, 'All
```

#### solution 3
```diff
-def compact(lst):
+def compact(lst):
+
+    """Return a copy of lst with non-true elements removed.
+
+        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
+        [1, 2, 'All
```

#### solution 4
```diff
-def compact(lst):
+def compact(lst):
+
+    """Return a copy of lst with non-true elements removed.
+
+        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
+        [1, 2, 'All
```

### in_range (task/124)

#### canonical solution
```python
def in_range(n, start, end = 0):  return start <= n <= end if end >= start else end <= n <= start
```

#### solution 0
```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+
+    if start < end:
+        return start <= n <= end
+    else:
+        return start <= n or n <= end
+
+# def sum_of_squares(n):
+#     s = 0
+#
```

#### solution 1
```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+
+	"""Returns True if n is between start and end. If end is not provided, it will return True if n is equal to start."""
+	if end == 0:
+		return n == start
+	else:
```

#### solution 2
```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+
+    if end == 0:
+        end = start
+        start = 0
+    return start <= n <= end
+
+def get_function_name():
+    return traceback.extract_stack(None, 2)[0
```

#### solution 3
```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+
+    if end == 0:
+        end = start
+        start = 0
+    return n >= start and n < end
+
+# 计算阶乘
+def factorial(n):
+   
```

#### solution 4
```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+
+    if end == 0:
+        end = start
+        start = 0
+    return n >= start and n < end
+
+def is_allowed_specific_char(string):
+    charRe = re.compile(
```

### daterange (task/125)

#### canonical solution
```python
from datetime import timedelta, date

def daterange(start, end):  return [start + timedelta(n) for n in range(int((end - start).days))]
```

#### solution 0
```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    for n in range(int ((end - start).days)):
+        yield start + timedelta(n)
+
+start_dt = date(2018, 5, 1)
+end_dt = date(2018, 6
```

#### solution 1
```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    for n in range(int ((end - start).days)):
+        yield start + timedelta(n)
+
+# list of days from today to the last day of the year
+dates = []
+today = date.
```

#### solution 2
```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    """
+    Generator that yields a date range between two dates.
+    """
+    for n in range(int ((end - start).days)):
+        yield start + timedelta(n)
+
+def day_has
```

#### solution 3
```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    for n in range(int ((end - start).days)):
+        yield start + timedelta(n)
+
+def get_users(datetime, date_from, date_to):
+    users = []
```

#### solution 4
```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    for n in range(int ((end - start).days)):
+        yield start + timedelta(n)
+
+# This code is here to find the day when maximum number of new cases were recorded in a particular country.
```

### chunk (task/126)

#### canonical solution
```python
from math import ceil

def chunk(lst, size):  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))
```

#### solution 0
```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    for i in range(0, len(lst), size):
+        yield lst[i:i + size]
+
+def get_progress_bar(current, total, length, prefix = '', suffix = '
```

#### solution 1
```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    """
+    Chunks a list into sublists of given size.
+
+    Parameters
+    ----------
+    lst : list
+        The list to chunk.
+    size : int
+        The chunk size.
+
+    Returns
```

#### solution 2
```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    return list(lst[i:i+size] for i in range(0, len(lst), size))
+
+def decode(xs):
+    return [chr(x) for x in xs]
```

#### solution 3
```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    return list(
+        map(lambda x: lst[x * size:x * size + size],
+            list(range(0, ceil(len(lst) / size)))))
+
+import matplot
```

#### solution 4
```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    return list(
+        map(lambda x: lst[x * size:x * size + size],
+            list(range(0, ceil(len(lst) / size)))))
+
+chunk([
```

### deep_flatten (task/127)

#### canonical solution
```python
from collections.abc import Iterable

def deep_flatten(lst):  return ([a for i in lst for a in
          deep_flatten(i)] if isinstance(lst, Iterable) else [lst])
```

#### solution 0
```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    for item in lst:
+        if isinstance(item, Iterable):
+            yield from deep_flatten(item)
+        else:
+            yield item
+
+lst = [[[1, 2, 3
```

#### solution 1
```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    """Recursively flatten a list"""
+    for el in lst:
+        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
+            yield from deep_fl
```

#### solution 2
```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    for el in lst:
+        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
+            yield from deep_flatten(el)
+        else:
+            yield
```

#### solution 3
```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    """Flatten an iterable deeply."""
+    for el in lst:
+        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
+            yield from deep_fl
```

#### solution 4
```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    result = []
+    for x in lst:
+        if isinstance(x, Iterable):
+            result.extend(deep_flatten(x))
+        else:
+            result.append(x)
```

### initialize_list_with_values (task/128)

#### canonical solution
```python
def initialize_list_with_values(n, val = 0):  return [val for x in range(n)]
```

#### solution 0
```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+
+    new_list = []
+    for i in range(n):
+        new_list.append(val)
+    return new_list
+
+def get_amount_of_memory_in_mb(input_string
```

#### solution 1
```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+
+    """
+    Creates a list of length n initialized with the value val.
+    """
+    return [val for i in range(n)]
+
+def get_vector_sum(vector):
+    """
+    Returns
```

#### solution 2
```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+
+    for i in range(n):
+        l.append(val)
+
+# add value v to position i
+def add_value(i, v):
+    l[i] += v
+
+# initialize list with
```

#### solution 3
```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+
+    list_with_values = []
+    for i in range(n):
+        list_with_values.append(val)
+    return list_with_values
+
+def initialize_2d_list_with_
```

#### solution 4
```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+
+    l = []
+    for i in range(n):
+        l.append(val)
+    return l
+
+def initialize_matrix_with_values(n, m, val = 0):
+    mat =
```

### average_by (task/129)

#### canonical solution
```python
def average_by(lst, fn = lambda x: x):  return sum(map(fn, lst), 0.0) / len(lst)
```

#### solution 0
```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+
+    """
+    Returns the average of list items that match the selector function
+    :param lst:
+    :param fn:
+    :return:
+    """
+    if not isinstance(lst, list):
```

#### solution 1
```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+
+    return sum(map(fn, lst)) / len(lst)
+
+#TODO: maybe use itertools.tee
+def split_list(lst, n = 2):
+    """ Split
```

#### solution 2
```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+
+    """
+    Return the average value of the elements in the given list, after mapping
+    each element to a value using the given function.
+
+    >>> average_by([{ 'n': 4 }, { 'n': 2 },
```

#### solution 3
```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+
+    """ Returns the average of a list (lst) of numbers.
+
+    :param lst: a list of numbers
+    :param fn: an optional function that is applied to the list before taking the average
+    :return
```

#### solution 4
```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+
+    """Return the average of lst, using fn to get values.
+    """
+    return sum(fn(x) for x in lst) / len(lst)
+
+def average_within_time(l
```

### key_of_max (task/130)

#### canonical solution
```python
def key_of_max(d):  return max(d, key = d.get)
```

#### solution 0
```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    return key_of_max_value(d)
+
+def main():
+    #读取文件
+    fin = open('words.txt')
+    #创建字
```

#### solution 1
```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    v=list(d.values())
+    k=list(d.keys())
+    return k[v.index(max(v))]
+print(key_of_max(score))
+score={'aa
```

#### solution 2
```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    key = None
+    max = -1
+    for k in d:
+        if d[k] > max:
+            max = d[k]
+            key = k
+    return key
+
+
+def test_
```

#### solution 3
```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    return max(d, key=d.get)
+
+def answer(snapshots, transactions):
+    accounts = {}
+    for snapshot in snapshots:
+        accounts[snapshot[0]] = int(snapshot[
```

#### solution 4
```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    """Returns the key in a dict d that corresponds to the maximum value of d.
+
+    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
+    >>> key_
```

### offset (task/131)

#### canonical solution
```python
def offset(lst, offset):  return lst[offset:] + lst[:offset]
```

#### solution 0
```diff
-def offset(lst, offset):
+def offset(lst, offset):
+
+    return lst[offset:] + lst[:offset]
+
+
+def read_file(filename):
+    with open(filename, 'r') as f:
+        return f.read()
+
+
+def write_file
```

#### solution 1
```diff
-def offset(lst, offset):
+def offset(lst, offset):
+
+    return lst[offset:] + lst[:offset]
+
+
+def _update_resolved_graph(resolved_graph, original_graph, node, items):
+    if node not in resolved_graph:
```

#### solution 2
```diff
-def offset(lst, offset):
+def offset(lst, offset):
+
+    return lst[offset:] + lst[:offset]
+
+
+class PlaybackMode(object):
+    """
+    Enum-like class that defines the playback modes for the playlist.
+    """
+
+    #:
```

#### solution 3
```diff
-def offset(lst, offset):
+def offset(lst, offset):
+
+    return lst[offset:] + lst[:offset]
+
+
+class TestRunner(object):
+    def __init__(self, bot, options):
+        self.bot = bot
+        self.options = options
```

#### solution 4
```diff
-def offset(lst, offset):
+def offset(lst, offset):
+
+    return lst[offset:] + lst[:offset]
+
+
+def roundrobin(*iterables):
+    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
+   
```

### intersection_by (task/132)

#### canonical solution
```python
def intersection_by(a, b, fn):  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
```

#### solution 0
```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+
+    result = []
+    for x in a:
+        for y in b:
+            if fn(x, y):
+                result.append(x)
+                break
+    return result
+
+
+def union_by(
```

#### solution 1
```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+
+    fn1 = lambda o: [ x for x in a if fn(o, x) ]
+    fn2 = lambda o: [ x for x in b if fn(o, x) ]
+    return intersection(fn
```

#### solution 2
```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+
+    '''
+    @param a list of objects
+    @param b list of objects
+    @param fn function to use to compute intersection
+    '''
+    return [ x for x in a if fn(x, b
```

#### solution 3
```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+
+    return dict([(x, x) for x in a if x in b and fn(x)])
+
+
+def find_closest_day(d):
+    """
+    Utility function used by update_daily_
```

#### solution 4
```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+
+    """
+    Returns the intersection of both iterables, where the intersection is defined
+    by the `fn` function.
+
+    :param a: iterable
+    :param b: iterable
+    :param fn: function
```

### union_by (task/133)

#### canonical solution
```python
def union_by(a, b, fn):  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))
```

#### solution 0
```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+
+    """
+    Returns the union of two lists, after applying the provided function
+    to each list element of both.
+    """
+    b = set(map(fn, b))
+    return [x for x in a
```

#### solution 1
```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+
+    """Union the two sets of objects by the key function.
+
+    The source order is preserved.
+
+    Parameters
+    ----------
+    a : list
+        The first set of objects.
+    b : list
+        The
```

#### solution 2
```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+
+    """Return the union of two lists, after applying the provided function
+    to each list element of both.
+
+    Duplicate elements will be ignored.
+
+    It uses a hash table to collect the results. The time complexity is
```

#### solution 3
```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+
+    """
+    Returns the union of two lists, after applying the provided function
+    to each list element of both.
+
+    Example:
+        union_by([1, 2, 3], [1, 2, 4], lambda
```

#### solution 4
```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+
+    """Combine two lists of dictionaries with different keys.
+
+    Each item in the result contains all the keys from
+    both items, with values from `b` overwriting values
+    from `a` if the same
```

### all_unique (task/134)

#### canonical solution
```python
def all_unique(lst):  return len(lst) == len(set(lst))
```

#### solution 0
```diff
-def all_unique(lst):
+def all_unique(lst):
+
+    """Are all the elements in the list unique?"""
+    return len(lst) == len(set(lst))
+
+
+class TypedList(list):
+    """List that can only contain a given type or
```

#### solution 1
```diff
-def all_unique(lst):
+def all_unique(lst):
+
+    lst.sort()
+    for i in range(len(lst)-1):
+        if lst[i] == lst[i+1]:
+            return False
+    return True
+
+# print(
```

#### solution 2
```diff
-def all_unique(lst):
+def all_unique(lst):
+
+    return len(lst) == len(set(lst))
+
+def sum_index_same(lst):
+    for i in range(len(lst)):
+        for j in range(i+
```

#### solution 3
```diff
-def all_unique(lst):
+def all_unique(lst):
+
+    '''
+    Написать функцию которая проверяет уник
```

#### solution 4
```diff
-def all_unique(lst):
+def all_unique(lst):
+
+    '''Check all items are unique'''
+    return len(lst) == len(set(lst))
+
+
+def check_timeseries(data, how):
+    '''Check that all items in a list
```

### pluck (task/135)

#### canonical solution
```python
def pluck(lst, key):  return [x.get(key) for x in lst]
```

#### solution 0
```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    return [item[key] for item in lst]
+
+def is_valid_json(text):
+    try:
+        json.loads(text)
+        return True
+    except ValueError:
+        return
```

#### solution 1
```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    "return a list of the given key in all the dicts in the list"
+    return [d[key] for d in lst]
+
+def _check_key(cls, key):
+    if is
```

#### solution 2
```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    return [val[key] for val in lst]
+
+
+def stop():
+    """
+    Stop all current requests and stop the reactor
+    """
+    global _running_requests
+    for req in _running
```

#### solution 3
```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    return [
+        elem[key]
+        for elem in lst
+    ]
+
+
+@register.simple_tag
+def active(request, pattern):
+    if pattern == '/':
+        return 'active
```

#### solution 4
```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    return [d[key] for d in lst]
+
+def process_file(filename):
+    '''
+    This function extracts data from the file and populates the lists:
+    header, data_types,
```

### for_each (task/136)

#### canonical solution
```python
def for_each(itr, fn):  for el in itr:
    fn(el)
```

#### solution 0
```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+
+    for elem in itr:
+        fn(elem)
+
+def find_first(itr, fn):
+    for elem in itr:
+        if fn(elem):
+            return elem
```

#### solution 1
```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+
+    return [fn(e) for e in itr]
+
+
+@given(st.lists(st.integers()))
+def test_for_each(lst):
+    lst_copy = copy.deep
```

#### solution 2
```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+
+    """
+    Iterate over an iterator and call a function on each element. Return a
+    list of the results.
+
+    Parameters
+    ----------
+    itr : iterator
+        The iterator.
+
+    fn : function
```

#### solution 3
```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+
+    for item in itr:
+        fn(item)
+
+
+def as_iterator(itr):
+    if not isinstance(itr, Iterator):
+        itr = iter(itr)
+    return
```

#### solution 4
```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+
+    for value in itr:
+        fn(value)
+
+def map(itr, fn):
+    return [fn(v) for v in itr]
+
+def filter(itr, fn):
+   
```

### every (task/137)

#### canonical solution
```python
def every(lst, fn = lambda x: x):  return all(map(fn, lst))
```

#### solution 0
```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+
+	for x in lst:
+		if not fn(x):
+			return False
+	return True
+
+def any(lst, fn = lambda x: x):
+	for x in lst:
```

#### solution 1
```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+
+    for i in lst:
+        if not fn(i):
+            return False
+    return True
+
+# def except_(lst, fn = lambda x: x):
+#     for i in lst:
```

#### solution 2
```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+
+	for x in lst:
+		if not fn(x):
+			return False
+	return True
+
+def any(lst, fn = lambda x: x):
+	for x in lst:
```

#### solution 3
```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+
+    for i in lst:
+        if not fn(i):
+            return False
+    return True
+
+def single(lst, fn = lambda x: x):
+    i = 0
+    for x in l
```

#### solution 4
```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+
+    return reduce(lambda x, y: x and fn(y), lst, True)
+
+def any(lst, fn = lambda x: x):
+    return reduce(lambda x, y: x or fn(
```

### byte_size (task/138)

#### canonical solution
```python
def byte_size(s):  return len(s.encode('utf-8'))
```

#### solution 0
```diff
-def byte_size(s):
+def byte_size(s):
+
+    """
+    Calculates the number of bytes necessary to encode the given string. This
+    method uses the same logic as the base64 module to determine the size of
+    the string but returns a byte count instead of a character count
```

#### solution 1
```diff
-def byte_size(s):
+def byte_size(s):
+
+    return len(s.encode('utf-8'))
+
+
+def get_extension(filename):
+    return filename.rsplit('.', 1)[1].lower()
```

#### solution 2
```diff
-def byte_size(s):
+def byte_size(s):
+
+    try:
+        return len(s.encode('utf-8'))
+    except UnicodeDecodeError:
+        return len(s)
+
+
+def get_terminal_size():
+    """
+    get
```

#### solution 3
```diff
-def byte_size(s):
+def byte_size(s):
+
+    """Return the length of s in bytes."""
+    return len(s.encode('utf-8'))
+
+
+def uid_to_slug(uid):
+    """Return a slug string based on the
```

#### solution 4
```diff
-def byte_size(s):
+def byte_size(s):
+
+    return len(s.encode('utf-8'))
+
+
+def get_statistics(rdd):
+    rdd_for_count = rdd.map(lambda x: x[0])
+    c
```

### pad_number (task/139)

#### canonical solution
```python
def pad_number(n, l):  return str(n).zfill(l)
```

#### solution 0
```diff
-def pad_number(n, l):
+def pad_number(n, l):
+
+    """
+    Pad the number n with zeros in order to get a string of length l.
+    """
+    return str(n).zfill(l)
+
+
+def parse_args():
+    parser = argparse
```

#### solution 1
```diff
-def pad_number(n, l):
+def pad_number(n, l):
+
+    s = str(n)
+    while len(s) < l:
+        s = '0' + s
+    return s
+
+def get_time_stamp():
+    return datetime.datetime.
```

#### solution 2
```diff
-def pad_number(n, l):
+def pad_number(n, l):
+
+    return ' ' * (l - len(str(n))) + str(n)
+
+
+def format_time(t):
+    return '{}s'.format(t) if t > 1 else '{}ms
```

#### solution 3
```diff
-def pad_number(n, l):
+def pad_number(n, l):
+
+    t = str(n)
+    while len(t) < l:
+        t = '0' + t
+    return t
+
+def double_hash(s):
+    return hashlib.sha256(hash
```

#### solution 4
```diff
-def pad_number(n, l):
+def pad_number(n, l):
+
+    """
+    takes an integer n and returns a string of length l (l >= len(str(n)))
+    representing n, so that lexicographic sorting of the string repr. leads to
+    correct ordering.
+   
```

### for_each_right (task/140)

#### canonical solution
```python
def for_each_right(itr, fn):  for el in itr[::-1]:
    fn(el)
```

#### solution 0
```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+
+    """
+    Call `fn` with each element of `itr` as the first arg and return `itr`.
+
+    `fn` is called right-to-left.
+
+    Args:
+        itr (
```

#### solution 1
```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+
+    """
+    Iterates over the iterable right-to-left, passing each result to a
+    callback.
+
+    Args:
+        itr (iterable): Iterable collection.
+        fn (callable):
```

#### solution 2
```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+
+    """
+    Performs a right-handed, fold-like iteration over the elements of an
+    iterable.
+
+    :param itr: The iterable to traverse.
+    :param fn: The function to apply.
```

#### solution 3
```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+
+    """
+    Calls the given function with each element in the given iterable, and then
+    returns the iterable.
+
+    Parameters
+    ----------
+    itr : iterable
+        The iterable to call the function
```

#### solution 4
```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+
+    itr = reversed(itr)
+    return for_each(itr, fn)
+
+
+def tap(val, fn):
+    fn(val)
+    return val
+
+
+def tap_all(itr
```

### is_anagram (task/141)

#### canonical solution
```python
from collections import Counter

def is_anagram(s1, s2):  return Counter(
    c.lower() for c in s1 if c.isalnum()
  ) == Counter(
    c.lower() for c in s2 if c.isalnum()
  )
```

#### solution 0
```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    return Counter(s1) == Counter(s2)
+
+def detect_anagrams(word, candidates):
+    return [candidate for candidate in candidates if is_anagram(word.lower(), candidate.lower
```

#### solution 1
```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    return Counter(s1) == Counter(s2)
+
+a = "fairy tales"
+b = "rail safety"
+
+print is_anagram(a, b)
+
+# other solution
+def is
```

#### solution 2
```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    return Counter(s1) == Counter(s2)
+
+def is_anagram2(s1, s2):
+    return sorted(s1) == sorted(s2)
+
+def is_anagram
```

#### solution 3
```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    s1 = ''.join(sorted(s1)).strip()
+    s2 = ''.join(sorted(s2)).strip()
+    return s1 == s2
+
+def count_anagrams
```

#### solution 4
```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    """
+    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
+    if s1 and s2 contain the same letters in a possibly different order.
+    E.
```

### decapitalize (task/142)

#### canonical solution
```python
def decapitalize(s, upper_rest = False):  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

#### solution 0
```diff
-def decapitalize(s, upper_rest = False):
+def decapitalize(s, upper_rest = False):
+
+    """Decapitalize the first letter of s."""
+    if s:
+        return s[0].lower() + (s[1:].upper() if upper_rest else s[1:])
+    else
```

#### solution 1
```diff
-def decapitalize(s, upper_rest = False):
+def decapitalize(s, upper_rest = False):
+
+    ''' Lowercases the first letter of s. '''
+    if s:
+        return s[0].lower() + (s[1:].upper() if upper_rest else s[1:])
+    else
```

#### solution 2
```diff
-def decapitalize(s, upper_rest = False):
+def decapitalize(s, upper_rest = False):
+
+    return s[:1].lower() + (s[1:].upper() if upper_rest else s[1:])
+
+def get_anchor_format(ref):
+    if ref.startswith('
```

#### solution 3
```diff
-def decapitalize(s, upper_rest = False):
+def decapitalize(s, upper_rest = False):
+
+    """decapitalize('FooBar') -> 'fooBar'
+    decapitalize('FooBar', True) -> 'fOOBAR'
+    """
+    return s[:1].lower() +
```

#### solution 4
```diff
-def decapitalize(s, upper_rest = False):
+def decapitalize(s, upper_rest = False):
+
+    if len(s) == 0:
+        return s
+    if len(s) == 1:
+        return s.lower()
+    return s[0].lower() + s[1:] if upper_rest else
```

### unique_elements (task/143)

#### canonical solution
```python
def unique_elements(li):  return list(set(li))
```

#### solution 0
```diff
-def unique_elements(li):
+def unique_elements(li):
+
+    return list(set(li))
+
+# Function to find the frequency of each element in a list
+def unique_frequency(li):
+    unique = unique_elements(li)
+    frequency = {}
+    for
```

#### solution 1
```diff
-def unique_elements(li):
+def unique_elements(li):
+
+    uniq_li = []
+    for element in li:
+        if element not in uniq_li:
+            uniq_li.append(element)
+    return uniq_li
+
+# D. Given
```

#### solution 2
```diff
-def unique_elements(li):
+def unique_elements(li):
+
+    new_li = []
+    for element in li:
+        if element not in new_li:
+            new_li.append(element)
+    return new_li
+
+# get a list of all files in
```

#### solution 3
```diff
-def unique_elements(li):
+def unique_elements(li):
+
+    return list(set(li))
+
+def remove_duplicates(li):
+    return list(set(li))
+
+def remove_duplicates_while_keeping_order(li):
+    seen =
```

#### solution 4
```diff
-def unique_elements(li):
+def unique_elements(li):
+
+    new_li = []
+    for ele in li:
+        if ele not in new_li:
+            new_li.append(ele)
+    return new_li
+
+def average_x(x_list
```

### rgb_to_hex (task/144)

#### canonical solution
```python
def rgb_to_hex(r, g, b):  return ('{:02X}' * 3).format(r, g, b)
```

#### solution 0
```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+
+    return '#%02x%02x%02x' % (r, g, b)
+
+def hex_to_rgb(value):
+    value = value.lstrip('#')
+    lv
```

#### solution 1
```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+
+    return '#%02x%02x%02x' % (r, g, b)
+
+#COLORS
+# from colour import Color
+#
+# red = Color("red")
+# print(red.
```

#### solution 2
```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+
+    """Return color as #rrggbb for the given color values."""
+    return '#%02x%02x%02x' % (r, g, b)
+
+def scale_rgb_tuple
```

#### solution 3
```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+
+    return '#%02x%02x%02x' % (r, g, b)
+
+def hex_to_rgb(value):
+    value = value.lstrip('#')
+    lv
```

#### solution 4
```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+
+    return '#%02x%02x%02x' % (r, g, b)
+
+def hex_to_rgb(value):
+    value = value.lstrip('#')
+    lv
```

### values_only (task/145)

#### canonical solution
```python
def values_only(flat_dict):  return list(flat_dict.values())
```

#### solution 0
```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+
+    for key, value in flat_dict.items():
+        if isinstance(value, dict):
+            yield from values_only(value)
+        else:
+            yield value
+
+#
+# new code start
```

#### solution 1
```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+
+    return [item[1] for item in flat_dict]
+
+
+def print_model_params(model):
+    print(40 * '=')
+    print(model)
+    print(40 * '=')
```

#### solution 2
```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+
+    for key, value in flat_dict.items():
+        if isinstance(value, dict):
+            for k, v in value.items():
+                yield f'{key}_{k}', v
+        else
```

#### solution 3
```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+
+    for key, value in flat_dict.items():
+        yield value
+
+
+def get_index(index):
+    return index
+
+
+def get_item(item):
+    return item
+
+
+def get_value(
```

#### solution 4
```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+
+    return [item[1] for item in flat_dict]
+
+
+def first_values_only(flat_dict):
+    return [item[1] for item in flat_dict][0]
+
+
+def flat_
```

### unfold (task/146)

#### canonical solution
```python
def unfold(fn, seed):  def fn_generator(val):
    while True: 
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]
```

#### solution 0
```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+
+    value = seed
+    while True:
+        yield value
+        value = fn(value)
+
+def with_index(it):
+    i = 0
+    for x in it:
+        yield (i, x
```

#### solution 1
```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+
+    """
+    >>> list(unfold(lambda x: [x + 1], 1))
+    [2, 3, 4, 5, 6, 7, 8, 9, 10]
+    """
+    while True:
```

#### solution 2
```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+
+    stack = deque([seed])
+    seen = set()
+    while stack:
+        x = stack.pop()
+        if x not in seen:
+            seen.add(x)
+            stack.extend
```

#### solution 3
```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+
+    return accumulate(fn, seed, identity)
+
+def unfold(fn, seed):
+    return reduce(lambda acc, elem: fn(acc, elem), [seed], identity)
+
+from operator import add
```

#### solution 4
```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+
+    """
+    Recursively perform (f . g) to the input until a non-function
+    value is found.
+
+    >>> inc, add = lambda x: x + 1, lambda x, y: x + y
```

### reverse (task/147)

#### canonical solution
```python
def reverse(itr):  return itr[::-1]
```

#### solution 0
```diff
-def reverse(itr):
+def reverse(itr):
+
+    res = []
+    for i in itr:
+        res.insert(0, i)
+    return res
+
+def replace_at(itr, idx, val):
+    return itr[:id
```

#### solution 1
```diff
-def reverse(itr):
+def reverse(itr):
+
+    lst = []
+    for i in itr:
+        lst.append(i)
+    return lst
+
+def reverse1(itr):
+    lst = []
+    for i in itr
```

#### solution 2
```diff
-def reverse(itr):
+def reverse(itr):
+
+    for i in range(len(itr)-1,-1,-1):
+        yield itr[i]
+
+def main():
+    iterator = [1,2,3,4,5]
+    print(
```

#### solution 3
```diff
-def reverse(itr):
+def reverse(itr):
+
+    return reversed(list(itr))
+
+
+def pipe(*funcs):
+    return functools.reduce(lambda f, g: lambda x: f(g(x)), funcs)
+
+
+def compose(*
```

#### solution 4
```diff
-def reverse(itr):
+def reverse(itr):
+
+    return itr[::-1]
+
+def main():
+    filename = input('Please enter the name of the file you want to get data from: ')
+    if os.path.exists(filename):
```

### is_divisible (task/148)

#### canonical solution
```python
def is_divisible(dividend, divisor):  return dividend % divisor == 0
```

#### solution 0
```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+
+    return dividend % divisor == 0
+
+def is_prime(n):
+    if n < 2:
+        return False
+    for i in range(2,n):
+        if is_divisible(n
```

#### solution 1
```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+
+    if dividend % divisor == 0:
+        return True
+    else:
+        return False
+
+# Let's test the function
+print(is_divisible(8, 2)) # Should be True
+print(
```

#### solution 2
```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+
+    if dividend % divisor == 0:
+        return True
+    else:
+        return False
+    
+#print(is_divisible(1, 3))
+#print(is_divisible(2, 3
```

#### solution 3
```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+
+    return dividend % divisor == 0
+
+def fizzbuzz(start, end):
+    for i in range(start, end):
+        if is_divisible(i, 15):
+            print("F
```

#### solution 4
```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+
+    """
+    This is an optional function to validate the
+    divisibility. You can write your own function
+    or delete this one.
+    """
+    if not isinstance(dividend, int) or not
```

### is_weekday (task/149)

#### canonical solution
```python
from datetime import datetime

def is_weekday(d = datetime.today()):  return d.weekday() <= 4
```

#### solution 0
```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    if d.weekday() in [5,6]:
+        return False
+    return True
+
+is_weekday()
+
+# Problem 9
+def is_leap_year(year = datetime.today().
```

#### solution 1
```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    if d.weekday() == 5 or d.weekday() == 6:
+        return False
+    return True
+
+print(is_weekday())
+
+def is_workday(d = datetime.today
```

#### solution 2
```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    return d.weekday() < 5
+
+print is_weekday()
+print is_weekday(datetime(2015, 8, 26))
+
+# lambda(匿名函数)
+
```

#### solution 3
```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    return d.weekday() < 5
+
+# Test if today is a weekday
+assert is_weekday()
+
+# Test if today is a weekend
+assert not is_weekday(datetime(2020, 7,
```

#### solution 4
```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    if (d.weekday() < 5):
+        return True
+    else:
+        return False
+
+print is_weekday()
+
+print is_weekday(datetime(2017,2,22))
```

### fahrenheit_to_celsius (task/150)

#### canonical solution
```python
def fahrenheit_to_celsius(degrees):  return ((degrees - 32) * 5/9)
```

#### solution 0
```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+
+    return round((degrees - 32) * (5/9), 2)
+
+
+def celsius_to_fahrenheit(degrees):
+    return round((degrees * (9/5)) + 32, 2
```

#### solution 1
```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+
+    celsius = (degrees - 32) * (5/9)
+    return celsius
+fahrenheit_to_celsius(55)
+def celsius_to_fahrenheit(degrees):
```

#### solution 2
```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+
+    return (degrees - 32) * (5 / 9)
+
+print("Freezing point of water:", fahrenheit_to_celsius(32))
+print("Boiling point of water:", fah
```

#### solution 3
```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+
+    """
+    Convert Fahrenheit temperature to Celsius.
+
+    :param degrees: degrees Fahrenheit
+    :return: degrees Celsius
+    """
+    return round((degrees - 32) * 5 / 9, 1)
+
+
+def c
```

#### solution 4
```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+
+    """
+    Converts temperature in degrees Fahrenheit to degrees Celsius.
+    """
+    return (degrees - 32) * 5 / 9
+
+def fahrenheit_to_kelvin(degrees):
+    """
```

### sum_by (task/151)

#### canonical solution
```python
def sum_by(lst, fn):  return sum(map(fn, lst))
```

#### solution 0
```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+
+    """
+    Returns the sum of lst[i] for each i where fn(lst[i]) is True.
+    lst -- a list of integers
+    fn -- a function that takes an integer and returns True
```

#### solution 1
```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+
+    return reduce(lambda x, y: x + y, map(fn, lst))
+
+
+def get_fibonacci_numbers(n):
+    first = 0
+    second = 1
+    fibon
```

#### solution 2
```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+
+    return reduce(lambda a, b: a + b, map(fn, lst))
+
+def product_by(lst, fn):
+    return reduce(lambda a, b: a * b, map(fn
```

#### solution 3
```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+
+    """Returns the sum of a list of numbers that is converted to a single key
+    with the provided function.
+
+    Arguments:
+        lst: a list of numbers
+        fn: a function to convert a number to
```

#### solution 4
```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+
+    '''
+    sum_by([{'name': 'joe', 'num': 3}, {'name': 'bob', 'num': 1}, {'name': 'tom', 'num': 4}], '
```

### find_key (task/152)

#### canonical solution
```python
def find_key(dict, val):  return next(key for key, value in dict.items() if value == val)
```

#### solution 0
```diff
-def find_key(dict, val):
+def find_key(dict, val):
+
+    """return the key of dictionary dic given the value"""
+    return [k for k, v in dict.iteritems() if v == val][0]
+
+def main():
+    # read the training files
+   
```

#### solution 1
```diff
-def find_key(dict, val):
+def find_key(dict, val):
+
+    """return the key of dictionary dic given the value"""
+    return [k for k, v in dict.iteritems() if v == val][0]
+
+class Topo(Topo):
+    def __init
```

#### solution 2
```diff
-def find_key(dict, val):
+def find_key(dict, val):
+
+    """return the key of dictionary dic given the value"""
+    return [k for k, v in dict.iteritems() if v == val][0]
+
+def p_value_matrix(df, col_
```

#### solution 3
```diff
-def find_key(dict, val):
+def find_key(dict, val):
+
+    for key, value in dict.items():
+        if val == value:
+            return key
+    return "key doesn't exist"
+
+# =============================================================================
+# Additional functions
+# =============================================================================
+
+def download_data
```

#### solution 4
```diff
-def find_key(dict, val):
+def find_key(dict, val):
+
+    """return the key of dictionary dic given the value"""
+    return [k for k, v in dict.iteritems() if v == val][0]
+# ===========================
+# ======= global
+# =========================
```

### to_hex (task/153)

#### canonical solution
```python
def to_hex(dec):  return hex(dec)
```

#### solution 0
```diff
-def to_hex(dec):
+def to_hex(dec):
+
+    dec = int(dec)
+    return str(hex(dec)[2:]).upper()
+
+
+def read_file(path):
+    with open(path, 'rb') as f:
+        raw = f.
```

#### solution 1
```diff
-def to_hex(dec):
+def to_hex(dec):
+
+    return '{0:02x}'.format(dec)
+
+def to_mac_range(start, end):
+    return ':'.join(map(to_hex, start)) + '-' + ':
```

#### solution 2
```diff
-def to_hex(dec):
+def to_hex(dec):
+
+    return "%x" % dec
+
+def to_ascii(value):
+    """
+    Converts specified value to ASCII string.
+    @param value: value to be converted
+    @type value: int|
```

#### solution 3
```diff
-def to_hex(dec):
+def to_hex(dec):
+
+    return hex(dec)[2:]
+
+def from_hex(hex_str):
+    return int(hex_str, 16)
+
+def xor_hex(hex_str1, hex_str2):
```

#### solution 4
```diff
-def to_hex(dec):
+def to_hex(dec):
+
+    hex_characters = '0123456789abcdef'
+    if dec > 255:
+        return 'ff'
+    else:
+        return hex_characters[int(dec / 16)] + hex_
```

### clamp_number (task/154)

#### canonical solution
```python
def clamp_number(num, a, b):  return max(min(num, max(a, b)), min(a, b))
```

#### solution 0
```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+
+    if num < a:
+        return a
+    elif num > b:
+        return b
+    else:
+        return num
+
+
+class PositionPlayer(Player):
+    def __init__(self, x,
```

#### solution 1
```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+
+    return max(a, min(b, num))
+
+def _should_run_key_press_event(x, y):
+    return x < SCREEN_WIDTH and y < SCREEN_
```

#### solution 2
```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+
+    """Clamps number between two other numbers."""
+    return max(a, min(b, num))
+
+
+def distance(x1, y1, x2, y2):
+    """Calculates the distance
```

#### solution 3
```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+
+    return max(a, min(b, num))
+
+def interp_number(val, start, end, a, b):
+    return clamp_number(a + ((b - a) * (val - start
```

#### solution 4
```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+
+    if num < a:
+        return a
+    elif num > b:
+        return b
+    else:
+        return num
+
+def clamp_char(char, min_char, max_char):
+   
```

### compose_right (task/155)

#### canonical solution
```python
from functools import reduce

def compose_right(*fns):  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
```

#### solution 0
```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    """
+    Compose the given functions, where the arguments are applied from right to left.
+    :param fns: The functions to compose.
+    :return: A function that composes the given functions.
+    """
```

#### solution 1
```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    return reduce(lambda f, g: lambda x: f(g(x)), fns)
+
+def make_compose_n(n):
+    if n <= 1:
+        return lambda f, g: lambda
```

#### solution 2
```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    # Right to left function composition
+    return reduce(lambda f, g: lambda x: f(g(x)), fns)
+
+def compose_left(*fns):
+    # Left to right function composition
+   
```

#### solution 3
```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    return reduce(lambda f, g: lambda x: f(g(x)), fns)
+
+def compose_left(*fns):
+    return reduce(lambda f, g: lambda x: g(f(x
```

#### solution 4
```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    """Returns a function that is the right-to-left composition of the given functions.
+    The returned function is called with the arguments it expects.
+    """
+    return reduce(lambda f, g: lambda *args,
```

### days_diff (task/156)

#### canonical solution
```python
def days_diff(start, end):  return (end - start).days
```

#### solution 0
```diff
-def days_diff(start, end):
+def days_diff(start, end):
+
+    start_date = date(start[0], start[1], start[2])
+    end_date = date(end[0], end[1], end[2])
+    diff = end_date - start_
```

#### solution 1
```diff
-def days_diff(start, end):
+def days_diff(start, end):
+
+    """Calculates the number of days between two days"""
+    start_date = datetime.strptime(start, '%Y-%m-%d')
+    end_date = datetime.strpt
```

#### solution 2
```diff
-def days_diff(start, end):
+def days_diff(start, end):
+
+    # convert dates to datetime format
+    start_datetime = datetime.datetime.strptime(start, '%Y-%m-%d')
+    end_datetime = datetime.datetime
```

#### solution 3
```diff
-def days_diff(start, end):
+def days_diff(start, end):
+
+    """
+        Find absolute diff in days between dates
+    """
+    end_date = datetime.strptime(end, '%Y-%m-%d')
+    start_date = datetime.str
```

#### solution 4
```diff
-def days_diff(start, end):
+def days_diff(start, end):
+
+    start = date(start[0], start[1], start[2])
+    end = date(end[0], end[1], end[2])
+    delta = end - start
+    return abs(delta
```

### is_contained_in (task/157)

#### canonical solution
```python
def is_contained_in(a, b):  for v in set(a):
    if a.count(v) > b.count(v):
      return False
  return True
```

#### solution 0
```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+
+    return a[0] >= b[0] and a[1] >= b[1] and a[2] <= b[2] and a[3] <= b[3]
+
+
+class Rectangle(object):
```

#### solution 1
```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+
+    a_ = np.array(a)
+    b_ = np.array(b)
+    return np.all(a_ >= b_) and np.all(a_ <= b_ + 1)
+
+
```

#### solution 2
```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+
+    """
+    Checks whether polygon A is contained in polygon B
+
+    """
+    if not isinstance(a, Polygon):
+        raise TypeError("A is not a Polygon")
+    if not isinstance
```

#### solution 3
```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+
+    """Return True if a is contained in b"""
+    if isinstance(a, dict) and isinstance(b, dict):
+        for k, v in a.items():
+            if k not in b:
```

#### solution 4
```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+
+    return is_type_of(a, b) and not is_type_of(b, a)
+
+
+def is_type_of(a, b):
+    return (isinstance(a, b) or
```

### drop_right (task/158)

#### canonical solution
```python
def drop_right(a, n = 1):  return a[:-n]
```

#### solution 0
```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+
+    return a[:len(a) - n]
+
+def drop_list(a, b):
+    return [x for x in a if x not in b]
+
+def append_list(a, b):
```

#### solution 1
```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+
+    """
+    Drops the last n elements from a list.
+    Example:
+        >>> drop_right([1, 2, 3, 4, 5], 3)
+        [1, 2, 3]
+    """
```

#### solution 2
```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+
+    return a[:-n]
+
+def to_upper(a):
+    return a.upper()
+
+def to_lower(a):
+    return a.lower()
+
+def trim(a):
+    return
```

#### solution 3
```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+
+    """
+    drop the last n elements of an array
+
+    :param a: array to drop elements from
+    :param n: number of elements to drop
+    :return: a new array with the last n elements dropped
```

#### solution 4
```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+
+    a = np.asarray(a)
+    return a[:a.shape[0] - n]
+
+def drop_left(a, n = 1):
+    a = np.asarray(a)
```

### gcd (task/159)

#### canonical solution
```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):  return reduce(_gcd, numbers)
```

#### solution 0
```diff
-from functools import reduce
-from math import gcd as _gcd
-
-def gcd(numbers):
+from functools import reduce
+from math import gcd as _gcd
+
+def gcd(numbers):
+
+    return reduce(_gcd, numbers)
+
+def lcm(numbers):
+    return reduce(lambda x, y: (x*y)//_gcd(x,y), numbers, 1)
+
+T
```

#### solution 1
```diff
-from functools import reduce
-from math import gcd as _gcd
-
-def gcd(numbers):
+from functools import reduce
+from math import gcd as _gcd
+
+def gcd(numbers):
+
+    return reduce(_gcd, numbers)
+
+def lcm(numbers):
+    return reduce(lambda x, y: (x*y)//_gcd(x,y), numbers, 1)
+
+def
```

#### solution 2
```diff
-from functools import reduce
-from math import gcd as _gcd
-
-def gcd(numbers):
+from functools import reduce
+from math import gcd as _gcd
+
+def gcd(numbers):
+
+    return reduce(_gcd, numbers)
+
+def lcm(numbers):
+    return reduce(lambda x, y: (x*y)//_gcd(x,y), numbers, 1)
+
+def
```

#### solution 3
```diff
-from functools import reduce
-from math import gcd as _gcd
-
-def gcd(numbers):
+from functools import reduce
+from math import gcd as _gcd
+
+def gcd(numbers):
+
+    return reduce(_gcd, numbers)
+
+def lcm(numbers):
+    return reduce(lambda x, y: (x*y)//_gcd(x,y), numbers, 1)
+
+n
```

#### solution 4
```diff
-from functools import reduce
-from math import gcd as _gcd
-
-def gcd(numbers):
+from functools import reduce
+from math import gcd as _gcd
+
+def gcd(numbers):
+
+    return reduce(_gcd, numbers)
+
+def lcm(numbers):
+    return reduce(lambda x, y: (x*y)//_gcd(x,y), numbers, 1)
+
+N
```

