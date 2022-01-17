### head (task/1)

#### canonical solution
```php
function head($items)
{  return reset($items);
}
```

#### solution 0
```diff
-function head($items)
-{
+function head($items)
+{
+ foreach ($items as $item) { $this->items[] = $item; } } }
+$items = array(1, 2, 3, 4, 5); $arr = new ArrayHead($items); echo $arr->
```

#### solution 1
```diff
-function head($items)
-{
+function head($items)
+{
+ echo "<table width=100% border=1 cellspacing=0 cellpadding=0><tr>"; foreach($items as $k=>$v) { echo "<td align=center valign=top><font color=$v
```

#### solution 2
```diff
-function head($items)
-{
+function head($items)
+{
+foreach from=$items item=item}
+{if $item.operation == "ADD"
+{set $i++
+}
+
+{/if}
+
+{/foreach}
+</programlisting>
+
+In
```

#### solution 3
```diff
-function head($items)
-{
+function head($items)
+{
+ $last = $items[count($items)-1]; $first = $items[0]; return $last['title'] . " – " . $first['title']; }
+$books = array( array('title'=>'
```

#### solution 4
```diff
-function head($items)
-{
+function head($items)
+{
+     return $items[0];     }
+function last($items)
+{     return $items[count($items)-1];     }
+$items = array('first','second','third','fourth','fifth');
```

### median (task/2)

#### canonical solution
```php
function median($numbers)
{  sort($numbers);
  $totalNumbers = count($numbers);
  $mid = floor($totalNumbers / 2);

  return ($totalNumbers % 2) === 0 ? ($numbers[$mid - 1] + $numbers[$mid]) / 2 : $numbers[$mid];
}
```

#### solution 0
```diff
-function median($numbers)
-{
+function median($numbers)
+{
+ $sum = 0; $count = 0; $divisor = 1; $quotient = 0; $remainder = 0; foreach ($numbers as $number) { $count++; $sum += $number;
```

#### solution 1
```diff
-function median($numbers)
-{
+function median($numbers)
+{
+ return $numbers[(($numbers.length - 1) / 2)]; }
+
+and then we can do things like this:
+
+echo median(range(0, 10)); // 3
+
+To be more specific,
```

#### solution 2
```diff
-function median($numbers)
-{
+function median($numbers)
+{
+
+
+function sum($array)
+
+function avg($array)
+
+function stdev($array)
+
+function range($number, $number2)
+
+function random()
+
+function array_sum($array)
+
+function
```

#### solution 3
```diff
-function median($numbers)
-{
+function median($numbers)
+{
+
+}
+
+An example usage of this function might be:
+$median = median(array('one', 'three', 'eight', 'sixteen'));
+$median = median(
+It is possible to consider that an
```

#### solution 4
```diff
-function median($numbers)
-{
+function median($numbers)
+{
+ $total = 0;
+for ($i = 0; $i < $numbers; $i++) {
+$total += $numbers[$i];
+}
+return $total / count($numbers);
+}
+
```

### take (task/3)

#### canonical solution
```php
function take($items, $n = 1)
{  return array_slice($items, 0, $n);
}
```

#### solution 0
```diff
-function take($items, $n = 1)
-{
+function take($items, $n = 1)
+{
+
+
+if (empty($items)) {
+
+echo "No items selected";
+
+} else {
+
+if ($n == 1) {
+
+echo "1 selected";
+
+} else {
+
+echo "";
+
```

#### solution 1
```diff
-function take($items, $n = 1)
-{
+function take($items, $n = 1)
+{
+ for ($i = 0; $i < $n; $i++) { $items[$i] = "Part " . $i; } return $items; }
+
+This is a naive implementation that might work on small arrays,
```

#### solution 2
```diff
-function take($items, $n = 1)
-{
+function take($items, $n = 1)
+{
+ $this->items = array_merge($this->items, $items);
+if ($n <= count($this->items)) {
+return true;
+}
+return false;
+}
+
+function numberOfTimes()
+{
```

#### solution 3
```diff
-function take($items, $n = 1)
-{
+function take($items, $n = 1)
+{
+ $this->items = array_merge($this->items, $items); return $this->items[$n-1]; }
+
+
+We then add a few items, and then retrieve the last element, as in Example 4-
```

#### solution 4
```diff
-function take($items, $n = 1)
-{
+function take($items, $n = 1)
+{
+ $result = array(); for ($i = 0; $i < $n; $i++) { $result[] = $items[$i]; } return $result; }
+
+
+Note
+
+
+As you can see, the function is
```

### last (task/4)

#### canonical solution
```php
function last($items)
{  return end($items);
}
```

#### solution 0
```diff
-function last($items)
-{
+function last($items)
+{
+
+
+function add()
+
+function get_last()
+
+function get_item_name()
+
+function get_item_length()
+
+function get_item_size()
+
+function add_item()
+
+function get
```

#### solution 1
```diff
-function last($items)
-{
+function last($items)
+{
+ $total = 0; $last = null; $i = 0; foreach ($items as $item) { if ($i == count($items)) { $last = $item; $total += $item->cost; break; }
```

#### solution 2
```diff
-function last($items)
-{
+function last($items)
+{
+ $last = null; if(is_array($items)) { $first = end($items); if(is_null($first)) { $last = null; } else { $last = $first; } } else { $last
```

#### solution 3
```diff
-function last($items)
-{
+function last($items)
+{
+
+
+function last2($items)
+
+function last3($items)
+
+function last4($items)
+
+function last5($items)
+
+function last6($items)
+
+function last7($items)
+
```

#### solution 4
```diff
-function last($items)
-{
+function last($items)
+{
+ $last = $items[$this->depth]; $this->depth--; return $last; }
+$first = $items[0];
+function first()
+{ $this->depth = 0; return $first; }
```

### isContains (task/5)

#### canonical solution
```php
function isContains($string, $needle)
{  return strpos($string, $needle) === false ? false : true;
}
```

#### solution 0
```diff
-function isContains($string, $needle)
-{
+function isContains($string, $needle)
+{
+ return preg_match('/'.$needle.'/', $string); }
+function isIn($array, $needle)
+{ foreach ($array as $item)
+{ if ($item == $needle)
```

#### solution 1
```diff
-function isContains($string, $needle)
-{
+function isContains($string, $needle)
+{
+ if (count($this->startsWith($string, $needle)) == 0) { return false; } else { return true; } }
+$in_array = function($needle, $haystack) use ($filter
```

#### solution 2
```diff
-function isContains($string, $needle)
-{
+function isContains($string, $needle)
+{
+     return (strpos($string, $needle) !== false);     }
+$text = "No longer with us is our beloved father and husband, Donald G.";
+echo "before: ".$text."<
```

#### solution 3
```diff
-function isContains($string, $needle)
-{
+function isContains($string, $needle)
+{
+     $needleLen = strlen($needle);     for ($i = 0; $i < strlen($string); $i++) {         if ($string[$i] == $needle[$need
```

#### solution 4
```diff
-function isContains($string, $needle)
-{
+function isContains($string, $needle)
+{
+ $needle = trim($needle); $needle = strtolower($needle); //first character is not compared if ($string[0] != $needle) return false; //needle can only be present at the
```

### curry (task/6)

#### canonical solution
```php
function curry($function)
{  $accumulator = function ($arguments) use ($function, &$accumulator) {
    return function (...$args) use ($function, $arguments, $accumulator) {
      $arguments = array_merge($arguments, $args);
      $reflection = new ReflectionFunction($function);
      $totalArguments = $reflection->getNumberOfRequiredParameters();

      if ($totalArguments <= count($arguments)) {
        return $function(...$arguments);
      }

      return $accumulator($arguments);
    };
  };

  return $accumulator([]);
}
```

#### solution 0
```diff
-function curry($function)
-{
+function curry($function)
+{
+ if(is_callable($function)){
+$result = $function();
+if($result instanceof Closure){
+return $result;
+elseif($result instanceof Array){
+return array_map($function, $result
```

#### solution 1
```diff
-function curry($function)
-{
+function curry($function)
+{
+ //function to execute return function($arg1, $arg2) use ($function) { return $function($arg1, $arg2); }; }
+$curryedAdd = curry(function($a, $b) { return
```

#### solution 2
```diff
-function curry($function)
-{
+function curry($function)
+{
+ $function = $function ?? ''; return function() use ($function) { $function($this); return $this; }; }
+$curryed = curry(function($number) { return $number + 1; });
+echo $
```

#### solution 3
```diff
-function curry($function)
-{
+function curry($function)
+{
+ return function($var1, $var2) use ($function) { return $function($var1, $var2); }; } $add1 = curry(function($x, $y) { return $x + $y; });
```

#### solution 4
```diff
-function curry($function)
-{
+function curry($function)
+{
+
+
+$function(mixed $arg1, mixed $arg2 = null)
+$function = (function(mixed $arg1, mixed $arg2 = null) 
+
+function curried($function)
+
+$
```

### isAnagram (task/7)

#### canonical solution
```php
function isAnagram($string1, $string2)
{  return count_chars($string1, 1) === count_chars($string2, 1);
}
```

#### solution 0
```diff
-function isAnagram($string1, $string2)
-{
+function isAnagram($string1, $string2)
+{
+
+
+function isPalindrome($string)
+
+{
+
+}
+
+function isPangram($string)
+
+{
+
+}
+
+function isPangram($string)
+
+{
+
+}
+
```

