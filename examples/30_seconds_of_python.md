#### index_of_all (task/1)

```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+
+    " Return index of value in list, -1 if not present "
+    for i in range ( len (lst)):
+    if lst[i] == value:
+    return i
+    return - 1
```

#### index_of_all (task/1)

```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+ """Returns index of all items that matches value""" return max(len(lst) for lst in lst if lst.index(value) != -1)
+    The index_of_all function will take a list and return the index of the first item that matches the value. In other words, it’s
```

#### index_of_all (task/1)

```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+
+    #print lst
+    for value in lst:
+    if value == value:
+    return index
+    return -1
+    index = index_of_all(lst, value)
+    if index != -1:
+    return index
+    return -1
```

#### index_of_all (task/1)

```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+
+    for i in range(len(lst)):
+    if lst[i] == value:
+    return i
+    return -1
```

#### index_of_all (task/1)

```diff
-def index_of_all(lst, value):
+def index_of_all(lst, value):
+
+    while lst and lst[0] != value:
+    lst = lst[1:]
+    return lst.index(value)
```

#### head (task/2)

```diff
-def head(lst):
+def head(lst):
+ return lst[0]
+    ▶ tuple
+    >>> lst = [head(head(head(head([1, 2, 3]))))] >>> lst [1, 2, 3]
+    ▶ tuple
+    >>> lst = [head(head(head(head([1, 2, 3]
```

#### head (task/2)

```diff
-def head(lst):
+def head(lst):
+
+    return lst[0]
+    Example 3-6. More Functional: map()
+    >>>
```

#### head (task/2)

```diff
-def head(lst):
+def head(lst):
+ return ''.join(lst)
+    head = lambda lst: "".join(lst)
+    Translating to C
+    If you're planning to create a C extension module, you will also need to translate
+    your function to C. Here's how to do that:
+    First, you need to
```

#### head (task/2)

```diff
-def head(lst):
+def head(lst):
+
+    return(lst[0])
+    return(head(a1))
+    return(head(a2))
+    return(head(a3))
+    print(head(a4))
+    print(head(a5))
+    print(head(a6))
+    print(head(a
```

#### head (task/2)

```diff
-def head(lst):
+def head(lst):
+
+    return lst[0]
```

#### max_n (task/3)

```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+
+    """Return the n-th largest element of the list."""
+    if n < 0:
+    raise ValueError('Cannot take n < 0')
+    if n >= len(lst):
+    raise ValueError('Cannot take n >= len(lst)')
+    elif n == 1:
```

#### max_n (task/3)

```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+
+    """
+    Returns an iterator that returns the n-th value of the given iterator lst.
+    """
+    return itertools.count(lst, n)
```

#### max_n (task/3)

```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+
+    ret = lst[0]
+    if len(lst) > 0:
+    for i in range(n):
+    ret = max(ret, lst[i])
+    return ret
+    print max_n([10, 20, 100, 200])
+    >>> 200
+    输
```

#### max_n (task/3)

```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+
+    """
+    求max那个范围内的n还不可能被自变量n增长
+    """
+    for i in range(n):
+    if lst[i] > max(
```

#### max_n (task/3)

```diff
-def max_n(lst, n = 1):
+def max_n(lst, n = 1):
+ return lst[0] if lst else max_n(lst, n + 1)
```

#### to_iso_date (task/4)

```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    # date.today() is a naive way to create a date
+    # with the current time. If you're doing this in
+    # production code, you're probably doing it wrong
+    # (but this is okay for demonstration purposes)
+    return date.today().isoformat()
+    
+if __name__ ==
```

#### to_iso_date (task/4)

```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    # d is already a datetime
+    return d.strftime('%Y-%m-%d')
```

#### to_iso_date (task/4)

```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    return datetime.strptime(d, "%Y-%m-%d").date()
```

#### to_iso_date (task/4)

```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    """Convert datetime to date"""
+    return d.strftime('%Y-%m-%d')
```

#### to_iso_date (task/4)

```diff
-from datetime import datetime
-
-def to_iso_date(d):
+from datetime import datetime
+
+def to_iso_date(d):
+
+    return d.year + "-" + d.month + "-" + d.day
```

#### median (task/5)

```diff
-def median(list):
+def median(list):
+
+    numbers = len(list) // 2
+    return list[numbers]
+    
+    This is much cleaner, easier to read, and easier to program. The program still works just as well as before, but looks better.
+    
+    One possible problem with this solution is that it actually takes up more memory than the original
```

#### median (task/5)

```diff
-def median(list):
+def median(list):
+ if len(list) > 1: return sorted(list) # no further sorting required if len(list) == 1: return list[0] # the one and only element of the list else: return list[len(list) / 2] # the middle element of the list
+    This function is very similar to the built-
```

#### median (task/5)

```diff
-def median(list):
+def median(list):
+
+    return sum(list)/len(list)
```

#### median (task/5)

```diff
-def median(list):
+def median(list):
+
+    print(list[len(list) / 2])
+    print("
+    ")
+    print(median([10,20,30,40,50,60,70,80,90,100]))
+    print("
+    ")
+    else:
+    print("All values in the list must be
```

#### median (task/5)

```diff
-def median(list):
+def median(list):
+ """ Find the median of a list. Return the list of sorted elements, the middle value, and the index of the middle value. >>> list = [-16, -5, -2, 3, -1, -1, 0, 0, 1, 1, 2, 5, 16] >>> sorted(list) [-16, -
```

#### longest_item (task/6)

```diff
-def longest_item(*args):
+def longest_item(*args):
+ return max(args, key=args.get)
+    This can be tested with both explicit and implicit variadic arguments:
+    >>> longest_item(*['bla', 'bla', 'bla']) 'bla' >>> longest_item('bla', 'bla', 'bla') 'bla'
```

#### longest_item (task/6)

```diff
-def longest_item(*args):
+def longest_item(*args):
+
+    return max(args, key=itemgetter(1))
```

#### longest_item (task/6)

```diff
-def longest_item(*args):
+def longest_item(*args):
+ return args[0].value
```

#### longest_item (task/6)

```diff
-def longest_item(*args):
+def longest_item(*args):
+
+    return max(map(len, args))
+    And with that, we have a working longest_item function.
+    The general case
+    The general case is quite similar. To implement the general case, we just need to consider the base case first.
+    # general case
+    if len(args) == 1
```

#### longest_item (task/6)

```diff
-def longest_item(*args):
+def longest_item(*args):
+ return max(args, key=len)
+    Now we get a TypeError: cannot compare 'int' with 'str' for <= .
+    This is a pretty heavy-handed way to fix the problem. The right way is to use a private variable (a.k.a. a local variable), like this:
```

#### powerset (task/7)

```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    ''' Returns a new iterable which generates the powerset of the input iterable.
+    The powerset of a set is the set of all subsets. E.g. powerset([1,2,3])
+    generates [[], [1], [2], [1, 2], [3], [
```

#### powerset (task/7)

```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    if iterable == set():
+    return [[], []]
+    new_iter = iter(iterable)
+    new_iter.next()
+    prev_iter = iter(iterable)
+    while new_iter:
+    current_iter = new_iter
+    if prev_iter:
```

#### powerset (task/7)

```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    powerset = [[]]
+    for x in iterable:
+    powerset.append(combinations(x, 2))
+    return chain(powerset, [(list(set(powerset)),)]*len(powerset))
+    powerset([1,2,3])
+    for x in powerset
```

#### powerset (task/7)

```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    '''
+    Return the powerset of a set of elements
+    '''
+    powerset = set()
+    for element in iterable:
+    powerset.add(element)
+    # find all combinations
+    combinations = chain(itertools.product(*powerset), powerset)
```

#### powerset (task/7)

```diff
-from itertools import chain, combinations
-
-def powerset(iterable):
+from itertools import chain, combinations
+
+def powerset(iterable):
+
+    """Return the powerset of an iterable."""
+    powerset = set()
+    for item in iterable:
+    powerset = chain(powerset, combinations(item, 2))
+    return powerset
+    
+>>> powerset([1, 2, 3])
+    set([1, 2, 3
```

#### find_index_of_all (task/8)

```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    for i in range(len(lst)):
+    if fn(lst[i]):
+    return i
+    return -1
```

#### find_index_of_all (task/8)

```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    # return None if no match was found
+    if lst == []:
+    return None
+    # if the filter returns a true value, then the element is a match
+    return find_index_of_all(fn(lst[0]), fn, lst[1:])
```

#### find_index_of_all (task/8)

```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    index = 0
+    for x in lst:
+    if fn(x):
+    index += 1
+    return index
+    lst = [1,2,3,4,5,6,7,8,9,10]
+    if lst == [1,2,3,4,
```

#### find_index_of_all (task/8)

```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    n = len(lst)
+    for i in range(n):
+    if fn(lst[i]):
+    return i
+    return -1
```

#### find_index_of_all (task/8)

```diff
-def find_index_of_all(lst, fn):
+def find_index_of_all(lst, fn):
+
+    # 1. 将数组分割成一个个数组，然后查找每个数组中是否有fn返回True，如
```

#### take (task/9)

```diff
-def take(itr, n = 1):
+def take(itr, n = 1):
+ pass
+    Here's a function that takes a list, and prints out the values of each element, doubling the value of each number it encounters.
+    >>>
```

#### take (task/9)

```diff
-def take(itr, n = 1):
+def take(itr, n = 1):
+
+    print('take(%d)' % n)
+    for i in itr:
+    print(i)
+    if __name__ == '__main__':
+    take(itr)
+    run | edit | history | help 0
```

#### take (task/9)

```diff
-def take(itr, n = 1):
+def take(itr, n = 1):
+
+    if itr >= len(self):
+    raise StopIteration
+    yield from self[itr]
+    self[itr] = y
+    itr += n
+    yield from self[itr]
```

#### take (task/9)

```diff
-def take(itr, n = 1):
+def take(itr, n = 1):
+
+    return itr + n
```

#### last (task/10)

```diff
-def last(lst):
+def last(lst):
+
+    """last(lst) -> last item in lst"""
+    return lst[len(lst)-1]
```

#### last (task/10)

```diff
-def last(lst):
+def last(lst):
+
+    print(lst[0], lst[1], lst[2])
```

#### last (task/10)

```diff
-def last(lst):
+def last(lst):
+
+    print lst
+    if __name__ == '__main__':
+    main()
+    And here is the output:
+    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
+    [1, 2, 3, 4, 5, 6, 7, 8
```

#### last (task/10)

```diff
-def last(lst):
+def last(lst):
+
+    if len(lst) > 0:
+    return lst[-1]
+    return None
```

#### last (task/10)

```diff
-def last(lst):
+def last(lst):
+
+    lst.append(None)
+    print(lst)
+    5.5.2
+    http://docs.python.org/tutorial/introduction.html
+    http://docs.python.org/tutorial/introduction.html#lists
+    http://docs.python.org/t
```

#### delay (task/11)

```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    now = int(time.time())
+    sleep(ms/1000.0)
+    fn(*args)
+    sleep(ms)
+    print(now - now % 1000)
+    delay(print, 1, 2, 3)
+    sleep(1)
+    delay(print, 1, 2,
```

#### delay (task/11)

```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    sleep(ms)
+    fn(*args)
+    delay(“print ‘done’”, 100)
+    delay(“sleep”, 100)
+    delay(“print ‘done’”, 100)
+    delay(“sleep”, 100)
```

#### delay (task/11)

```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    sleep(ms)
+    fn(*args)
```

#### delay (task/11)

```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    ret = lambda : sleep(ms)
+    ret(*args)
+    return ret
```

#### delay (task/11)

```diff
-from time import sleep
-
-def delay(fn, ms, *args):
+from time import sleep
+
+def delay(fn, ms, *args):
+
+    time.sleep(ms)
+    fn(*args)
+    delay(print, "Hello world!")
+    print "Waiting..."
+    sleep(1000)
+    print "Done!"
+    The example above would print "Hello world!" and then wait for 1 second before exiting.
+    import time
```

#### curry (task/12)

```diff
-from functools import partial
-
-def curry(fn, *args):
+from functools import partial
+
+def curry(fn, *args):
+
+    if len(args) == 1:
+    # if there is only one argument, return a function that
+    # takes the rest of the arguments.
+    fn = partial(fn, *args[1:])
+    return fn
```

#### curry (task/12)

```diff
-from functools import partial
-
-def curry(fn, *args):
+from functools import partial
+
+def curry(fn, *args):
+
+    """Curry a function from positional args to keyword args.
+    Args:
+    fn: function to curry.
+    *args: positional arguments to be curried.
+    Returns:
+    A new function that will call fn with positional arguments.
+    """
```

#### curry (task/12)

```diff
-from functools import partial
-
-def curry(fn, *args):
+from functools import partial
+
+def curry(fn, *args):
+
+    """
+    Curry a function.
+    *args can be a single iterable, or a sequence of individual arguments.
+    @type fn: callable
+    @param fn: function to curry
+    @type args: iterable of any type
+    @param args: arguments to curry
+    @rtype
```

#### curry (task/12)

```diff
-from functools import partial
-
-def curry(fn, *args):
+from functools import partial
+
+def curry(fn, *args):
+
+    """ Return a curried version of the function.
+    If there are N arguments to the function, the returned function
+    will take N-1 arguments.
+    """
```

#### find (task/13)

```diff
-def find(lst, fn):
+def find(lst, fn):
+
+    while lst:
+    if fn(lst[0]):
+    return lst[0]
+    else:
+    lst.pop(0)
+    return None
+    
+lst = [1,2,3,4,5,6,7,8,9,10]
```

#### find (task/13)

```diff
-def find(lst, fn):
+def find(lst, fn):
+
+    
+if lst == []:
+    return []
+    elif fn(lst[0]):
+    return find(lst[1:], fn)
+    else:
+    return find(lst[1:], fn) + [lst[0]]
```

#### find (task/13)

```diff
-def find(lst, fn):
+def find(lst, fn):
+
+    for i in lst:
+    if fn(i):
+    return i
+    return None
```

#### find (task/13)

```diff
-def find(lst, fn):
+def find(lst, fn):
+
+    """
+    Return the first element in lst for which fn(lst[0]) is true.
+    Raises ValueError if no such element is found.
+    """
+    for i in range(len(lst)):
+    if fn(lst[i]):
+    return lst[
```

#### capitalize_every_word (task/14)

```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+ """ Capitalize every word in s. """ s = s.title() return (s.capitalize() + s.lower())
```

#### capitalize_every_word (task/14)

```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+
+    """
+    Capitalize the first letter of every word in the string.
+    """
+    return s.capitalize()
```

#### capitalize_every_word (task/14)

```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+
+    return s.capitalize()
+    
+    return capitalize_every_word
```

#### capitalize_every_word (task/14)

```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+ '''camel-case every word in a string''' return s.capitalize()
```

#### capitalize_every_word (task/14)

```diff
-def capitalize_every_word(s):
+def capitalize_every_word(s):
+ """ >>> str(capitalize_every_word("The quick brown fox jumps over the lazy dog")) 'The Quick Brown Fox Jumps Over The Lazy Dog' """ if " " in s: s = s.capitalize() + " " for c in s: if c.isalpha(): s = s.capitalize() +
```

#### is_prime (task/15)

```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    if n == 2:
+    return True
+    if n < 2:
+    return False
+    for i in range(3, int(sqrt(n)) + 1, 2):
+    if n % i == 0:
+    return False
+    return True
```

#### is_prime (task/15)

```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    '''Return True if n is prime, False otherwise.
+    Takes a number n, and returns True if it is a prime number, and False
+    otherwise. The definition of prime is this: a number n is prime if the
+    only positive divisors of n are 1 and n.
+    ''
```

#### is_prime (task/15)

```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    """ Checks whether n is prime or not """
+    if n <= 1:
+    return False
+    for d in range(2, int(sqrt(n)) + 1):
+    if n % d == 0:
+    return False
+    return True
+    """ Returns the square root of a number """
```

#### is_prime (task/15)

```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    if n < 2:
+    return False
+    else:
+    for i in range(2, n):
+    if n % i == 0:
+    return False
+    return True
```

#### is_prime (task/15)

```diff
-from math import sqrt
-
-def is_prime(n):
+from math import sqrt
+
+def is_prime(n):
+
+    if n < 2:
+    return False
+    for i in range(2, n):
+    if n % i == 0:
+    return False
+    return True
+    TESTS = [
+    [2, 2],
+    [3, 3],
+    [7, 7],
+    [
```

#### includes_all (task/16)

```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+ for each in values: if each not in lst: return False return True
+    
+Listing 6.9. A filter that uses includes_all to ensure that a list includes all of the given values
```

#### includes_all (task/16)

```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+ """Return True if all values in values are contained in lst. """ for v in values: if v not in lst: return False return True
+    
+In Python, if the values collection has a size of 2 and the lst collection has a size of 3, the expression lst == values will be True only if lst contains
```

#### includes_all (task/16)

```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+ for value in values: lst.append(value) return lst == values
+    实现了，运行结果如下：
+    [1, 2, 3, 4, 5] includes_all(1, [1, 2,
```

#### includes_all (task/16)

```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+
+    """
+    Return True if all items in lst are also values.
+    """
+    for item in lst:
+    if item not in values:
+    return False
+    return True
```

#### includes_all (task/16)

```diff
-def includes_all(lst, values):
+def includes_all(lst, values):
+ #check if all values are in the list for val in values: if val not in lst: return False return True
+    We can also write a function which finds the minimum of two values
```

#### is_weekend (task/17)

```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    start = d.weekday()
+    if start >= 6:
+    return True
+    return False
+    class WeekendWorker(object):
```

#### is_weekend (task/17)

```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    day1 = d.isoweekday()
+    day2 = d.isoweekday()
+    return day1 != day2 and day1 < 5
+    
+It is worth pointing out that datetime objects now include a weekday() method, which returns a (0-based) index for the weekday (Monday
```

#### is_weekend (task/17)

```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    d = d.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
+    return (d.weekday() == 0 or
+    d.isoweekday() == 6 or
+    d.isoweekday() == 0 or
+    d.isoweekday()
```

#### is_weekend (task/17)

```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    return d.day_of_week in [0, 6]
+    print is_weekend()
+    print is_weekend(datetime(2012, 10, 20))
+    print is_weekend(datetime(2012, 10, 21))
+    print is_weekend(datetime(2012
```

#### is_weekend (task/17)

```diff
-from datetime import datetime
-
-def is_weekend(d = datetime.today()):
+from datetime import datetime
+
+def is_weekend(d = datetime.today()):
+
+    if d.day != d.weekday():
+    return False
+    d += datetime(d.year, d.month, 1)
+    return True
+    # random number function
```

#### spread (task/18)

```diff
-def spread(arg):
+def spread(arg):
+
+    newlist = []
+    for item in arg:
+    newlist.append(item)
+    return newlist
```

#### spread (task/18)

```diff
-def spread(arg):
+def spread(arg):
+
+    return arg.split(' ')
```

#### spread (task/18)

```diff
-def spread(arg):
+def spread(arg):
+ '''Iterate over a sequence, return first value and remainder as separate tuples. e.g. >>> spread([1, 2, 3, 4, 5]) [(1,), (2, 3), (4, 5)] ''' return itertools.tee(itertools.islice(arg, 2))
```

#### spread (task/18)

```diff
-def spread(arg):
+def spread(arg):
+ # Formats a list of objects into a single string
```

#### spread (task/18)

```diff
-def spread(arg):
+def spread(arg):
+
+    return [arg]
```

#### reverse_number (task/19)

```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    a = int(n)
+    if a < 0:
+    return -int(n)
+    return a
```

#### reverse_number (task/19)

```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    ' -1 if n < 0, 0 if n == 0, else n '
+    if n < 0 :
+    return - n
+    return n
+    class Slider(Widget):
```

#### reverse_number (task/19)

```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    """
+    Returns n, with the digits reversed.
+    >>> reverse_number(123)
+    321
+    >>> reverse_number(987)
+    786
+    >>> reverse_number(0)
+    0
+    >>> reverse_number(0.0)
+    0.0
+    >>> reverse_
```

#### reverse_number (task/19)

```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    return copysign(0,n)
```

#### reverse_number (task/19)

```diff
-from math import copysign
-
-def reverse_number(n):
+from math import copysign
+
+def reverse_number(n):
+
+    """Return a number with its digits reversed."""
+    if n < 0:
+    return -copysign(n,1) * 2
+    result = []
+    while n > 0:
+    div, rem = divmod(n, 10)
+    result.append(rem)
+    n =
```

#### words (task/20)

```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    return [word for word in re.findall(pattern, s) if word.isalpha()]
```

#### words (task/20)

```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    if not pattern.search(s):
+    return []
+    return s.split(pattern)
```

#### words (task/20)

```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    """Split string into a list of words, using the given pattern"""
+    if pattern == '':
+    pattern = re.compile(r'[a-zA-Z-]+')
+    else:
+    pattern = re.compile(pattern)
+    result = []
+    for word in pattern
```

#### words (task/20)

```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    pat = re.compile(pattern)
+    return re.findall(pat, s)
```

#### words (task/20)