#### solution 1
```diff
-function isAnagram($string1, $string2)
-{
+function isAnagram($string1, $string2)
+{
+
+$length1 = strlen($string1);
+$length2 = strlen($string2);
+if($length1 != $length2) return 0;
+$char1 = $string1[0];
+$char2
```

#### solution 2
```diff
-function isAnagram($string1, $string2)
-{
+function isAnagram($string1, $string2)
+{
+ $length1 = strlen($string1); $length2 = strlen($string2); $alpha1 = substr($string1, 0, $length1-1); $alpha2 = substr($string2, 0, $length
```

#### solution 3
```diff
-function isAnagram($string1, $string2)
-{
+function isAnagram($string1, $string2)
+{
+ // return true if $string1 is a substring of $string2
+}
+The function isAnagram accepts two strings as parameters and then checks if the first one is a substring of the second one.
+
+If the same method
```

#### solution 4
```diff
-function isAnagram($string1, $string2)
-{
+function isAnagram($string1, $string2)
+{
+ $string1 = strtolower($string1); $string2 = strtolower($string2); for($i = 0; $i < strlen($string1); $i++) { if(strcmp($string1
```

### hasDuplicates (task/8)

#### canonical solution
```php
function hasDuplicates($items)
{  return count($items) > count(array_unique($items));
}
```

#### solution 0
```diff
-function hasDuplicates($items)
-{
+function hasDuplicates($items)
+{
+ $hasDuplicates = false; foreach ($items as $item) { if (in_array($item, $previous)) { $hasDuplicates = true; break; } } return $hasDuplicates; }
```

#### solution 1
```diff
-function hasDuplicates($items)
-{
+function hasDuplicates($items)
+{
+ $found = 0; $value = 0; foreach ($items as $item) { if (isset($this->cache[$item->id])) { if ($this->cache[$item->id]->value == $
```

#### solution 2
```diff
-function hasDuplicates($items)
-{
+function hasDuplicates($items)
+{
+ return $items->filter(function($item) use ($items) { return !$items->contains($item); }); }
+}
+
+This approach could be easily extended to define an interface for the list of items and test the many
```

#### solution 3
```diff
-function hasDuplicates($items)
-{
+function hasDuplicates($items)
+{
+ $duplicates = []; foreach ($items as $key => $item) { if (in_array($item, $duplicates)) { $duplicates[] = $key; } else { $duplicates[] =
```

#### solution 4
```diff
-function hasDuplicates($items)
-{
+function hasDuplicates($items)
+{
+     $results = array();     $count = count($items);     $index = 0;     foreach ($items as $item) {         if (!array_key_exists($item, $results
```

### factorial (task/9)

#### canonical solution
```php
function factorial($n)
{  if ($n <= 1) {
    return 1;
  }

  return $n * factorial($n - 1);
}
```

#### solution 0
```diff
-function factorial($n)
-{
+function factorial($n)
+{
+
+
+function factorial($n)
+
+This function is named with a different name than the generic function and is called with different arguments. Since the function is named, it is clear to the programmer calling it what will be returned.
+
```

#### solution 1
```diff
-function factorial($n)
-{
+function factorial($n)
+{
+
+
+function factorial($n)
+
+Here we have to add in the extra step of adding 1 to the running total. We can do this by performing the first loop iteration, then adding 1 to the running total before starting the second loop
```

#### solution 2
```diff
-function factorial($n)
-{
+function factorial($n)
+{
+ $n = intval($n); $n = $n * (1..$n-1); return $n; }
+$n = '6'; echo "$n! = ".factorial($n)."<br>";
```

#### solution 3
```diff
-function factorial($n)
-{
+function factorial($n)
+{
+
+</syntaxhighlight>
+</div>
+
+<div id="factorial"></div>
+
+<div id="factorial"></div>
+
+<div id="factorial"></div>
+
+<div id="
```

#### solution 4
```diff
-function factorial($n)
-{
+function factorial($n)
+{
+
+
+The output is:
+
+1! = 1
+2! = 2
+3! = 6
+4! = 24
+5! = 120
+
+To prove that the results are correct, we can follow the execution of the program
```

### once (task/10)

#### canonical solution
```php
function once($function)
{  return function (...$args) use ($function) {
    static $called = false;
    if ($called) {
      return;
    }
    $called = true;
    return $function(...$args);
  };
}
```

#### solution 0
```diff
-function once($function)
-{
+function once($function)
+{
+
+global $settings;
+
+$this->_settings['alnum'] = true;
+
+$this->_settings['alpha'] = true;
+
+$this->_settings['space'] = true;
+
+$this->
```

#### solution 1
```diff
-function once($function)
-{
+function once($function)
+{
+ if(is_callable($function)) { $function(); } else { trigger_error("Function %s not found", $function); } }
+function trigger_error($message)
+{ error_log("Caught exception in function
```

#### solution 2
```diff
-function once($function)
-{
+function once($function)
+{
+ $entry_count = 0; $entry_start = -1; $entry_end = -1; $non_entry_start = -1; $non_entry_end = -1; $context = ''; $pattern
```

#### solution 3
```diff
-function once($function)
-{
+function once($function)
+{
+
+
+function pre-function($function)
+
+function post-function($function)
+
+function once-twice($function)
+
+function once-twice($function)
+
+function once-twice($function)
+
```

#### solution 4
```diff
-function once($function)
-{
+function once($function)
+{
+ $function = strtolower($function);
+if (in_array($function, $functions)) {
+$cache[$function] = $GLOBALS[$function];
+return $cache[$function];
+else
```

### endsWith (task/11)

#### canonical solution
```php
function endsWith($haystack, $needle)
{  return strrpos($haystack, $needle) === (strlen($haystack) - strlen($needle));
}
```

#### solution 0
```diff
-function endsWith($haystack, $needle)
-{
+function endsWith($haystack, $needle)
+{
+ $haystack = trim($haystack); $needle = trim($needle); if ($haystack === $needle) { return true; } if ($haystack === '') { return false; } return str
```

#### solution 1
```diff
-function endsWith($haystack, $needle)
-{
+function endsWith($haystack, $needle)
+{
+ if(strlen($haystack) < strlen($needle)) { return false; } else { $haystack = substr($haystack, 0, strlen($needle)); for($i = 0; $i
```

#### solution 2
```diff
-function endsWith($haystack, $needle)
-{
+function endsWith($haystack, $needle)
+{
+
+
+function indexOf($haystack, $needle)
+
+function countOccurrences($haystack, $needle)
+
+function countOccurrences($haystack, $needle, $offset = 0
```

#### solution 3
```diff
-function endsWith($haystack, $needle)
-{
+function endsWith($haystack, $needle)
+{
+
+
+function strlen($string)
+
+{
+
+function strrev($string)
+
+{
+
+function strstr($haystack, $needle)
+
+{
+
+function strtolower($string)
```

#### solution 4
```diff
-function endsWith($haystack, $needle)
-{
+function endsWith($haystack, $needle)
+{
+
+
+function add(x, y)
+
+function sub(x, y)
+
+function mul(x, y)
+
+function div(x, y)
+
+function mod(x, y)
+
+function pow(
```

### lcm (task/12)

#### canonical solution
```php
function lcm(...$numbers)
{  $ans = $numbers[0];
  for ($i = 1, $max = count($numbers); $i < $max; $i++) {
    $ans = (($numbers[$i] * $ans) / gcd($numbers[$i], $ans));
  }

  return $ans;
}
```

#### solution 0
```diff
-function lcm(...$numbers)
-{
+function lcm(...$numbers)
+{
+ 
+}
+
+This is the interface for the function:
+
+function lcm(...$numbers)
+
+This is an example use of the function:
+
+lcm(4,6,8)
+
+This is
```

#### solution 1
```diff
-function lcm(...$numbers)
-{
+function lcm(...$numbers)
+{
+ $sqrtnums = $numbers | foreach {$_ * $_} $sum = 0 foreach ($n in $sqrtnums) { $sum += $n } return [math]::pow($sum,
```

#### solution 2
```diff
-function lcm(...$numbers)
-{
+function lcm(...$numbers)
+{
+
+$result = 1;
+foreach($numbers as $number)
+{
+$result *= $number;
+}
+return $result;
+}
+
+The LCM of the list of integers 1, 2, and
```

#### solution 3
```diff
-function lcm(...$numbers)
-{
+function lcm(...$numbers)
+{
+
+function next_lcm(...$numbers)
+{
+function lcm_gcd(...$numbers)
+{
+function lcm_gcd(...$numbers)
+{
+function lcm_l
```

#### solution 4
```diff
-function lcm(...$numbers)
-{
+function lcm(...$numbers)
+{
+
+$lcm = 1;
+for ($i = 1; $i < $numbers; $i++) {
+
+$lcm *= $numbers[$i];
+
+}
+
+return $lcm;
```

### without (task/13)

#### canonical solution
```php
function without($items, ...$params)
{  return array_values(array_diff($items, $params));
}
```

#### solution 0
```diff
-function without($items, ...$params)
-{
+function without($items, ...$params)
+{
+ # $items is an array or a Traversable object
+}
+
+
```