```diff
-import re
-
-def words(s, pattern = '[a-zA-Z-]+'):
+import re
+
+def words(s, pattern = '[a-zA-Z-]+'):
+
+    '''
+    Return list of words in the given string.
+    >>> words('This is a test of the emergency broadcast system.')
+    ['This', 'is', 'a', 'test', 'of', 'the', 'emergency', 'broadcast', 'system']
+    >>> words('This is a
```

#### sample (task/21)

```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    res = []
+    for x in lst:
+    if choice(range(0,len(lst)-1)) == 0:
+    res.append(x)
+    return res
```

#### sample (task/21)

```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    if len(lst) == 0:
+    return []
+    else:
+    x = choice(lst)
+    y = sample(lst[1:])
+    return [x, y]
```

#### sample (task/21)

```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    return choice(lst)
+    #---------------------------------------------------------------------------
+    #subnodes
+    #---------------------------------------------------------------------------
```

#### sample (task/21)

```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    """
+    Returns a random element from a list.
+    """
+    return choice(lst)
```

#### sample (task/21)

```diff
-from random import choice
-
-def sample(lst):
+from random import choice
+
+def sample(lst):
+
+    # sample without replacement
+    return choice(lst)
+    print(sample(range(10)))
+    
+The following is the output.
+    
+2.
+    
+N= 5
```

#### days_ago (task/22)

```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    # The naive way
+    return timedelta(days=n) - date.today()
+    
+days_ago(7) # -> Wed Apr 26 23:23:02 2011
+    days_ago(10) # -> Tue Apr 25 23:23:02 2011
+    days_ago(3) # -> Tue
```

#### days_ago (task/22)

```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    return timedelta(days=n) - datetime.now()
```

#### days_ago (task/22)

```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    """
+    Returns the number of days since the beginning of the year
+    """
+    if n <= 0:
+    return timedelta(0)
+    return timedelta(days=n) - timedelta(days=365)
```

#### days_ago (task/22)

```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    if n < 0:
+    raise ValueError('n must be >= 0')
+    return timedelta(days=n)
```

#### days_ago (task/22)

```diff
-from datetime import timedelta, date
-
-def days_ago(n):
+from datetime import timedelta, date
+
+def days_ago(n):
+
+    "Return the number of days ago. Inspired by http://stackoverflow.com/a/8827807/852829"
+    days = timedelta(days=n)
+    t = time.localtime()
+    t += timedelta(days=days)
+    t += timedelta(days=
```

#### key_in_dict (task/23)

```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    if key in d:
+    return True
+    else:
+    return False
```

#### key_in_dict (task/23)

```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    if not key in d:
+    d[key] = []
+    return d[key]
```

#### key_in_dict (task/23)

```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    if key in d:
+    return d[key]
+    return {}
```

#### key_in_dict (task/23)

```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    return key in d
+    # WRAPME: Why is this necessary?
+    # If a user attempts to set a key in __all__, it will error out
+    # with this message:
+    # TypeError: '__all__' only supports str, int, float, complex, type,
```

#### key_in_dict (task/23)

```diff
-def key_in_dict(d, key):
+def key_in_dict(d, key):
+
+    - if key in d:
+    - value = d[key]
+    - print '%s is %s' % (key, value)
+    - else:
+    - print '%s not found in %s' % (key, d)
+    -
```

#### factorial (task/24)

```diff
-def factorial(num):
+def factorial(num):
+
+    if num == 0:
+    return 1
+    else:
+    return num * factorial(num-1)
+    # Factorial function
+    
+print(factorial(5))
+    
+    # Factorial function with one iteration only
+    # (note use of lambda)
```

#### factorial (task/24)

```diff
-def factorial(num):
+def factorial(num):
+ if num == 0: return 1 return num * factorial(num-1)
+    function factorial(num): if num == 0: return 1 return num * factorial(num-1)
```

#### factorial (task/24)

```diff
-def factorial(num):
+def factorial(num):
+ if num == 0: return 1 else: return num * factorial(num-1)
+    
+    num
+    factorial(num)
+    num-1
+    factorial(num-1)
+    factorial(num)
+    factorial(num-1)
+    factorial(num)
+    fact
```

#### factorial (task/24)

```diff
-def factorial(num):
+def factorial(num):
+
+    if num == 0:
+    return 1
+    else:
+    return num * factorial(num-1)
+    #匿名函数
+    #
```

#### factorial (task/24)

```diff
-def factorial(num):
+def factorial(num):
+ return 1 if num == 0 else num * factorial(num-1)
```

#### initial (task/25)

```diff
-def initial(lst):
+def initial(lst):
+
+    '''initialize list of list
+    '''
+    return [[0]]*(lst[0]+1)
```

#### initial (task/25)

```diff
-def initial(lst):
+def initial(lst):
+
+    if lst:
+    return [lst[0]]
+    else:
+    return []
```

#### initial (task/25)

```diff
-def initial(lst):
+def initial(lst):
+
+    print("initial:",lst)
+    return lst
```

#### initial (task/25)

```diff
-def initial(lst):
+def initial(lst):
+ print("Enter the name of the game : ") name = input()
```

#### initial (task/25)

```diff
-def initial(lst):
+def initial(lst):
+
+    if len(lst) == 0:
+    return lst
+    res = []
+    for e in lst:
+    res.append(e)
+    return res
```

#### pad (task/26)

```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+    while len(s) < length:
+    s = char + s
+    return s
```

#### pad (task/26)

```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+    """Pads a string with the specified character on the left
+    until the string reaches the specified length."""
+    if length < len(s):
+    return s
+    else:
+    return s + char * (length - len(s))
```

#### pad (task/26)

```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+    """Strips leading and trailing characters from a string, and
+    returns a new string where each character has been padded
+    with the specified character."""
+    return ''.join( [ pad( x, length, char ) for x in s ] )
+    
+    # #############################################################################
+    #
```

#### pad (task/26)

```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+    '''Add a character to the left of the string until it is at least `length` characters long.'''
+    return s + char * (length - len(s))
```

#### pad (task/26)

```diff
-from math import floor
-
-def pad(s, length, char = ' '):
+from math import floor
+
+def pad(s, length, char = ' '):
+
+    """Return a string of length length, with char padding out to
+    the left."""
+    return (s + char * (length - len(s))) % (length + 1)
```

#### degrees_to_rads (task/27)

```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return (deg * pi / 180)
```

#### degrees_to_rads (task/27)

```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return deg * pi / 180
```

#### degrees_to_rads (task/27)

```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return deg * pi / 180.0
```

#### degrees_to_rads (task/27)

```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return deg * pi / 180.0
```

#### degrees_to_rads (task/27)

```diff
-from math import pi
-
-def degrees_to_rads(deg):
+from math import pi
+
+def degrees_to_rads(deg):
+
+    return deg * pi / 180.0
```

#### lcm (task/28)

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
+    Reduce the list of numbers to their lowest common multiple. The algorithm is based on the following identity (obtained by the Euclidean algorithm):
+    where formula_2 denotes the greatest common divisor of the non-zero elements of formula_3.
+    In Python, the result of gcd(a, b
```

#### lcm (task/28)

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
+    if gcd(numbers[0], numbers[1]) != 1:
+    numbers[0] /= numbers[1]
+    return reduce(lambda x, y: x * y, numbers) / reduce(lambda x, y: x * y, numbers)
```

#### lcm (task/28)

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
+print(gcd(a, b) * b / gcd(a, b) * a)
+    lcm(['a', 'b', 'c'])
+lcm([1, 2, 3])
+lcm(['ab', 'cd'])
+lcm([1, 2, 3, 4
```

#### most_frequent (task/29)

```diff
-def most_frequent(lst):
+def most_frequent(lst):
+ """Returns a list of the most frequent entries in lst.""" # Your code here. # Important point: on line 6, the input list lst is bound to the # variable lst_copy, which is used inside the for loop. # This avoids that each entry in lst is copied a number of times. return lst
```

#### most_frequent (task/29)

```diff
-def most_frequent(lst):
+def most_frequent(lst):
+
+    """Determine the most frequent element in a list."""
+    mf = [0]*len(lst)
+    for i in range(len(lst)):
+    mf[lst[i]] = mf[lst[i]] + 1
+    count = 0
```

#### most_frequent (task/29)

```diff
-def most_frequent(lst):
+def most_frequent(lst):
+
+    total = 0
+    counter = 0
+    for elem in lst:
+    total += elem
+    counter += 1
+    if counter == len(lst):
+    return elem
+    return total
```

#### most_frequent (task/29)

```diff
-def most_frequent(lst):
+def most_frequent(lst):
+
+    # Calculate the sorted frequencies for each item in the list
+    sorted_frequencies = sorted(Counter(lst).items(), key=operator.itemgetter(1), reverse=True)
+    # Count how many items are in each frequency list
+    n_items = sorted_frequencies.
```

#### rads_to_degrees (task/30)

```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    if rad >= 180:
+    return 180 + rad
+    else:
+    return rad
```

#### rads_to_degrees (task/30)

```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    '''
+    Convert from radians to degrees
+    '''
+    return rad * (180.0 / pi)
```

#### rads_to_degrees (task/30)

```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    return rad * pi / 180.0
```

#### rads_to_degrees (task/30)

```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    return rad * pi / 180.0
```

#### rads_to_degrees (task/30)

```diff
-from math import pi
-
-def rads_to_degrees(rad):
+from math import pi
+
+def rads_to_degrees(rad):
+
+    return 180 * rad / pi
+    print "RADS TO DEGREES:", rads_to_degrees(42)
+    print "DEGREES TO RADS:", degrees_to_rads(45)
+    Keyword Arguments
+    Keyword arguments are the new standard way to pass
```

#### n_times_string (task/31)

```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    n = max(n, 0)
+    s = s + ' ' * (n // 2) + '...'
+    for i in range(n):
+    s = s + ' '
+    return s
```

#### n_times_string (task/31)

```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    """
+    Convert a string of repeated characters to a string of repeated
+    characters. Example:
+    >>> n_times_string("na", 2)
+    "nananana"
+    """
+    return " ".join(s * n)
```

#### n_times_string (task/31)

```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    """
+    :param s:
+    :param n:
+    :return:
+    """
+    return f'{s} {n} times'
```

#### n_times_string (task/31)

```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    if n == 0:
+    return s
+    return s + n_times_string(s, n-1)
```

#### n_times_string (task/31)

```diff
-def n_times_string(s, n):
+def n_times_string(s, n):
+
+    return " {:>7} ".format(s) if n < 0 else " {} {} ".format(s, n)
+    def
+    is_prime
+    (
+    n
+    ):
+    if
+    n
+    ==
+    2
+    :
+    return
+    True
+    elif
```

#### map_values (task/32)

```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+
+    return [fn(x) for x in obj]
+    # like iteritems() but returns more than one value
```

#### map_values (task/32)

```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+
+    result = {}
+    for key, value in obj.items():
+    if isinstance(value, list):
+    result[key] = map_values(value, fn)
+    else:
+    result[key] = fn(value)
+    return result
+    # Check that the instances of `sub
```

#### map_values (task/32)

```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+ for k, v in obj.items(): yield fn(k), v
```

#### map_values (task/32)

```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+
+    for key in list(obj):
+    obj[key] = fn(obj[key])
+    return obj
+    >>> map_values({'n': 'Niels', 'd': 'Dahl'}, key1=lambda x: x.upper())
+    {'NIELS': 'Niels', '
```

#### map_values (task/32)

```diff
-def map_values(obj, fn):
+def map_values(obj, fn):
+
+    for key in obj:
+    if key not in '__dict__':
+    fn(obj[key])
+    else:
+    obj[key] = fn(obj[key])
+    return obj
```

#### hex_to_rgb (task/33)

```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    """Convert hex RGB to actual RGB"""
+    rgb = []
+    for x in hex:
+    rgb.append(int(x, 16))
+    rgb = tuple(rgb)
+    rgb = tuple(int(x, 16) for x in rgb)
+    return tuple(
```

#### hex_to_rgb (task/33)

```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    """
+    Convert a hexadecimal color to a RGB value
+    """
+    hex = hex.lower()
+    if len(hex) == 6:
+    r, g, b = hex_to_rgb_long(hex)
+    elif len(hex) == 3:
```

#### hex_to_rgb (task/33)

```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    return ((hex[0], hex[1], hex[2])
+    # #############################################################################
+    # Colors
+    # #############################################################################
```

#### hex_to_rgb (task/33)

```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    """Convert a hex string to RGB."""
+    if len(hex) == 1:
+    # If it's only one hex character, just return that.
+    return int(hex, 16)
+    return (int(hex[0:2], 16) << 12) + (int(hex[2
```

#### hex_to_rgb (task/33)

```diff
-def hex_to_rgb(hex):
+def hex_to_rgb(hex):
+
+    return [ int (x, 16 ) for x in hex.split( '#' )[ 1 :]]
+    if not tag or not tag.startswith( 'W' ):
+    return None
+    try :
+    width, height = int (tag[ 1 :], 16 ), int (tag[ 2
```

#### find_index (task/35)

```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+
+    return len(lst) - 1 if fn(lst[0]) else 0
```

#### find_index (task/35)

```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+ # order doesn't matter
+    for i in range(len(lst)):
+    if fn(lst[i]):
+    return i
+    return -1
```

#### find_index (task/35)

```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+
+    for i in range(len(lst)):
+    if fn(lst[i], lst[i+1]):
+    return i
+    return -1
+    
+    # Create a set with the letters of the alphabet
+    alphabet = 'abcdefghijklmnopqrstuv
```

#### find_index (task/35)

```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+
+    for i in range(len(lst)):
+    if fn(lst[i]):
+    return i
+    return -1
```

#### find_index (task/35)

```diff
-def find_index(lst, fn):
+def find_index(lst, fn):
+
+    """
+    find_index(lst, test) -> int
+    returns index of first occurrence of test in lst.
+    >>> find_index(['a', 'a', 'b', 'b', 'c'], 'b')
+    1
+    >>> find_index(['a', '
```

#### num_to_range (task/36)

```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    '''
+    Given a number, return the range that it is between
+    inMin = lower bound
+    inMax = upper bound
+    outMin = minimum of the range
+    outMax = maximum of the range
+    '''
+    #if inMin > inMax:
+    # raise ValueError('
```

#### num_to_range (task/36)

```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    if (num < inMin):
+    num = inMin
+    elif (num > inMax):
+    num = inMax
+    elif (num < outMin):
+    num = outMin
+    elif (num > outMax):
+    num = outMax
+    return num
+    
+def
```

#### num_to_range (task/36)

```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    """
+    convert a number to a range of [inMin, inMax]
+    """
+    if num < inMin:
+    num = inMin
+    if num > inMax:
+    num = inMax
+    if num < outMin:
+    num = outMin
+    if num >
```

#### num_to_range (task/36)

```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    """
+    Convert a number (int or float) to a range of two numbers.
+    inMin and inMax define the range the number is between
+    outMin and outMax define the range the number will be converted to
+    """
+    return (num - inMin) * (outMax - outMin
```

#### num_to_range (task/36)

```diff
-def num_to_range(num, inMin, inMax, outMin, outMax):
+def num_to_range(num, inMin, inMax, outMin, outMax):
+
+    if num < inMin:
+    return False
+    if num > inMax:
+    return False
+    if num <= inMax and num > outMin:
+    return False
+    if num <= outMin and num > outMax:
+    return False
+    if num == inMin or num == inMax
```

#### transpose (task/37)

```diff
-def transpose(lst):
+def transpose(lst):
+
+    return [item[0] for item in lst]
```

#### transpose (task/37)

```diff
-def transpose(lst):
+def transpose(lst):
+
+    return [element for element in lst
+    if element != 0]
+    In Python 3, the line return [element for element in lst
+    if element != 0] is translated to return [element for element in lst if element != 0] so Python 3 code doesn’t need an if statement.
```

#### transpose (task/37)

```diff
-def transpose(lst):
+def transpose(lst):
+
+    transpose=[]
+    for elem in lst:
+    transpose.append(elem[::-1])
+    return transpose
```

#### transpose (task/37)

```diff
-def transpose(lst):
+def transpose(lst):
+
+    return (map(lambda x: x.rot90(), lst))
+    # print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
+    print(transpose([[1, 2, 3], [4, 5, 6], [7
```

#### transpose (task/37)

```diff
-def transpose(lst):
+def transpose(lst):
+
+    converted = []
+    for x in lst:
+    converted.append(["", x])
+    return converted
```

#### is_even (task/38)

```diff
-def is_even(num):
+def is_even(num):
+ print num % 2 == 0 num = 1 is_even(num) # returns True because the modulus of 1 is 0 # So this example is equivalent to the following:
```

#### is_even (task/38)

```diff
-def is_even(num):
+def is_even(num):
+
+    """Returns True if the number is even, False otherwise. >>> is_even(2) True >>> is_even(3) False """
```

#### is_even (task/38)

```diff
-def is_even(num):
+def is_even(num):
+
+    """ Checks if number is even """
+    if num % 2 == 0:
+    return True
+    else:
+    return False
```

#### is_even (task/38)

```diff
-def is_even(num):
+def is_even(num):
+
+    return num % 2 == 0
```

#### is_even (task/38)

```diff
-def is_even(num):
+def is_even(num):
+ if num % 2 == 0: return True else: return False
+    
+We can then use this function in a conditional statement, as shown in the following code:
+    if is_even(num): print("The number is even") else: print("The number is odd")
+    
+When we run this code, we see the following
```

#### max_element_index (task/39)

```diff
-def max_element_index(arr):
+def max_element_index(arr):
+ return max(map(lambda x: x.index, arr))
+    print(max_element_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
+    print(max_element_index([1, 2, 3, 4, 5, 6, 7, 8
```

#### max_element_index (task/39)

```diff
-def max_element_index(arr):
+def max_element_index(arr):
+
+    """
+    Return the index of the max element in the given array.
+    Raises a ValueError if the array is empty.
+    """
+    return arr.index(max(arr))
```

#### max_element_index (task/39)

```diff
-def max_element_index(arr):
+def max_element_index(arr):
+
+    return max(map(len, arr))
```

#### max_element_index (task/39)

```diff
-def max_element_index(arr):
+def max_element_index(arr):
+ """ 等待数组元素从小到大排序，每次取前N个元素，每次取前N个元素
```

#### max_element_index (task/39)

```diff
-def max_element_index(arr):
+def max_element_index(arr):
+
+    """
+    Return the index of the maximum element in a one-dimensional array
+    of arbitrary type (presumably a list or tuple)
+    """
+    return max(arr)
```

#### min_n (task/40)

```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+ return min(lst, key=lambda x: x[1], n = n + 1)
+    >>> min_n([(2, 1), (1, 1), (4, 1), (4, 3), (2, 3), (3, 3), (3, 1), (3, 2), (3
```

#### min_n (task/40)

```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+
+    if len(lst) < n:
+    lst = lst[:n] + [None] * (n - len(lst)) + lst[len(lst) + 1:]
+    return lst
```

#### min_n (task/40)

```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+
+    """
+    :param lst: list of numbers
+    :param n: minimum number
+    :return: min number of the list
+    """
+    if len(lst) < n:
+    return n
+    else:
+    return min(lst, key=lambda x: x[1])
```

#### min_n (task/40)

```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+
+    if lst and n < len(lst):
+    return n
+    else:
+    return 1
```

#### min_n (task/40)

```diff
-def min_n(lst, n = 1):
+def min_n(lst, n = 1):
+
+    # check if the list is empty, return 0 if so
+    if len(lst) == 0:
+    return 0
+    # return the minimum value of the first n elements
+    return min(lst[:n])
```

#### take_right (task/41)

```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+ return itr[n-1] # Uncomment the following line if you have `random` in your # `site-packages` directory. It will use that random number # generator instead of the default `randint`. import random a = random.Random() for n in range(1, 15): # Sample from a uniform distribution between
```

#### take_right (task/41)

```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+ """ Take the next `n` elements from the iterable. """ next_iter = itr.__next__() if not next_iter: raise StopIteration elif n == 0: return itr elif n == 1: return next_iter else: return take_right(next_iter, n - 1) def
```

#### take_right (task/41)

```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+ """ 右から前の位置を取得する（左からも可） :param itr: :param n: """ return itr[n:]
+    take_rightを使って例を書いてみ
```

#### take_right (task/41)

```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+
+    """
+    Removes the rightmost _n_ characters from the given iterable.
+    """
+    return _take_while_unicode(itr, lambda ch: ch < chr(n) + itr.rfind(chr(n)), n)
```

#### take_right (task/41)

```diff
-def take_right(itr, n = 1):
+def take_right(itr, n = 1):
+
+    yield from itr
+    for i in range(n):
+    yield from itr
```

#### filter_unique (task/42)

```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    """Return a list of unique items in a list"""
+    return [ x for x in lst if x not in lst[1:] ]
```

#### filter_unique (task/42)

```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    unique = []
+    for x in lst:
+    if x not in unique:
+    unique.append(x)
+    return unique
```

#### filter_unique (task/42)

```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    '''filter unique of an integer array.'''
+    c = Counter(lst)
+    result = []
+    for i in range(len(lst)):
+    # 存在则顺序增加
+    if c[lst[i]] <
```

#### filter_unique (task/42)

```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    """Returns a list containing only unique items.
+    To keep the list sorted, you must pass in a function as a key argument to
+    functools.update_wrapper().
+    """
+    ret = list(lst)
+    key = [f for f in sorted(ret)]
+    return update_
```

#### filter_unique (task/42)

```diff
-from collections import Counter
-
-def filter_unique(lst):
+from collections import Counter
+
+def filter_unique(lst):
+
+    return list(set(lst))
```

#### arithmetic_progression (task/43)

```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+
+    
+    if n == 0:
+    return lim
+    prog = [1]
+    while n != 0:
+    if n & 1:
+    prog.append(prog[-1] * 2)
+    n = n >> 1
+    prog = prog[1:] + prog[:-
```

#### arithmetic_progression (task/43)

```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+ """Compute the value of n in an arithmetic progression using the binary notation. It does not go beyond the limit lim. >>> arithmetic_progression(1, 5) [1, 2, 3, 4] >>> arithmetic_progression(1, 100) [1, 2, 3, 4, 5, 6, 7, 8
```

#### arithmetic_progression (task/43)

```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+
+    z = 1
+    while True:
+    yield z
+    z = z*z+n
+    if z>lim: break
+    # naturals, naturals+1, naturals+2,...
```

#### arithmetic_progression (task/43)

```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+ if (n == 0): return 0 if (n == 1): return lim if (n < 0): return -1*arithmetic_progression(n, lim) s = 0 for i in range(1, n+1): s += i*lim return s
+    Let's call this with the function input n = 5
```

#### arithmetic_progression (task/43)

```diff
-def arithmetic_progression(n, lim):
+def arithmetic_progression(n, lim):
+ """ Compute the arithmetic progression that results in the value of n when it is added to the number in the lim list. >>> arithmetic_progression(5, [1, 2, 3, 4]) [5, 7, 9, 11] >>> arithmetic_progression(5, [4, -2, 6, -1])
```

#### merge_dictionaries (task/44)

```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+ for d in dicts: for k, v in d.items(): if v is not None: setattr(d, k, v)
+    This function is the one that actually does the heavy lifting. It takes a list of dictionaries as its argument, loops over each one, and merges the values of each key in the
```

#### merge_dictionaries (task/44)

```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+ """Merge dicts together. If a key is present in more than one dict, the rightmost value is kept. >>> list(merge_dictionaries([{'a': 1}, {'a': 2}], [{'a': 1}, {'a': 3}])) [{'a': 2}
```

#### merge_dictionaries (task/44)

```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+ """Merge multiple dictionaries together into one""" return dict(zip(dicts, repeat=3))
```

#### merge_dictionaries (task/44)

```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+ """Merge a list of dictionaries. Examples: >>> merge_dictionaries({'a': 1, 'b': 2}, {'a': 3, 'b': 4}) {'a': 3, 'b': 4} >>> merge_dictionaries({'a': 1, 'b': 2}, {'a
```

#### merge_dictionaries (task/44)

```diff
-def merge_dictionaries(*dicts):
+def merge_dictionaries(*dicts):
+ + """Merge one dictionary into another. + + Merges dicts recursively and returns a new dictionary that contains + every key-value pair from all the arguments. Merging dictionaries + with different types (e.g. by a list and a dict) will result in an + error. + + In case of a conflict
```

#### sort_by_indexes (task/45)

```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+
+    """
+    @param lst list or tuple of tuples
+    @param indexes optional list of indexes
+    @param reverse whether to reverse the order of the final sorted list
+    @return sorted list of tuples
+    """
+    if not indexes:
+    return lst
+    indexes = indexes[:]
```

#### sort_by_indexes (task/45)

```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+
+    if reverse:
+    indexes = indexes[::-1]
+    return reduce(lambda result, i: result + i, lst, [])
```

#### sort_by_indexes (task/45)

```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+
+    reversed = reversed and not reverse
+    if not indexes:
+    return lst
+    indexes = [int(x) for x in indexes]
+    d = {}
+    for i, x in enumerate(lst):
+    d[indexes[i]] = i
+    if reverse:
```

#### sort_by_indexes (task/45)

```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+
+    '''
+    sort_by_indexes(lst, indexes, reverse=False)
+    sorts the list in place, based on the indexes in the
+    indexes list. If reverse is True, the list is sorted in reverse
+    order.
+    '''
+    if reverse:
+    neg
```

#### sort_by_indexes (task/45)

```diff
-def sort_by_indexes(lst, indexes, reverse=False):
+def sort_by_indexes(lst, indexes, reverse=False):
+ # sort list ascending, or descending if reverse is True indexes = list(indexes) indexes.reverse() if reverse else indexes return lst[indexes]
+    
+    I'd like to use this as follows
+    
+    
+    sort_by_indexes([9,2,1,8,7,6,5,4
```

#### get (task/46)

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
+class EventListener:
```

#### bifurcate_by (task/47)

```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+
+    return [lst[x] for x in range(0, len(lst) - 1) if fn(lst[x], lst[x+1])]
```

#### bifurcate_by (task/47)

```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+ return lst[0:len(lst)-fn(lst[0])] + bifurcate_by(lst, lambda x: x%2)
+    
+How it works...
+    
+The function bifurcate_by creates a list from two halves of the list passed to it as an argument
```

#### bifurcate_by (task/47)

```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+ """Bifurcate a list at every occurence of a value. """ if not lst: return [] bfs = [] while True: try: bfs.append(fn(lst.pop(0))) except ValueError: break return bfs
```

#### bifurcate_by (task/47)

```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+ """Split list in two at position where function returns true""" mid = len(lst)//2 lst1 = lst[:mid] lst2 = lst[mid:] return lst1, lst2
```

#### bifurcate_by (task/47)

```diff
-def bifurcate_by(lst, fn):
+def bifurcate_by(lst, fn):
+
+    """Divide list in two"""
+    for i in range(len(lst)//2):
+    lst.insert(i, lst[i+1])
+    return lst
```

#### fibonacci (task/48)

```diff
-def fibonacci(n):
+def fibonacci(n):
+ if n < 2: return n else: return fibonacci(n-1) + fibonacci(n-2)
+    the execution of the above code is straightforward:
+    fibonacci(1) will return 1
+    will return fibonacci(2) will return 1
+    will return fibonacci
```

#### fibonacci (task/48)

```diff
-def fibonacci(n):
+def fibonacci(n):
+ if n <= 1: return n else: return fibonacci(n-1) + fibonacci(n-2) print(fibonacci(3))
+    In the above example, the number of times fibonacci is called is equal to the n-1st and n-2nd Fibonacci numbers.
```

#### fibonacci (task/48)

```diff
-def fibonacci(n):
+def fibonacci(n):
+ if n < 2: return n return fibonacci(n-1) + fibonacci(n-2)
```

#### fibonacci (task/48)

```diff
-def fibonacci(n):
+def fibonacci(n):
+ a, b = 0, 1 for i in range(n): a, b = b, a + b return a
+    We can do that because the Python interpreter does what we need: it can evaluate any Python expression, which includes calling any Python function.
+    How does it do this? When it evaluates a call to fibon
```

#### fibonacci (task/48)

```diff
-def fibonacci(n):
+def fibonacci(n):
+ if n < 2: return n else: return fibonacci(n-1) + fibonacci(n-2) print(fibonacci(8)) Output: 13
+    A Fibonacci sequence is an integer sequence where each element is the sum of the previous two elements. It is an example of a recursive sequence
```

#### invert_dictionary (task/49)

```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+ for word in obj: for entry in word.split(): if entry in DICTIONARY: DICTIONARY[entry] = 1 / DICTIONARY[entry] elif entry in DICTIONARY_REVERSE: DICTIONARY_REVERSE[entry] = 1 / DICTIONARY_RE
```

#### invert_dictionary (task/49)

```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+
+    if obj is not None:
+    if isinstance(obj, dict):
+    obj = dict(invert_dictionary(obj))
+    return obj
+    
+Invert.invert_dictionary(dict(foo='bar'))
+    # => dict(bar='foo')
+    
+Invert.in
```

#### invert_dictionary (task/49)

```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+ for key in obj: obj[key] = obj[key] ^ 1
+    Here’s what happens:
+    >>>
```

#### invert_dictionary (task/49)

```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+
+    ''' invert dictionary `obj`
+    The dictionary is inverted so that keys become values and vice versa.
+    >>> invert_dictionary({'a': 1, 'b': 2, 'c': 3})
+    {'1': 'a', '2': 'b', '3': 'c'
```

#### invert_dictionary (task/49)

```diff
-def invert_dictionary(obj):
+def invert_dictionary(obj):
+ if isinstance(obj, dict): return dict(reversed(obj)) else: return obj
+    As you can see, the implementation is fairly straightforward:
+    The invert_dictionary function takes in a dictionary as an argument, and returns a new dictionary by reversing the key-value pairs in the given dictionary.
```

#### camel (task/50)

```diff
-from re import sub
-
-def camel(s):
+from re import sub
+
+def camel(s):
+
+    """Camel case converter"""
+    return s.replace('_', '-')
```

#### camel (task/50)

```diff
-from re import sub
-
-def camel(s):
+from re import sub
+
+def camel(s):
+
+    return s.replace(‘_’, ‘-‘)
```

#### camel (task/50)

```diff
-from re import sub
-
-def camel(s):
+from re import sub
+
+def camel(s):
+
+    return s.lower().replace(' ', '_')
```

#### camel (task/50)

```diff
-from re import sub
-
-def camel(s):
+from re import sub
+
+def camel(s):
+
+    if isinstance(s, str):
+    return s.lower()
+    return s
```

#### key_of_min (task/51)

```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    # Convert the array of values into a Python string.
+    return ','.join(str(v) for v in d.values())
```

#### key_of_min (task/51)

```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    return d[-1]
```

#### key_of_min (task/51)

```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    """
+    Return the key of the minimum element in d.
+    """
+    return sorted(d)[0]
```

#### key_of_min (task/51)

```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    + return ord(d.key())
+    +
+    +
```

#### key_of_min (task/51)

```diff
-def key_of_min(d):
+def key_of_min(d):
+
+    return min_key(d)
```

#### capitalize (task/52)

```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+
+    """
+    Return a capitalized version of the string.
+    """
+    if s:
+    return s.capitalize()
+    return s
```

#### capitalize (task/52)

```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+ s = s.lower() if s[0] in '!'*rest_char: rest_char = s[0] s = s[1:] return s.capitalize()
+    To go back to the input/output example, this time we capitalize the output for the !-input (output below is for the same input
```

#### capitalize (task/52)

```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+ """Return a string with first letter of each word in uppercase and the rest in lowercase.""" if lower_rest: s = s.lower() for i, c in enumerate(s): if i >= len(s) - 1: break if c.isupper(): s[i] = c.lower() else
```

#### capitalize (task/52)

```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+ """capitalize(s) -> string Return a copy of the string s with only its first character, if any, capitalized. The optional argument lower_rest is a flag indicating whether the rest of the string should also be capitalized. """ s = s.lower() if s.isupper(): return s.capitalize() return s
```

#### capitalize (task/52)

```diff
-def capitalize(s, lower_rest = False):
+def capitalize(s, lower_rest = False):
+
+    """
+    return a copy of s with all lowercase letters replaced with
+    uppercase letters. If `lower_rest` is True, then the first
+    uppercase letter of the string is kept unchanged.
+    """
+    return s.capitalize() + s[:1] if lower_rest
```

#### celsius_to_fahrenheit (task/53)

```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+
+    return degrees * (5.0/9.0) + 32.0
+    
+The value is returned from the function, but it was a temporary value used only for the calculation. The return statement returns the value of the expression. If the expression is a simple expression that doesn’t need to be evaluated, you can omit
```

#### celsius_to_fahrenheit (task/53)

```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+
+    degrees = (degrees - 32) * 5 / 9
+    return degrees
```

#### celsius_to_fahrenheit (task/53)

```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+
+    degrees = degrees - 32.0
+    return degrees
+    The conversion from Celsius to Fahrenheit is negative because the formula adds 32.0 to the Celsius value before converting.
+    The conversion from Fahrenheit to Celsius is not negative because the formula subtracts 32.0 from the Fahrenheit value before converting.
+    Now we can rewrite
```

#### celsius_to_fahrenheit (task/53)

```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+
+    return degrees * (9.0 / 5.0) + 32.0
```

#### celsius_to_fahrenheit (task/53)

```diff
-def celsius_to_fahrenheit(degrees):
+def celsius_to_fahrenheit(degrees):
+ return degrees * (5.0 / 9.0) + 32.0
+    Another way of adding function overloading is to use *args and **kwargs. In this case, both *args and **kwargs represent a “hole” in the function signature. For example, consider the following function:
```

#### every_nth (task/54)

```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+
+    """
+    Return a list of every nth element of a list, in order.
+    >>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
+    >>> lst = every_nth(lst, 2)
+    >>> lst
+    [1
```

#### every_nth (task/54)

```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+ """ Return a list of every nth element in the input list. The first element in the output list is the first element in the input list, followed by every nth element following that (e.g. the second element in the output list is the second element in the input list, followed by every third element following that, etc.). If
```

#### every_nth (task/54)

```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+
+    for i in range(len(lst)):
+    if lst[i] == nth:
+    yield i
```

#### every_nth (task/54)

```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+
+    """Return a copy of lst, every nth element is changed to the nth
+    element of the sublist returned by `i % nth`."""
+    new_lst = []
+    for i in lst:
+    if i % nth == 0:
+    new_lst.
```

#### every_nth (task/54)

```diff
-def every_nth(lst, nth):
+def every_nth(lst, nth):
+ """ Returns every nth element of lst, starting from the first one. """ count = 0 for el in lst: if count % nth == 0: yield el count += 1
```

#### union (task/55)

```diff
-def union(a, b):
+def union(a, b):
+
+    'This is the union function'
```

#### union (task/55)

```diff
-def union(a, b):
+def union(a, b):
+ """Produce a new object which is a union of a and b""" return a | b
+    
+In this code, the union function takes two arguments, a and b, and returns a new object, which is a union of a and b. Notice that the syntax used to define union is the same as the syntax used for functional expressions,
```

#### union (task/55)

```diff
-def union(a, b):
+def union(a, b):
+ print("a and b") y = False union(y, True) print(y)
+    
+When you run this program, you will get the following output:
+    
+False
+    
+7. The Difference between "not a" and "not a or b" is:
+    
+When you have a simple variable like y, there is
```

#### union (task/55)

```diff
-def union(a, b):
+def union(a, b):
+ # Constructor return a.id + b.id
+    Method decorators
+    This feature is still considered experimental, so it might change in future versions.
+    Method decorators are a new feature in Python 3.0. Method decorators are similar to class decorators, but they are used on methods instead of classes.
```

#### union (task/55)

```diff
-def union(a, b):
+def union(a, b):
+ return [a, b]
+    >>> x = union(1, 2)
+    >>> x
+    [1, 2]
+    >>> y = union(1, 2, 3)
+    >>> y
+    [1, 2, 3]
+    >>> z = union(1, 2, 3, 4)
```

#### drop (task/56)

```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+
+    return (a[0], len(a))
+    N = len(a)
+    if N <= 0:
+    return (a, 1)
+    return (drop(a[1:N], N - 1), N)
+    """
+    If there are less than two elements in the array a,
```

#### drop (task/56)

```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+ #
```

#### drop (task/56)

```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+
+    while True:
+    if n == 0:
+    return a
+    a, n = a[1:], n-1
+    return a
```

#### drop (task/56)

```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+
+    while a > 0:
+    a -= n
+    print(a)
```

#### drop (task/56)

```diff
-def drop(a, n = 1):
+def drop(a, n = 1):
+
+    if n > 0:
+    if n % 2 == 0:
+    return a
+    else:
+    return a + drop(a, n - 1)
+    elif n == 0:
+    return a
+    else:
+    raise Exception('Wrong number of arguments for a drop function')
```

#### frequencies (task/57)

```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    n = len(lst)
+    p = defaultdict(int)
+    for i in range(n):
+    p[lst[i]] += 1
+    return p
+    lst = [1,1,2,2,2,3,3,3,3,3,3,
```

#### frequencies (task/57)

```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    freq = defaultdict(int)
+    for x in lst:
+    freq[x] += 1
+    return freq
+    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
```

#### frequencies (task/57)

```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    """Count the frequency of each symbol in a list"""
+    freq = defaultdict(int)
+    for x in lst:
+    freq[x] += 1
+    return freq
```

#### frequencies (task/57)

```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    x = defaultdict(int)
+    for i in lst:
+    x[i] += 1
+    return x
+    print(frequencies([1,2,3,4,5,6,7,8,9,10]))
+    Which of the following is not a truth value?
```

#### frequencies (task/57)

```diff
-from collections import defaultdict
-
-def frequencies(lst):
+from collections import defaultdict
+
+def frequencies(lst):
+
+    total = 0
+    for n,v in lst:
+    total += v
+    frequencies = defaultdict(int)
+    for n,v in lst:
+    frequencies[n] += 1
+    return frequencies
```

#### initialize_list_with_range (task/58)

```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+ # This is a generator function. It *could* be a simple function, # but it's a generator function because it's convenient to just # keep calling it to get more elements. end = start step = step while end < start: yield start start += step
+    """
+    for i in range(1, 10):
```

#### initialize_list_with_range (task/58)

```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+
+    new_list = []
+    while start < end:
+    new_list.append(start)
+    start += step
+    return new_list
```

#### initialize_list_with_range (task/58)

```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+
+    '''initialize_list_with_range(end, start=0, step=1) returns
+    a list containing all numbers between start and end,
+    inclusive, and separated by step. If start is greater than
+    end, an empty list is returned.
+    '''
+    return [start
```

#### initialize_list_with_range (task/58)

```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+
+    """
+    Return a list containing the numbers between start and end,
+    with step elements between consecutive numbers.
+    """
+    if step == 0:
+    step = 1
+    return list(range(start, end + step, step))
```

#### initialize_list_with_range (task/58)

```diff
-def initialize_list_with_range(end, start = 0, step = 1):
+def initialize_list_with_range(end, start = 0, step = 1):
+
+    """Create a new list of end-start elements, in steps of
+    end-start, defaulting to 1."""
+    return [start] + list(itertools.repeat(start, step))
```

#### cumsum (task/59)

```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    result = list(lst)
+    for x in lst:
+    result.append(x)
+    return accumulate(result, 0)
```

#### cumsum (task/59)

```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    cum = sum(lst)
+    return list(accumulate(lst, cum))
```

#### cumsum (task/59)

```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    s = []
+    for e in lst:
+    s.append(s[-1] + e)
+    return s[-1]
```

#### cumsum (task/59)

```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    cumsum = []
+    for i in lst:
+    cumsum.append(cumsum[-1] + i)
+    return cumsum[-1]
+    #comparison of the cumsum between the two date arrays
```

#### cumsum (task/59)

```diff
-from itertools import accumulate
-
-def cumsum(lst):
+from itertools import accumulate
+
+def cumsum(lst):
+
+    return accumulate(lst, 0)
+    The cumsum function uses itertools.accumulate to merge successive values from the given list into a cumulative sum, which it returns. The accumulator argument to accumulate is 0 for the first element in the list, and then the sum of the previous two elements for the second
```

#### months_diff (task/60)

```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    """
+    :param start:
+    :param end:
+    :return:
+    """
+    return (end - start) * 12
```

#### months_diff (task/60)

```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    ''' Calculates the difference in months between two datetimes '''
+    start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
+    end_date = datetime.datetime.strptime(end, '%Y-%m-%
```

#### months_diff (task/60)

```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    """Returns the number of months between two datetimes.
+    If one date is later than the other, it will be negative.
+    """
+    end = end.replace(day=1)
+    return end - start + 1
```

#### months_diff (task/60)

```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    while start < end:
+    start += 1
+    while start >= end:
+    start -= 1
+    return months_diff(start, end)
```

#### months_diff (task/60)

```diff
-from math import ceil
-
-def months_diff(start, end):
+from math import ceil
+
+def months_diff(start, end):
+
+    return ceil((end - start) / 30.43)
```

#### collect_dictionary (task/61)

```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    return defaultdict(list)
+    class Tuple(collections.namedtuple('Tuple', ['a', 'b'])):
+    pass
+    test = Tuple(1, 2)
+    test.a, test.b = 0, 0
+    test.a, test.b = 3
```

#### collect_dictionary (task/61)

```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    """Turn an object into a dictionary."""
+    if isinstance(obj, dict):
+    return obj
+    elif isinstance(obj, list):
+    return defaultdict(obj)
+    elif isinstance(obj, set):
+    return defaultdict(set)
+    elif isinstance(
```

#### collect_dictionary (task/61)

```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    if isinstance(obj, dict):
+    return obj
+    else:
+    return defaultdict(obj)
```

#### collect_dictionary (task/61)

```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    if type(obj) is not list:
+    obj = [obj]
+    d = defaultdict(int)
+    for item in obj:
+    d[str(item[0])] += 1
+    return d
```

#### collect_dictionary (task/61)

```diff
-from collections import defaultdict
-
-def collect_dictionary(obj):
+from collections import defaultdict
+
+def collect_dictionary(obj):
+
+    """Collect an object's dictionary contents into a list.
+    Return a list of the keys of the object's dictionary.
+    """
+    d = {}
+    for key in dir(obj):
+    d[key] = getattr(obj, key)
+    return d.keys()
```

#### binomial_coefficient (task/62)

```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    if k == 0:
+    return n
+    elif k == 1:
+    return n * n
+    else:
+    return n * binomial_coefficient(n - 1, k - 1) * binomial_coefficient(n - 1, k)
```

#### binomial_coefficient (task/62)

```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    if k == 0:
+    return n
+    elif k == 1:
+    return n
+    else:
+    return n * binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)
+    for i in range(1, 1001
```

#### binomial_coefficient (task/62)

```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    """
+    Returns binomial coefficient(n, k)
+    """
+    if k < 0 or k > n:
+    raise ZeroDivisionError( ' %d k must be >= 0 and < %d ' % (k, n))
+    if k == 0 :
+    return 1
+    c =
```

#### binomial_coefficient (task/62)

```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    b = 1
+    for i in range(n):
+    b *= (i + k) // (n - i)
+    return b
```

#### binomial_coefficient (task/62)

```diff
-from math import comb
-
-def binomial_coefficient(n, k):
+from math import comb
+
+def binomial_coefficient(n, k):
+
+    if k <= 0:
+    return 0
+    else:
+    return n * binomial_coefficient(n-1, k-1) +
+    binomial_coefficient(n-1, k)
```

#### find_keys (task/63)

```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    """
+    Return list of all keys in dict
+    """
+    return [k for k in dict.keys() if val in dict[k]]
```

#### find_keys (task/63)

```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    for key in dict:
+    if key == val:
+    return key
+    return None
```

#### find_keys (task/63)

```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    1176 n/a if dict.has_key(val):
+    1177 n/a return dict[val]
+    1178 n/a
+    1179 n/a # simple dicts
+    1180 n/a d = {1:1, 2:2}
+    1181 n/
```

#### find_keys (task/63)

```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    if dict.has_key(val):
+    return val
+    else:
+    return find_keys(dict, val, 2)
```

#### find_keys (task/63)

```diff
-def find_keys(dict, val):
+def find_keys(dict, val):
+
+    if dict.has_key(val):
+    return [val]
+    else:
+    return []
```

#### when (task/64)

```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+ super().when(predicate, when_true) return True return super().when(predicate, when_true) when_true.connect(lambda: print("Fired when predicate returns True")) when_false.connect(lambda: print("Fired when predicate returns False"))
+    Lambda expressions are also used to provide
```

#### when (task/64)

```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+ return when_true
```

#### when (task/64)

```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+ ... with self.assertRaises(RuntimeError): pass
```

#### when (task/64)

```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+
+    return function(self, *args, **kwargs):
+    return predicate(self, *args, **kwargs)
```

#### when (task/64)

```diff
-def when(predicate, when_true):
+def when(predicate, when_true):
+
+    """
+    Returns True if the predicate is true for any of the elements.
+    """
+    # Returns False if predicate is True for all the elements
+    # and returns True if predicate is True for any of the elements
+    if predicate(element):
+    return True
+    else:
+    return False
```

#### chunk_into_n (task/65)

```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    """
+    :param lst: list
+    :param n: number of elements in each chunk
+    :return: list of chunks
+    """
+    remainder = lst[0]
+    while len(remainder) > 0 and n > 0:
+    chunk = []
+    for
```

#### chunk_into_n (task/65)

```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    lst = lst[1:]
+    for j in range(0, n, 2):
+    lst = lst[:-2] + lst[2:]
+    return lst
```

#### chunk_into_n (task/65)

```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    return [lst[i:i+n] for i in range(0, len(lst), n)]
```

#### chunk_into_n (task/65)

```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    '''
+    lst is a sequence of arbitrary objects
+    n is the length of each chunk of lst
+    returns a sequence of n - 1 lists containing the last element of lst
+    '''
+    result = []
+    while lst and len(lst) > 0:
+    result
```

#### chunk_into_n (task/65)

```diff
-from math import ceil
-
-def chunk_into_n(lst, n):
+from math import ceil
+
+def chunk_into_n(lst, n):
+
+    """Chunk a list into n size pieces and return the list of pieces."""
+    if len(lst) < n:
+    return [lst]
+    remainder = len(lst) % n
+    pieces = []
+    for i in range(0, n, remainder):
```

#### km_to_miles (task/66)

```diff
-def km_to_miles(km):
+def km_to_miles(km):
+ return km / 1000.0 # Convert km to miles miles = km_to_miles(10) print(miles) 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
```

#### km_to_miles (task/66)

```diff
-def km_to_miles(km):
+def km_to_miles(km):
+
+    return float(km) / 1000.0 * 1.60934 # [miles]
```

#### km_to_miles (task/66)

```diff
-def km_to_miles(km):
+def km_to_miles(km):
+
+    return km * 1.609
```

#### km_to_miles (task/66)

```diff
-def km_to_miles(km):
+def km_to_miles(km):
+
+    km = km / 1.609
+    return km
+    
+It was easier to convert the original km_to_miles() function to a new one that accepts a km value rather than an integer. This allows you to apply any kind of numeric input as a km value.
+    Now that we have a reusable function, let
```

#### km_to_miles (task/66)

```diff
-def km_to_miles(km):
+def km_to_miles(km):
+ return km/1000.0
```

#### max_by (task/67)

```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+ """Return the max value of a list according to a function. >>> max_by(['a', 'b', 'c'], str.lower) 'b' >>> max_by(['a', 'b', 'c'], lambda x: x.upper()) 'C' """ return sorted(lst, key=lambda
```

#### max_by (task/67)

```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+
+    max_index = 0
+    max_value = lst[0]
+    for i in range(1, len(lst)):
+    if fn(lst[i], lst[max_index]):
+    max_index = i
+    max_value = lst[i]
```

#### max_by (task/67)

```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+ """ return max(lst, key=fn) """ return max(lst, key=lambda x: fn(x))
```

#### max_by (task/67)

```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+
+    return sorted(lst, key=fn)
+    max_by = property(max_by)
```

#### max_by (task/67)

```diff
-def max_by(lst, fn):
+def max_by(lst, fn):
+ """ return the maximum element in a list by the given key """ return max(lst, key=fn)
```

#### min_element_index (task/68)

```diff
-def min_element_index(arr):
+def min_element_index(arr):
+
+    """Return the index of the first smallest element in the array, or None if the array is empty."""
+    min_value = float('inf')
+    i = 0
+    while i < len(arr):
+    if arr[i] < min_value:
+    min_value = arr[i]
```

#### min_element_index (task/68)

```diff
-def min_element_index(arr):
+def min_element_index(arr):
+
+    """
+    求min_element_index函数
+    """
+    import operator
```

#### min_element_index (task/68)

```diff
-def min_element_index(arr):
+def min_element_index(arr):
+
+    """Returns the index of the first element in arr which is less than or equal to all other elements.
+    >>> a = [-1, -2, -3, 0, 1, 2, 3]
+    >>> min_element_index(a)
+    2
+    >>> min_element_index(a,
```

#### min_element_index (task/68)

```diff
-def min_element_index(arr):
+def min_element_index(arr):
+ """ >>> min_element_index([1, 4, 6, 5, 3, 2]) 2 >>> min_element_index([1, 4, 6, 5, 3, 2, 1]) 1 """ if len(arr) < 2: return None return arr[min(0, len(arr) - 1)]
```

#### min_element_index (task/68)

```diff
-def min_element_index(arr):
+def min_element_index(arr):
+
+    return min(arr, key=arr.__getitem__)
+    return [(i,j) for i,j in zip(min_element_index(A), min_element_index(B))]
+    N.B. This version is definitely not optimal, but I leave it as an exercise for the
```

#### initialize_2d_list (task/69)

```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    if val is None:
+    val = [i for i in range(w)]
+    w, h = int(w), int(h)
+    arr = np.zeros((w, h, 3), dtype=np.uint8)
+    # The first 2 dimensions are for width and height.
```

#### initialize_2d_list (task/69)

```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    if val is None:
+    val = [random.randint(0,255) for i in range(w*h)]
+    width = w
+    height = h
+    l = []
+    for y in range(height):
+    for x in range(width):
+    if val is not None
```

#### initialize_2d_list (task/69)

```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    """Initialize 2D list of values."""
+    if val is None:
+    val = np.random.randn(w, h)
+    lst = np.zeros((w, h), dtype = np.float64)
+    for x in range(w):
+    for y in
```

#### initialize_2d_list (task/69)

```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    if val is None:
+    val = [0 for i in range(w)]
+    return [val]
```

#### initialize_2d_list (task/69)

```diff
-def initialize_2d_list(w, h, val = None):
+def initialize_2d_list(w, h, val = None):
+
+    """This is the same as `initialize_2d_list` but it takes two arguments
+    instead of four. Note that ``w`` and ``h`` must be odd numbers
+    with a common factor.
+    Args:
+    w: The width of the image.
+    h: The height of the
```

#### dict_to_list (task/70)

```diff
-def dict_to_list(d):
+def dict_to_list(d):
+ if d: return [x.upper() for x in d.items()] else: return []
+    
+Now that we have the data in a format we can use, we can formulate the query. I start with the phrase that was in the request:
+    
+for term in query_string.split('+'): query_word
```

#### dict_to_list (task/70)

```diff
-def dict_to_list(d):
+def dict_to_list(d):
+ return [d.pop(0) for d in d.items()]
+    Wow, that looks like a good candidate for a Python implementation of a Lisp loop. It looks like a for loop with a function call for an expression.
+    We can certainly emulate this in Python with a for loop, but we can do better. Let
```

#### dict_to_list (task/70)

```diff
-def dict_to_list(d):
+def dict_to_list(d):
+ return [x for x in d.values() if x is not None] # list with non-None values
```

#### dict_to_list (task/70)

```diff
-def dict_to_list(d):
+def dict_to_list(d):
+ return d.items() lst = [] lst.append(D['MARC']) lst.append(D['BIBLIO']) lst.append(D['MASTER']) for d in dict_to_list(dic): for r in d: if r.startswith('00'):
```

#### dict_to_list (task/70)

```diff
-def dict_to_list(d):
+def dict_to_list(d):
+
+    return [{k: v} for k, v in d.items()]
+    
+class P(collections.Hashable):
```

#### average (task/71)

```diff
-def average(*args):
+def average(*args):
+
+    return sum(args) / len(args)
+    print(average(3, 4, 5))
+    print(average([4, 5, 6], [7, 8, 9], [10, 11, 12]))
+    $ python average.py
+    6.0
+    6.5
```

#### average (task/71)

```diff
-def average(*args):
+def average(*args):
+ #print "The average is", sum(args)/len(args)
```

#### average (task/71)

```diff
-def average(*args):
+def average(*args):
+ total = 0.0 for n in args: total += n return total / len(args)
```

#### average (task/71)

```diff
-def average(*args):
+def average(*args):
+ """Return the average of the arguments""" return sum(args) / len(args)
```

#### intersection (task/72)

```diff
-def intersection(a, b):
+def intersection(a, b):
+ # Return a tuple containing intersecting elements from both sequences if len(a) != len(b): return [] return a[i] for i in range(len(b)): if a[i] == b[i]: yield a[i]
+    
+When we call intersection with two sequences a and b, it returns a sequence
```

#### intersection (task/72)

```diff
-def intersection(a, b):
+def intersection(a, b):
+
+    """
+    Return the intersection of two sets as a new set.
+    """
+    c = []
+    for x in a:
+    if x in b:
+    c.append(x)
+    return Set(c)
+    # ##############################################################################
+    # Functions: Searching
```

#### intersection (task/72)

```diff
-def intersection(a, b):
+def intersection(a, b):
+ - n = len(a) - m = len(b) - for i in range(n): - if a[i] == b[i]: - return False - return True - -class Test_intersection: - -
```

#### intersection (task/72)

```diff
-def intersection(a, b):
+def intersection(a, b):
+ return a&b # trace class: trace(start, end, mask) # start and end are uint32s (why?) # mask is a 1b uint32 class trace(object):
```

#### intersection (task/72)

```diff
-def intersection(a, b):
+def intersection(a, b):
+ return a.intersects(b) or b.intersects(a) #intersection - intersect a and b, keeping first intersection if there is one
```

#### hamming_distance (task/73)

```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+
+    a = list(a)
+    b = list(b)
+    return sum(abs(a[i] - b[i]))
```

#### hamming_distance (task/73)

```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+ + import string + return string.hamming_distance(a, b) + +
```

#### hamming_distance (task/73)

```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+
+    total = 0
+    for i in range(len(a)):
+    if a[i] != b[i]:
+    total += 1
+    return total
```

#### hamming_distance (task/73)

```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+ """Compute the Hamming distance between two strings. >>> hamming_distance('spam', 'spam') # unique characters 2 >>> hamming_distance('spam', 'scam') # equal characters 0 >>> hamming_distance('spam', 'sapm') # equal and unique characters 2 >>> hamming_distance
```

#### hamming_distance (task/73)

```diff
-def hamming_distance(a, b):
+def hamming_distance(a, b):
+
+    if a == b:
+    return 0
+    elif a < b:
+    return 1
+    elif a > b:
+    return -1
+    else:
+    return hamming_distance(b, a)
```

#### digitize (task/74)

```diff
-def digitize(n):
+def digitize(n):
+ # check n for integer-ness if n.isdigit(): return n
```

#### digitize (task/74)

```diff
-def digitize(n):
+def digitize(n):
+
+    # -*- coding: utf-8 -*-
+    # 数字をデジタル化する関数
```

#### digitize (task/74)

```diff
-def digitize(n):
+def digitize(n):
+ return n.digits if __name__ == '__main__': digitize(1234567)
+    This looks OK, but there are a few things to note:
+    If you are referencing the digits in a string, you must first import the string module. Otherwise, you get a NameError: name 'digits'
```

#### digitize (task/74)

```diff
-def digitize(n):
+def digitize(n):
+
+    """Digitize n according to the scheme in the comment below."""
+    n = abs(n)
+    if n <= 9:
+    return chr(n)
+    result = []
+    # Base 10 to base 36, one digit per line.
+    for base in range(0, 36,
```

#### digitize (task/74)

```diff
-def digitize(n):
+def digitize(n):
+ if n == 0: return 0 if n < 0: return -1 if n == 1: return 1 else: return sum(digitize(n-1) + digitize(n-2)) number = 10.0 number.digitize()
+    which will return
+    1 0 0 0 0 0 0 0 0 0 0
```

#### roll (task/75)

```diff
-def roll(lst, offset):
+def roll(lst, offset):
+ """Arbitrary function for rolling arbitrary lists.""" return [x for x in lst + [x + offset] if x % 2 == 0] # Test the function. for lst in [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1],
```

#### roll (task/75)

```diff
-def roll(lst, offset):
+def roll(lst, offset):
+
+    for k in lst:
+    if k < offset:
+    lst.remove(k)
+    lst.insert(offset, k)
+    return lst
```

#### roll (task/75)

```diff
-def roll(lst, offset):
+def roll(lst, offset):
+
+    if lst.count(x) != 0:
+    return [x, lst[offset:]]
+    return [lst[offset], lst[:offset]]
+    #
+    #
+    #
+    #
+    #
+    #
+    #
+    #
+    #
+    #
```

#### roll (task/75)

```diff
-def roll(lst, offset):
+def roll(lst, offset):
+ # roll a list of numbers left or right once return lst + [lst[i]+offset for i in range(len(lst)-1)]
```

#### roll (task/75)

```diff
-def roll(lst, offset):
+def roll(lst, offset):
+
+    lst.append(lst[offset])
```

#### some (task/76)

```diff
-def some(lst, fn = lambda x: x):
+def some(lst, fn = lambda x: x):
+
+    for x in lst:
+    if fn(x):
+    return True
+    return False
```

#### some (task/76)

```diff
-def some(lst, fn = lambda x: x):
+def some(lst, fn = lambda x: x):
+ if type(lst) is list: return [fn(x) for x in lst] else: return lst
```

#### some (task/76)

```diff
-def some(lst, fn = lambda x: x):
+def some(lst, fn = lambda x: x):
+ return lst.filter(fn)
```

#### some (task/76)

```diff
-def some(lst, fn = lambda x: x):
+def some(lst, fn = lambda x: x):
+ return some(lst, lambda x: fn(x))
```

#### combine_values (task/77)

```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    """Combine multiple dictionaries into one dictionary."""
+    combined = defaultdict(list)
+    for i, d in enumerate(dicts):
+    combined[i].extend(d)
+    return combined
```

#### combine_values (task/77)

```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    """
+    Return a dict whose keys are all the keys in dicts and values are the
+    corresponding values in dicts.
+    """
+    combined = {}
+    for d in dicts:
+    combined[d[key]] = d[value]
+    return combined
+    if __
```

#### combine_values (task/77)

```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    """Return a dictionary combining values from each of the given dictionaries.
+    If a key is in any of the given dictionaries, the value from that dictionary
+    is returned. Otherwise a new value is generated using the given generators.
+    """
+    return defaultdict(combine_function(getattr(v,
```

#### combine_values (task/77)

```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    values = defaultdict(list)
+    for d in dicts:
+    for k, v in d.items():
+    if k not in values:
+    values[k] = []
+    values[k].append(v)
+    return values
```

#### combine_values (task/77)

```diff
-from collections import defaultdict
-
-def combine_values(*dicts):
+from collections import defaultdict
+
+def combine_values(*dicts):
+
+    """
+    Transforms a list of dictionaries into a single dictionary with
+    the same key-value pairs.
+    """
+    return defaultdict(lambda: 0, *dicts)
```

#### flatten (task/78)

```diff
-def flatten(lst):
+def flatten(lst):
+
+    if not lst:
+    return []
+    for x in lst:
+    if isinstance(x, list):
+    return [flatten(x)]
+    return x
```

#### flatten (task/78)

```diff
-def flatten(lst):
+def flatten(lst):
+
+    if not lst:
+    return []
+    else:
+    return [x for x in lst if x]
+    # example usage
+    >>> print(flatten([1,2,[3,4],5]))
+    [1, 2, 3, 4, 5]
+    """
```

#### flatten (task/78)

```diff
-def flatten(lst):
+def flatten(lst):
+ """ Flatten a list of lists, into a list of the same items """ # print('flattening', lst) if not lst: return [] lst.append(lst[0]) for x in lst[1:]: lst.append(x) return lst
```

#### flatten (task/78)

```diff
-def flatten(lst):
+def flatten(lst):
+
+    return reduce(lambda x, y: x+y, lst, [] )
+    If we store all the maps in a list, then we can call flatten() on that list, and it will return the sum of all the maps:
+    >>> flatten([[1,2], [3,4]])
```

#### flatten (task/78)

```diff
-def flatten(lst):
+def flatten(lst):
+
+    return reduce(lambda a,b: a+b, lst)
+    lst = [1,2,3,4,5,6,7,8,9,10]
+    print(flatten(lst))
+    
+This is how the program works. First, the lst list is assigned
```

#### symmetric_difference_by (task/79)

```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    return a - set(b) if fn(a, b) else b - set(a)
+    
+    #Tests:
```

#### symmetric_difference_by (task/79)

```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    """
+    n the set of all finite sequences of elements from `A` and `B`
+    sorted by length.
+    """
+    sorted_a = sorted(a)
+    sorted_b = sorted(b)
+    sorted_difference = [ x for x in sorted_a
```

#### symmetric_difference_by (task/79)

```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    return lambda c: (a[c] if c in a else b[c] if c in b else c)
+    self.__invariants.add(symmetric_difference_by(self.__invariants))
+    """
```

#### symmetric_difference_by (task/79)

```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    """Compute the symmetric difference of a and b and apply function fn.
+    Args:
+    a: A set
+    b: A set
+    fn: A function to apply to each element in the output.
+    Returns:
+    A set.
+    """
+    return set (a | b)
```

#### symmetric_difference_by (task/79)

```diff
-def symmetric_difference_by(a, b, fn):
+def symmetric_difference_by(a, b, fn):
+
+    return fn(a, b) | fn(b, a)
```

#### find_last_index (task/80)

```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+
+    """Find the index of the last occurrence of value in the list"""
+    index = -1
+    found = False
+    for i in range(len(lst)):
+    if fn(lst[i]):
+    found = True
+    index = i
+    break
+    if not found:
```

#### find_last_index (task/80)

```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+
+    """
+    iterable: list or tuple
+    fn: function
+    """
+    index = 0
+    for item in lst:
+    if fn(item):
+    index = index + 1
+    return index
```

#### find_last_index (task/80)

```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+ # List comprehension can use “_” to ignore values. return max(0, len(lst) - len(lst) - fn(lst[-1]))
+    And finally, the main program will use all of the above functions to find the last index of a particular string in a list of strings.
```

#### find_last_index (task/80)

```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+
+    last_index = None
+    for i in range(len(lst)):
+    if fn(lst[i]):
+    last_index = i
+    return last_index
```

#### find_last_index (task/80)

```diff
-def find_last_index(lst, fn):
+def find_last_index(lst, fn):
+ # Find the last index of item in the list. # Base case. if lst == []: return None # Recursive case. return find_last_index(lst[1:], fn)
+    Here is the Python code:
```

#### weighted_average (task/81)

```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+
+    total = 0
+    for num in nums:
+    total += num * weights[num]
+    return total / weights.sum()
```

#### weighted_average (task/81)

```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+ '''Calculate the weighted average of the values in nums, weighted by the weights in weights. Uses the same formula as np.mean, but is faster for larger arrays because it doesn't require making a copy of the array. ''' return np.sum(nums * weights, axis=0) / weights.sum()
```

#### weighted_average (task/81)

```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+ return sum(nums) / weights
+    To do:
+    Extend to multidimensional arrays
+    10. Data Analysis - Linear Regression
+    Some problems in data analysis can be best solved using linear regression. Linear regression is used to fit a line to a set of data.
+    The concept of a line of best
```

#### weighted_average (task/81)

```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+ return nums / weights.sum()
```

#### weighted_average (task/81)

```diff
-def weighted_average(nums, weights):
+def weighted_average(nums, weights):
+ return sum(nums) / sum(weights) mylist = [8, 3, 12, 9, 0, 1, 5, 4, 6, 0, 4, 9, 1, 0, 5, 9, 6, 5, 0, 1, 2, 3, 5, 9, 0, 1, 5, 9
```

#### bifurcate (task/82)

```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    """
+    Return a new list containing all elements of lst
+    that pass the test defined by filter.
+    """
+    return list(filter(lambda x: x in lst, lst))
```

#### bifurcate (task/82)

```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    if filter(lst[0]):
+    return lst[0], bifurcate(lst[1:], filter)
+    return lst[0], None
+    
+This function splits a list into two new lists, by recursively splitting the head of the list until the filter criteria is met
```

#### bifurcate (task/82)

```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    """Bifurcate list into a list of elements for which the filter returns True
+    and a list of elements for which the filter returns False"""
+    result = []
+    for elt in lst:
+    if filter(elt):
+    result.append(elt)
+    else:
+    result
```

#### bifurcate (task/82)

```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    """Bifurcate a list of lists into two lists of the same size
+    Return two lists of the same size as the input list, where the
+    input list is a list of lists.
+    Each list in the input list will appear as a list in the two
+    output lists.
+    >>> l
```

#### bifurcate (task/82)

```diff
-def bifurcate(lst, filter):
+def bifurcate(lst, filter):
+
+    # Checks if lst contains items in filter
+    if filter is None:
+    # filter can be None when calling from list comprehension
+    filter = set()
+    for i in lst:
+    if i in filter:
+    # item is in filter
+    lst.remove(i)
+    return
```

#### all_equal (task/83)

```diff
-def all_equal(lst):
+def all_equal(lst):
+
+    """a test that returns True when all items in a list are equal."""
+    for item in lst:
+    if item != lst[0]:
+    return False
+    return True
```

#### all_equal (task/83)

```diff
-def all_equal(lst):
+def all_equal(lst):
+
+    if type(lst) is not list:
+    return False
+    for x in lst:
+    if x != lst[0]:
+    return False
+    return True
```

#### all_equal (task/83)

```diff
-def all_equal(lst):
+def all_equal(lst):
+ ''' Ensures that two lists are the same length and all elements are equal. ''' for i in range(len(lst)): if not lst[i] == lst[i]: return False return True
+    This function checks that two lists are the same length and that all elements are equal. Because we write it
```

#### all_equal (task/83)

```diff
-def all_equal(lst):
+def all_equal(lst):
+ for i in lst: if i != lst[0]: return False return True
```

#### all_equal (task/83)

```diff
-def all_equal(lst):
+def all_equal(lst):
+
+    for i in lst:
+    for j in lst:
+    if i != j:
+    return False
+    return True
```

#### difference (task/84)

```diff
-def difference(a, b):
+def difference(a, b):
+
+    """Return the difference of a and b.
+    
+    >>> from sympy import Symbol, difference
+    >>> x, y = Symbol('x y'), Symbol('x')
+    >>> difference(x, y)
+    x - y
+    >>> difference(x, x)
+    0
+    >>> difference(x
```

#### difference (task/84)

```diff
-def difference(a, b):
+def difference(a, b):
+
+    return a - b
+    
+Here, the function difference( ) defines a function difference( ) that accepts two values and returns the difference of the two values. The function difference( ) is called a “method.” To call the method difference( ), you use the syntax:
+    result = methodname(arg1,
```

#### difference (task/84)

```diff
-def difference(a, b):
+def difference(a, b):
+ return a-b
+    #!/usr/bin/env python3 class Point:
```

#### difference (task/84)

```diff
-def difference(a, b):
+def difference(a, b):
+ return a - b
```

#### difference (task/84)

```diff
-def difference(a, b):
+def difference(a, b):
+ return a - b
```

#### kebab (task/85)

```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    return sub(r'(?:[{}])|(?:[^$\w()\[\]\-.!\\/]*$)|(?:[^\u0000-\u001F\u007F]*[\u007F-\u0000])', r'\u%04
```

#### kebab (task/85)

```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    return re.sub(r'(\w+[-+])', lambda match: int(match.group(1)), s)
+    #json.dumps(s, ensure_ascii=False)
+    s = '"foo":'
+    print kebab(s)
+    9. Comp
```

#### kebab (task/85)

```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    return s.replace(‘_’, ‘-‘).lower()
```

#### kebab (task/85)

```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    return s.replace(' ', '_')
+    for line in sub('^#.*$', '').split('
+    '):
+    line = line.strip()
+    if len(line) > 0:
+    print line
+    _b = kebab(line)
+    if line.start
```

#### kebab (task/85)

```diff
-from re import sub
-
-def kebab(s):
+from re import sub
+
+def kebab(s):
+
+    return s.encode('utf-8')[::-1]
```

#### miles_to_km (task/86)

```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+ return miles * 1.609344 print miles_to_km(miles)
+    The previous example will not work! The reason is that the interpreter considers the statement a syntax error, so it raises a SyntaxError exception. It is important to understand that there is no way to catch this exception with a try/except block,
```

#### miles_to_km (task/86)

```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+ return miles * 1.609344
```

#### miles_to_km (task/86)

```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+ return miles * 1.609344 return miles_to_km
+    Next, we’ll create a new variable miles_to_km that calls miles_to_km() . We’ll also create a new variable called miles_to_meters . We’ll use miles_to_meters to store
```

#### miles_to_km (task/86)

```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+ return miles / 1.609344
```

#### miles_to_km (task/86)

```diff
-def miles_to_km(miles):
+def miles_to_km(miles):
+ return miles * 1.609344
```

#### sum_of_powers (task/87)

```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+
+    end = int(end)
+    result = 1
+    while end >= start:
+    result *= power
+    end -= 1
+    return result
+    # the output for the last two calls is:
+    # In [7]: c = Power.sum_of_powers(4)
+    # In
```

#### sum_of_powers (task/87)

```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+
+    return sum([pow(start, end - 1, power) for power in range(power)])
```

#### sum_of_powers (task/87)

```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+ end = end - 1 if end < 0: end = 0 if power == 1: return sum(x**(end-start)) else: return sum(x**power*sum_of_powers(end-start, power-1, start))
+    >>> from math import pow >>> timeit sum_of_powers(10
```

#### sum_of_powers (task/87)

```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+
+    total = 0
+    while power <= end:
+    total += start
+    total *= power
+    power += 1
+    return total
+    if __name__ == '__main__':
+    print(sum_of_powers(10, 3))
+    print(sum_of_powers(10,
```

#### sum_of_powers (task/87)

```diff
-def sum_of_powers(end, power = 2, start = 1):
+def sum_of_powers(end, power = 2, start = 1):
+
+    """
+    End must be >= start
+    """
```

#### compose (task/88)

```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    """
+    Return a function that composes any number of other functions.
+    """
+    return reduce(lambda f, g: lambda x: f(g(x)), fns)
```

#### compose (task/88)

```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    "Returns a function that represents the application of all the
+    *fns. For example, compose(f, g, h)(x) is equivalent to f(g(h(x)))."
+    return reduce(lambda f, g: f(g), fns)
+    // This can be done in pure
```

#### compose (task/88)

```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    r = reduce(lambda x, y: x(y), fns)
+    return lambda x: r(x)
+    f = lambda x: x+1
+    g = lambda x: x**2
+    print(compose(f, g))
+    >>> print(compose(f, g
```

#### compose (task/88)

```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    return reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)
+    Then, you can use @compose to define a new inner function that calls the given functions and returns the result:
+    >>>
```

#### compose (task/88)

```diff
-from functools import reduce
-
-def compose(*fns):
+from functools import reduce
+
+def compose(*fns):
+
+    return reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)
+    example = functools.partial(compose, lambda x:x+2, lambda x:x+3)
+    example(1) # returns 6
+    The partial function is defined
```

#### similarity (task/89)

```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    if len(a) != len(b):
+    return 0
+    for i in range(len(a)):
+    if a[i] != b[i]:
+    return 0
+    return 1
```

#### similarity (task/89)

```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    return a.lower() == b.lower()
+    
+if any(contains(person, name) for name in [
+    'Tom', 'B', 'J', 'G', 'Alice'
+    ]):
+    # ...
+    2.2.1.2.2.2.4.3
```

#### similarity (task/89)

```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    return a.lower() == b.lower()
```

#### similarity (task/89)

```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    # get the results of the analogical task
+    ret = a.analogical_results()
+    # check if the two datasets are identical
+    if ret is not None:
+    # get the analogical task results
+    ar = b.analogical_results()
+    # check if they are identical
```

#### similarity (task/89)

```diff
-def similarity(a, b):
+def similarity(a, b):
+
+    """Return similarity of two strings."""
+    # The default is to return a float in the range [0, 1].
+    #
+    # https://en.wikipedia.org/wiki/Cosine_similarity
+    return np.dot(a, b) / (np.linalg.norm(
```

#### have_same_contents (task/90)

```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    '''
+    Check if two strings have the same contents.
+    '''
+    for i in range(len(a)):
+    if a[i] != b[i]:
+    return False
+    return True
```

#### have_same_contents (task/90)

```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    a.contents == b.contents
```

#### have_same_contents (task/90)

```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    - """
+    - Checks if the content of a file is the same as another file.
+    -
+    - This checks the content of a file a is the same as another file b
+    -
+    - :type a: string
+    - :type b: string
+    - :rtype: bool
```

#### have_same_contents (task/90)

```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    + r = open(a).read()
+    + s = open(b).read()
+    + return r == s
+    +
```

#### have_same_contents (task/90)

```diff
-def have_same_contents(a, b):
+def have_same_contents(a, b):
+
+    return a.content == b.content
+    >>> have_same_contents(file_a, file_b)
+    True
+    >>> have_same_contents(file_a, file_b)
+    False
+    >>> have_same_contents(file_a, file_b)
```

#### days_from_now (task/91)

```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    days = n.days
+    if days < 0:
+    raise ValueError('Days cannot be negative: %d' % days)
+    else:
+    return timedelta(days=days)
```

#### days_from_now (task/91)

```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    days = timedelta(days=n)
+    y = days.days
+    m = days.days * 365 + days.month
+    d = days.days * 30 + days.days
+    return date(y, m, d)
```

#### days_from_now (task/91)

```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    """ A function to return the number of days until now plus the given number of days """
+    return timedelta(days=n) - date.today()
```

#### days_from_now (task/91)

```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    return timedelta(days=n)
```

#### days_from_now (task/91)

```diff
-from datetime import timedelta, date
-
-def days_from_now(n):
+from datetime import timedelta, date
+
+def days_from_now(n):
+
+    if n == 0:
+    return date.today()
+    d = timedelta(days=n)
+    days = d.days + timedelta(days=1)
+    return date(year=d.year, month=d.month, day=d.day, hour=d.hour,
```

#### cast_list (task/92)

```diff
-def cast_list(val):
+def cast_list(val):
+
+    if isinstance(val, int):
+    return val
+    elif isinstance(val, float):
+    return val
+    elif isinstance(val, list):
+    for n in range(len(val)):
+    val[n] = cast_list(val[n])
+    return
```

#### cast_list (task/92)

```diff
-def cast_list(val):
+def cast_list(val):
+ + """ + Uncast val into a list + """ + val = val.strip() + if len(val) == 0: + return None + elif len(val) == 1: + return val + else: + parts = val.split('_') + parts = [int(part) for part in parts] + return
```

#### cast_list (task/92)

```diff
-def cast_list(val):
+def cast_list(val):
+
+    return [int(i) for i in val.split()]
```

#### cast_list (task/92)

```diff
-def cast_list(val):
+def cast_list(val):
+
+    return [val]
```

#### cast_list (task/92)

```diff
-def cast_list(val):
+def cast_list(val):
+
+    if type(val) == str:
+    if val == 'true':
+    return True
+    if val == 'false':
+    return False
+    if val == 'null':
+    return None
+    if val == 'None':
+    return None
+    if val == '[]':
+    return list
```

#### sort_dict_by_value (task/93)

```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+
+    
+    if reverse:
+    d = {v: k for k, v in d.items()}
+    else:
+    d = {v: k for k, v in d.items()}
+    return d
```

#### sort_dict_by_value (task/93)

```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+
+    """
+    Return a sorted dict and its reverse sorted copy, both
+    having values in the `d` dict in sorted order.
+    
+    Arguments:
+    d: dict to sort
+    reverse: boolean (default: False)
+    """
+    if not isinstance(d, dict):
+    raise
```

#### sort_dict_by_value (task/93)

```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+ """A sort_dict helper function.""" if not isinstance(d, dict): raise TypeError('d must be a dict') if reverse: sorted(d.items(), key=lambda t: t[1], reverse=True) else: sorted(d.items(), key=lambda t: t[0], reverse=False
```

#### sort_dict_by_value (task/93)

```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+
+    """ Sort a dictionary's items by value.
+    Arguments:
+    d -- a dictionary
+    reverse -- True, to sort in reverse order
+    """
+    if not isinstance (d, dict ):
+    raise TypeError ( " sort_dict_by_value() argument must be a dictionary " )
```

#### sort_dict_by_value (task/93)

```diff
-def sort_dict_by_value(d, reverse = False):
+def sort_dict_by_value(d, reverse = False):
+ """Sort dict by value. Arguments: d (dict) Dictionary to sort. reverse (bool) If True, sort in reverse order. """ if d: key_sort_value = {} for key, value in d.items(): if key not in key_sort_value: key_sort_value[key] = key_
```

#### slugify (task/94)

```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    return re.sub(r'\s+', '-', s.lower())
```

#### slugify (task/94)

```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    return re.sub(r'[^\w\s]+', '-', s).lower()
```

#### slugify (task/94)

```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    return s.replace(' ', '-')
```

#### slugify (task/94)

```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    return re.sub(r"(?u)\b(?:[a-z0-9]+[a-z0-9]+[a-z0-9]+[a-z0-9]+|[a-z0-9]+[a-z0-9]+[a-z0-
```

#### slugify (task/94)

```diff
-import re
-
-def slugify(s):
+import re
+
+def slugify(s):
+
+    """
+    http://stackoverflow.com/questions/1603357/slugify-words-with-underscores
+    """
+    return re.sub(r'[^\w]', '-', s).strip('-').lower()
```

#### to_roman_numeral (task/95)

```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+ roman = "" value = num if num >= 4000000: value = (num/1000000)*1000 num = value elif num >= 1000000: value = (num/1000000)*100 num = value elif num >= 10000: value = num elif num >= 1000: value = num*10 num = value elif num
```

#### to_roman_numeral (task/95)

```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+ """convert number to roman numeral""" if isinstance(num, int): return roman_numeral(num)
```

#### to_roman_numeral (task/95)

```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+ roman = [] for numeral, power in roman_numeral_powers: roman.append(numeral * power) return ''.join(roman) 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
```

#### to_roman_numeral (task/95)

```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+
+    if num < 0:
+    return '-' + roman_numeral(num)
+    return roman_numeral(num)
+    
+The to_roman_numeral function takes a positive integer, and returns a string of the form "MCDLXXXIV" for numbers in the range 0 to 3999
```

#### to_roman_numeral (task/95)

```diff
-def to_roman_numeral(num):
+def to_roman_numeral(num):
+ roman = [] while num >= 100: num = num // 100 roman.append(num) while num >= 10: num = num // 10 roman.append(num) while num >= 1: num = num // 1 roman.append(num) return roman
```

#### check_prop (task/96)

```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+
+    98 n/a with self.assertRaises(AssertionError):
+    99 n/a fn(None, prop)
+    100 n/a with self.assertRaises(AssertionError):
+    101 n/a fn(None, False)
+    102 n/a with self.assert
```

#### check_prop (task/96)

```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+
+    # return True if fn is a function whose property prop is defined
```

#### check_prop (task/96)

```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+
+    # For testing a function, rather than a method of a class, we
+    # get the class object and call the method on that.
+    # For example, here we test __len__ on a class, rather than
+    # a built-in operation of a string.
+    obj = fn.__self__
```

#### check_prop (task/96)

```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+ return fn(lhs, prop, rhs)
```

#### check_prop (task/96)

```diff
-def check_prop(fn, prop):
+def check_prop(fn, prop):
+ if prop not in fn._prop_map: fn._prop_map[prop] = callable(fn)
```

#### count_occurrences (task/97)

```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+
+    counter = 0
+    for v in lst:
+    if v == val:
+    counter += 1
+    return counter
```

#### count_occurrences (task/97)

```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+ # take all values in lst and count the number of times they # occur. # if the item is already in the count, then just add 1. # if it's not, then add it and count it. return lst.count(val) + lst.count(val) + 1
+    And a test for this
```

#### count_occurrences (task/97)

```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+
+    counts = dict()
+    for e in lst:
+    if e == val:
+    counts[e] = counts.get(e, 0) + 1
+    return counts
```

#### count_occurrences (task/97)

```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+
+    count = 0
+    for i in lst:
+    if i == val:
+    count += 1
+    return count
```

#### count_occurrences (task/97)

```diff
-def count_occurrences(lst, val):
+def count_occurrences(lst, val):
+ return lst.count(val)
```

#### find_parity_outliers (task/98)

```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    return (nums.count(n) * 0.5).count(0)
```

#### find_parity_outliers (task/98)

```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    """Finds outliers based on the parity of a set of integers."""
+    c = Counter(nums)
+    for x in c:
+    outliers = c.get(x, 0)
+    outliers += x
+    outliers -= c.get(x, 0)
```

#### find_parity_outliers (task/98)

```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    count = Counter()
+    for i in range(nums):
+    count[i] += 1
+    outliers = []
+    for i in range(len(count)):
+    if count[i] > 4 * len(count) / 3:
+    outliers.append(i)
```

#### find_parity_outliers (task/98)

```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    """
+    Finds the number of outlier parity samples, where outlier means "the
+    number of samples whose parity differs from the parity of the
+    sample's majority class" (which is a majority-vote classifier in this
+    example).
+    """
+    outliers = 0
+    for i
```

#### find_parity_outliers (task/98)

```diff
-from collections import Counter
-
-def find_parity_outliers(nums):
+from collections import Counter
+
+def find_parity_outliers(nums):
+
+    c = Counter(nums)
+    c = c.drop(1)
+    count = c.most_common(3)
+    print count
+    count = c.most_common(4)
+    print count
+    count = c.most_common(5)
+    print count
+    count
```

#### to_dictionary (task/99)

```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+ """Takes a list of 2-tuples and returns a dictionary""" return {key: value for key, value in zip(keys, values)}
```

#### to_dictionary (task/99)

```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+
+    return { k: v for k, v in zip(keys, values) }
```

#### to_dictionary (task/99)

```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+
+    """Convert a list of keys to a dictionary."""
+    if isinstance(keys, str):
+    keys = [keys]
+    if isinstance(values, str):
+    values = [values]
+    return {key: value for key, value in zip(keys, values)}
+    
+We are
```

#### to_dictionary (task/99)

```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+ """Get dictionary representation of sequence.""" dict = {} for key in keys: dict[key] = values[key] return dict
```

#### to_dictionary (task/99)

```diff
-def to_dictionary(keys, values):
+def to_dictionary(keys, values):
+ """Encode a dictionary into a JSON structure in the form of a dictionary.""" if not isinstance(values, dict): values = {values} d = {} for key in keys: d[key] = values[key] return d
```

#### geometric_progression (task/100)

```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    """An iterable that yields end, start*step, start*step*step, ...
+    until 2*step+1 == end.
+    """
+    step += 1
+    end = 2*step + 1
+    while step < end:
+    yield start * step
+    step += step
```

#### geometric_progression (task/100)

```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    if step == 1:
+    return [start]
+    elif step == 2:
+    return [start, start + start]
+    elif step == 3:
+    return [start, start + start + start]
+    elif step == 4:
+    return [start, start + start + start
```

#### geometric_progression (task/100)

```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    """Calculate the nth term of a geometric progression"""
+    n = int(end/step)
+    num = start
+    denom = step
+    sum = num * step
+    if n > 0:
+    return sum + (n-1)*denom
+    elif n == 0:
```

#### geometric_progression (task/100)

```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    """
+    Compute nth term of geometric progression.
+    >>> geometric_progression(5, 1, 2)
+    5
+    >>> geometric_progression(15, 2, 3)
+    60
+    >>> geometric_progression(1000, 6, 4)
+    100000
+    >>> geometric
```

#### geometric_progression (task/100)

```diff
-from math import floor, log
-
-def geometric_progression(end, start=1, step=2):
+from math import floor, log
+
+def geometric_progression(end, start=1, step=2):
+
+    """Return successive terms of the Arithmetic Progression
+    Arithmetic Progression:
+    http://en.wikipedia.org/wiki/Arithmetic_progression
+    """
+    next = start
+    for i in range(end):
+    next = next * step
+    return next
```

#### find_last (task/101)

```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    return _find_last(lst, _reverse=True, fn)
+    
+    # 根据索引在list中找出最后一个元素
```

#### find_last (task/101)

```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    # Prevent infinite loop
+    found = False
+    for i in range(len(lst)):
+    if fn(lst[i]):
+    found = True
+    break
+    if not found:
+    return -1
+    return lst[len(lst)-1]
```

#### find_last (task/101)

```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    """
+    lst:list
+    fn:function
+    return the last item of lst for which fn(lst[-1]) is true
+    """
+    # todo: return the last item of lst for which fn(lst[-1]) is true
+    lst.sort()
```

#### find_last (task/101)

```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    print("Find last: ", end="")
+    if len(lst) > 0:
+    result = lst[len(lst)-1]
+    else:
+    result = None
+    print(result)
+    return result
```

#### find_last (task/101)

```diff
-def find_last(lst, fn):
+def find_last(lst, fn):
+
+    '''Returns the last element of a list that satisfies the function and all its predecessors.
+    '''Returns the last element of a list that satisfies the function and all its predecessors.
+    It might be faster to use this if you can guarantee that the list is sorted.
+    It might be faster to use this if you
```

#### sort_dict_by_key (task/102)

```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    """
+    When given a dict, return a dict with the elements sorted by key.
+    If the `reverse` flag is True, the sort is reversed.
+    >>> list(sort_dict_by_key({'a': 1, 'b': 2, 'c': 3}, reverse = True))
```

#### sort_dict_by_key (task/102)

```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    if reverse:
+    d = {val: key for key, val in d.items()}
+    return d
```

#### sort_dict_by_key (task/102)

```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    if not reverse:
+    d.sort(key = lambda k: k[1])
+    else:
+    d.sort(key = lambda k: k[0])
+    return d
```

#### sort_dict_by_key (task/102)

```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    '''Return a new dictionary with its entries sorted by key. If
+    reverse is True, then the entries are sorted in reverse order.
+    >>> d = { 'one' : 1, 'two' : 2, 'three' : 3 }
+    >>> d.sort_dict_by_key()
```

#### sort_dict_by_key (task/102)

```diff
-def sort_dict_by_key(d, reverse = False):
+def sort_dict_by_key(d, reverse = False):
+
+    """Sort the dictionary d by key.
+    d must be a dictionary, not a list.
+    In case of reverse, the result is a dictionary where the keys are
+    sorted in reverse order.
+    """
+    if type(d) != type({}):
+    raise TypeError("d must be
```

#### split_lines (task/103)

```diff
-def split_lines(s):
+def split_lines(s):
+
+    return s.split('
+    ')
+    
+    #!/usr/bin/env python
+    #-*- coding: utf-8 -*-
+    import sys
+    if len(sys.argv) == 1:
+    sys.exit('python script filename')
+    file = sys.arg
```

#### split_lines (task/103)

```diff
-def split_lines(s):
+def split_lines(s):
+
+    return s.split('
+    ')
```

#### split_lines (task/103)

```diff
-def split_lines(s):
+def split_lines(s):
+
+    """Split a single line of text into a list of lines"""
+    lines = []
+    for x in s.split("
+    "):
+    lines.append(x)
+    return lines
```

#### split_lines (task/103)

```diff
-def split_lines(s):
+def split_lines(s):
+
+    lines = s.split('
+    ')
+    return lines
```

#### split_lines (task/103)

```diff
-def split_lines(s):
+def split_lines(s):
+ # Python3
+    r = s.rstrip()
+    for line in r.split('
+    '):
+    yield line
```

#### includes_any (task/104)

```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+
+    for x in values:
+    if x in lst:
+    return True
+    return False
```

#### includes_any (task/104)

```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+
+    """
+    Return True if any of the values are contained in lst.
+    """
+    for val in values:
+    if val in lst:
+    return True
+    return False
+    
+    # delete_any_
```

#### includes_any (task/104)

```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+ include = False while lst and not include: if values.is_in(lst[0]): include = True lst.remove(lst[0]) return include
```

#### includes_any (task/104)

```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+ """ Returns true if any item in the list matches any value in the list. """ for item in lst: if item in values: return True return False >>> includes_any([1, 2, 3], [1, 2, 3]) True >>> includes_any([1, 2, 3], [1, 2, 4]) False
```

#### includes_any (task/104)

```diff
-def includes_any(lst, values):
+def includes_any(lst, values):
+ # Like includes() but returns true if any value is found in # list. return (x in lst for x in values)
```

#### merge (task/105)

```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+
+    """
+    Return a DataFrame with the rows of each given DataFrame
+    merged together.
+    In the case of duplicate keys, the values from the columns
+    of the left DataFrame will be used.
+    Additional keyword arguments are passed to pandas.DataFrame.merge.
+    For example,
```

#### merge (task/105)

```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+
+    """
+    Return a Series or DataFrame with duplicate rows removed,
+    row-wise.
+    Arguments:
+    *args: A list of Series or DataFrame objects to merge
+    Returns:
+    A Series or DataFrame object
+    Examples:
+    >>> df = pd.DataFrame({"
```

#### merge (task/105)

```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+ + "Merge multiple fields into a single field. Fields are + specified as sequences of tuples, or lists of tuples in + case of fields with aliases. + + For example:: + + Age = Struct('age', [('name', 'name', 'name')]) + + Name = Struct('name', [('first',
```

#### merge (task/105)

```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+
+    result = list(args)
+    for i in range(len(result)):
+    result[i] = tuple(result[i])
+    for i in range(len(result)):
+    result[i] = list(result[i])
+    return result
```

#### merge (task/105)

```diff
-def merge(*args, fill_value = None):
+def merge(*args, fill_value = None):
+
+    """Merge the elements of each tuple in the args list together.
+    If a fill_value is provided, it is used for values of args
+    where there are multiple entries of the same key.
+    """
+    args = tuple (args)
+    fill_value = fill_value or args[ 0 ]
```

#### min_by (task/106)

```diff
-def min_by(lst, fn):
+def min_by(lst, fn):
+
+    """min_by(lst, fn) -> (min, lst)"""
+    res = []
+    for item in lst:
+    if fn(item):
+    res.append(item)
+    if len(res) == 1:
+    return res[0], lst
+    return
```

#### min_by (task/106)

```diff
-def min_by(lst, fn):
+def min_by(lst, fn):
+
+    """ Returns the minimum of a sequence as determined by the key given by the function
+    >>> min_by(['a', 'b', 'c'], lambda x: -x.lower())
+    'a'
+    """
+    return min ( filter ( lambda x : fn ( x ) < 0 , lst
```

#### min_by (task/106)

```diff
-def min_by(lst, fn):
+def min_by(lst, fn):
+ """Min, returns the min of an iterable lst, based on the function fn""" m = min(lst, key=fn) if m is None: return None return m
+    Python 模块集合
+    从 Python 2.6 开始，它
```

#### min_by (task/106)

```diff
-def min_by(lst, fn):
+def min_by(lst, fn):
+
+    return min(lst, key=fn)
+    That is, min_by does the minimum of the list lst using the function fn.
+    For min_by to work, it needs to be able to compare any two elements of lst. To do that, it takes the comparison function fn and then calls it
```

#### add_days (task/107)

```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    return d + timedelta(days = n)
+    # The following function returns a tuple of the current date and
+    # the number of seconds since the epoch.
```

#### add_days (task/107)

```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    return d + timedelta(days = n)
```

#### add_days (task/107)

```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    """Adds days to a date"""
+    d += timedelta(days = n)
+    return d.date()
```

#### add_days (task/107)

```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    return datetime.combine(d, datetime(d.year, d.month, d.day + n))
```

#### add_days (task/107)

```diff
-from datetime import datetime, timedelta
-
-def add_days(n, d = datetime.today()):
+from datetime import datetime, timedelta
+
+def add_days(n, d = datetime.today()):
+
+    yield d
+    d += timedelta(n * 24 * 60 * 60)
+    d += timedelta(n * 24 * 60 * 60)
+    d += timedelta(n * 24 * 60 * 60)
+    yield d
```

#### palindrome (task/108)

```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+    if s == '':
+    return True
+    for i in range(len(s)):
+    if s[i] != s[len(s) - i - 1]:
+    return False
+    return True
```

#### palindrome (task/108)

```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+    return s == s[::-1]
```

#### palindrome (task/108)

```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+    r = []
+    for c in s:
+    if c != ' ' and c != '\t' and c != '
+    ' and c != '\r':
+    r.append(c)
+    if len(r) > 1:
+    return False
+    r.reverse()
```

#### palindrome (task/108)

```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+    """Returns true if s is a palindrome, false otherwise"""
+    return s == s[::-1]
+    
+for s in [
+    "No way Jose",
+    "A man, a plan, a canal - Panama!",
+    "Able was I ere I saw Elba",
```

#### palindrome (task/108)

```diff
-from re import sub
-
-def palindrome(s):
+from re import sub
+
+def palindrome(s):
+
+    """
+    return True if the string is a palindrome
+    """
+    return s == s[::-1]
```

#### none (task/109)

```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+
+    """
+    Sorts the list, ignoring order.
+    """
+    lst.sort(cmp = None )
+    if not lst:
+    return None
+    else :
+    return lst
```

#### none (task/109)

```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+ return (lambda f: lst and (fn(f()) or f())) #print(none([(2, 3), (4, 5), (6, 7), (8, 9)], lambda x: x[0])) #define x1(a, b) lambda *x: a * b #define x
```

#### none (task/109)

```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+ return None if len(lst) == 0 else None return lambda x: x
```

#### none (task/109)

```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+
+    lst[:] = fn(lst[:])
```

#### none (task/109)

```diff
-def none(lst, fn = lambda x: x):
+def none(lst, fn = lambda x: x):
+ if not lst: return None elif not fn(lst[0]): return None else: return lst[1] if len(args) == 1: if isinstance(args[0], int): return none(args[0], lambda x: x) else: return none(args[0], lambda x:
```

#### tail (task/110)

```diff
-def tail(lst):
+def tail(lst):
+ return [t for t in lst if t]
```

#### tail (task/110)

```diff
-def tail(lst):
+def tail(lst):
+
+    return lst[1:] if lst else [lst[0]]
```

#### tail (task/110)

```diff
-def tail(lst):
+def tail(lst):
+
+    print(lst[len(lst)-1])
+    #tail([1,2,3,4,5])
+    #[2,3,4,5]
+    #tail([1,2,3,4,5,6])
+    #[2,3,4,5]
```

#### tail (task/110)

```diff
-def tail(lst):
+def tail(lst):
+
+    return (lst[0], tail(lst[1:]))
+    print("***")
+    print(head_tail("abcd"))
+    print(head_tail("acbd"))
+    print(head_tail("abcde"))
+    print(head_tail("abccde"))
```

#### tail (task/110)

```diff
-def tail(lst):
+def tail(lst):
+
+    return lst[-1] + [lst[-2]]
```

#### has_duplicates (task/111)

```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+
+    has_duplicates = False
+    for x in lst:
+    if x in lst:
+    has_duplicates = True
+    return has_duplicates
+    4.4.3 判断一个数是否是素数
```

#### has_duplicates (task/111)

```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+ if set(lst) != set(set(lst)): return True return False
```

#### has_duplicates (task/111)

```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+
+    """ Returns True if some item in the list is also in the list.
+    >>> has_duplicates([1, 2, 2, 3, 2, 1])
+    True
+    >>> has_duplicates([1, 2, 2, 3, 2, 1])
+    False
+    >>> has_
```

#### has_duplicates (task/111)

```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+
+    #We check if any element in lst is repeated
+    for i in lst:
+    if i in lst:
+    return True
+    return False
```

#### has_duplicates (task/111)

```diff
-def has_duplicates(lst):
+def has_duplicates(lst):
+
+    '''Checks if the list has duplicate values in it
+    '''
+    unique_values = []
+    for item in lst:
+    if item not in unique_values:
+    unique_values.append(item)
+    return len(unique_values) == len(lst)
```

#### map_dictionary (task/112)

```diff
-def map_dictionary(itr, fn):
+def map_dictionary(itr, fn):
+
+    for (key, value) in itr:
+    fn(key, value)
+    return itr
```

#### map_dictionary (task/112)

```diff
-def map_dictionary(itr, fn):
+def map_dictionary(itr, fn):
+ return itr, fn
```

#### map_dictionary (task/112)

```diff
-def map_dictionary(itr, fn):
+def map_dictionary(itr, fn):
+ """ map_dictionary(itr, fn) -> dictionary """ if isinstance(itr, tuple): itr = (itr,) cur = {key: value for key, value in itr} return fn(cur)
```

#### map_dictionary (task/112)

```diff
-def map_dictionary(itr, fn):
+def map_dictionary(itr, fn):
+ return itr.map(fn)
+    6.4 Generators
+    A generator function is one that can be paused and resumed, which is particularly useful for producing sequences. One can implement a generator by writing a function that contains a yield statement. When the function is called, it returns a Generator object. This object has a .next
```

#### count_by (task/113)

```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+    counts = defaultdict(int)
+    for x in lst:
+    counts[fn(x)] += 1
+    return counts
```

#### count_by (task/113)

```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+    ''' Count items in list by fn '''
+    return defaultdict(fn)
```

#### count_by (task/113)

```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+    cnt = defaultdict(int)
+    for x in lst:
+    cnt[fn(x)] += 1
+    return cnt
```

#### count_by (task/113)

```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+    counts = defaultdict(int)
+    for i, x in enumerate(lst):
+    if fn(x):
+    counts[fn(x)] += 1
+    return counts
```

#### count_by (task/113)

```diff
-from collections import defaultdict
-
-def count_by(lst, fn = lambda x: x):
+from collections import defaultdict
+
+def count_by(lst, fn = lambda x: x):
+
+    """Returns a dictionary whose keys are the number of occurences of each
+    element in lst and the values are those elements"""
+    dict = defaultdict(int)
+    for x in lst:
+    dict[fn(x)] += 1
+    return dict
```

#### difference_by (task/114)

```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+ if isinstance(a, dict) and not isinstance(b, dict): return dict(x for x in a if fn(x, b) is not None) return a - b
```

#### difference_by (task/114)

```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+ """ Return the difference between `a` and `b` after applying `fn` to each. For example, ``difference_by(1, 2, lambda x: x - 1)`` returns the list ``[0, 1]``. If `fn` returns `None`, use the identity function `id()` instead.
```

#### difference_by (task/114)

```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+ """Return the elements of a which are not in b""" if not a or not b: return [] if isinstance(a, list) and isinstance(b, list): return filter(fn, a) if isinstance(a, set) and isinstance(b, set): return filter(fn, a) if isinstance
```

#### difference_by (task/114)

```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+ # 比较所有的元素后返回比较结果 return [i for i in a if i != b[i]] # 重复最大的长度
```

#### difference_by (task/114)

```diff
-def difference_by(a, b, fn):
+def difference_by(a, b, fn):
+
+    return (a - b) / fn(a, b)
+    I decided to use the Python decorator syntax for the time being, but could have used the full Pythonic approach with state classes as well:
```

#### from_iso_date (task/115)

```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    return d.year, d.month, d.day
```

#### from_iso_date (task/115)

```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    """Create a datetime object from an ISO date string."""
+    d = d.replace(':', '.')
+    y, m, d = d.split('-' if len(d) > 2 else '')
+    return datetime(y, m, d)
```

#### from_iso_date (task/115)

```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    '''Convert an ISO date string to a Python datetime instance.
+    d: An ISO date string.
+    '''
+    m = d.split('T')[0]
+    d = datetime.datetime(m, int(d.split('-')[1]), int(d.split
```

#### from_iso_date (task/115)

```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    """Convert d to a datetime object.
+    D should be a string in the format 'YYYY-MM-DD' or 'YYYYMMDD'.
+    """
+    try:
+    return datetime.strptime(d, '%Y-%m-%d')
+    except Value
```

#### from_iso_date (task/115)

```diff
-from datetime import datetime
-
-def from_iso_date(d):
+from datetime import datetime
+
+def from_iso_date(d):
+
+    """Convert a date string in ISO format to a datetime object."""
+    if d.startswith("-"):
+    return datetime(year=1900+int(d[1:3]), month=d[3:5], day=d[5:7])
+    return datetime(year
```

#### filter_non_unique (task/116)

```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    """ Returns a new list with all duplicates removed.
+    :param lst: list of strings
+    """
+    unique = []
+    seen = {}
+    for s in lst:
+    if s not in seen:
+    seen[s] = True
+    unique.append(s)
```

#### filter_non_unique (task/116)

```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    counter = Counter(lst)
+    return [x for x in lst if x not in counter]
+    with open('my_file.txt') as f:
+    non_unique = filter_non_unique(f.readlines())
+    for line in non_unique:
+    print(line
```

#### filter_non_unique (task/116)

```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    results = Counter()
+    for item in lst:
+    if item in results:
+    results[item] += 1
+    else:
+    results[item] = 1
+    return results
```

#### filter_non_unique (task/116)

```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    return [item for item in lst if item not in lst]
+    bacon_counts = Counter(["bacon", "bacon", "bacon", "bacon", "bacon", "bacon", "bacon", "bacon", "bacon", "bacon", "bacon
```

#### filter_non_unique (task/116)

```diff
-from collections import Counter
-
-def filter_non_unique(lst):
+from collections import Counter
+
+def filter_non_unique(lst):
+
+    # This only works if the unique values are in the first half of the list
+    #
+    # From http://stackoverflow.com/questions/1305863/how-to-remove-duplicates-from-a-list-in-python
+    #
+    # "This is the trick
```

#### symmetric_difference (task/117)

```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+
+    c = []
+    d = []
+    for i in range(len(a)):
+    for j in range(len(b)):
+    if a[i] != b[j]:
+    c.append(a[i])
+    d.append(b[j])
+    return c
```

#### symmetric_difference (task/117)

```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+
+    return reduce(operator.add, a, b)
```

#### symmetric_difference (task/117)

```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+
+    return a + b * (len(a) - len(b))
```

#### symmetric_difference (task/117)

```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+ # The value of a is not changed. c = [] while a != b: c.append(a) a = b b = c return c
+    By using a generator expression, the value of a is not changed, only the reference is copied to c. This eliminates the need for a list in the return statement.
+    So
```

#### symmetric_difference (task/117)

```diff
-def symmetric_difference(a, b):
+def symmetric_difference(a, b):
+
+    if a > b:
+    return {a, b}
+    else:
+    return {b, a}
```

#### snake (task/118)

```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    """ Snakes are nice. """
+    return s
```

#### snake (task/118)

```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    """
+    Return a string of 's' where each letter is replaced with a
+    random English letter in the same position.
+    """
+    sub('', s)
+    # random order
+    for i in range(len(s)):
+    j = random.randint(0, len(s
```

#### snake (task/118)

```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    # Replace all symbols with the same symbol
+    for i in range(len(s)):
+    if s[i] != s[i-1]:
+    if s[i] == '*':
+    for j in range(i+1, len(s)):
+    s[j] =
```

#### snake (task/118)

```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    while len(s)>0:
+    s = s[1:] + s[:-1]
+    s = s[::-1]
+    return s
```

#### snake (task/118)

```diff
-from re import sub
-
-def snake(s):
+from re import sub
+
+def snake(s):
+
+    """Take a string and return a string with a snake on each
+    line, with the snake facing left."""
+    # Note: "q" is the same as "quit". If a user inputs "q",
+    # we have to assume that the user is not interested in
+    # playing the game.
```

#### keys_only (task/119)

```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+ return flat_dict.items()
```

#### keys_only (task/119)

```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+
+    result = {}
+    for key in flat_dict.keys():
+    result[key] = flat_dict[key]
+    return result
```

#### keys_only (task/119)

```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+
+    flat_dict = flat_dict.items()
+    for key in flat_dict:
+    if key not in list (get_keys(flat_dict)):
+    flat_dict.pop(key)
+    return flat_dict
```

#### keys_only (task/119)

```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+ return list(flat_dict.keys())
+    As the name suggests, keys_only will return a list of keys, but not the values.
+    So, that’s it!
+    I hope this article will help you to understand how Python dictionary works internally.
+    If you like what you just read, please consider
```

#### keys_only (task/119)

```diff
-def keys_only(flat_dict):
+def keys_only(flat_dict):
+ # flat_dict is a dictionary with only the keys # return the keys as a list return flat_dict.keys() # keys_only is a function # keys_only = {'a': 1, 'b': 2, 'c': 3} print(keys_only(keys_only)) # ['a', 'b',
```

#### is_odd (task/120)

```diff
-def is_odd(num):
+def is_odd(num):
+
+    return num % 2 == 1
+    
+# Use is_odd to build a statement that calls itself:
```

#### is_odd (task/120)

```diff
-def is_odd(num):
+def is_odd(num):
+
+    """
+    Input: 1,2,3,4,5,6
+    Output: True
+    """
+    if num % 2 == 0:
+    return False
+    else:
+    return True
```

#### is_odd (task/120)

```diff
-def is_odd(num):
+def is_odd(num):
+
+    if num % 2 == 0:
+    return False
+    else:
+    return True
+    #implementing it
+    if is_odd(1):
+    print("1 is odd.")
+    else:
+    print("1 is even.")
+    Output:
+    1 is odd.
+    2
```

#### is_odd (task/120)

```diff
-def is_odd(num):
+def is_odd(num):
+ if num % 2 == 0: return False else: return True is_odd = a @property
```

#### is_odd (task/120)

```diff
-def is_odd(num):
+def is_odd(num):
+
+    """
+    Return True if `num` is odd, False otherwise.
+    """
+    return num % 2 == 1
```

#### group_by (task/121)

```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    """Group a sequence by a key.
+    Like `groupby` but no default value is required.
+    """
+    if not lst:
+    return
+    return defaultdict(list)
```

#### group_by (task/121)

```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    """Return a list of lists with the same length as lst. Each list
+    contains items of lst grouped according to fn(item).
+    >>> group_by(['abc', 'a', 'b', 'c'], str.lower)
+    [('a', 'abc'), ('b', '
```

#### group_by (task/121)

```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    return (defaultdict(list) for x in lst for y in x for fn(y) in y)
```

#### group_by (task/121)

```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    'groupby: return list of lists, where each sublist contains
+    elements that are all equivalent when passed as the first
+    argument to fn'
+    return defaultdict(list)
```

#### group_by (task/121)

```diff
-from collections import defaultdict
-
-def group_by(lst, fn):
+from collections import defaultdict
+
+def group_by(lst, fn):
+
+    """
+    Return a generator that produces lists of items, grouped according to fn(item).
+    Examples
+    --------
+    >>> list(group_by(['abc', 'def'], str.lower))
+    ['a', 'b', 'c', 'd', 'e', 'f']
+    >>>
```

#### to_binary (task/122)

```diff
-def to_binary(n):
+def to_binary(n):
+
+    if n < 0x00100000:
+    n = ((n & 0xFFFFFF) << 21) | ((n >> 21) & 0xFFFFFF)
+    if n < 0x00100000:
+    n = ((n & 0xFFFFFF) << 14) | ((n >> 14)
```

#### to_binary (task/122)

```diff
-def to_binary(n):
+def to_binary(n):
+ return bin(n)[2:]
```

#### to_binary (task/122)

```diff
-def to_binary(n):
+def to_binary(n):
+
+    return bin(n).rjust(8, '0')
```

#### to_binary (task/122)

```diff
-def to_binary(n):
+def to_binary(n):
+ '''convert numbers to binary''' num = n * 2 exponent = math.log(num, 2) + 1 return (num, exponent)
```

#### to_binary (task/122)

```diff
-def to_binary(n):
+def to_binary(n):
+
+    ''' :param n: integer :return: binary representation of n '''
+    b = '0b'
+    for nr in xrange(0, n):
+    b += '1' * (2 ** (nr & 0x f))
+    return b
```

#### compact (task/123)

```diff
-def compact(lst):
+def compact(lst):
+
+    return ''.join(lst)
```

#### compact (task/123)

```diff
-def compact(lst):
+def compact(lst):
+ if len(lst) > 1: return [x for x in lst if x not in lst[1:]] else: return lst[0] >>> lst = ['x', 'y', 'x', 'z'] >>> compact(lst) ['x', 'y', 'z'] >>> compact(['
```

#### compact (task/123)

```diff
-def compact(lst):
+def compact(lst):
+
+    """
+    只要给出n个元素，就可以压缩n个元素，因为压缩后仍是n个元素
```

#### compact (task/123)

```diff
-def compact(lst):
+def compact(lst):
+
+    return lst[1:] if lst[0] == lst[1:] else lst[0]
```

#### compact (task/123)

```diff
-def compact(lst):
+def compact(lst):
+
+    if lst != []:
+    # lst = ['B', 'A', 'C', 'D'] -> lst = ['B', 'A', 'C', 'D']
+    lst = lst[:len(lst)-1] + lst[-1:]
+    return lst
```

#### in_range (task/124)

```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+ """InRange(n, start, end) -> True if n is in the range start <= n < end."""
+    # It would be nice to use the fast C version for this.
+    # But n is not guaranteed to be a native int.
+    n_d = [int(i) for i in n
```

#### in_range (task/124)

```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+ """ Check if a number is in the range given. """ if n >= start and n <= end: return True else: return False
+    Besides the function, we also have a special "class-method" that lets us call this function as a method of a class.
+    >>> class MyClass(object): ...
```

#### in_range (task/124)

```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+
+    return (n >= start and n <= end)
+    
+if __name__ == '__main__':
+    print(0 in_range(5))
+    print(1 in_range(5))
+    print(2 in_range(5))
+    print(3 in_range(5))
```

#### in_range (task/124)

```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+
+    'Binary search for a number in a range'
+    return n >= start and n <= end
```

#### in_range (task/124)

```diff
-def in_range(n, start, end = 0):
+def in_range(n, start, end = 0):
+
+    # we check for the range of the value
+    return (n >= start) and (n <= end)
+    
+class Numeric:
```

#### daterange (task/125)

```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    """
+    Return date objects for the interval.
+    """
+    return (date(end - timedelta(days=1)),
+    date(end - timedelta(days=2)),
+    date(end - timedelta(days=3)),
+    date(end - timedelta(days=4)))
```

#### daterange (task/125)

```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    """Create a date range (start and end)"""
+    return date(start.year, start.month, start.day)
+    + timedelta(days=end.days_from(start))
```

#### daterange (task/125)

```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    """ Given start and end datetimes, return a list of datetimes
+    that represents the duration.
+    """
+    d = timedelta(days=end - start)
+    d += timedelta(days=1)
+    return [d.date()] + list(d.timedelta(days=
```

#### daterange (task/125)

```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    if end < start:
+    return -1, None
+    return start, end
```

#### daterange (task/125)

```diff
-from datetime import timedelta, date
-
-def daterange(start, end):
+from datetime import timedelta, date
+
+def daterange(start, end):
+
+    if not start or not end:
+    raise ValueError('At least one of start or end must be '
+    'defined')
+    if start < end:
+    if end > datetime.max:
+    end = datetime.max
+    if start > datetime.min:
+    start = dat
```

#### chunk (task/126)

```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    if len(lst) <= size:
+    return lst
+    return chunk(lst[:size], size) + lst[size:]
```

#### chunk (task/126)

```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    """
+    Split a list into chunks.
+    """
+    rem = len(lst) % size
+    if rem == 0:
+    return [lst]
+    else:
+    return [lst[:rem] + chunk(lst, size) + lst[rem:]]
```

#### chunk (task/126)

```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    '''Divide a list into equal length pieces'''
+    n = len(lst)
+    chunks = []
+    for i in range(0, n/size):
+    chunks.append(lst[i*size:(i+1)*size])
+    return chunks
```

#### chunk (task/126)

```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    if lst:
+    s = []
+    i = 0
+    lst = list(lst)
+    while i < len(lst):
+    s.append(lst[i])
+    i += 1
+    if i > 0:
+    s[-1] = lst[
```

#### chunk (task/126)

```diff
-from math import ceil
-
-def chunk(lst, size):
+from math import ceil
+
+def chunk(lst, size):
+
+    chunk = []
+    i = 0
+    while i < len(lst):
+    x = lst[i]
+    lst[i] = lst[i+1]
+    lst[i+1] = x
+    chunk.append(x)
+    i += 1
```

#### deep_flatten (task/127)

```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    if isinstance(lst, Iterable):
+    if isinstance(lst, collections.Mapping):
+    return lst
+    else:
+    return deep_flatten(deep_flatten(lst))
+    else:
+    return [lst]
+    
+>>> lst = [[1
```

#### deep_flatten (task/127)

```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    if isinstance(lst, (Iterable, list)):
+    return deep_flatten(iter(lst))
+    else:
+    return [deep_flatten(x) for x in lst]
+    if __name__ == '__main__':
+    lst = [
```

#### deep_flatten (task/127)

```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    """deep_flatten([[1, 2], [3, 4]]) --> [1, 2, 3, 4]"""
+    for el in lst:
+    for lst2 in deep_flatten(el):
+    yield lst2
+    # map函数是Python中
```

#### deep_flatten (task/127)

```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    if isinstance(lst, Iterable):
+    for i in lst:
+    yield from deep_flatten(i)
+    yield from lst
```

#### deep_flatten (task/127)

```diff
-from collections.abc import Iterable
-
-def deep_flatten(lst):
+from collections.abc import Iterable
+
+def deep_flatten(lst):
+
+    """
+    `lst` is a list-like object.
+    Returns a new list where each element is the result of a
+    deep_flatten on its respective element.
+    """
+    return [deep_flatten(x) for x in lst]
```

#### initialize_list_with_values (task/128)

```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+
+    list_with_values = []
+    for i in range(n):
+    list_with_values.append(val)
+    return list_with_values
```

#### initialize_list_with_values (task/128)

```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+
+    result = []
+    for i in range(n):
+    result.append(val)
+    return result
+    4.4.4 不使用可变参数的初始化规则
+    不使用可变参
```

#### initialize_list_with_values (task/128)

```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+
+    self.items = [val] * n
+    self.len = n
```

#### initialize_list_with_values (task/128)

```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+
+    list_with_values = []
+    for i in range(n):
+    list_with_values.append(val)
+    return list_with_values
```

#### initialize_list_with_values (task/128)

```diff
-def initialize_list_with_values(n, val = 0):
+def initialize_list_with_values(n, val = 0):
+ + for i in range(n): + this_list.append(val) + +
```

#### average_by (task/129)

```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+
+    return sum(lst) / float(len(lst))
```

#### average_by (task/129)

```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+ return reduce(lambda x, y: x + y, lst, 0) / (len(lst) if fn else lambda x: x) if (len(lst) > 0) else 0
+    """
```

#### average_by (task/129)

```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+ return sum(fn(i) for i in lst) / len(lst)
+    In a sense, these two definitions of the average_by function are equivalent. However, the second version is more succinct and avoids repeating the argument x in the body of the function. In general, using lambda as an abbreviation for a function
```

#### average_by (task/129)

```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+
+    lst = list(lst)
+    total = 0
+    for x in lst:
+    total += fn(x)
+    return total/len(lst)
```

#### average_by (task/129)

```diff
-def average_by(lst, fn = lambda x: x):
+def average_by(lst, fn = lambda x: x):
+ avg = 0.0 for x in lst: avg += fn(x) return avg
+    avg_num = average_by(lst, lambda x: x)
+    $ time python fibonacci_average.py 50 Real: 0m0.095s
+    1000000
+    1000000
```

#### key_of_max (task/130)

```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    return d.max()
```

#### key_of_max (task/130)

```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    if d is KeyError:
+    return -1
+    elif d is int:
+    return d
+    elif d is str:
+    try:
+    return int(d)
+    except ValueError:
+    return -1
+    elif d is dict:
+    return max(d.
```

#### key_of_max (task/130)

```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    return d.keys()[0]
```

#### key_of_max (task/130)

```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    return d.get('_key', None)
```

#### key_of_max (task/130)

```diff
-def key_of_max(d):
+def key_of_max(d):
+
+    """
+    Returns the key of the highest value in the
+    dictionary.
+    """
+    return d.keys()[d.max()]
```

#### offset (task/131)

```diff
-def offset(lst, offset):
+def offset(lst, offset):
+
+    """ offset函数统计某个实体在某一列中的最小值，且如果有不存在就为0
+    """
+    if lst
```

#### offset (task/131)

```diff
-def offset(lst, offset):
+def offset(lst, offset):
+ return lst[offset]
+    However, this is not a good solution. If you want to remove the offset from the list, you need to remember to call this function with an offset of zero. If you forget and call the function with an offset of one, the offset will be included in the result. This is really a problem with
```

#### offset (task/131)

```diff
-def offset(lst, offset):
+def offset(lst, offset):
+ """Return a slice of lst from offset to the end of the list.""" return lst[offset:offset+1]
```

#### offset (task/131)

```diff
-def offset(lst, offset):
+def offset(lst, offset):
+
+    lst = lst[:offset] + lst[offset:]
+    return lst
```

#### offset (task/131)

```diff
-def offset(lst, offset):
+def offset(lst, offset):
+
+    """
+    """
+    return lst[offset]
```

#### intersection_by (task/132)

```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+ ...
```

#### intersection_by (task/132)

```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+ try: return fn(a, b) except TypeError: return lambda x, y: x == y intersection_by(1, 2, lambda x, y: x > y) #=> 2 intersection_by(1, 2, lambda x, y: x <= y) #=> 2 intersection_by(1, 2,
```

#### intersection_by (task/132)

```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+ return len(set(a).intersection(set(b))) a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] b = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

#### intersection_by (task/132)

```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+
+    if type(a) is type(b):
+    return lambda x: (fn(x, a) if fn(x, a) else x)
+    else:
+    return lambda x: (fn(x, b) if fn(x, b) else x)
+    #
+    # Compute
```

#### intersection_by (task/132)

```diff
-def intersection_by(a, b, fn):
+def intersection_by(a, b, fn):
+ """ `intersection_by(a, b, fn)` returns a dictionary whose keys are all the elements of `a` that are also in `b`, and whose values are the same as `f(k)` for each key `k` in `a` also in `b`. >>> intersection_by([1, 2
```

#### union_by (task/133)

```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+
+    + return type(a) is type(b) and a.union_by(b, fn)
+    +
+    +
```

#### union_by (task/133)

```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+ return a.union_by(b, fn) >>> Union(set([1, 2, 3]), set([2, 3, 4, 5, 6])) {1, 2, 3, 4, 5, 6}
+    优雅的统计函数
+    >>>
```

#### union_by (task/133)

```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+ return {k: v for k, v in zip(a, b) if fn(k, v)}\r
+    result = {10: 1, 11: 2, 12: 3, 13: 4, 14: 5}\r
+    for i in range(1, 15):\r
+    print('union_
```

#### union_by (task/133)

```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+
+    if isinstance(a, tuple) and isinstance(b, tuple):
+    return tuple(union_by(a, b, fn))
+    else:
+    return fn(a, b)
```

#### union_by (task/133)

```diff
-def union_by(a, b, fn):
+def union_by(a, b, fn):
+
+    result = []
+    for x in a:
+    if x in b:
+    result.append(fn(x, b[x]))
+    return result
```

#### all_unique (task/134)

```diff
-def all_unique(lst):
+def all_unique(lst):
+ """returns all unique elements in lst""" unique = [] for item in lst: if item not in unique: unique.append(item) return unique
```

#### all_unique (task/134)

```diff
-def all_unique(lst):
+def all_unique(lst):
+ """ >>> a = [1, 2, 2, 2, 3, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 10] >>> all_unique(a) [1, 2, 3, 4, 5, 6, 7, 8, 9
```

#### all_unique (task/134)

```diff
-def all_unique(lst):
+def all_unique(lst):
+ lst.sort() for i in range(len(lst)): if (lst[i] != lst[i+1]): return True return False #lst = ["AAA", "BBB", "CCC", "DDD", "EEE"] #lst.sort() #print(all_unique(
```

#### all_unique (task/134)

```diff
-def all_unique(lst):
+def all_unique(lst):
+ return list(set(lst))
```

#### all_unique (task/134)

```diff
-def all_unique(lst):
+def all_unique(lst):
+ """ filter out duplicate elements from list lst""" if not lst: return [] return set(lst)
```

#### pluck (task/135)

```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    raise NotImplementedError()
```

#### pluck (task/135)

```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    result = []
+    for e in lst:
+    if e[key] == key:
+    result.append(e)
+    return result
```

#### pluck (task/135)

```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    """
+    Return a list with the values of `key` found in `lst`
+    """
+    return [v for k, v in lst if key == k]
```

#### pluck (task/135)

```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    if key in lst:
+    return lst[key]
+    else:
+    return None
+    val_dict.update(pluck(data, 'type'))
+    In the preceding code, we first read the data attribute of the form to get the list of data fields, then we go through each
```

#### pluck (task/135)

```diff
-def pluck(lst, key):
+def pluck(lst, key):
+
+    return getattr(lst, key)
```

#### for_each (task/136)

```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+ for elem in itr: fn(elem) for elem in for_each(itr): fn(elem)
+    In this case, for_each is an iterable factory, which produces an iterable that loops over all items in the iterable it receives as an argument. We call for_each with an
```

#### for_each (task/136)

```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+ for item in itr: fn(item)
+    for_each.py
```

#### for_each (task/136)

```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+ return [fn(x) for x in itr]
+    
+Then, we can write:
+    for_each(sorted(v), lambda x: x**2)
+    
+Or, we can write:
+    for_each(sorted(v), lambda x, y: x + y)
+    
+This id
```

#### for_each (task/136)

```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+ pass for_each(range(5), print)
+    
+The for_each function defines the function (fn) that will be called for each item in the iteration. The function (fn) will be called as itr.fn(itr), so the variable itr must be defined in the function (fn). In this case,
```

#### for_each (task/136)

```diff
-def for_each(itr, fn):
+def for_each(itr, fn):
+ + return [fn(x) for x in itr] + +
```

#### every (task/137)

```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+ return lambda x: fn(x) if isinstance(lst, list) else [fn(x) for x in lst]
```

#### every (task/137)

```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+ """Generate a stream that passes every element through the given function""" if not lst: return while True: x = lst.pop(0) if fn(x): yield x
```

#### every (task/137)

```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+ return [fn(x) for x in lst]
```

#### every (task/137)

```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+ if not lst: return lst return [fn(x) for x in lst]
+    To make this a little clearer, here's an example of using it:
+    >>>
```

#### every (task/137)

```diff
-def every(lst, fn = lambda x: x):
+def every(lst, fn = lambda x: x):
+ """Converts [lst] into a list of 1s where fn returns true, and 0s otherwise""" if all(fn(x) for x in lst): return [1] else: return [0]
+    4.3.3 . . . . . . . . . . . . . . . . .
```

#### byte_size (task/138)

```diff
-def byte_size(s):
+def byte_size(s):
+
+    return struct.calcsize(s)
```

#### byte_size (task/138)

```diff
-def byte_size(s):
+def byte_size(s):
+
+    for char in s:
+    if char in string.digits:
+    return 1
+    return 2
```

#### byte_size (task/138)

```diff
-def byte_size(s):
+def byte_size(s):
+
+    # size in bytes of a str instance
+    return struct.calcsize(s)
+    
+class StrUnpickler(object):
+    """Unpickler for the new str type."""
```

#### byte_size (task/138)

```diff
-def byte_size(s):
+def byte_size(s):
+
+    size = 0
+    for c in s:
+    size += 1
+    
+    return size
```

#### byte_size (task/138)

```diff
-def byte_size(s):
+def byte_size(s):
+
+    return struct.calcsize(struct.pack('>L', len(s)))
```

#### pad_number (task/139)

```diff
-def pad_number(n, l):
+def pad_number(n, l):
+
+    if l < 0:
+    return n - int(n / l) * l
+    return n
```

#### pad_number (task/139)

```diff
-def pad_number(n, l):
+def pad_number(n, l):
+
+    n = int(n)
+    for i in range(len(n)):
+    n = "0" + n
+    return n
```

#### pad_number (task/139)

```diff
-def pad_number(n, l):
+def pad_number(n, l):
+ # returns string of l 0s appended to n if n <= 0: return '0' else: return str(n) + '0' * (l - len(str(n))) i = 0 for arg in arg_list: i += 1 for j in range(i): arg_list[j] = arg_
```

#### pad_number (task/139)

```diff
-def pad_number(n, l):
+def pad_number(n, l):
+
+    n = int(n)
+    if n < 0:
+    n = -n
+    if n % 10 == 0:
+    n = '0' + n
+    return n
+    
+print(pad_number(7, 4))
+    print(pad_number(-7, 4))
+    print
```

#### pad_number (task/139)

```diff
-def pad_number(n, l):
+def pad_number(n, l):
+ if n < 0: n = -n elif n > 9999: n = 9999 else: n = n + 0 pad_number = lambda n, l: '%0%i' % (n, l) # Pad a number to a given length.
```

#### for_each_right (task/140)

```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+
+    # from pypy.objspace.std.container import Iterator, Container
+    #
+    # itr = Iterator(itr)
+    # container = Container(container)
+    # try:
+    # while True:
+    # try:
+    # try:
+    # itr.
```

#### for_each_right (task/140)

```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+
+    i = 0
+    while i < len(itr):
+    fn(i)
+    i += 1
```

#### for_each_right (task/140)

```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+ + for_each_right(itr, fn, False) # calling for_each_right with argument True +
```

#### for_each_right (task/140)

```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+
+    + for_each_right(itr, fn):
+    # Go through the right node entries and find all of the
+    # right-most nodes that are not already in the rightmost tree.
+    - right_root = right_leaf.find_rightmost_node(right_root)
+    -
```

#### for_each_right (task/140)

```diff
-def for_each_right(itr, fn):
+def for_each_right(itr, fn):
+ # ...
+    for_each_right() is a function that works like for_each() , except that it iterates through a container in a right-to-left order. This allows you to use it to process the right-most element of the iterable first, and works well when the iteration is driven by the call to each
```

#### is_anagram (task/141)

```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    """Check if two strings are anagrams."""
+    return any(c1 == c2 for c1, c2 in zip(s1, s2))
+    
+if __name__ == '__main__':
+    import operator
+    print("Operator Method:")
+    c1 = Counter('
```

#### is_anagram (task/141)

```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    """Return True if strings s1 and s2 are anagrams.
+    Anagrams are words that can be rearranged to form another
+    word, e.g. \"mice\" and \"cime\" are anagrams of each other.
+    >>> is_anagram('bbbb', 'aaa
```

#### is_anagram (task/141)

```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    """
+    Returns True if s1 and s2 are anagrams, False otherwise.
+    s1 and s2 can be either str or unicode objects.
+    """
+    c1 = Counter(s1)
+    c2 = Counter(s2)
+    return all(c1.get(
```

#### is_anagram (task/141)

```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    """
+    :param s1:
+    :param s2:
+    :return:
+    """
+    """
+    s1 = s1.lower()
+    s2 = s2.lower()
+    return s1.isidentical(s2) and len(s1) == len(
```

#### is_anagram (task/141)

```diff
-from collections import Counter
-
-def is_anagram(s1, s2):
+from collections import Counter
+
+def is_anagram(s1, s2):
+
+    "Returns True if s1 and s2 are anagrams"
+    return s1.lower() == s2.lower() and \
+    list(set(s1) & set(s2)) == set([])
```

#### decapitalize (task/142)

```diff
-def decapitalize(s, upper_rest = False):
+def decapitalize(s, upper_rest = False):
+
+    """
+    returns the string s with non-capitalized letters replaced with their lowercase
+    equivalents. If upper_rest is True, the rest of the string is also
+    decapitalized.
+    """
+    if upper_rest:
+    return s.upper() + s[:1
```

#### decapitalize (task/142)

```diff
-def decapitalize(s, upper_rest = False):
+def decapitalize(s, upper_rest = False):
+
+    """
+    Replace digits in `s` with the first letter of their name.
+    If `upper_rest` is `True`, keep the rest of the letters as is.
+    """
+    # int-like semantics:
+    # ```
+    # >>> decapitalize("1000000")
```

#### decapitalize (task/142)

```diff
-def decapitalize(s, upper_rest = False):
+def decapitalize(s, upper_rest = False):
+
+    """
+    Decapitalizes a string or a portion of a string.
+    Does not work with ASCII characters.
+    """
+    if upper_rest:
+    return s.upper() + s[1:].lower()
+    else:
+    return s.lower() + s[1:].upper
```

#### decapitalize (task/142)

```diff
-def decapitalize(s, upper_rest = False):
+def decapitalize(s, upper_rest = False):
+ return s if upper_rest else s.capitalize()
+    >>>
```

#### unique_elements (task/143)

```diff
-def unique_elements(li):
+def unique_elements(li):
+
+    """
```

#### unique_elements (task/143)

```diff
-def unique_elements(li):
+def unique_elements(li):
+ if len(li) == 0: return [] else: return [e for e in li if e not in li[1:]]
+    (4) 查询记录库
+    我们可以使用上面的小程序
```

#### unique_elements (task/143)

```diff
-def unique_elements(li):
+def unique_elements(li):
+
+    7. for element in li:
+    8. yield element
```

#### unique_elements (task/143)

```diff
-def unique_elements(li):
+def unique_elements(li):
+
+    x = set()
+    for elem in li:
+    if elem not in x:
+    x.add(elem)
+    return x
```

#### unique_elements (task/143)

```diff
-def unique_elements(li):
+def unique_elements(li):
+
+    unique_elements = []
+    for elem in li:
+    if elem not in unique_elements:
+    unique_elements.append(elem)
+    return unique_elements
```

#### rgb_to_hex (task/144)

```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+
+    """Convert RGB color to #RRGGBB format"""
+    return r + r * 6 , g + g * 6 , b + b * 6
```

#### rgb_to_hex (task/144)

```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+ return (r << 16) + (g << 8) + b
```

#### rgb_to_hex (task/144)

```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+
+    """Convert RGB values to hex string.
+    """
+    return '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))
```

#### rgb_to_hex (task/144)

```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+
+    '''Convert an RGB color to a hex string'''
+    if r > 255 or g > 255 or b > 255:
+    raise ValueError('rgb value out of range: %r' % (r,))
+    hexstr = '#'
+    if r > g > b:
```

#### rgb_to_hex (task/144)

```diff
-def rgb_to_hex(r, g, b):
+def rgb_to_hex(r, g, b):
+
+    """Returns hex color code for given RGB values"""
+    return " %02x%02x%02x " % (r, g, b)
```

#### values_only (task/145)

```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+
+    """
+    This method returns a flattened dict, for example dict(a=1, b=2) -> {'a': 1, 'b': 2}
+    """
+    flat_dict = {}
+    for (k, v) in flat_dict.items():
+    flat_dict[k] =
```

#### values_only (task/145)

```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+ flat_dict = flat_dict.copy() return flat_dict.values() # This just builds a dictionary that is two entries # longer than the value of the max_flat_dict_len max_flat_dict_len = 10 # This builds the dictionary to use for the flat dictionary # and then flattens it. flat_
```

#### values_only (task/145)

```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+
+    # Convert flat dict to list of unique values
+    flat_dict_values = []
+    for item in flat_dict:
+    flat_dict_values.append(item)
+    return flat_dict_values
```

#### values_only (task/145)

```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+ if not flat_dict.get('last_update', None): return flat_dict return flat_dict
```

#### values_only (task/145)

```diff
-def values_only(flat_dict):
+def values_only(flat_dict):
+ """Return only the values from a flat dict""" values = flat_dict.values() if values: return values else: return []
```

#### unfold (task/146)

```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+
+    """Get a generator that computes items in the cartesian product.
+    Args:
+    fn: function that returns an item of the cartesian product.
+    seed: an item of the cartesian product.
+    Returns:
+    A generator that yields all items of the cartesian product.
+    """
```

#### unfold (task/146)

```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+ # The stack is [seed, fn()]
```

#### unfold (task/146)

```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+
+    # Binary search to find the insertion point.
+    # (Note that this *starts* at the end of the list.)
+    pos = len(self) - 1
+    while pos >= 0:
+    key = (seed ^ self[pos]) & (2 ** 32 - 1)
+    if key in
```

#### unfold (task/146)

```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+
+    return (fn(seed), fn(seed))
```

#### unfold (task/146)

```diff
-def unfold(fn, seed):
+def unfold(fn, seed):
+
+    719 return (mul(fn, seed), add(mul(fn, seed), seed))
+    720 # Defining an initial state
+    721
```

#### reverse (task/147)

```diff
-def reverse(itr):
+def reverse(itr):
+
+    global alpha
+    if not alpha:
+    alpha = len(itr)
+    for n in range(alpha, 0, -1):
+    itr[n] = itr[0:n]
+    return itr
```

#### reverse (task/147)

```diff
-def reverse(itr):
+def reverse(itr):
+
+    return [value for value in itr]
+    # Finalize the list of rules
+    return rules
```

#### reverse (task/147)

```diff
-def reverse(itr):
+def reverse(itr):
+
+    """given a list returns a reversed copy of it"""
+    if not isinstance(itr, list):
+    return [itr]
+    return [x for x in itr[::-1]]
```

#### reverse (task/147)

```diff
-def reverse(itr):
+def reverse(itr):
+
+    - """Return an iterator to the last index of the reversed iterator.
+    - """
+    - for x in itr:
+    - yield x
+    - return itr
+    -
+    -class Queue:
+    - """A queue class.
+    - A queue is a first-in-first
```

#### reverse (task/147)

```diff
-def reverse(itr):
+def reverse(itr):
+
+    for i in range(len(itr)):
+    if itr[i] < itr[i-1]:
+    itr[i], itr[i-1] = itr[i-1], itr[i]
+    return itr
+    
+    # main method
+    if
```

#### is_divisible (task/148)

```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+ divisor = divisor.lower() return dividend % divisor == 0
+    The is_divisible function compares the remainder of dividing the first argument by the second argument, and returns True if the result is 0, and False otherwise.
+    See the section if Statement for a description of the if statement, and the section
```

#### is_divisible (task/148)

```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+
+    """
+    dividend and divisor are ints
+    dividend is not 0
+    divisor is not 0
+    """
+    return True
+    """
+    Square root
+    https://docs.python.org/2/library/math.html#math.sqrt
+    http
```

#### is_divisible (task/148)

```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+ """Return True if the divisor is divisible by the dividend""" while divisor > 0: if dividend % divisor == 0: return True divisor = divisor - 1 return False
+    It's also possible to use the shorthand syntax of the ** operator if it's clear from the code that the argument is
```

#### is_divisible (task/148)

```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+ return (dividend % divisor) == 0
```

#### is_divisible (task/148)

```diff
-def is_divisible(dividend, divisor):
+def is_divisible(dividend, divisor):
+
+    if dividend % divisor == 0:
+    return True
+    else:
+    return False
+    
+    if __name__ == '__main__':
+    import sys
+    if sys.version_info[0] == 2:
+    print "2.x version"
+    else:
+    print
```

#### is_weekday (task/149)

```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    return d.day >= 5 and d.day <= 2
+    if __name__ == '__main__':
+    import sys
+    if len(sys.argv) != 2:
+    print("USAGE:", sys.argv[0], "URL")
+    exit(1)
+    url
```

#### is_weekday (task/149)

```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    return d.weekday() in [0, 6]
```

#### is_weekday (task/149)

```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    if d.weekday() == 5:
+    return True
+    else:
+    return False
+    if __name__ == "__main__":
+    print is_weekday(datetime.today())
+    print is_weekday(datetime.today() + timedelta(days=1))
```

#### is_weekday (task/149)

```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    s = d.strftime('%A')
+    return s.startswith('Mon') or s.startswith('Tue') or s.startswith('Wed') or s.startswith('Thu') or s.startswith('Fri') or s.startswith('Sat') or s
```

#### is_weekday (task/149)

```diff
-from datetime import datetime
-
-def is_weekday(d = datetime.today()):
+from datetime import datetime
+
+def is_weekday(d = datetime.today()):
+
+    if (d.weekday() == 0):
+    return False
+    return True
+    When it comes to the actual testing itself, we’ll use the core unittest module and have a number of tests we want to check for. For this, we’ll also have to write a number of helper functions
```

#### fahrenheit_to_celsius (task/150)

```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+
+    return degrees - 32.0
+    Example:
+    >>> print(fahrenheit_to_celsius(100)) 50.0 >>> print(fahrenheit_to_celsius(200)) 100.0 >>> print(fahrenheit_to_celsius(250)) 150.0 >>> print
```

#### fahrenheit_to_celsius (task/150)

```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+
+    return (degrees - 32) * 5 / 9
```

#### fahrenheit_to_celsius (task/150)

```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+ """Convert Fahrenheit degrees to Celsius.""" return degrees * 1.8 + 32
+    The name of a function can be anything you want, as long as it obeys the rules for identifiers (see the sidebar).
+    Arguments and Parameters
+    Functions are called by writing the function’s name followed by a list of
```

#### fahrenheit_to_celsius (task/150)

```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+ """Given a number of degrees in Fahrenheit, return the number of degrees in Celsius.""" return degrees * (5.0/9.0) + 32.0
+    If you are familiar with C or C++, you can think of the return statement as an early return from a function. The equivalent of the return statement in C is
```

#### fahrenheit_to_celsius (task/150)

```diff
-def fahrenheit_to_celsius(degrees):
+def fahrenheit_to_celsius(degrees):
+ # degrees is the number of degrees Fahrenheit to convert. return (degrees-32)*5/9.0
```

#### sum_by (task/151)

```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+
+    return reduce(lambda a, b: a + b, lst, 0)
+    print(sum_by([2, 3, 1, 4, 7, 8], sum))
+    
+In the preceding example, we have a function sum_by, which takes a list and a function as an argument. This function can
```

#### sum_by (task/151)

```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+ total = 0 for value in lst: total += fn(value) return total
+    In the first example, the programmer is thinking about what is necessary to perform the task. In the second example, the programmer is thinking about the properties of the task itself.
+    Now, let's look at the class to see how it works.
```

#### sum_by (task/151)

```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+
+    return reduce(lambda x, y: x + y, lst, 0)
+    print(sum_by([1,2,3,4,5], lambda x: x**2))
+    print(sum_by([1,2,3,4,5], lambda x: x**2, 0
```

#### sum_by (task/151)

```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+ return reduce(lambda x, y: x + y, lst, 0)
+    This is a tail-recursive implementation of a sum. So, if we pass a list of numbers, it will add them up and return the result.
+    >>> sum_by([1, 2, 3, 4, 5], lambda x
```

#### sum_by (task/151)

```diff
-def sum_by(lst, fn):
+def sum_by(lst, fn):
+
+    ret = 0
+    for e in lst:
+    ret += fn(e)
+    return ret
+    In Python, the lambda is implemented using the
```

#### find_key (task/152)

```diff
-def find_key(dict, val):
+def find_key(dict, val):
+ return val in dict
```

#### find_key (task/152)

```diff
-def find_key(dict, val):
+def find_key(dict, val):
+
+    """
+    Returns True if a key exists, otherwise False.
+    """
+    for key in sorted(dict.keys()):
+    if dict[key] == val:
+    return True
+    return False
```

#### find_key (task/152)

```diff
-def find_key(dict, val):
+def find_key(dict, val):
+
+    for key in sorted(dict.keys()):
+    if key == val:
+    return key
+    return None
```

#### find_key (task/152)

```diff
-def find_key(dict, val):
+def find_key(dict, val):
+
+    """
+    Find the key in the dictionary that matches the given value.
+    If the value is not a key in the dictionary, raise a KeyError.
+    """
+    if val in dict:
+    return dict[val]
+    else:
+    raise KeyError('Key \'%s\' not found'
```

#### find_key (task/152)

```diff
-def find_key(dict, val):
+def find_key(dict, val):
+
+    for key in dict:
+    if key == val:
+    return key
+    return None
```

#### to_hex (task/153)

```diff
-def to_hex(dec):
+def to_hex(dec):
+
+    """
+    Convert a number to a four-digit base-16 number in hexadecimal.
+    """
+    return ' { :04x } ' .format(dec)
```

#### to_hex (task/153)

```diff
-def to_hex(dec):
+def to_hex(dec):
+
+    return '{:04x}'.format(dec)
```

#### to_hex (task/153)

```diff
-def to_hex(dec):
+def to_hex(dec):
+ return "0x%x" % dec
+    +
+    + #
+    + # It is assumed that the given bytes do NOT have a 0x00 prefix
+    + #
+    +
+    + # Convert the ascii hex string in hex to a byte sequence with
+    + # binary representation in hex.
```

#### to_hex (task/153)

```diff
-def to_hex(dec):
+def to_hex(dec):
+
+    """Convert to hexadecimal number string."""
+    if dec < 0:
+    raise ValueError("Non-numeric value: %s" % dec)
+    elif dec == 0:
+    return "0"
+    return str(dec)[2:]
+    
+    class LPLayer(
```

#### to_hex (task/153)

```diff
-def to_hex(dec):
+def to_hex(dec):
+ return dec.encode('hex') To convert to an int, use the int() function: >>> int(to_hex(11234)) 11234 The bytes module has more functions for working with binary data. For example, to pad a number with zeros on the left, use the bytes.pad() function: >>> import bytes >>>
```

#### clamp_number (task/154)

```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+ return a if num < a else b
+    When you run the above code, it prints:
+    9 5
+    As expected. But what about the following:
+    >>>
```

#### clamp_number (task/154)

```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+ if num < a: return a if num > b: return b return num
```

#### clamp_number (task/154)

```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+
+    if num < a:
+    return a
+    elif num > b:
+    return b
+    else:
+    return num
```

#### clamp_number (task/154)

```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+ if num > b: return b if num < a: return a else: return num
+    Here, the function takes two arguments (a and b) and returns a single number. The function is a one-to-one map from the domain to the range. If either of the arguments are null, then the result will be null.
```

#### clamp_number (task/154)

```diff
-def clamp_number(num, a, b):
+def clamp_number(num, a, b):
+
+    assert a <= b
+    return num
```

#### compose_right (task/155)

```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    r = reduce(lambda x, y: x(y), fns, None)
+    return r(None)
+    # create a new decorator, @approximate, which calls the decorated function
+    # with the provided tolerance and returns the result
+    @approximate(1e-7)
```

#### compose_right (task/155)

```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    return reduce(lambda x, y: x(y), fns, None)
+    The classic use case for this is to define a new function that calls multiple others, where you have no use for the return value from any of the functions. As an example, suppose we wanted to generate a new random number each time we call
```

#### compose_right (task/155)

```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    """compose fns right to left"""
+    # XXX make clear how to handle the case of different
+    # arities
+    fns = [reduce(lambda x, y: x(y)(*fns[-1])(*fns[:-1]))]
+    return reduce(lambda
```

#### compose_right (task/155)

```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    """
+    Return a fn that is the right composition of a list of fns.
+    """
+    return reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)
+    # The original source of this reduction is unknown.
```

#### compose_right (task/155)

```diff
-from functools import reduce
-
-def compose_right(*fns):
+from functools import reduce
+
+def compose_right(*fns):
+
+    #print "composing fns"
+    result = fns[-1](fns[-2](*fns[-3:]))
+    return reduce(operator.add, fns, result)
+    #sum [1,2,3] = reduce(operator.add, [1,2
```

#### days_diff (task/156)

```diff
-def days_diff(start, end):
+def days_diff(start, end):
+
+    """Calculate the number of days between two datetime.datetime
+    objects.
+    """
+    return (end - start).days
```

#### days_diff (task/156)

```diff
-def days_diff(start, end):
+def days_diff(start, end):
+ end = time.mktime(end.timetuple()) return (end - start).days
```

#### days_diff (task/156)

```diff
-def days_diff(start, end):
+def days_diff(start, end):
+ """ Finds the number of days difference between two datetime objects """ d1 = datetime.datetime(start.year, start.month, start.day) d2 = datetime.datetime(end.year, end.month, end.day) return d2 - d1.date() - d1.days
```

#### days_diff (task/156)

```diff
-def days_diff(start, end):
+def days_diff(start, end):
+ diff = end - start if diff < 0: return "in the future" elif diff == 0: return "today" elif diff < 60: return str(diff).zfill(2) + " minute" elif diff < 3600: return str(diff/60).zfill(2) + " hour" el
```

#### days_diff (task/156)

```diff
-def days_diff(start, end):
+def days_diff(start, end):
+
+    start = datetime.datetime.utcfromtimestamp(start)
+    end = datetime.datetime.utcfromtimestamp(end)
+    d = timedelta(days=end-start)
+    return d.days
```

#### is_contained_in (task/157)

```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+ # A and B must be sets. # If they are the same set, they are contained in each other. if a == b: return True # elif they have different sizes, then there are items # in a that are not in b, and vice versa. return a.size != b.size # elif a is a proper
```

#### is_contained_in (task/157)

```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+ # Your code here return 0
+    这个函数的功能是判断一个数是否属于另一个数组中，下面是使用这个函数
```

#### is_contained_in (task/157)

```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+
+    return (a < b) and (b < a)
```

#### is_contained_in (task/157)

```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+ return a.contains(b) or b.contains(a) or a == b or b == a or a.is_subset_of(b) or b.is_subset_of(a)
+    The definition above uses the or operator. This is the right thing to do if you have to decide
```

#### is_contained_in (task/157)

```diff
-def is_contained_in(a, b):
+def is_contained_in(a, b):
+
+    """Raises ValueError if `a` and `b` are disjoint sets."""
+    if not a.intersection(b) == None:
+    raise ValueError('Cannot test containment in a disjoint set.')
+    if not b.intersection(a) == None:
```

#### drop_right (task/158)

```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+
+    if n == 1:
+    return a
+    elif n % 2 == 0:
+    return a + a
+    else:
+    return a - a
+    
+    # 'seed' is just a simple list.
+    # return the first element of 'seed'
```

#### drop_right (task/158)

```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+
+    + """Drop the rightmost n elements of a list.
+    +
+    + >>> drop_right([1, 2, 3, 4, 5, 6, 7, 8])
+    + [1, 2, 3, 4, 5, 6, 7]
+    + """
+    + return list(a
```

#### drop_right (task/158)

```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+ for i in range(1, n): a = a[:i] + a[i+1:] return a
+    This version is the same as the version in the previous section, except that it uses two variables a and n and two loops instead of one.
+    The while loop is entered on line 4 and exited on line
```

#### drop_right (task/158)

```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+
+    if (a.endswith('0') and len(a) > n):
+    return a[:n] + '0' + a[-n:]
+    else:
+    return a
```

#### drop_right (task/158)

```diff
-def drop_right(a, n = 1):
+def drop_right(a, n = 1):
+
+    """Drop rightmost `n` elements of `a`."""
+    return a[n:]
```

#### gcd (task/159)

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
+    The following lines give the definition of the private methods _lt (less than) and _le (less than or equal). The first one returns 1 when the first parameter is smaller than the second one, 0 otherwise. The second one returns 1 when the first parameter is smaller than or equal to the second one, 0 otherwise.
```