#### solution 1
```diff
-function without($items, ...$params)
-{
+function without($items, ...$params)
+{
+ // ... }
+
+You could say that the second argument is a named list, but it can have only a single element.
+
+Structures are very similar to anonymous unions in C. We could write an array-of-structures like
```

#### solution 2
```diff
-function without($items, ...$params)
-{
+function without($items, ...$params)
+{
+ <script> var $items = $items; if ($items === null) return; if ($items instanceof HTMLElement) { $items = $items.getAttribute('data-tooltip'); } if ($items === null)
```

#### solution 3
```diff
-function without($items, ...$params)
-{
+function without($items, ...$params)
+{
+ $params = iterator_to_array($params);
+foreach ($items as $key => $item) {
+if (isset($params[$key])) {
+$value = $params[$key];
+$items
```

#### solution 4
```diff
-function without($items, ...$params)
-{
+function without($items, ...$params)
+{
+
+
+To define a class, the "class" keyword is used. To instantiate an object, the "new" keyword is used:
+
+To define a class, the "class" keyword is used. To instantiate an object,
```

### fibonacci (task/14)

#### canonical solution
```php
function fibonacci($n)
{  $sequence = [0, 1];

  for ($i = 2; $i < $n; $i++) {
    $sequence[$i] = $sequence[$i-1] + $sequence[$i-2];
  }

  return $sequence;
}
```

#### solution 0
```diff
-function fibonacci($n)
-{
+function fibonacci($n)
+{
+
+
+function bernoulli($n)
+
+function factorial($n)
+
+function fft($n)
+
+function gcd($a, $b)
+
+function get_pid()
+
+function lcm($
```

#### solution 1
```diff
-function fibonacci($n)
-{
+function fibonacci($n)
+{
+
+
+echo(n);
+}
+
+?>
+
+Example of recursion:
+
+<?php
+
+function fibonacci($n)
+
+{
+
+if ($n < 2)
+
+{
+
+return 1
```

#### solution 2
```diff
-function fibonacci($n)
-{
+function fibonacci($n)
+{
+
+
+}
+This function does exactly the same thing as the previous one, but it is not functional.
+
+In the functional definition of fibonacci the argument n is not the source of data, it is the "context" of the
```

#### solution 3
```diff
-function fibonacci($n)
-{
+function fibonacci($n)
+{
+ if ($n <= 2) { return 1; } return fibonacci($n - 1) + fibonacci($n - 2); } }
+
+
+
+This is a recursive function that calls itself to determine the values for n = 1
```

#### solution 4
```diff
-function fibonacci($n)
-{
+function fibonacci($n)
+{
+
+
+function fibo(int $n)
+
+function fibo(int $n)
+
+function fibo(int $n)
+
+function fibo(int $n)
+
+function fibo(int $n)
```

### groupBy (task/15)

#### canonical solution
```php
function groupBy($items, $func)
{  $group = [];
  foreach ($items as $item) {
    if ((!is_string($func) && is_callable($func)) || function_exists($func)) {
      $key = call_user_func($func, $item);
      $group[$key][] = $item;
    } elseif (is_object($item)) {
      $group[$item->{$func}][] = $item;
    } elseif (isset($item[$func])) {
      $group[$item[$func]][] = $item;
    }
  }

  return $group;
}
```

#### solution 0
```diff
-function groupBy($items, $func)
-{
+function groupBy($items, $func)
+{
+ $items = iterator_to_array($items); $groups = array(); foreach ($items as $item) { $groups[$func($item)] = $item; } return $groups; } function GroupBy($data, $
```

#### solution 1
```diff
-function groupBy($items, $func)
-{
+function groupBy($items, $func)
+{
+ return array_map($func, $items); }
+}
+
+In the above example, the method groupBy() returns an array, whose items are arrays of the same size, each with a single member. The method simply maps the value
```

#### solution 2
```diff
-function groupBy($items, $func)
-{
+function groupBy($items, $func)
+{
+
+
+function ($items, $func)
+
+foreach ($items as $key => $value)
+
+foreach ($items as $key => $value)
+
+foreach ($items as $key => $value)
+
```

#### solution 3
```diff
-function groupBy($items, $func)
-{
+function groupBy($items, $func)
+{
+ $groups = array(); foreach ($items as $item) { $groups[$func($item)] = $item; } return $groups; }
+$items = collect(['a', 'b', 'c', 'd',
```

#### solution 4
```diff
-function groupBy($items, $func)
-{
+function groupBy($items, $func)
+{
+     $groupBy = array();     foreach ($items as $item) {         if ($func($item)) {             $groupBy[] = $item;     }     }     return $
```

### maxN (task/16)

#### canonical solution
```php
function maxN($numbers)
{  $maxValue = max($numbers);
  $maxValueArray = array_filter($numbers, function ($value) use ($maxValue) {
    return $maxValue === $value;
  });

  return count($maxValueArray);
}
```

#### solution 0
```diff
-function maxN($numbers)
-{
+function maxN($numbers)
+{
+ if($numbers > $max) return $max; $max = $numbers; return $max; }
+$maxN = maxN(array_unique(range(10)))
+$maxN = 10
+
+While this
```

#### solution 1
```diff
-function maxN($numbers)
-{
+function maxN($numbers)
+{
+
+
+The maxn() function can be called with a single numeric value or with an array of numeric values. Both cases are shown below.
+
+$result = maxn(10);
+
+echo $result;
+
+echo "<br
```

#### solution 2
```diff
-function maxN($numbers)
-{
+function maxN($numbers)
+{
+ return $numbers[0] * $numbers[1] * ... * $numbers[$numbers.Length - 1]; } }
+This would be straightforward to understand, but it's also a bit wordy. It would
```

#### solution 3
```diff
-function maxN($numbers)
-{
+function maxN($numbers)
+{
+ 
+
+<poem>The first number is: $numbers[0]
+The last number is: $numbers[$numbers.Length - 1]
+The maximum number is: $numbers[$numbers.
```

#### solution 4
```diff
-function maxN($numbers)
-{
+function maxN($numbers)
+{
+
+
+Works with: PowerShell version 3
+
+This function works with PowerShell v3 and later.
+
+function MaxN {
+
+$collection = @(1..10)
+
+$max = $collection | sort | select -first
```

### drop (task/17)

#### canonical solution
```php
function drop($items, $n = 1)
{  return array_slice($items, $n);
}
```

#### solution 0
```diff
-function drop($items, $n = 1)
-{
+function drop($items, $n = 1)
+{
+ foreach ($items as $item) { if (in_array($item, $n)) { unset($items[$n]); $n--; } } }
+
+
+
+echo "How many items would you like to drop?
```

#### solution 1
```diff
-function drop($items, $n = 1)
-{
+function drop($items, $n = 1)
+{
+     $items = array_slice($items, 0, $n);     return $items;     }
+In this example, we're just copying the items to a new array, but it could just as easily be a pivot
```

#### solution 2
```diff
-function drop($items, $n = 1)
-{
+function drop($items, $n = 1)
+{
+ $count = 0;
+foreach ($items as $i) {
+return $count;
+}
+The above code can be used in an asynchronous way as well, but it would require the following:
+
+function drop($items,
```

#### solution 3
```diff
-function drop($items, $n = 1)
-{
+function drop($items, $n = 1)
+{
+ $tmp = array_reverse($items); return array_splice($tmp, $n, 1); }
+(note: you can use this function in other cases as well: for example in a form submit function, where you want to
```

#### solution 4
```diff
-function drop($items, $n = 1)
-{
+function drop($items, $n = 1)
+{
+      $items = [0,1,2,3,4,5,6,7,8,9,10];      $i = 0;      while ($i <= $n)      {         
```

### orderBy (task/18)

#### canonical solution
```php
function orderBy($items, $attr, $order)
{  $sortedItems = [];
  foreach ($items as $item) {
    $key = is_object($item) ? $item->{$attr} : $item[$attr];
    $sortedItems[$key] = $item;
  }
  if ($order === 'desc') {
    krsort($sortedItems);
  } else {
    ksort($sortedItems);
  }

  return array_values($sortedItems);
}
```

#### solution 0
```diff
-function orderBy($items, $attr, $order)
-{
+function orderBy($items, $attr, $order)
+{
+
+
+}
+
+// function getCount($items, $attr)
+{
+
+}
+
+// function getItem($items, $attr)
+{
+
+}
+
+// function getItemCount($items, $attr)
```

#### solution 1
```diff
-function orderBy($items, $attr, $order)
-{
+function orderBy($items, $attr, $order)
+{
+  $items = array_filter($items, 'is_numeric');  $sort_array = array();  foreach ($items as $key => $value) {   $sort_array[$key] = strtou
```

#### solution 2
```diff
-function orderBy($items, $attr, $order)
-{
+function orderBy($items, $attr, $order)
+{
+
+
+function orderByDesc($items, $attr, $order)
+{
+
+function orderByDesc($items, $attr, $order)
+{
+
+function orderByArray($items, $attr, $order)
```

#### solution 3
```diff
-function orderBy($items, $attr, $order)
-{
+function orderBy($items, $attr, $order)
+{
+
+
+function getItemId($items, $attr)
+
+function getItemKeys($items, $attr)
+
+function getItemCount($items, $attr)
+
+function getItemTitle($items, $attr)
+
```

#### solution 4
```diff
-function orderBy($items, $attr, $order)
-{
+function orderBy($items, $attr, $order)
+{
+  if (isset($attr['from'])) { $order = $attr['from']; unset($attr['from']); }  $items = array_slice($items, 0, $order);  foreach ($items
```

### rotate (task/19)

#### canonical solution
```php
function rotate($array, $shift = 1)
{  for ($i = 0; $i < $shift; $i++) {
    array_push($array, array_shift($array));
  }

  return $array;
}
```

#### solution 0
```diff
-function rotate($array, $shift = 1)
-{
+function rotate($array, $shift = 1)
+{
+
+foreach($array as $value)
+
+$array = array_rotate($array, $shift);
+return $array;
+}
+
+Inline Functions
+
+The inline keyword can be used on a function. It is
```

#### solution 1
```diff
-function rotate($array, $shift = 1)
-{
+function rotate($array, $shift = 1)
+{
+
+function rotate($array, $shift = 1)
+
+function rotate($array, $shift = 1)
+
+function rotate($array, $shift = 1)
+
+function rotate($array, $shift = 1)
+
+function
```

#### solution 2
```diff
-function rotate($array, $shift = 1)
-{
+function rotate($array, $shift = 1)
+{
+ # shift the array
+# 1) set the new base $base = $array[0];
+# 2) identify the leftovers
+# 3) build the right array (passing in the base)
+# 4) return the new
```

#### solution 3
```diff
-function rotate($array, $shift = 1)
-{
+function rotate($array, $shift = 1)
+{
+ if (is_array($array)) { $array2 = array(); for ($i = 0; $i < count($array); $i++) { $array2[$i] = $array[$i] + $shift;
```

#### solution 4
```diff
-function rotate($array, $shift = 1)
-{
+function rotate($array, $shift = 1)
+{
+
+
+function rotate($array, $shift = 1)
+
+function rotate_left($array, $shift = 1)
+
+function rotate_right($array, $shift = 1)
+
+function reverse($array)
+
+function
```

### shorten (task/20)

#### canonical solution
```php
function shorten($input, $length = 100, $end = '...')
{  if (mb_strlen($input) <= $length) {
    return $input;
  }

  return rtrim(mb_substr($input, 0, $length, 'UTF-8')) . $end;
}
```

#### solution 0
```diff
-function shorten($input, $length = 100, $end = '...')
-{
+function shorten($input, $length = 100, $end = '...')
+{
+ $segments = array(); $result = ''; $expiration = ''; $input = preg_replace('#[\r
+]#', '', $input); $input = preg_replace('#[\s
```

#### solution 1
```diff
-function shorten($input, $length = 100, $end = '...')
-{
+function shorten($input, $length = 100, $end = '...')
+{
+
+
+function pad($input, $length = 100, $end = '...')
+{
+
+function repeat($input, $count = 1, $end = '...')
+{
+
+function repeatUntil($input, $end
```

#### solution 2
```diff
-function shorten($input, $length = 100, $end = '...')
-{
+function shorten($input, $length = 100, $end = '...')
+{
+
+
+function join($input, $sep = ', ')
+
+function get_date($input, $default = 'now')
+
+function j_strftime($input, $format, $timestamp = 'now')
```

#### solution 3
```diff
-function shorten($input, $length = 100, $end = '...')
-{
+function shorten($input, $length = 100, $end = '...')
+{
+
+$output = "";
+for ($i = 0; $i < $length; $i++) {
+if (strlen($input) > $i) {
+else {
+$output .= $end;
+$output
```

#### solution 4
```diff
-function shorten($input, $length = 100, $end = '...')
-{
+function shorten($input, $length = 100, $end = '...')
+{
+ $remainder = strlen($input);
+while ( strlen($input) >= $length ) {
+if ( substr($input, -1) != $end ) {
+$input = substr($input, 0, -1
```

### average (task/21)

#### canonical solution
```php
function average(...$items)
{  $count = count($items);
  
  return $count === 0 ? 0 : array_sum($items) / $count;
}
```

#### solution 0
```diff
-function average(...$items)
-{
+function average(...$items)
+{
+
+
+return $items[mean(scalar(@items))];
+
+}
+
+This function would have to be defined in the same module as the function that calls it.
+
+Note that overloading functions in this way is
```

#### solution 1
```diff
-function average(...$items)
-{
+function average(...$items)
+{
+     $sum = 0;     foreach ($items as $item) {         $sum += $item;     }     return $sum / count($items);     }
+The first difference is that the
```

#### solution 2
```diff
-function average(...$items)
-{
+function average(...$items)
+{
+   return ($items * $items) / (sum($items) - sum(distinct(...$items)));   }
+This method is very similar to the one we implemented before. Instead of using distinct() it calls sum() to
```

#### solution 3
```diff
-function average(...$items)
-{
+function average(...$items)
+{
+     return (sum(...$items)) / (length(...$items));     }
+If you run this, you'll see that average is faster for small inputs but not for large inputs. What's going on?
+The
```

#### solution 4
```diff
-function average(...$items)
-{
+function average(...$items)
+{
+     return ($items[0] + $items[1] + $items[2]...) / 3;     }
+Instead of being a problem, this is a golden opportunity. We can use the fact that the values are now
```

### reject (task/22)

#### canonical solution
```php
function reject($items, $func)
{  return array_values(array_diff($items, array_filter($items, $func)));
}
```

#### solution 0
```diff
-function reject($items, $func)
-{
+function reject($items, $func)
+{
+
+
+$items = $items * 10;
+
+$items = $items * 10;
+
+echo $items;
+
+echo $func('Parent::reject()');
+
+echo $func('Parent::reject()');
```

#### solution 1
```diff
-function reject($items, $func)
-{
+function reject($items, $func)
+{
+ $this->items[$items[0]] = $func($items[1]); return $this; } } $myShoppingCart = new ShoppingCart(); $myShoppingCart->addItem('apple', 'Eat it!');
```

#### solution 2
```diff
-function reject($items, $func)
-{
+function reject($items, $func)
+{
+ }
+
+
+$items = [1, 2, 3];
+
+$func = function ($i) { return $i * 3; };
+
+call_user_func_array('reject', $items, $func);
```

#### solution 3
```diff
-function reject($items, $func)
-{
+function reject($items, $func)
+{
+
+
+<!--BEGINNING OF FUNCTION PARAMETERS-->
+
+$items = $arg1;
+
+$func = $arg2;
+
+<!--END OF FUNCTION PARAMETERS-->
+
```

#### solution 4
```diff
-function reject($items, $func)
-{
+function reject($items, $func)
+{
+ echo '<p>' . $items . '</p>'; } ?>
+<p> <form action="<?php echo $PHP_SELF; ?>" method="post"> <?php $i = 0;
```

### any (task/23)

#### canonical solution
```php
function any($items, $func)
{  return count(array_filter($items, $func)) > 0;
}
```

#### solution 0
```diff
-function any($items, $func)
-{
+function any($items, $func)
+{
+ if (isset($items[0])) { 
+
+The $items array is usually an associative array or object, and the $func is the name of a user-defined function that acts on a single item in the array.
```

#### solution 1
```diff
-function any($items, $func)
-{
+function any($items, $func)
+{
+ 
+
+function any($items, $func)
+{ 
+
+function collect($items, $func)
+{ 
+
+function flatten($items, $func)
+{ 
+
+function collect_list($items,
```

#### solution 2
```diff
-function any($items, $func)
-{
+function any($items, $func)
+{
+
+
+If there are not enough items to call the $func on, we call the $func with an empty array and return that.
+If there are enough items, we call the $func on each item, and return the result of the
```

#### solution 3
```diff
-function any($items, $func)
-{
+function any($items, $func)
+{
+
+
+<br>
+
+<br>
+
+}
+
+<br>
+
+function sum($numbers)
+{
+
+<br>
+
+<br>
+
+}
+
+<br>
+
+function mean
```

#### solution 4
```diff
-function any($items, $func)
-{
+function any($items, $func)
+{
+ foreach($items as $item) { if($func($item)) { return true; } } return false; }
+Step 2: Add the processor that will handle the tag
+In order to pass a test item through our processor, we
```

### flatten (task/24)

#### canonical solution
```php
function flatten($items)
{  $result = [];
  foreach ($items as $item) {
    if (!is_array($item)) {
      $result[] = $item;
    } else {
      array_push($result, ...array_values($item));
    }
  }

  return $result;
}
```

#### solution 0
```diff
-function flatten($items)
-{
+function flatten($items)
+{
+  foreach ($items as $item)
+{  if (is_array($item))
+{  foreach ($item as $subitem)
+{  flatten($subitem);
+ }
+ }
+ }
```

#### solution 1
```diff
-function flatten($items)
-{
+function flatten($items)
+{
+      foreach ($items as $item)     {         // if its not an array, send it along         if (!is_array($item))         {             $items[] = $
```

#### solution 2
```diff
-function flatten($items)
-{
+function flatten($items)
+{
+ $output = []; foreach ($items as $item) { $output[] = $item; } return $output; } function flatten(array $items)
+pow($a, $b) { return $a ** $b
```

#### solution 3
```diff
-function flatten($items)
-{
+function flatten($items)
+{
+     $result = [];     foreach ($items as $item)     {         if (is_array($item))         {             $result[] = flatten($item);             }
```

#### solution 4
```diff
-function flatten($items)
-{
+function flatten($items)
+{
+
+
+function flatten(array $items)
+
+{
+
+function flatten(array $items)
+
+var_dump(flatten([1,2,3,4,5,6,7,8,9,
```

### startsWith (task/25)

#### canonical solution
```php
function startsWith($haystack, $needle)
{  return strpos($haystack, $needle) === 0;
}
```

#### solution 0
```diff
-function startsWith($haystack, $needle)
-{
+function startsWith($haystack, $needle)
+{
+
+}
+
+This function will search any given string for the first occurrence of a given substring.
+
+PHP allows any number of functions to be defined within a single PHP file, as long as the file is executed as a PHP script
```

#### solution 1
```diff
-function startsWith($haystack, $needle)
-{
+function startsWith($haystack, $needle)
+{
+
+
+function startsWith($haystack, $needle)
+
+function startsWith($haystack, $needle)
+
+function startsWith($haystack, $needle)
+
+function startsWith($hay
```

#### solution 2
```diff
-function startsWith($haystack, $needle)
-{
+function startsWith($haystack, $needle)
+{
+ 
+if ($needle === $haystack) {
+return true;
+} elseif ($needle !== null) {
+return false;
+} else {
+return null;
+}
+
+function trimStart($string
```

#### solution 3
```diff
-function startsWith($haystack, $needle)
-{
+function startsWith($haystack, $needle)
+{
+ $haystack = strtolower($haystack); $needle = strtolower($needle); $needlelen = strlen($needle); $needlepos = strpos($haystack, $
```

#### solution 4
```diff
-function startsWith($haystack, $needle)
-{
+function startsWith($haystack, $needle)
+{
+     $needle = strtolower($needle);     $haystack = strtolower($haystack);     if (strpos($haystack, $needle) === false)      
```

### clampNumber (task/26)

#### canonical solution
```php
function clampNumber($num, $a, $b)
{  return max(min($num, max($a, $b)), min($a, $b));
}
```

#### solution 0
```diff
-function clampNumber($num, $a, $b)
-{
+function clampNumber($num, $a, $b)
+{
+
+The third argument is used in cases where a binary operation is not defined for two values. For example, there is no binary operation defined for the number zero, and the addition operator only accepts two numbers. To handle this case, we define a
```

#### solution 1
```diff
-function clampNumber($num, $a, $b)
-{
+function clampNumber($num, $a, $b)
+{
+
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num,
```

#### solution 2
```diff
-function clampNumber($num, $a, $b)
-{
+function clampNumber($num, $a, $b)
+{
+ return $num / $a / $b; }
+
+
+function clampNumber($num, $a, $b)
+{ return $num / ($a / $b); }
+
+
+function clampNumber($num, $a, $
```

#### solution 3
```diff
-function clampNumber($num, $a, $b)
-{
+function clampNumber($num, $a, $b)
+{
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $
```

#### solution 4
```diff
-function clampNumber($num, $a, $b)
-{
+function clampNumber($num, $a, $b)
+{
+
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num,
```

### pull (task/27)

#### canonical solution
```php
function pull(&$items, ...$params)
{  $items = array_values(array_diff($items, $params));
  return $items;
}
```

#### solution 0
```diff
-function pull(&$items, ...$params)
-{
+function pull(&$items, ...$params)
+{
+
+
+// This is just to show how you can use param()
+
+// to quickly add params to a function.
+{
+// Same as above, but using named params
+
+// Note: This example uses the PHP 5.3
```

#### solution 1
```diff
-function pull(&$items, ...$params)
-{
+function pull(&$items, ...$params)
+{
+
+
+$items is an array of scalar variables that are to be passed by reference.
+
+function set($$var1, ..., $var_n)
+
+function set(&$var1, ..., $var_n
```

#### solution 2
```diff
-function pull(&$items, ...$params)
-{
+function pull(&$items, ...$params)
+{
+
+
+function get_children($items, ...$params)
+
+function get_parent($items, ...$params)
+
+function get_grandparent($items, ...$params)
+
+function get_children_from_item
```

#### solution 3
```diff
-function pull(&$items, ...$params)
-{
+function pull(&$items, ...$params)
+{
+ # implementation
+}
+
+Note that this function expects a reference to an array, since the caller of the function may be calling it with a longer array than what the function needs.
+
+For an example, see the recode() function in
```

#### solution 4
```diff
-function pull(&$items, ...$params)
-{
+function pull(&$items, ...$params)
+{
+ $items->each(function($item, $index) use($params) { //  // $item is a single item from the collection //  // $index is the index of that item in the collection }); }
+$items
```

### compose (task/28)

#### canonical solution
```php
function compose(...$functions)
{  return array_reduce(
    $functions,
    function ($carry, $function) {
      return function ($x) use ($carry, $function) {
        return $function($carry($x));
      };
    },
    function ($x) {
      return $x;
    }
  );
}
```

#### solution 0
```diff
-function compose(...$functions)
-{
+function compose(...$functions)
+{
+     $arity = count($functions);     $body = $functions[0];     foreach ($functions[1 .. $arity] as $i => $f)     {         $body =
```

#### solution 1
```diff
-function compose(...$functions)
-{
+function compose(...$functions)
+{
+
+}
+
+Composition of functions is useful for cases where a large number of similar functions are required.
+
+In functional programming, a higher-order function is a function that takes one or more functions as arguments or returns a function as its
```

#### solution 2
```diff
-function compose(...$functions)
-{
+function compose(...$functions)
+{
+     return function () {         return $functions(...call_args());     };     }
+This is a very powerful concept, but it's not always immediately obvious when to use it. There's actually a very
```

#### solution 3
```diff
-function compose(...$functions)
-{
+function compose(...$functions)
+{
+
+
+function memoize(func) {
+
+function memoize(func) {
+
+formula_93:
+
+function memoize(func) {
+
+formula_93:
+
+formula_95:
+
```

#### solution 4
```diff
-function compose(...$functions)
-{
+function compose(...$functions)
+{
+
+
+$last = $functions[$#functions];
+
+return function() use ($last) {
+
+$last($this);
+};
+}
+
+Composing the functions "f" and "g" to create
```

### findLastIndex (task/29)

#### canonical solution
```php
function findLastIndex($items, $func)
{  $keys = array_keys(array_filter($items, $func));

  return array_pop($keys);
}
```

#### solution 0
```diff
-function findLastIndex($items, $func)
-{
+function findLastIndex($items, $func)
+{
+
+
+function insertLast($items, $item)
+
+function findLast($items, $func)
+
+function removeLast($items, $item)
+
+function findLastIndex($items, $func)
+
+function insertBefore
```

#### solution 1
```diff
-function findLastIndex($items, $func)
-{
+function findLastIndex($items, $func)
+{
+     $lastIndex = array_search($func, $items, true);     return $lastIndex; }
+/** * Get the last element in the array. * * @param array $items * @return mixed * @since
```

#### solution 2
```diff
-function findLastIndex($items, $func)
-{
+function findLastIndex($items, $func)
+{
+ $lastIndex = -1; $result = []; foreach ($items as $item) { if ($func($item)) { $result[$lastIndex] = $item; $lastIndex++; } } return $result; }
+
```

#### solution 3
```diff
-function findLastIndex($items, $func)
-{
+function findLastIndex($items, $func)
+{
+
+if(sizeof($items) > 0)
+
+The negative operator "-=" is used to remove the values from the array.
+
+$items = array_remove($items, 3);
+
+echo $items[array_search
```

#### solution 4
```diff
-function findLastIndex($items, $func)
-{
+function findLastIndex($items, $func)
+{
+     return array_search($func, array_reverse($items));     }
+The only other place where we need to use this is in the array_column function. The issue here is that if the array happens to be sorted and
```

### slugify (task/30)

#### canonical solution
```php
function slugify($text) {  $text = preg_replace('~[^\pL\d]+~u', '-', $text);
  $text = iconv('utf-8', 'us-ascii//TRANSLIT', $text);
  $text = preg_replace('~[^-\w]+~', '', $text);
  $text = preg_replace('~-+~', '-', $text);
  $text = strtolower($text);
  $text = trim($text, " \t\n\r\0\x0B-");
  if (empty($text)) {
    return 'n-a';
  }
  return $text;
}
```

#### solution 0
```diff
-function slugify($text) {
+function slugify($text) {
+ $text = preg_replace("/[^a-z0-9-_]+/", "", $text); return preg_replace("/[a-z0-9-_]+/", "", $text
```

#### solution 1
```diff
-function slugify($text) {
+function slugify($text) {
+ $text = preg_replace("/[a-zA-Z0-9-_]+/", "", $text); $text = preg_replace("/[^a-zA-Z0-9-
```

#### solution 2
```diff
-function slugify($text) {
+function slugify($text) {
+ $text = preg_replace('/[a-z]/', '', $text); $text = preg_replace('/[A-Z]/', '', $text); $text = preg_replace('
```

#### solution 3
```diff
-function slugify($text) {
+function slugify($text) {
+ $text = preg_replace('/(\.{2,}|{2,})/',"$1-",$text); $text = preg_replace('/(\S+)/',"-$1",$text); $text
```

#### solution 4
```diff
-function slugify($text) {
+function slugify($text) {
+
+
+foreach (array('A-Z', 'a-z', '0-9', ' ') as $c) {
+
+$text = strtolower($text) . strtoupper($c);
```

### isUpperCase (task/31)

#### canonical solution
```php
function isUpperCase($string)
{  return $string === strtoupper($string);
}
```

#### solution 0
```diff
-function isUpperCase($string)
-{
+function isUpperCase($string)
+{
+ 
+
+function isUpperCase($string)
+{ 
+
+function isUpperCase($string)
+{ 
+
+function isUpperCase($string)
+{ 
+
+function isUpperCase($string)
```

#### solution 1
```diff
-function isUpperCase($string)
-{
+function isUpperCase($string)
+{
+ $string = strtoupper($string); }
+
+The above function will create a new case version of the string it is given, which in this case will be "Welcome to LOWERCASE!".
+
+PHP can be embedded
```

#### solution 2
```diff
-function isUpperCase($string)
-{
+function isUpperCase($string)
+{
+ $string = strtoupper($string);
+}
+Notice that the strtoupper() function is called with $string as its only argument. PHP always passes by value, so the actual string will be passed in, and the function
```

#### solution 3
```diff
-function isUpperCase($string)
-{
+function isUpperCase($string)
+{
+     return (strtoupper($string) === $string);     }
+The array_unique() function will produce a new array that contains all the values from the original array but not repeating values.
+The PHP (5.
```

#### solution 4
```diff
-function isUpperCase($string)
-{
+function isUpperCase($string)
+{
+ return ((string) $string) [0] >= 'A' && ((string) $string) [0] <= 'Z'; }
+This is the smallest valid PHP program. It has 2 source lines and 2 executable lines. It uses
```

### countVowels (task/32)

#### canonical solution
```php
function countVowels($string)
{  preg_match_all('/[aeiou]/i', $string, $matches);

  return count($matches[0]);
}
```

#### solution 0
```diff
-function countVowels($string)
-{
+function countVowels($string)
+{
+
+$length = strlen($string);
+$diff = 0;
+for ($i = 0; $i < $length; $i++) {
+if (substr($string, $i, 1) == 'a') {
```

#### solution 1
```diff
-function countVowels($string)
-{
+function countVowels($string)
+{
+ 
+
+function countVowels($string)
+
+The algorithm can be expressed in terms of the number of vowels with the following recurrence relation:
+
+For example, given "abracadabra", we have:
```

#### solution 2
```diff
-function countVowels($string)
-{
+function countVowels($string)
+{
+
+$vowels = ['a', 'e', 'i', 'o', 'u'];
+$lettercount = 0;
+
+while(strlen($string) > 0)
+{
+$lettercount += count($
```

#### solution 3
```diff
-function countVowels($string)
-{
+function countVowels($string)
+{
+
+
+"C"
+
+"Java"
+
+"Whisky"
+
+This method determines the number of vowels in a string by counting the vowel characters and ignoring all others. Vowels in this case are any of the following
```

#### solution 4
```diff
-function countVowels($string)
-{
+function countVowels($string)
+{
+ $numVowels = 0;
+$length = strlen($string);
+for ($i = 0; $i < $length; $i++) {
+$vowelCount = count_chars($string, $i
```

### palindrome (task/33)

#### canonical solution
```php
function palindrome($string)
{  return strrev($string) === (string) $string;
}
```

#### solution 0
```diff
-function palindrome($string)
-{
+function palindrome($string)
+{
+
+
+$len = strlen($string);
+
+for ($i = 0; $i < $len; $i++) {
+
+if ($string[$i] != $string[$i + 1]) {
+
+return
```

#### solution 1
```diff
-function palindrome($string)
-{
+function palindrome($string)
+{
+ $string = trim($string); $string = strtolower($string); $string = preg_replace('/[^a-z0-9]/', '', $string); $string = preg_replace('
```

#### solution 2
```diff
-function palindrome($string)
-{
+function palindrome($string)
+{
+
+
+The variable $string is assigned a value to represent the string.
+The variable $string is now the string, and is referenced in the next line.
+The variable $string is assigned the string representation.
+The string is compared to
```

#### solution 3
```diff
-function palindrome($string)
-{
+function palindrome($string)
+{
+
+
+echo "The string is $string";
+
+}
+
+?>
+The output of the script will be:
+The string is palindrome
+
+The following example is a complete, valid script which performs no output, but
```

#### solution 4
```diff
-function palindrome($string)
-{
+function palindrome($string)
+{
+ $string = strtolower($string); $string = preg_replace('/[^a-zA-Z0-9]/', '', $string); $string = strrev($string); return (strcmp
```

### firstStringBetween (task/34)

#### canonical solution
```php
function firstStringBetween($haystack, $start, $end)
{  return trim(strstr(strstr($haystack, $start), $end, true), $start . $end);
}
```

#### solution 0
```diff
-function firstStringBetween($haystack, $start, $end)
-{
+function firstStringBetween($haystack, $start, $end)
+{
+
+
+function firstStringBetween($haystack, $start, $end)
+
+{
+
+// the following is the recommended minimum contents of a validator
+function pwgReservedPagesValidator( $content )
+
```

#### solution 1
```diff
-function firstStringBetween($haystack, $start, $end)
-{
+function firstStringBetween($haystack, $start, $end)
+{
+
+function firstStringBetween($haystack, $start, $end)
+
+{
+function firstStringBetween($haystack, $start, $end)
+
+{
+
+function firstStringBetween($haystack, $
```

#### solution 2
```diff
-function firstStringBetween($haystack, $start, $end)
-{
+function firstStringBetween($haystack, $start, $end)
+{
+     $start = strpos($haystack, $start, $end);     return substr($haystack, $start, strlen($end));     }
+The $start and $end variables are passed by reference
```

#### solution 3
```diff
-function firstStringBetween($haystack, $start, $end)
-{
+function firstStringBetween($haystack, $start, $end)
+{
+
+function firstStringBetween($haystack, $start, $end)
+
+The main difference between the two PHP implementations is the used data structure. In the Python version the sequence was used, which is optimized for accessing elements. In the
```

#### solution 4
```diff
-function firstStringBetween($haystack, $start, $end)
-{
+function firstStringBetween($haystack, $start, $end)
+{
+
+
+function lastStringBetween($haystack, $start, $end)
+{
+
+function between(array $haystack, $needle, $offset = 0)
+{
+
+function stringBetween(string $h
```

### tail (task/35)

#### canonical solution
```php
function tail($items)
{  return count($items) > 1 ? array_slice($items, 1) : $items;
}
```

#### solution 0
```diff
-function tail($items)
-{
+function tail($items)
+{
+
+function trim($string)
+
+function number_formats($number, $places)
+
+function time_formats($time, $locale)
+
+function date_formats($date, $locale)
+
+function
```

#### solution 1
```diff
-function tail($items)
-{
+function tail($items)
+{
+     // do something with $items here     }
+This works. It's clean, it's simple, and it doesn't generate any warnings. You can call it from anywhere, and you know exactly what it's going to do.
```

#### solution 2
```diff
-function tail($items)
-{
+function tail($items)
+{
+
+
+function sub1($items)
+
+function sub2($items)
+
+function sub3($items)
+
+function sub4($items)
+
+function sub5($items)
+
+function sub6($items)
+
```

#### solution 3
```diff
-function tail($items)
-{
+function tail($items)
+{
+ $i = 0;
+}
+
+
+Example:
+
+$result = array_unique(array_unique(array_unique(array_unique(array_unique(array_unique(array_unique(array_unique(array_
```

#### solution 4
```diff
-function tail($items)
-{
+function tail($items)
+{
+
+
+The next two arguments define the head and tail of the list respectively.
+The arguments are passed in the same order as they are defined in the list.
+
+The return value is the rest of the list from the tail argument up to
```

### memoize (task/36)

#### canonical solution
```php
function memoize($func)
{  return function () use ($func) {
    static $cache = [];

    $args = func_get_args();
    $key = serialize($args);
    $cached = true;

    if (!isset($cache[$key])) {
      $cache[$key] = $func(...$args);
      $cached = false;
    }

    return ['result' => $cache[$key], 'cached' => $cached];
  };
}
```

#### solution 0
```diff
-function memoize($func)
-{
+function memoize($func)
+{
+
+
+if (!isset($cache[$func])) {
+
+$cache[$func] = (object) $func();
+
+}
+
+return $cache[$func];
+
+}
+
+In Python 2.
```

#### solution 1
```diff
-function memoize($func)
-{
+function memoize($func)
+{
+
+
+Here are some examples of how memoize() might be used.
+The following example shows how memoize() can be used to cache the results of a function that uses sequential search to search an array for a value. This is a very
```

#### solution 2
```diff
-function memoize($func)
-{
+function memoize($func)
+{
+     if (function_exists('array_unique')) {         $cache = array_unique(array_merge($func(), array_keys($func())));         return function() use ($cache)
```

#### solution 3
```diff
-function memoize($func)
-{
+function memoize($func)
+{
+
+$cache = [];
+if (is_callable($func)) {
+$cache = [$func];
+}
+return $cache;
+}
+// usage example:
+$myfunc = function($arg) {
+$
```

#### solution 4
```diff
-function memoize($func)
-{
+function memoize($func)
+{
+     $cache = array();     $max = count($cache);     return function () use ($func, &$cache, $max) {         if ($max == count($cache)) {             $cache
```

### isLowerCase (task/37)

#### canonical solution
```php
function isLowerCase($string)
{  return $string === strtolower($string);
}
```

#### solution 0
```diff
-function isLowerCase($string)
-{
+function isLowerCase($string)
+{
+ if (strtolower($string) == $string) { return true; } return false; }
+function isUpperCase($string)
+{ if (strtoupper($string) == $string) { return true;
```

#### solution 1
```diff
-function isLowerCase($string)
-{
+function isLowerCase($string)
+{
+ $string = strtolower($string); return ($string{0} >= 'a' && $string{0} <= 'z'); }
+
+
+function isURL($string)
+{ return (preg_match('#^
```

#### solution 2
```diff
-function isLowerCase($string)
-{
+function isLowerCase($string)
+{
+
+
+function isUpperCase($string)
+
+function isDigit($string)
+
+function isAlpha($string)
+
+function isAlnum($string)
+
+function isValidEmail($string)
+
+function isValid
```

#### solution 3
```diff
-function isLowerCase($string)
-{
+function isLowerCase($string)
+{
+ $lowercase = array(  //Latin   0xC6,  //small c,  //Latin   0xC7,  //small c with cedilla,  //Latin
```

#### solution 4
```diff
-function isLowerCase($string)
-{
+function isLowerCase($string)
+{
+
+
+function isCapitalized($string)
+
+function isOneOf($array, $value)
+
+function isNumeric($string)
+
+function isNumeric($value)
+
+function isDate($value)
+
+function
```

### isEven (task/38)

#### canonical solution
```php
function isEven($number)
{  return ($number % 2) === 0;
}
```

#### solution 0
```diff
-function isEven($number)
-{
+function isEven($number)
+{
+ if ($number % 2 == 0) { return true; } else { return false; } }
+
+The function isEven is called with the argument number. This argument is then compared to 0, and if they are equal, true is returned
```

#### solution 1
```diff
-function isEven($number)
-{
+function isEven($number)
+{
+ return $number % 2 == 0; }
+
+Add-Type -AssemblyName System.Windows.Forms
+
+[Windows.Forms.MessageBox]::Show("The result is ", isEven($x), ".", "Information
```

#### solution 2
```diff
-function isEven($number)
-{
+function isEven($number)
+{
+
+
+function isEven($number)
+
+This function is part of the "zebra_num" package, which means it has to be named "zebra_num_isEven". The package is given a unique name using the "
```

#### solution 3
```diff
-function isEven($number)
-{
+function isEven($number)
+{
+ if ($number % 2 == 0) { return true; } else { return false; } }
+This is not a good idea for two reasons. The first is that it is not as readable as it could be. There is a lot of
```

#### solution 4
```diff
-function isEven($number)
-{
+function isEven($number)
+{
+ return ($number % 2) == 0; }
+
+
+Now the PHP code can be rewritten to the following:
+
+function isEven($number)
+{ return (function($number) use ($isEven) { return $isEven($
```

### findLast (task/39)

#### canonical solution
```php
function findLast($items, $func)
{  $filteredItems = array_filter($items, $func);

  return array_pop($filteredItems);
}
```

#### solution 0
```diff
-function findLast($items, $func)
-{
+function findLast($items, $func)
+{
+ $items->last(); $func($items); }
+function findFirst($items, $func)
+{ $items->first(); $func($items); }
+function createRandomString($size)
+{ $letters = array('a
```

#### solution 1
```diff
-function findLast($items, $func)
-{
+function findLast($items, $func)
+{
+   $lastItem = null;   foreach ($items as $item) {     if ($func($item) === true) {         $lastItem = $item;     break;     }     }  
```

#### solution 2
```diff
-function findLast($items, $func)
-{
+function findLast($items, $func)
+{
+
+
+function findLast($items, $func)
+
+{
+
+function f($items, $func)
+
+{
+
+function f($items, $func)
+
+{
+
+function f($items, $func)
```

#### solution 3
```diff
-function findLast($items, $func)
-{
+function findLast($items, $func)
+{
+ foreach ($items as $item) { if ($func($item)) { return $item; } } return false; } 
+
+A particular application of this function is to find the last element of an array that satisfies a given test,
```

#### solution 4
```diff
-function findLast($items, $func)
-{
+function findLast($items, $func)
+{
+
+
+function next($items, $func)
+
+function prev($items, $func)
+
+function move($items, $from, $to, $direction, $delay = 0)
+
+function skip($items, $from
```

### minN (task/40)

#### canonical solution
```php
function minN($numbers)
{  $minValue = min($numbers);
  $minValueArray = array_filter($numbers, function ($value) use ($minValue) {
    return $minValue === $value;
  });

  return count($minValueArray);
}
```

#### solution 0
```diff
-function minN($numbers)
-{
+function minN($numbers)
+{
+
+
+function maxN($numbers)
+
+function minN($array)
+
+function maxN($array)
+
+function minN1($array)
+
+function maxN1($array)
+
+function minN2($
```

#### solution 1
```diff
-function minN($numbers)
-{
+function minN($numbers)
+{
+
+}
+
+And then we can call it as follows:
+
+function callMinN($numbers)
+{
+
+}
+
+And to call the function:
+
+$callMinN = new callMinN(4,
```

#### solution 2
```diff
-function minN($numbers)
-{
+function minN($numbers)
+{
+     return min($numbers);     }
+We can't really test function minN yet, but we can go ahead and create a test for the min function.
+$ phpunit --verbose
+PHPUnit 4.4
```

#### solution 3
```diff
-function minN($numbers)
-{
+function minN($numbers)
+{
+
+
+$numbers = array_filter($numbers);
+
+echo "The minimum number is: " . $numbers[0] . "<br>";
+
+}
+
+?>
+
+Output:
+The minimum
```

#### solution 4
```diff
-function minN($numbers)
-{
+function minN($numbers)
+{
+
+
+function sum_of_squares($numbers)
+
+function check_if_prime($numbers)
+
+function is_prime($numbers)
+
+function next_prime($numbers)
+
+function next_
```

### all (task/41)

#### canonical solution
```php
function all($items, $func)
{  return count(array_filter($items, $func)) === count($items);
}
```

#### solution 0
```diff
-function all($items, $func)
-{
+function all($items, $func)
+{
+ foreach ($items as $item) { $func($item); } }
+
+
+$items is the array being sorted.
+
+$func is the sorting function.
+
+
+Sorting a list is a common task, and it is often
```

#### solution 1
```diff
-function all($items, $func)
-{
+function all($items, $func)
+{
+ for($i=0; $i<count($items); $i++) {
+
+Since there is no requirement that this function modify any of the input arguments, it is safe to pass them by reference, since the function does not modify them
```

#### solution 2
```diff
-function all($items, $func)
-{
+function all($items, $func)
+{
+
+The all() function applies a callback to every item in an array or collection. This callback should be a function that takes one argument and returns either true or false. All elements for which the callback returns true are included in the new array.
```

#### solution 3
```diff
-function all($items, $func)
-{
+function all($items, $func)
+{
+ $func(array_slice($items, 0, 1)); }
+
+function map2($items, $mapper, $converter)
+{ foreach ($items as $key => $value) { $converter($
```

#### solution 4
```diff
-function all($items, $func)
-{
+function all($items, $func)
+{
+
+$items = func($items);
+return $items;
+}
+$items = all(array('A', 'B', 'C', 'D'), function($item) {
+return strtoupper($item);
+});
```

### pluck (task/42)

#### canonical solution
```php
function pluck($items, $key)
{  return array_map( function($item) use ($key) {
    return is_object($item) ? $item->$key : $item[$key];
  }, $items);
}
```

#### solution 0
```diff
-function pluck($items, $key)
-{
+function pluck($items, $key)
+{
+
+function pluck($items, $key)
+
+The names of the functions are similar, but the parameters are different.
```

#### solution 1
```diff
-function pluck($items, $key)
-{
+function pluck($items, $key)
+{
+ return array_values(array_unique($items))[$key]; }
+function pluck_and_key($items, $key)
+{ return array_values(array_unique($items))[$key]; }
+function
```

#### solution 2
```diff
-function pluck($items, $key)
-{
+function pluck($items, $key)
+{
+ $key = "functionName"; # change this to the name of the function you want to call
+return $items->functionName($key);
+}
+
+The above code defines a new function called pluck() which can be used just
```

#### solution 3
```diff
-function pluck($items, $key)
-{
+function pluck($items, $key)
+{
+
+
+function make_map()
+
+function convert_to_ints($values)
+
+function convert_to_strings($values)
+
+function show_header()
+
+function show_map()
+
+function print_table()
```

#### solution 4
```diff
-function pluck($items, $key)
-{
+function pluck($items, $key)
+{
+     // iterate over the array, plucking values of $key
+}
+$array = array('a'=>'b','c'=>'d','e'=>'f');
+$array_key = array('a
```

### approximatelyEqual (task/43)

#### canonical solution
```php
function approximatelyEqual($number1, $number2, $epsilon = 0.001)
{  return abs($number1 - $number2) < $epsilon;
}
```

#### solution 0
```diff
-function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{
+function approximatelyEqual($number1, $number2, $epsilon = 0.001)
+{
+ if ($number1 - $number2 > $epsilon) { return false; } else { return true; } }
+#endregion
+
+#region setters and getters
+#region constructors
+#endregion
+
```

#### solution 1
```diff
-function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{
+function approximatelyEqual($number1, $number2, $epsilon = 0.001)
+{
+     return (fabs($number1 - $number2) < $epsilon);     }
+The $epsilon variable is used to specify how close the two numbers need to be to be considered equal. The function returns
```

#### solution 2
```diff
-function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{
+function approximatelyEqual($number1, $number2, $epsilon = 0.001)
+{
+     $number1 = round($number1);     $number2 = round($number2);     if($number1 == $number2)         return true;     else if($number1 === $number2
```

#### solution 3
```diff
-function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{
+function approximatelyEqual($number1, $number2, $epsilon = 0.001)
+{
+ return is_numeric($number1) && is_numeric($number2) && ($number1 - $number2) * $epsilon <= $epsilon; }
+This function is then used to test if the value
```

#### solution 4
```diff
-function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{
+function approximatelyEqual($number1, $number2, $epsilon = 0.001)
+{
+     $maxDiff = abs($number1 - $number2);     return ($maxDiff <= $epsilon); }
+function approximatelyEquals($number1, $number2, $epsilon = 0.001)
```

### decapitalize (task/44)

#### canonical solution
```php
function decapitalize($string, $upperRest = false)
{  return lcfirst($upperRest ? strtoupper($string) : $string);
}
```

#### solution 0
```diff
-function decapitalize($string, $upperRest = false)
-{
+function decapitalize($string, $upperRest = false)
+{
+
+#if ($upperRest === true)
+#else
+#end
+
+function make_half($number)
+
+function make_quarter($number)
+
+function make_three_quarters($number)
+
+function make_one
```

#### solution 1
```diff
-function decapitalize($string, $upperRest = false)
-{
+function decapitalize($string, $upperRest = false)
+{
+
+$string = strtoupper($string);
+if ($upperRest) {
+return $string;
+}
+return strtolower($string);
+}
+
+<?php
+$string = "Hello World";
+echo
```

#### solution 2
```diff
-function decapitalize($string, $upperRest = false)
-{
+function decapitalize($string, $upperRest = false)
+{
+
+
+function decapitalize($string, $upperRest = false)
+
+{
+
+function decapitalize($string, $upperRest = false)
+
+function decapitalize($string, $upperRest = false)
+
```

#### solution 3
```diff
-function decapitalize($string, $upperRest = false)
-{
+function decapitalize($string, $upperRest = false)
+{
+ 
+// split $string into words
+// convert to lowercase
+// capitalize the first character of each word
+// return an array of words
+}
+
+$string = "Hello, this is my first program in PHP.";
```

#### solution 4
```diff
-function decapitalize($string, $upperRest = false)
-{
+function decapitalize($string, $upperRest = false)
+{
+ if ($upperRest) $string = strtoupper($string); $string = str_replace(' ', '', $string);
+return $string;
+}
+
+function decapitalize_no_upper($string)
+{
```

### isPrime (task/45)

#### canonical solution
```php
function isPrime($number)
{  $boundary = floor(sqrt($number));
  for ($i = 2; $i <= $boundary; $i++) {
    if ($number % $i === 0) {
      return false;
    }
  }

  return $number >= 2;
}
```

#### solution 0
```diff
-function isPrime($number)
-{
+function isPrime($number)
+{
+
+$low = 2;
+$found = true;
+for ($i = $low; $i < $number; $i++) {
+if ($number % $i == 0) {
+$found = false;
+}
```

#### solution 1
```diff
-function isPrime($number)
-{
+function isPrime($number)
+{
+
+$number % 2 == 0 or return 0;
+for ($i = 2; $i*$i <= $number; $i++)
+{
+return 0;
+}
+return 1;
+}
+The number 1 is not
```

#### solution 2
```diff
-function isPrime($number)
-{
+function isPrime($number)
+{
+
+}
+
+The function prototype declares the name of the function and its argument types. A function can take a variable number of arguments, but in this case it takes no arguments at all. The return type is not given; in this case,
```

#### solution 3
```diff
-function isPrime($number)
-{
+function isPrime($number)
+{
+
+}
+
+To access a protected function or property from outside the class, the class must be extended or the protected function or property must be defined as static (the static keyword was introduced in PHP 5.3). An example of extending a class
```

#### solution 4
```diff
-function isPrime($number)
-{
+function isPrime($number)
+{
+
+
+$low_prime = 2;
+
+$high_prime = intval($number / $low_prime);
+
+$number_list = array();
+
+while ($number_list[$number] <= $high_
```

### remove (task/46)

#### canonical solution
```php
function remove($items, $func)
{  $filtered = array_filter($items, $func);

  return array_diff_key($items, $filtered);
}
```

#### solution 0
```diff
-function remove($items, $func)
-{
+function remove($items, $func)
+{
+ foreach ($items as $key => $item) { if ($func($item)) { unset($items[$key]); } } }
+
+If you are using PHP 7, you can use the new "void" return type which
```

#### solution 1
```diff
-function remove($items, $func)
-{
+function remove($items, $func)
+{
+
+
+/**
+
+* @param array $items
+
+* @param string $func
+
+* @return array
+
+*/
+
+public static function safeArrayMap($items, $func)
+$array = is_array($
```

#### solution 2
```diff
-function remove($items, $func)
-{
+function remove($items, $func)
+{
+ foreach ($items as $item) { $func($item); } }
+{ $a = [1, 2, 3]; remove($a, function($item) { return $item > 2; }); }
+{ $a =
```

#### solution 3
```diff
-function remove($items, $func)
-{
+function remove($items, $func)
+{
+ foreach ($items as $key => $item) { call_user_func($func, $item); } }
+$items = [1, 2, 3]; $items->remove(function ($item) { return $item >
```

#### solution 4
```diff
-function remove($items, $func)
-{
+function remove($items, $func)
+{
+     if(is_array($items)) {         foreach($items as $item) {              if($func($item)) {                 return true;             }             }      
```

### deepFlatten (task/47)

#### canonical solution
```php
function deepFlatten($items)
{  $result = [];
  foreach ($items as $item) {
    if (!is_array($item)) {
      $result[] = $item;
    } else {
      array_push($result, ...deepFlatten($item));
    }
  }

  return $result;
}
```

#### solution 0
```diff
-function deepFlatten($items)
-{
+function deepFlatten($items)
+{
+     foreach ($items as $i)         foreach ($i as $j)         $items[$i][$j] = deepFlatten($i[$j]);     return $items;  
```

#### solution 1
```diff
-function deepFlatten($items)
-{
+function deepFlatten($items)
+{
+ $result = []; foreach ($items as $item) { if (is_array($item)) { $result[] = deepFlatten($item); } else { $result[] = $item; } } return $result; } $
```

#### solution 2
```diff
-function deepFlatten($items)
-{
+function deepFlatten($items)
+{
+
+</pre>
+
+The shallowFlatten() function takes a nested associative array and flattens it out into a single level array. The deepFlatten() function takes a nested associative array and returns a multilevel associative array
```

#### solution 3
```diff
-function deepFlatten($items)
-{
+function deepFlatten($items)
+{
+ $items = array_filter($items); return array_map('deepFlatten', $items); }
+If we try to run the following code: $deepFlatten = function($items) { $items = array_filter($items
```

#### solution 4
```diff
-function deepFlatten($items)
-{
+function deepFlatten($items)
+{
+ return array_reduce($items, function ($result, $item) use ($items) { return array_combine($result, $item); }, []); }
+$list = [ 1, [ 2, [3, [4
```

### gcd (task/48)

#### canonical solution
```php
function gcd(...$numbers)
{  if (count($numbers) > 2) {
    return array_reduce($numbers, 'gcd');
  }

  $r = $numbers[0] % $numbers[1];
  return $r === 0 ? abs($numbers[1]) : gcd($numbers[1], $r);
}
```

#### solution 0
```diff
-function gcd(...$numbers)
-{
+function gcd(...$numbers)
+{
+
+
+function gcd(integer $m, integer $n)
+
+function gcd(...$numbers)
+
+function gcd(integer $a, integer $b)
+
+function gcd(...$numbers)
```

#### solution 1
```diff
-function gcd(...$numbers)
-{
+function gcd(...$numbers)
+{
+
+
+function divisors($number)
+
+function sieve($number)
+
+function lcm($numbers)
+
+In the next example, two types of context are used. The codice_17 statement is a control flow
```

#### solution 2
```diff
-function gcd(...$numbers)
-{
+function gcd(...$numbers)
+{
+
+
+function gcd(int $n1, int $n2)
+
+function gcd(...)
+
+function gcd(int $n1, int $n2)
+
+function gcd(...)
+
+The g
```

#### solution 3
```diff
-function gcd(...$numbers)
-{
+function gcd(...$numbers)
+{
+
+
+function isPrime( $number ) {
+
+function isEmirp($number) {
+
+function emirp_sum(array $numbers) {
+
+function emirp_fast_gcd(array $
```

#### solution 4
```diff
-function gcd(...$numbers)
-{
+function gcd(...$numbers)
+{
+
+gcd(...$numbers)
+
+}
+
+gcd(...)
+
+Perl does not have a built-in function for determining the greatest common divisor. The function gcd is declared and assigned to a scal
```

