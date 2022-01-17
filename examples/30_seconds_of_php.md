### head (task/1)

#### canonical solution

```php
function head($items)
{
  return reset($items);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,3 @@

 function head($items)
-{  return reset($items);
-}
+{ foreach ($items as $item) { $this->items[] = $item; } } }
+$items = array(1, 2, 3, 4, 5); $arr = new ArrayHead($items); echo $arr->
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,2 @@

 function head($items)
-{  return reset($items);
-}
+{ echo "<table width=100% border=1 cellspacing=0 cellpadding=0><tr>"; foreach($items as $k=>$v) { echo "<td align=center valign=top><font color=$v
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,8 @@

 function head($items)
-{  return reset($items);
+{foreach from=$items item=item}
+{if $item.operation == "ADD"
+{set $i++
 }
+
+{/if}
+
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,3 @@

 function head($items)
-{  return reset($items);
-}
+{ $last = $items[count($items)-1]; $first = $items[0]; return $last['title'] . " – " . $first['title']; }
+$books = array( array('title'=>'
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,5 @@

 function head($items)
-{  return reset($items);
-}
+{     return $items[0];     }
+function last($items)
+{     return $items[count($items)-1];     }
+$items = array('first','second','third','fourth','fifth');
```

### median (task/2)

#### canonical solution

```php
function median($numbers)
{
  sort($numbers);
  $totalNumbers = count($numbers);
  $mid = floor($totalNumbers / 2);

  return ($totalNumbers % 2) === 0 ? ($numbers[$mid - 1] + $numbers[$mid]) / 2 : $numbers[$mid];
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,7 +1,2 @@

 function median($numbers)
-{  sort($numbers);
-  $totalNumbers = count($numbers);
-  $mid = floor($totalNumbers / 2);
-
-  return ($totalNumbers % 2) === 0 ? ($numbers[$mid - 1] + $numbers[$mid]) / 2 : $numbers[$mid];
-}
+{ $sum = 0; $count = 0; $divisor = 1; $quotient = 0; $remainder = 0; foreach ($numbers as $number) { $count++; $sum += $number;
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,7 +1,8 @@

 function median($numbers)
-{  sort($numbers);
-  $totalNumbers = count($numbers);
-  $mid = floor($totalNumbers / 2);
+{ return $numbers[(($numbers.length - 1) / 2)]; }
 
-  return ($totalNumbers % 2) === 0 ? ($numbers[$mid - 1] + $numbers[$mid]) / 2 : $numbers[$mid];
-}
+and then we can do things like this:
+
+echo median(range(0, 10)); // 3
+
+To be more specific,
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,8 +1,13 @@

 function median($numbers)
 {
-  sort($numbers);
-  $totalNumbers = count($numbers);
-  $mid = floor($totalNumbers / 2);
 
-  return ($totalNumbers % 2) === 0 ? ($numbers[$mid - 1] + $numbers[$mid]) / 2 : $numbers[$mid];
-}
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
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,8 +1,8 @@

 function median($numbers)
 {
-  sort($numbers);
-  $totalNumbers = count($numbers);
-  $mid = floor($totalNumbers / 2);
+}
 
-  return ($totalNumbers % 2) === 0 ? ($numbers[$mid - 1] + $numbers[$mid]) / 2 : $numbers[$mid];
-}
+An example usage of this function might be:
+$median = median(array('one', 'three', 'eight', 'sixteen'));
+$median = median(
+It is possible to consider that an
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,7 +1,8 @@

 function median($numbers)
-{  sort($numbers);
-  $totalNumbers = count($numbers);
-  $mid = floor($totalNumbers / 2);
+{ $total = 0;
+for ($i = 0; $i < $numbers; $i++) {
+$total += $numbers[$i];
+}
+return $total / count($numbers);
+}
 
-  return ($totalNumbers % 2) === 0 ? ($numbers[$mid - 1] + $numbers[$mid]) / 2 : $numbers[$mid];
-}
```

### take (task/3)

#### canonical solution

```php
function take($items, $n = 1)
{
  return array_slice($items, 0, $n);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,9 @@

 function take($items, $n = 1)
 {
-  return array_slice($items, 0, $n);
-}
+
+if (empty($items)) {
+
+echo "No items selected";
+
+} else {
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,4 @@

 function take($items, $n = 1)
-{  return array_slice($items, 0, $n);
-}
+{ for ($i = 0; $i < $n; $i++) { $items[$i] = "Part " . $i; } return $items; }
+
+This is a naive implementation that might work on small arrays,
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,8 @@

 function take($items, $n = 1)
-{  return array_slice($items, 0, $n);
+{ $this->items = array_merge($this->items, $items);
+if ($n <= count($this->items)) {
+return true;
 }
+return false;
+}
+
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,5 @@

 function take($items, $n = 1)
-{  return array_slice($items, 0, $n);
-}
+{ $this->items = array_merge($this->items, $items); return $this->items[$n-1]; }
+
+
+We then add a few items, and then retrieve the last element, as in Example 4-
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,8 @@

 function take($items, $n = 1)
-{  return array_slice($items, 0, $n);
-}
+{ $result = array(); for ($i = 0; $i < $n; $i++) { $result[] = $items[$i]; } return $result; }
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
{
  return end($items);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,9 @@

 function last($items)
 {
-  return end($items);
-}
+
+function add()
+
+function get_last()
+
+function get_item_name()
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,2 @@

 function last($items)
-{  return end($items);
-}
+{ $total = 0; $last = null; $i = 0; foreach ($items as $item) { if ($i == count($items)) { $last = $item; $total += $item->cost; break; }
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,2 @@

 function last($items)
-{  return end($items);
-}
+{ $last = null; if(is_array($items)) { $first = end($items); if(is_null($first)) { $last = null; } else { $last = $first; } } else { $last
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,4 +1,9 @@

 function last($items)
 {
-  return end($items);
-}
+
+function last2($items)
+
+function last3($items)
+
+function last4($items)
+
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,5 @@

 function last($items)
-{  return end($items);
-}
+{ $last = $items[$this->depth]; $this->depth--; return $last; }
+$first = $items[0];
+function first()
+{ $this->depth = 0; return $first; }
```

### isContains (task/5)

#### canonical solution

```php
function isContains($string, $needle)
{
  return strpos($string, $needle) === false ? false : true;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,5 @@

 function isContains($string, $needle)
-{  return strpos($string, $needle) === false ? false : true;
-}
+{ return preg_match('/'.$needle.'/', $string); }
+function isIn($array, $needle)
+{ foreach ($array as $item)
+{ if ($item == $needle)
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,3 @@

 function isContains($string, $needle)
-{  return strpos($string, $needle) === false ? false : true;
-}
+{ if (count($this->startsWith($string, $needle)) == 0) { return false; } else { return true; } }
+$in_array = function($needle, $haystack) use ($filter
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,4 @@

 function isContains($string, $needle)
-{  return strpos($string, $needle) === false ? false : true;
-}
+{     return (strpos($string, $needle) !== false);     }
+$text = "No longer with us is our beloved father and husband, Donald G.";
+echo "before: ".$text."<
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,2 @@

 function isContains($string, $needle)
-{  return strpos($string, $needle) === false ? false : true;
-}
+{     $needleLen = strlen($needle);     for ($i = 0; $i < strlen($string); $i++) {         if ($string[$i] == $needle[$need
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,2 @@

 function isContains($string, $needle)
-{  return strpos($string, $needle) === false ? false : true;
-}
+{ $needle = trim($needle); $needle = strtolower($needle); //first character is not compared if ($string[0] != $needle) return false; //needle can only be present at the
```

### curry (task/6)

#### canonical solution

```php
function curry($function)
{
  $accumulator = function ($arguments) use ($function, &$accumulator) {
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
--- canonical..php

+++ solution0..php

@@ -1,17 +1,7 @@

 function curry($function)
-{  $accumulator = function ($arguments) use ($function, &$accumulator) {
-    return function (...$args) use ($function, $arguments, $accumulator) {
-      $arguments = array_merge($arguments, $args);
-      $reflection = new ReflectionFunction($function);
-      $totalArguments = $reflection->getNumberOfRequiredParameters();
-
-      if ($totalArguments <= count($arguments)) {
-        return $function(...$arguments);
-      }
-
-      return $accumulator($arguments);
-    };
-  };
-
-  return $accumulator([]);
-}
+{ if(is_callable($function)){
+$result = $function();
+if($result instanceof Closure){
+return $result;
+elseif($result instanceof Array){
+return array_map($function, $result
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,17 +1,3 @@

 function curry($function)
-{  $accumulator = function ($arguments) use ($function, &$accumulator) {
-    return function (...$args) use ($function, $arguments, $accumulator) {
-      $arguments = array_merge($arguments, $args);
-      $reflection = new ReflectionFunction($function);
-      $totalArguments = $reflection->getNumberOfRequiredParameters();
-
-      if ($totalArguments <= count($arguments)) {
-        return $function(...$arguments);
-      }
-
-      return $accumulator($arguments);
-    };
-  };
-
-  return $accumulator([]);
-}
+{ //function to execute return function($arg1, $arg2) use ($function) { return $function($arg1, $arg2); }; }
+$curryedAdd = curry(function($a, $b) { return
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,17 +1,4 @@

 function curry($function)
-{  $accumulator = function ($arguments) use ($function, &$accumulator) {
-    return function (...$args) use ($function, $arguments, $accumulator) {
-      $arguments = array_merge($arguments, $args);
-      $reflection = new ReflectionFunction($function);
-      $totalArguments = $reflection->getNumberOfRequiredParameters();
-
-      if ($totalArguments <= count($arguments)) {
-        return $function(...$arguments);
-      }
-
-      return $accumulator($arguments);
-    };
-  };
-
-  return $accumulator([]);
-}
+{ $function = $function ?? ''; return function() use ($function) { $function($this); return $this; }; }
+$curryed = curry(function($number) { return $number + 1; });
+echo $
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,17 +1,2 @@

 function curry($function)
-{  $accumulator = function ($arguments) use ($function, &$accumulator) {
-    return function (...$args) use ($function, $arguments, $accumulator) {
-      $arguments = array_merge($arguments, $args);
-      $reflection = new ReflectionFunction($function);
-      $totalArguments = $reflection->getNumberOfRequiredParameters();
-
-      if ($totalArguments <= count($arguments)) {
-        return $function(...$arguments);
-      }
-
-      return $accumulator($arguments);
-    };
-  };
-
-  return $accumulator([]);
-}
+{ return function($var1, $var2) use ($function) { return $function($var1, $var2); }; } $add1 = curry(function($x, $y) { return $x + $y; });
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,18 +1,9 @@

 function curry($function)
 {
-  $accumulator = function ($arguments) use ($function, &$accumulator) {
-    return function (...$args) use ($function, $arguments, $accumulator) {
-      $arguments = array_merge($arguments, $args);
-      $reflection = new ReflectionFunction($function);
-      $totalArguments = $reflection->getNumberOfRequiredParameters();
 
-      if ($totalArguments <= count($arguments)) {
-        return $function(...$arguments);
-      }
+$function(mixed $arg1, mixed $arg2 = null)
+$function = (function(mixed $arg1, mixed $arg2 = null) 
 
-      return $accumulator($arguments);
-    };
-  };
+function curried($function)
 
-  return $accumulator([]);
-}
+$
```

### isAnagram (task/7)

#### canonical solution

```php
function isAnagram($string1, $string2)
{
  return count_chars($string1, 1) === count_chars($string2, 1);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,9 @@

 function isAnagram($string1, $string2)
 {
-  return count_chars($string1, 1) === count_chars($string2, 1);
+
+function isPalindrome($string)
+
+{
+
 }
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,4 +1,7 @@

 function isAnagram($string1, $string2)
 {
-  return count_chars($string1, 1) === count_chars($string2, 1);
-}
+$length1 = strlen($string1);
+$length2 = strlen($string2);
+if($length1 != $length2) return 0;
+$char1 = $string1[0];
+$char2
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,2 @@

 function isAnagram($string1, $string2)
-{  return count_chars($string1, 1) === count_chars($string2, 1);
-}
+{ $length1 = strlen($string1); $length2 = strlen($string2); $alpha1 = substr($string1, 0, $length1-1); $alpha2 = substr($string2, 0, $length
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,6 @@

 function isAnagram($string1, $string2)
-{  return count_chars($string1, 1) === count_chars($string2, 1);
+{ // return true if $string1 is a substring of $string2
 }
+The function isAnagram accepts two strings as parameters and then checks if the first one is a substring of the second one.
+
+If the same method
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,2 @@

 function isAnagram($string1, $string2)
-{  return count_chars($string1, 1) === count_chars($string2, 1);
-}
+{ $string1 = strtolower($string1); $string2 = strtolower($string2); for($i = 0; $i < strlen($string1); $i++) { if(strcmp($string1
```

### hasDuplicates (task/8)

#### canonical solution

```php
function hasDuplicates($items)
{
  return count($items) > count(array_unique($items));
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,2 @@

 function hasDuplicates($items)
-{  return count($items) > count(array_unique($items));
-}
+{ $hasDuplicates = false; foreach ($items as $item) { if (in_array($item, $previous)) { $hasDuplicates = true; break; } } return $hasDuplicates; }
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,2 @@

 function hasDuplicates($items)
-{  return count($items) > count(array_unique($items));
-}
+{ $found = 0; $value = 0; foreach ($items as $item) { if (isset($this->cache[$item->id])) { if ($this->cache[$item->id]->value == $
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,5 @@

 function hasDuplicates($items)
-{  return count($items) > count(array_unique($items));
+{ return $items->filter(function($item) use ($items) { return !$items->contains($item); }); }
 }
+
+This approach could be easily extended to define an interface for the list of items and test the many
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,2 @@

 function hasDuplicates($items)
-{  return count($items) > count(array_unique($items));
-}
+{ $duplicates = []; foreach ($items as $key => $item) { if (in_array($item, $duplicates)) { $duplicates[] = $key; } else { $duplicates[] =
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,2 @@

 function hasDuplicates($items)
-{  return count($items) > count(array_unique($items));
-}
+{     $results = array();     $count = count($items);     $index = 0;     foreach ($items as $item) {         if (!array_key_exists($item, $results
```

### factorial (task/9)

#### canonical solution

```php
function factorial($n)
{
  if ($n <= 1) {
    return 1;
  }

  return $n * factorial($n - 1);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,8 +1,7 @@

 function factorial($n)
 {
-  if ($n <= 1) {
-    return 1;
-  }
 
-  return $n * factorial($n - 1);
-}
+function factorial($n)
+
+This function is named with a different name than the generic function and is called with different arguments. Since the function is named, it is clear to the programmer calling it what will be returned.
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,8 +1,6 @@

 function factorial($n)
 {
-  if ($n <= 1) {
-    return 1;
-  }
 
-  return $n * factorial($n - 1);
-}
+function factorial($n)
+
+Here we have to add in the extra step of adding 1 to the running total. We can do this by performing the first loop iteration, then adding 1 to the running total before starting the second loop
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,7 +1,3 @@

 function factorial($n)
-{  if ($n <= 1) {
-    return 1;
-  }
-
-  return $n * factorial($n - 1);
-}
+{ $n = intval($n); $n = $n * (1..$n-1); return $n; }
+$n = '6'; echo "$n! = ".factorial($n)."<br>";
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,8 +1,12 @@

 function factorial($n)
 {
-  if ($n <= 1) {
-    return 1;
-  }
+</syntaxhighlight>
+</div>
 
-  return $n * factorial($n - 1);
-}
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
--- canonical..php

+++ solution4..php

@@ -1,8 +1,12 @@

 function factorial($n)
 {
-  if ($n <= 1) {
-    return 1;
-  }
 
-  return $n * factorial($n - 1);
-}
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
{
  return function (...$args) use ($function) {
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
--- canonical..php

+++ solution0..php

@@ -1,11 +1,11 @@

 function once($function)
 {
-  return function (...$args) use ($function) {
-    static $called = false;
-    if ($called) {
-      return;
-    }
-    $called = true;
-    return $function(...$args);
-  };
-}
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
--- canonical..php

+++ solution1..php

@@ -1,10 +1,4 @@

 function once($function)
-{  return function (...$args) use ($function) {
-    static $called = false;
-    if ($called) {
-      return;
-    }
-    $called = true;
-    return $function(...$args);
-  };
-}
+{ if(is_callable($function)) { $function(); } else { trigger_error("Function %s not found", $function); } }
+function trigger_error($message)
+{ error_log("Caught exception in function
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,10 +1,2 @@

 function once($function)
-{  return function (...$args) use ($function) {
-    static $called = false;
-    if ($called) {
-      return;
-    }
-    $called = true;
-    return $function(...$args);
-  };
-}
+{ $entry_count = 0; $entry_start = -1; $entry_end = -1; $non_entry_start = -1; $non_entry_end = -1; $context = ''; $pattern
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,11 +1,13 @@

 function once($function)
 {
-  return function (...$args) use ($function) {
-    static $called = false;
-    if ($called) {
-      return;
-    }
-    $called = true;
-    return $function(...$args);
-  };
-}
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
--- canonical..php

+++ solution4..php

@@ -1,10 +1,6 @@

 function once($function)
-{  return function (...$args) use ($function) {
-    static $called = false;
-    if ($called) {
-      return;
-    }
-    $called = true;
-    return $function(...$args);
-  };
-}
+{ $function = strtolower($function);
+if (in_array($function, $functions)) {
+$cache[$function] = $GLOBALS[$function];
+return $cache[$function];
+else
```

### endsWith (task/11)

#### canonical solution

```php
function endsWith($haystack, $needle)
{
  return strrpos($haystack, $needle) === (strlen($haystack) - strlen($needle));
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,2 @@

 function endsWith($haystack, $needle)
-{  return strrpos($haystack, $needle) === (strlen($haystack) - strlen($needle));
-}
+{ $haystack = trim($haystack); $needle = trim($needle); if ($haystack === $needle) { return true; } if ($haystack === '') { return false; } return str
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,2 @@

 function endsWith($haystack, $needle)
-{  return strrpos($haystack, $needle) === (strlen($haystack) - strlen($needle));
-}
+{ if(strlen($haystack) < strlen($needle)) { return false; } else { $haystack = substr($haystack, 0, strlen($needle)); for($i = 0; $i
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,4 +1,8 @@

 function endsWith($haystack, $needle)
 {
-  return strrpos($haystack, $needle) === (strlen($haystack) - strlen($needle));
-}
+
+function indexOf($haystack, $needle)
+
+function countOccurrences($haystack, $needle)
+
+function countOccurrences($haystack, $needle, $offset = 0
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,4 +1,9 @@

 function endsWith($haystack, $needle)
 {
-  return strrpos($haystack, $needle) === (strlen($haystack) - strlen($needle));
-}
+
+function strlen($string)
+
+{
+
+function strrev($string)
+
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,4 +1,9 @@

 function endsWith($haystack, $needle)
 {
-  return strrpos($haystack, $needle) === (strlen($haystack) - strlen($needle));
-}
+
+function add(x, y)
+
+function sub(x, y)
+
+function mul(x, y)
+
```

### lcm (task/12)

#### canonical solution

```php
function lcm(...$numbers)
{
  $ans = $numbers[0];
  for ($i = 1, $max = count($numbers); $i < $max; $i++) {
    $ans = (($numbers[$i] * $ans) / gcd($numbers[$i], $ans));
  }

  return $ans;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,8 +1,13 @@

 function lcm(...$numbers)
-{  $ans = $numbers[0];
-  for ($i = 1, $max = count($numbers); $i < $max; $i++) {
-    $ans = (($numbers[$i] * $ans) / gcd($numbers[$i], $ans));
-  }
+{ 
+}
 
-  return $ans;
-}
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
--- canonical..php

+++ solution1..php

@@ -1,8 +1,2 @@

 function lcm(...$numbers)
-{  $ans = $numbers[0];
-  for ($i = 1, $max = count($numbers); $i < $max; $i++) {
-    $ans = (($numbers[$i] * $ans) / gcd($numbers[$i], $ans));
-  }
-
-  return $ans;
-}
+{ $sqrtnums = $numbers | foreach {$_ * $_} $sum = 0 foreach ($n in $sqrtnums) { $sum += $n } return [math]::pow($sum,
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,9 +1,11 @@

 function lcm(...$numbers)
 {
-  $ans = $numbers[0];
-  for ($i = 1, $max = count($numbers); $i < $max; $i++) {
-    $ans = (($numbers[$i] * $ans) / gcd($numbers[$i], $ans));
-  }
+$result = 1;
+foreach($numbers as $number)
+{
+$result *= $number;
+}
+return $result;
+}
 
-  return $ans;
-}
+The LCM of the list of integers 1, 2, and
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,9 +1,9 @@

 function lcm(...$numbers)
 {
-  $ans = $numbers[0];
-  for ($i = 1, $max = count($numbers); $i < $max; $i++) {
-    $ans = (($numbers[$i] * $ans) / gcd($numbers[$i], $ans));
-  }
-
-  return $ans;
-}
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
--- canonical..php

+++ solution4..php

@@ -1,9 +1,10 @@

 function lcm(...$numbers)
 {
-  $ans = $numbers[0];
-  for ($i = 1, $max = count($numbers); $i < $max; $i++) {
-    $ans = (($numbers[$i] * $ans) / gcd($numbers[$i], $ans));
-  }
+$lcm = 1;
+for ($i = 1; $i < $numbers; $i++) {
 
-  return $ans;
+$lcm *= $numbers[$i];
+
 }
+
+return $lcm;
```

### without (task/13)

#### canonical solution

```php
function without($items, ...$params)
{
  return array_values(array_diff($items, $params));
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,5 @@

 function without($items, ...$params)
-{  return array_values(array_diff($items, $params));
+{ # $items is an array or a Traversable object
 }
+
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,6 @@

 function without($items, ...$params)
-{  return array_values(array_diff($items, $params));
-}
+{ // ... }
+
+You could say that the second argument is a named list, but it can have only a single element.
+
+Structures are very similar to anonymous unions in C. We could write an array-of-structures like
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,2 @@

 function without($items, ...$params)
-{  return array_values(array_diff($items, $params));
-}
+{ <script> var $items = $items; if ($items === null) return; if ($items instanceof HTMLElement) { $items = $items.getAttribute('data-tooltip'); } if ($items === null)
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,6 @@

 function without($items, ...$params)
-{  return array_values(array_diff($items, $params));
-}
+{ $params = iterator_to_array($params);
+foreach ($items as $key => $item) {
+if (isset($params[$key])) {
+$value = $params[$key];
+$items
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,4 +1,6 @@

 function without($items, ...$params)
 {
-  return array_values(array_diff($items, $params));
-}
+
+To define a class, the "class" keyword is used. To instantiate an object, the "new" keyword is used:
+
+To define a class, the "class" keyword is used. To instantiate an object,
```

### fibonacci (task/14)

#### canonical solution

```php
function fibonacci($n)
{
  $sequence = [0, 1];

  for ($i = 2; $i < $n; $i++) {
    $sequence[$i] = $sequence[$i-1] + $sequence[$i-2];
  }

  return $sequence;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,10 +1,14 @@

 function fibonacci($n)
 {
-  $sequence = [0, 1];
 
-  for ($i = 2; $i < $n; $i++) {
-    $sequence[$i] = $sequence[$i-1] + $sequence[$i-2];
-  }
+function bernoulli($n)
 
-  return $sequence;
-}
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
--- canonical..php

+++ solution1..php

@@ -1,10 +1,15 @@

 function fibonacci($n)
 {
-  $sequence = [0, 1];
 
-  for ($i = 2; $i < $n; $i++) {
-    $sequence[$i] = $sequence[$i-1] + $sequence[$i-2];
-  }
+echo(n);
+}
 
-  return $sequence;
-}
+?>
+
+Example of recursion:
+
+<?php
+
+function fibonacci($n)
+
+{
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,10 +1,7 @@

 function fibonacci($n)
 {
-  $sequence = [0, 1];
 
-  for ($i = 2; $i < $n; $i++) {
-    $sequence[$i] = $sequence[$i-1] + $sequence[$i-2];
-  }
+}
+This function does exactly the same thing as the previous one, but it is not functional.
 
-  return $sequence;
-}
+In the functional definition of fibonacci the argument n is not the source of data, it is the "context" of the
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,9 +1,6 @@

 function fibonacci($n)
-{  $sequence = [0, 1];
+{ if ($n <= 2) { return 1; } return fibonacci($n - 1) + fibonacci($n - 2); } }
 
-  for ($i = 2; $i < $n; $i++) {
-    $sequence[$i] = $sequence[$i-1] + $sequence[$i-2];
-  }
 
-  return $sequence;
-}
+
+This is a recursive function that calls itself to determine the values for n = 1
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,10 +1,12 @@

 function fibonacci($n)
 {
-  $sequence = [0, 1];
 
-  for ($i = 2; $i < $n; $i++) {
-    $sequence[$i] = $sequence[$i-1] + $sequence[$i-2];
-  }
+function fibo(int $n)
 
-  return $sequence;
-}
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
{
  $group = [];
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
--- canonical..php

+++ solution0..php

@@ -1,15 +1,2 @@

 function groupBy($items, $func)
-{  $group = [];
-  foreach ($items as $item) {
-    if ((!is_string($func) && is_callable($func)) || function_exists($func)) {
-      $key = call_user_func($func, $item);
-      $group[$key][] = $item;
-    } elseif (is_object($item)) {
-      $group[$item->{$func}][] = $item;
-    } elseif (isset($item[$func])) {
-      $group[$item[$func]][] = $item;
-    }
-  }
-
-  return $group;
-}
+{ $items = iterator_to_array($items); $groups = array(); foreach ($items as $item) { $groups[$func($item)] = $item; } return $groups; } function GroupBy($data, $
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,15 +1,5 @@

 function groupBy($items, $func)
-{  $group = [];
-  foreach ($items as $item) {
-    if ((!is_string($func) && is_callable($func)) || function_exists($func)) {
-      $key = call_user_func($func, $item);
-      $group[$key][] = $item;
-    } elseif (is_object($item)) {
-      $group[$item->{$func}][] = $item;
-    } elseif (isset($item[$func])) {
-      $group[$item[$func]][] = $item;
-    }
-  }
+{ return array_map($func, $items); }
+}
 
-  return $group;
-}
+In the above example, the method groupBy() returns an array, whose items are arrays of the same size, each with a single member. The method simply maps the value
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,16 +1,11 @@

 function groupBy($items, $func)
 {
-  $group = [];
-  foreach ($items as $item) {
-    if ((!is_string($func) && is_callable($func)) || function_exists($func)) {
-      $key = call_user_func($func, $item);
-      $group[$key][] = $item;
-    } elseif (is_object($item)) {
-      $group[$item->{$func}][] = $item;
-    } elseif (isset($item[$func])) {
-      $group[$item[$func]][] = $item;
-    }
-  }
 
-  return $group;
-}
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
--- canonical..php

+++ solution3..php

@@ -1,15 +1,3 @@

 function groupBy($items, $func)
-{  $group = [];
-  foreach ($items as $item) {
-    if ((!is_string($func) && is_callable($func)) || function_exists($func)) {
-      $key = call_user_func($func, $item);
-      $group[$key][] = $item;
-    } elseif (is_object($item)) {
-      $group[$item->{$func}][] = $item;
-    } elseif (isset($item[$func])) {
-      $group[$item[$func]][] = $item;
-    }
-  }
-
-  return $group;
-}
+{ $groups = array(); foreach ($items as $item) { $groups[$func($item)] = $item; } return $groups; }
+$items = collect(['a', 'b', 'c', 'd',
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,15 +1,2 @@

 function groupBy($items, $func)
-{  $group = [];
-  foreach ($items as $item) {
-    if ((!is_string($func) && is_callable($func)) || function_exists($func)) {
-      $key = call_user_func($func, $item);
-      $group[$key][] = $item;
-    } elseif (is_object($item)) {
-      $group[$item->{$func}][] = $item;
-    } elseif (isset($item[$func])) {
-      $group[$item[$func]][] = $item;
-    }
-  }
-
-  return $group;
-}
+{     $groupBy = array();     foreach ($items as $item) {         if ($func($item)) {             $groupBy[] = $item;     }     }     return $
```

### maxN (task/16)

#### canonical solution

```php
function maxN($numbers)
{
  $maxValue = max($numbers);
  $maxValueArray = array_filter($numbers, function ($value) use ($maxValue) {
    return $maxValue === $value;
  });

  return count($maxValueArray);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,8 +1,6 @@

 function maxN($numbers)
-{  $maxValue = max($numbers);
-  $maxValueArray = array_filter($numbers, function ($value) use ($maxValue) {
-    return $maxValue === $value;
-  });
+{ if($numbers > $max) return $max; $max = $numbers; return $max; }
+$maxN = maxN(array_unique(range(10)))
+$maxN = 10
 
-  return count($maxValueArray);
-}
+While this
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,9 +1,10 @@

 function maxN($numbers)
 {
-  $maxValue = max($numbers);
-  $maxValueArray = array_filter($numbers, function ($value) use ($maxValue) {
-    return $maxValue === $value;
-  });
 
-  return count($maxValueArray);
-}
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
--- canonical..php

+++ solution2..php

@@ -1,8 +1,3 @@

 function maxN($numbers)
-{  $maxValue = max($numbers);
-  $maxValueArray = array_filter($numbers, function ($value) use ($maxValue) {
-    return $maxValue === $value;
-  });
-
-  return count($maxValueArray);
-}
+{ return $numbers[0] * $numbers[1] * ... * $numbers[$numbers.Length - 1]; } }
+This would be straightforward to understand, but it's also a bit wordy. It would
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,8 +1,6 @@

 function maxN($numbers)
-{  $maxValue = max($numbers);
-  $maxValueArray = array_filter($numbers, function ($value) use ($maxValue) {
-    return $maxValue === $value;
-  });
+{ 
 
-  return count($maxValueArray);
-}
+<poem>The first number is: $numbers[0]
+The last number is: $numbers[$numbers.Length - 1]
+The maximum number is: $numbers[$numbers.
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,9 +1,12 @@

 function maxN($numbers)
 {
-  $maxValue = max($numbers);
-  $maxValueArray = array_filter($numbers, function ($value) use ($maxValue) {
-    return $maxValue === $value;
-  });
 
-  return count($maxValueArray);
-}
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
{
  return array_slice($items, $n);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,6 @@

 function drop($items, $n = 1)
-{  return array_slice($items, $n);
-}
+{ foreach ($items as $item) { if (in_array($item, $n)) { unset($items[$n]); $n--; } } }
+
+
+
+echo "How many items would you like to drop?
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,3 @@

 function drop($items, $n = 1)
-{  return array_slice($items, $n);
-}
+{     $items = array_slice($items, 0, $n);     return $items;     }
+In this example, we're just copying the items to a new array, but it could just as easily be a pivot
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,8 @@

 function drop($items, $n = 1)
-{  return array_slice($items, $n);
+{ $count = 0;
+foreach ($items as $i) {
+return $count;
 }
+The above code can be used in an asynchronous way as well, but it would require the following:
+
+function drop($items,
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,3 @@

 function drop($items, $n = 1)
-{  return array_slice($items, $n);
-}
+{ $tmp = array_reverse($items); return array_splice($tmp, $n, 1); }
+(note: you can use this function in other cases as well: for example in a form submit function, where you want to
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,2 @@

 function drop($items, $n = 1)
-{  return array_slice($items, $n);
-}
+{      $items = [0,1,2,3,4,5,6,7,8,9,10];      $i = 0;      while ($i <= $n)      {         
```

### orderBy (task/18)

#### canonical solution

```php
function orderBy($items, $attr, $order)
{
  $sortedItems = [];
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
--- canonical..php

+++ solution0..php

@@ -1,15 +1,16 @@

 function orderBy($items, $attr, $order)
 {
-  $sortedItems = [];
-  foreach ($items as $item) {
-    $key = is_object($item) ? $item->{$attr} : $item[$attr];
-    $sortedItems[$key] = $item;
-  }
-  if ($order === 'desc') {
-    krsort($sortedItems);
-  } else {
-    ksort($sortedItems);
-  }
 
-  return array_values($sortedItems);
 }
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
--- canonical..php

+++ solution1..php

@@ -1,14 +1,2 @@

 function orderBy($items, $attr, $order)
-{  $sortedItems = [];
-  foreach ($items as $item) {
-    $key = is_object($item) ? $item->{$attr} : $item[$attr];
-    $sortedItems[$key] = $item;
-  }
-  if ($order === 'desc') {
-    krsort($sortedItems);
-  } else {
-    ksort($sortedItems);
-  }
-
-  return array_values($sortedItems);
-}
+{  $items = array_filter($items, 'is_numeric');  $sort_array = array();  foreach ($items as $key => $value) {   $sort_array[$key] = strtou
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,15 +1,10 @@

 function orderBy($items, $attr, $order)
 {
-  $sortedItems = [];
-  foreach ($items as $item) {
-    $key = is_object($item) ? $item->{$attr} : $item[$attr];
-    $sortedItems[$key] = $item;
-  }
-  if ($order === 'desc') {
-    krsort($sortedItems);
-  } else {
-    ksort($sortedItems);
-  }
 
-  return array_values($sortedItems);
-}
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
--- canonical..php

+++ solution3..php

@@ -1,15 +1,11 @@

 function orderBy($items, $attr, $order)
 {
-  $sortedItems = [];
-  foreach ($items as $item) {
-    $key = is_object($item) ? $item->{$attr} : $item[$attr];
-    $sortedItems[$key] = $item;
-  }
-  if ($order === 'desc') {
-    krsort($sortedItems);
-  } else {
-    ksort($sortedItems);
-  }
 
-  return array_values($sortedItems);
-}
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
--- canonical..php

+++ solution4..php

@@ -1,14 +1,2 @@

 function orderBy($items, $attr, $order)
-{  $sortedItems = [];
-  foreach ($items as $item) {
-    $key = is_object($item) ? $item->{$attr} : $item[$attr];
-    $sortedItems[$key] = $item;
-  }
-  if ($order === 'desc') {
-    krsort($sortedItems);
-  } else {
-    ksort($sortedItems);
-  }
-
-  return array_values($sortedItems);
-}
+{  if (isset($attr['from'])) { $order = $attr['from']; unset($attr['from']); }  $items = array_slice($items, 0, $order);  foreach ($items
```

### rotate (task/19)

#### canonical solution

```php
function rotate($array, $shift = 1)
{
  for ($i = 0; $i < $shift; $i++) {
    array_push($array, array_shift($array));
  }

  return $array;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,8 +1,11 @@

 function rotate($array, $shift = 1)
 {
-  for ($i = 0; $i < $shift; $i++) {
-    array_push($array, array_shift($array));
-  }
+foreach($array as $value)
 
-  return $array;
+$array = array_rotate($array, $shift);
+return $array;
 }
+
+Inline Functions
+
+The inline keyword can be used on a function. It is
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,8 +1,11 @@

 function rotate($array, $shift = 1)
 {
-  for ($i = 0; $i < $shift; $i++) {
-    array_push($array, array_shift($array));
-  }
+function rotate($array, $shift = 1)
 
-  return $array;
-}
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
--- canonical..php

+++ solution2..php

@@ -1,7 +1,6 @@

 function rotate($array, $shift = 1)
-{  for ($i = 0; $i < $shift; $i++) {
-    array_push($array, array_shift($array));
-  }
-
-  return $array;
-}
+{ # shift the array
+# 1) set the new base $base = $array[0];
+# 2) identify the leftovers
+# 3) build the right array (passing in the base)
+# 4) return the new
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,7 +1,2 @@

 function rotate($array, $shift = 1)
-{  for ($i = 0; $i < $shift; $i++) {
-    array_push($array, array_shift($array));
-  }
-
-  return $array;
-}
+{ if (is_array($array)) { $array2 = array(); for ($i = 0; $i < count($array); $i++) { $array2[$i] = $array[$i] + $shift;
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,8 +1,12 @@

 function rotate($array, $shift = 1)
 {
-  for ($i = 0; $i < $shift; $i++) {
-    array_push($array, array_shift($array));
-  }
 
-  return $array;
-}
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
{
  if (mb_strlen($input) <= $length) {
    return $input;
  }

  return rtrim(mb_substr($input, 0, $length, 'UTF-8')) . $end;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,7 +1,3 @@

 function shorten($input, $length = 100, $end = '...')
-{  if (mb_strlen($input) <= $length) {
-    return $input;
-  }
-
-  return rtrim(mb_substr($input, 0, $length, 'UTF-8')) . $end;
-}
+{ $segments = array(); $result = ''; $expiration = ''; $input = preg_replace('#[\r
+]#', '', $input); $input = preg_replace('#[\s
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,8 +1,10 @@

 function shorten($input, $length = 100, $end = '...')
 {
-  if (mb_strlen($input) <= $length) {
-    return $input;
-  }
 
-  return rtrim(mb_substr($input, 0, $length, 'UTF-8')) . $end;
-}
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
--- canonical..php

+++ solution2..php

@@ -1,8 +1,8 @@

 function shorten($input, $length = 100, $end = '...')
 {
-  if (mb_strlen($input) <= $length) {
-    return $input;
-  }
 
-  return rtrim(mb_substr($input, 0, $length, 'UTF-8')) . $end;
-}
+function join($input, $sep = ', ')
+
+function get_date($input, $default = 'now')
+
+function j_strftime($input, $format, $timestamp = 'now')
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,8 +1,8 @@

 function shorten($input, $length = 100, $end = '...')
 {
-  if (mb_strlen($input) <= $length) {
-    return $input;
-  }
-
-  return rtrim(mb_substr($input, 0, $length, 'UTF-8')) . $end;
-}
+$output = "";
+for ($i = 0; $i < $length; $i++) {
+if (strlen($input) > $i) {
+else {
+$output .= $end;
+$output
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,7 +1,5 @@

 function shorten($input, $length = 100, $end = '...')
-{  if (mb_strlen($input) <= $length) {
-    return $input;
-  }
-
-  return rtrim(mb_substr($input, 0, $length, 'UTF-8')) . $end;
-}
+{ $remainder = strlen($input);
+while ( strlen($input) >= $length ) {
+if ( substr($input, -1) != $end ) {
+$input = substr($input, 0, -1
```

### average (task/21)

#### canonical solution

```php
function average(...$items)
{
  $count = count($items);
  
  return $count === 0 ? 0 : array_sum($items) / $count;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,6 +1,10 @@

 function average(...$items)
 {
-  $count = count($items);
-  
-  return $count === 0 ? 0 : array_sum($items) / $count;
+
+return $items[mean(scalar(@items))];
+
 }
+
+This function would have to be defined in the same module as the function that calls it.
+
+Note that overloading functions in this way is
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,5 +1,3 @@

 function average(...$items)
-{  $count = count($items);
-  
-  return $count === 0 ? 0 : array_sum($items) / $count;
-}
+{     $sum = 0;     foreach ($items as $item) {         $sum += $item;     }     return $sum / count($items);     }
+The first difference is that the
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,5 +1,3 @@

 function average(...$items)
-{  $count = count($items);
-  
-  return $count === 0 ? 0 : array_sum($items) / $count;
-}
+{   return ($items * $items) / (sum($items) - sum(distinct(...$items)));   }
+This method is very similar to the one we implemented before. Instead of using distinct() it calls sum() to
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,5 +1,4 @@

 function average(...$items)
-{  $count = count($items);
-  
-  return $count === 0 ? 0 : array_sum($items) / $count;
-}
+{     return (sum(...$items)) / (length(...$items));     }
+If you run this, you'll see that average is faster for small inputs but not for large inputs. What's going on?
+The
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,5 +1,3 @@

 function average(...$items)
-{  $count = count($items);
-  
-  return $count === 0 ? 0 : array_sum($items) / $count;
-}
+{     return ($items[0] + $items[1] + $items[2]...) / 3;     }
+Instead of being a problem, this is a golden opportunity. We can use the fact that the values are now
```

### reject (task/22)

#### canonical solution

```php
function reject($items, $func)
{
  return array_values(array_diff($items, array_filter($items, $func)));
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,9 @@

 function reject($items, $func)
 {
-  return array_values(array_diff($items, array_filter($items, $func)));
-}
+
+$items = $items * 10;
+
+$items = $items * 10;
+
+echo $items;
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,2 @@

 function reject($items, $func)
-{  return array_values(array_diff($items, array_filter($items, $func)));
-}
+{ $this->items[$items[0]] = $func($items[1]); return $this; } } $myShoppingCart = new ShoppingCart(); $myShoppingCart->addItem('apple', 'Eat it!');
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,8 @@

 function reject($items, $func)
-{  return array_values(array_diff($items, array_filter($items, $func)));
-}
+{ }
+
+
+$items = [1, 2, 3];
+
+$func = function ($i) { return $i * 3; };
+
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,4 +1,9 @@

 function reject($items, $func)
 {
-  return array_values(array_diff($items, array_filter($items, $func)));
-}
+
+<!--BEGINNING OF FUNCTION PARAMETERS-->
+
+$items = $arg1;
+
+$func = $arg2;
+
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,3 @@

 function reject($items, $func)
-{  return array_values(array_diff($items, array_filter($items, $func)));
-}
+{ echo '<p>' . $items . '</p>'; } ?>
+<p> <form action="<?php echo $PHP_SELF; ?>" method="post"> <?php $i = 0;
```

### any (task/23)

#### canonical solution

```php
function any($items, $func)
{
  return count(array_filter($items, $func)) > 0;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,4 @@

 function any($items, $func)
-{  return count(array_filter($items, $func)) > 0;
-}
+{ if (isset($items[0])) { 
+
+The $items array is usually an associative array or object, and the $func is the name of a user-defined function that acts on a single item in the array.
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,8 @@

 function any($items, $func)
-{  return count(array_filter($items, $func)) > 0;
-}
+{ 
+
+function any($items, $func)
+{ 
+
+function collect($items, $func)
+{ 
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,4 +1,5 @@

 function any($items, $func)
 {
-  return count(array_filter($items, $func)) > 0;
-}
+
+If there are not enough items to call the $func on, we call the $func with an empty array and return that.
+If there are enough items, we call the $func on each item, and return the result of the
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,4 +1,9 @@

 function any($items, $func)
 {
-  return count(array_filter($items, $func)) > 0;
+
+<br>
+
+<br>
+
 }
+
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,4 @@

 function any($items, $func)
-{  return count(array_filter($items, $func)) > 0;
-}
+{ foreach($items as $item) { if($func($item)) { return true; } } return false; }
+Step 2: Add the processor that will handle the tag
+In order to pass a test item through our processor, we
```

### flatten (task/24)

#### canonical solution

```php
function flatten($items)
{
  $result = [];
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
--- canonical..php

+++ solution0..php

@@ -1,12 +1,8 @@

 function flatten($items)
-{  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...array_values($item));
-    }
-  }
-
-  return $result;
-}
+{  foreach ($items as $item)
+{  if (is_array($item))
+{  foreach ($item as $subitem)
+{  flatten($subitem);
+ }
+ }
+ }
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,12 +1,2 @@

 function flatten($items)
-{  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...array_values($item));
-    }
-  }
-
-  return $result;
-}
+{      foreach ($items as $item)     {         // if its not an array, send it along         if (!is_array($item))         {             $items[] = $
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,12 +1,3 @@

 function flatten($items)
-{  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...array_values($item));
-    }
-  }
-
-  return $result;
-}
+{ $output = []; foreach ($items as $item) { $output[] = $item; } return $output; } function flatten(array $items)
+pow($a, $b) { return $a ** $b
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,12 +1,2 @@

 function flatten($items)
-{  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...array_values($item));
-    }
-  }
-
-  return $result;
-}
+{     $result = [];     foreach ($items as $item)     {         if (is_array($item))         {             $result[] = flatten($item);             }
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,13 +1,10 @@

 function flatten($items)
 {
-  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...array_values($item));
-    }
-  }
 
-  return $result;
-}
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
{
  return strpos($haystack, $needle) === 0;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,7 @@

 function startsWith($haystack, $needle)
 {
-  return strpos($haystack, $needle) === 0;
 }
+
+This function will search any given string for the first occurrence of a given substring.
+
+PHP allows any number of functions to be defined within a single PHP file, as long as the file is executed as a PHP script
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,4 +1,9 @@

 function startsWith($haystack, $needle)
 {
-  return strpos($haystack, $needle) === 0;
-}
+
+function startsWith($haystack, $needle)
+
+function startsWith($haystack, $needle)
+
+function startsWith($haystack, $needle)
+
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,8 @@

 function startsWith($haystack, $needle)
-{  return strpos($haystack, $needle) === 0;
-}
+{ 
+if ($needle === $haystack) {
+return true;
+} elseif ($needle !== null) {
+return false;
+} else {
+return null;
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,2 @@

 function startsWith($haystack, $needle)
-{  return strpos($haystack, $needle) === 0;
-}
+{ $haystack = strtolower($haystack); $needle = strtolower($needle); $needlelen = strlen($needle); $needlepos = strpos($haystack, $
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,2 @@

 function startsWith($haystack, $needle)
-{  return strpos($haystack, $needle) === 0;
-}
+{     $needle = strtolower($needle);     $haystack = strtolower($haystack);     if (strpos($haystack, $needle) === false)      
```

### clampNumber (task/26)

#### canonical solution

```php
function clampNumber($num, $a, $b)
{
  return max(min($num, max($a, $b)), min($a, $b));
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,3 @@

 function clampNumber($num, $a, $b)
 {
-  return max(min($num, max($a, $b)), min($a, $b));
-}
+The third argument is used in cases where a binary operation is not defined for two values. For example, there is no binary operation defined for the number zero, and the addition operator only accepts two numbers. To handle this case, we define a
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,4 +1,9 @@

 function clampNumber($num, $a, $b)
 {
-  return max(min($num, max($a, $b)), min($a, $b));
-}
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,8 @@

 function clampNumber($num, $a, $b)
-{  return max(min($num, max($a, $b)), min($a, $b));
-}
+{ return $num / $a / $b; }
+
+
+function clampNumber($num, $a, $b)
+{ return $num / ($a / $b); }
+
+
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,4 +1,9 @@

 function clampNumber($num, $a, $b)
 {
-  return max(min($num, max($a, $b)), min($a, $b));
-}
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
--- canonical..php

+++ solution4..php

@@ -1,4 +1,9 @@

 function clampNumber($num, $a, $b)
 {
-  return max(min($num, max($a, $b)), min($a, $b));
-}
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
+function clampNumber($num, $a, $b)
+
```

### pull (task/27)

#### canonical solution

```php
function pull(&$items, ...$params)
{
  $items = array_values(array_diff($items, $params));
  return $items;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,5 +1,10 @@

 function pull(&$items, ...$params)
 {
-  $items = array_values(array_diff($items, $params));
-  return $items;
-}
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
--- canonical..php

+++ solution1..php

@@ -1,5 +1,8 @@

 function pull(&$items, ...$params)
 {
-  $items = array_values(array_diff($items, $params));
-  return $items;
-}
+
+$items is an array of scalar variables that are to be passed by reference.
+
+function set($$var1, ..., $var_n)
+
+function set(&$var1, ..., $var_n
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,5 +1,10 @@

 function pull(&$items, ...$params)
 {
-  $items = array_values(array_diff($items, $params));
-  return $items;
-}
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
--- canonical..php

+++ solution3..php

@@ -1,4 +1,7 @@

 function pull(&$items, ...$params)
-{  $items = array_values(array_diff($items, $params));
-  return $items;
+{ # implementation
 }
+
+Note that this function expects a reference to an array, since the caller of the function may be calling it with a longer array than what the function needs.
+
+For an example, see the recode() function in
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,4 +1,3 @@

 function pull(&$items, ...$params)
-{  $items = array_values(array_diff($items, $params));
-  return $items;
-}
+{ $items->each(function($item, $index) use($params) { //  // $item is a single item from the collection //  // $index is the index of that item in the collection }); }
+$items
```

### compose (task/28)

#### canonical solution

```php
function compose(...$functions)
{
  return array_reduce(
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
--- canonical..php

+++ solution0..php

@@ -1,13 +1,2 @@

 function compose(...$functions)
-{  return array_reduce(
-    $functions,
-    function ($carry, $function) {
-      return function ($x) use ($carry, $function) {
-        return $function($carry($x));
-      };
-    },
-    function ($x) {
-      return $x;
-    }
-  );
-}
+{     $arity = count($functions);     $body = $functions[0];     foreach ($functions[1 .. $arity] as $i => $f)     {         $body =
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,14 +1,7 @@

 function compose(...$functions)
 {
-  return array_reduce(
-    $functions,
-    function ($carry, $function) {
-      return function ($x) use ($carry, $function) {
-        return $function($carry($x));
-      };
-    },
-    function ($x) {
-      return $x;
-    }
-  );
 }
+
+Composition of functions is useful for cases where a large number of similar functions are required.
+
+In functional programming, a higher-order function is a function that takes one or more functions as arguments or returns a function as its
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,13 +1,3 @@

 function compose(...$functions)
-{  return array_reduce(
-    $functions,
-    function ($carry, $function) {
-      return function ($x) use ($carry, $function) {
-        return $function($carry($x));
-      };
-    },
-    function ($x) {
-      return $x;
-    }
-  );
-}
+{     return function () {         return $functions(...call_args());     };     }
+This is a very powerful concept, but it's not always immediately obvious when to use it. There's actually a very
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,14 +1,15 @@

 function compose(...$functions)
 {
-  return array_reduce(
-    $functions,
-    function ($carry, $function) {
-      return function ($x) use ($carry, $function) {
-        return $function($carry($x));
-      };
-    },
-    function ($x) {
-      return $x;
-    }
-  );
-}
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
--- canonical..php

+++ solution4..php

@@ -1,14 +1,12 @@

 function compose(...$functions)
 {
-  return array_reduce(
-    $functions,
-    function ($carry, $function) {
-      return function ($x) use ($carry, $function) {
-        return $function($carry($x));
-      };
-    },
-    function ($x) {
-      return $x;
-    }
-  );
+
+$last = $functions[$#functions];
+
+return function() use ($last) {
+
+$last($this);
+};
 }
+
+Composing the functions "f" and "g" to create
```

### findLastIndex (task/29)

#### canonical solution

```php
function findLastIndex($items, $func)
{
  $keys = array_keys(array_filter($items, $func));

  return array_pop($keys);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,6 +1,11 @@

 function findLastIndex($items, $func)
 {
-  $keys = array_keys(array_filter($items, $func));
 
-  return array_pop($keys);
-}
+function insertLast($items, $item)
+
+function findLast($items, $func)
+
+function removeLast($items, $item)
+
+function findLastIndex($items, $func)
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,5 +1,3 @@

 function findLastIndex($items, $func)
-{  $keys = array_keys(array_filter($items, $func));
-
-  return array_pop($keys);
-}
+{     $lastIndex = array_search($func, $items, true);     return $lastIndex; }
+/** * Get the last element in the array. * * @param array $items * @return mixed * @since
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,5 +1,3 @@

 function findLastIndex($items, $func)
-{  $keys = array_keys(array_filter($items, $func));
+{ $lastIndex = -1; $result = []; foreach ($items as $item) { if ($func($item)) { $result[$lastIndex] = $item; $lastIndex++; } } return $result; }
 
-  return array_pop($keys);
-}
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,6 +1,9 @@

 function findLastIndex($items, $func)
 {
-  $keys = array_keys(array_filter($items, $func));
+if(sizeof($items) > 0)
 
-  return array_pop($keys);
-}
+The negative operator "-=" is used to remove the values from the array.
+
+$items = array_remove($items, 3);
+
+echo $items[array_search
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,5 +1,3 @@

 function findLastIndex($items, $func)
-{  $keys = array_keys(array_filter($items, $func));
-
-  return array_pop($keys);
-}
+{     return array_search($func, array_reverse($items));     }
+The only other place where we need to use this is in the array_column function. The issue here is that if the array happens to be sorted and
```

### slugify (task/30)

#### canonical solution

```php
function slugify($text) {
  $text = preg_replace('~[^\pL\d]+~u', '-', $text);
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
--- canonical..php

+++ solution0..php

@@ -1,11 +1 @@

-function slugify($text) {  $text = preg_replace('~[^\pL\d]+~u', '-', $text);
-  $text = iconv('utf-8', 'us-ascii//TRANSLIT', $text);
-  $text = preg_replace('~[^-\w]+~', '', $text);
-  $text = preg_replace('~-+~', '-', $text);
-  $text = strtolower($text);
-  $text = trim($text, " \t\n\r\0\x0B-");
-  if (empty($text)) {
-    return 'n-a';
-  }
-  return $text;
-}
+function slugify($text) { $text = preg_replace("/[^a-z0-9-_]+/", "", $text); return preg_replace("/[a-z0-9-_]+/", "", $text
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,11 +1 @@

-function slugify($text) {  $text = preg_replace('~[^\pL\d]+~u', '-', $text);
-  $text = iconv('utf-8', 'us-ascii//TRANSLIT', $text);
-  $text = preg_replace('~[^-\w]+~', '', $text);
-  $text = preg_replace('~-+~', '-', $text);
-  $text = strtolower($text);
-  $text = trim($text, " \t\n\r\0\x0B-");
-  if (empty($text)) {
-    return 'n-a';
-  }
-  return $text;
-}
+function slugify($text) { $text = preg_replace("/[a-zA-Z0-9-_]+/", "", $text); $text = preg_replace("/[^a-zA-Z0-9-
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,11 +1 @@

-function slugify($text) {  $text = preg_replace('~[^\pL\d]+~u', '-', $text);
-  $text = iconv('utf-8', 'us-ascii//TRANSLIT', $text);
-  $text = preg_replace('~[^-\w]+~', '', $text);
-  $text = preg_replace('~-+~', '-', $text);
-  $text = strtolower($text);
-  $text = trim($text, " \t\n\r\0\x0B-");
-  if (empty($text)) {
-    return 'n-a';
-  }
-  return $text;
-}
+function slugify($text) { $text = preg_replace('/[a-z]/', '', $text); $text = preg_replace('/[A-Z]/', '', $text); $text = preg_replace('
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,11 +1 @@

-function slugify($text) {  $text = preg_replace('~[^\pL\d]+~u', '-', $text);
-  $text = iconv('utf-8', 'us-ascii//TRANSLIT', $text);
-  $text = preg_replace('~[^-\w]+~', '', $text);
-  $text = preg_replace('~-+~', '-', $text);
-  $text = strtolower($text);
-  $text = trim($text, " \t\n\r\0\x0B-");
-  if (empty($text)) {
-    return 'n-a';
-  }
-  return $text;
-}
+function slugify($text) { $text = preg_replace('/(\.{2,}|{2,})/',"$1-",$text); $text = preg_replace('/(\S+)/',"-$1",$text); $text
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,12 +1,5 @@

 function slugify($text) {
-  $text = preg_replace('~[^\pL\d]+~u', '-', $text);
-  $text = iconv('utf-8', 'us-ascii//TRANSLIT', $text);
-  $text = preg_replace('~[^-\w]+~', '', $text);
-  $text = preg_replace('~-+~', '-', $text);
-  $text = strtolower($text);
-  $text = trim($text, " \t\n\r\0\x0B-");
-  if (empty($text)) {
-    return 'n-a';
-  }
-  return $text;
-}
+
+foreach (array('A-Z', 'a-z', '0-9', ' ') as $c) {
+
+$text = strtolower($text) . strtoupper($c);
```

### isUpperCase (task/31)

#### canonical solution

```php
function isUpperCase($string)
{
  return $string === strtoupper($string);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,8 @@

 function isUpperCase($string)
-{  return $string === strtoupper($string);
-}
+{ 
+
+function isUpperCase($string)
+{ 
+
+function isUpperCase($string)
+{ 
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,6 @@

 function isUpperCase($string)
-{  return $string === strtoupper($string);
-}
+{ $string = strtoupper($string); }
+
+The above function will create a new case version of the string it is given, which in this case will be "Welcome to LOWERCASE!".
+
+PHP can be embedded
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,4 @@

 function isUpperCase($string)
-{  return $string === strtoupper($string);
+{ $string = strtoupper($string);
 }
+Notice that the strtoupper() function is called with $string as its only argument. PHP always passes by value, so the actual string will be passed in, and the function
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,4 @@

 function isUpperCase($string)
-{  return $string === strtoupper($string);
-}
+{     return (strtoupper($string) === $string);     }
+The array_unique() function will produce a new array that contains all the values from the original array but not repeating values.
+The PHP (5.
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,3 @@

 function isUpperCase($string)
-{  return $string === strtoupper($string);
-}
+{ return ((string) $string) [0] >= 'A' && ((string) $string) [0] <= 'Z'; }
+This is the smallest valid PHP program. It has 2 source lines and 2 executable lines. It uses
```

### countVowels (task/32)

#### canonical solution

```php
function countVowels($string)
{
  preg_match_all('/[aeiou]/i', $string, $matches);

  return count($matches[0]);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,6 +1,6 @@

 function countVowels($string)
 {
-  preg_match_all('/[aeiou]/i', $string, $matches);
-
-  return count($matches[0]);
-}
+$length = strlen($string);
+$diff = 0;
+for ($i = 0; $i < $length; $i++) {
+if (substr($string, $i, 1) == 'a') {
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,5 +1,8 @@

 function countVowels($string)
-{  preg_match_all('/[aeiou]/i', $string, $matches);
+{ 
 
-  return count($matches[0]);
-}
+function countVowels($string)
+
+The algorithm can be expressed in terms of the number of vowels with the following recurrence relation:
+
+For example, given "abracadabra", we have:
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,6 +1,8 @@

 function countVowels($string)
 {
-  preg_match_all('/[aeiou]/i', $string, $matches);
+$vowels = ['a', 'e', 'i', 'o', 'u'];
+$lettercount = 0;
 
-  return count($matches[0]);
-}
+while(strlen($string) > 0)
+{
+$lettercount += count($
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,6 +1,10 @@

 function countVowels($string)
 {
-  preg_match_all('/[aeiou]/i', $string, $matches);
 
-  return count($matches[0]);
-}
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
--- canonical..php

+++ solution4..php

@@ -1,5 +1,5 @@

 function countVowels($string)
-{  preg_match_all('/[aeiou]/i', $string, $matches);
-
-  return count($matches[0]);
-}
+{ $numVowels = 0;
+$length = strlen($string);
+for ($i = 0; $i < $length; $i++) {
+$vowelCount = count_chars($string, $i
```

### palindrome (task/33)

#### canonical solution

```php
function palindrome($string)
{
  return strrev($string) === (string) $string;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,9 @@

 function palindrome($string)
 {
-  return strrev($string) === (string) $string;
-}
+
+$len = strlen($string);
+
+for ($i = 0; $i < $len; $i++) {
+
+if ($string[$i] != $string[$i + 1]) {
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,2 @@

 function palindrome($string)
-{  return strrev($string) === (string) $string;
-}
+{ $string = trim($string); $string = strtolower($string); $string = preg_replace('/[^a-z0-9]/', '', $string); $string = preg_replace('
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,4 +1,7 @@

 function palindrome($string)
 {
-  return strrev($string) === (string) $string;
-}
+
+The variable $string is assigned a value to represent the string.
+The variable $string is now the string, and is referenced in the next line.
+The variable $string is assigned the string representation.
+The string is compared to
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,4 +1,9 @@

 function palindrome($string)
 {
-  return strrev($string) === (string) $string;
+
+echo "The string is $string";
+
 }
+
+?>
+The output of the script will be:
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,2 @@

 function palindrome($string)
-{  return strrev($string) === (string) $string;
-}
+{ $string = strtolower($string); $string = preg_replace('/[^a-zA-Z0-9]/', '', $string); $string = strrev($string); return (strcmp
```

### firstStringBetween (task/34)

#### canonical solution

```php
function firstStringBetween($haystack, $start, $end)
{
  return trim(strstr(strstr($haystack, $start), $end, true), $start . $end);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,9 @@

 function firstStringBetween($haystack, $start, $end)
 {
-  return trim(strstr(strstr($haystack, $start), $end, true), $start . $end);
-}
+
+function firstStringBetween($haystack, $start, $end)
+
+{
+
+// the following is the recommended minimum contents of a validator
+function pwgReservedPagesValidator( $content )
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,4 +1,9 @@

 function firstStringBetween($haystack, $start, $end)
 {
-  return trim(strstr(strstr($haystack, $start), $end, true), $start . $end);
-}
+function firstStringBetween($haystack, $start, $end)
+
+{
+function firstStringBetween($haystack, $start, $end)
+
+{
+
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,3 @@

 function firstStringBetween($haystack, $start, $end)
-{  return trim(strstr(strstr($haystack, $start), $end, true), $start . $end);
-}
+{     $start = strpos($haystack, $start, $end);     return substr($haystack, $start, strlen($end));     }
+The $start and $end variables are passed by reference
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,4 +1,5 @@

 function firstStringBetween($haystack, $start, $end)
 {
-  return trim(strstr(strstr($haystack, $start), $end, true), $start . $end);
-}
+function firstStringBetween($haystack, $start, $end)
+
+The main difference between the two PHP implementations is the used data structure. In the Python version the sequence was used, which is optimized for accessing elements. In the
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,4 +1,9 @@

 function firstStringBetween($haystack, $start, $end)
 {
-  return trim(strstr(strstr($haystack, $start), $end, true), $start . $end);
-}
+
+function lastStringBetween($haystack, $start, $end)
+{
+
+function between(array $haystack, $needle, $offset = 0)
+{
+
```

### tail (task/35)

#### canonical solution

```php
function tail($items)
{
  return count($items) > 1 ? array_slice($items, 1) : $items;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,9 @@

 function tail($items)
 {
-  return count($items) > 1 ? array_slice($items, 1) : $items;
-}
+function trim($string)
+
+function number_formats($number, $places)
+
+function time_formats($time, $locale)
+
+function date_formats($date, $locale)
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,3 @@

 function tail($items)
-{  return count($items) > 1 ? array_slice($items, 1) : $items;
-}
+{     // do something with $items here     }
+This works. It's clean, it's simple, and it doesn't generate any warnings. You can call it from anywhere, and you know exactly what it's going to do.
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,4 +1,9 @@

 function tail($items)
 {
-  return count($items) > 1 ? array_slice($items, 1) : $items;
-}
+
+function sub1($items)
+
+function sub2($items)
+
+function sub3($items)
+
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,8 @@

 function tail($items)
-{  return count($items) > 1 ? array_slice($items, 1) : $items;
+{ $i = 0;
 }
+
+
+Example:
+
+$result = array_unique(array_unique(array_unique(array_unique(array_unique(array_unique(array_unique(array_unique(array_
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,4 +1,7 @@

 function tail($items)
 {
-  return count($items) > 1 ? array_slice($items, 1) : $items;
-}
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
{
  return function () use ($func) {
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
--- canonical..php

+++ solution0..php

@@ -1,17 +1,14 @@

 function memoize($func)
 {
-  return function () use ($func) {
-    static $cache = [];
 
-    $args = func_get_args();
-    $key = serialize($args);
-    $cached = true;
+if (!isset($cache[$func])) {
 
-    if (!isset($cache[$key])) {
-      $cache[$key] = $func(...$args);
-      $cached = false;
-    }
+$cache[$func] = (object) $func();
 
-    return ['result' => $cache[$key], 'cached' => $cached];
-  };
 }
+
+return $cache[$func];
+
+}
+
+In Python 2.
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,17 +1,5 @@

 function memoize($func)
 {
-  return function () use ($func) {
-    static $cache = [];
 
-    $args = func_get_args();
-    $key = serialize($args);
-    $cached = true;
-
-    if (!isset($cache[$key])) {
-      $cache[$key] = $func(...$args);
-      $cached = false;
-    }
-
-    return ['result' => $cache[$key], 'cached' => $cached];
-  };
-}
+Here are some examples of how memoize() might be used.
+The following example shows how memoize() can be used to cache the results of a function that uses sequential search to search an array for a value. This is a very
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,16 +1,2 @@

 function memoize($func)
-{  return function () use ($func) {
-    static $cache = [];
-
-    $args = func_get_args();
-    $key = serialize($args);
-    $cached = true;
-
-    if (!isset($cache[$key])) {
-      $cache[$key] = $func(...$args);
-      $cached = false;
-    }
-
-    return ['result' => $cache[$key], 'cached' => $cached];
-  };
-}
+{     if (function_exists('array_unique')) {         $cache = array_unique(array_merge($func(), array_keys($func())));         return function() use ($cache)
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,17 +1,11 @@

 function memoize($func)
 {
-  return function () use ($func) {
-    static $cache = [];
-
-    $args = func_get_args();
-    $key = serialize($args);
-    $cached = true;
-
-    if (!isset($cache[$key])) {
-      $cache[$key] = $func(...$args);
-      $cached = false;
-    }
-
-    return ['result' => $cache[$key], 'cached' => $cached];
-  };
+$cache = [];
+if (is_callable($func)) {
+$cache = [$func];
 }
+return $cache;
+}
+// usage example:
+$myfunc = function($arg) {
+$
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,16 +1,2 @@

 function memoize($func)
-{  return function () use ($func) {
-    static $cache = [];
-
-    $args = func_get_args();
-    $key = serialize($args);
-    $cached = true;
-
-    if (!isset($cache[$key])) {
-      $cache[$key] = $func(...$args);
-      $cached = false;
-    }
-
-    return ['result' => $cache[$key], 'cached' => $cached];
-  };
-}
+{     $cache = array();     $max = count($cache);     return function () use ($func, &$cache, $max) {         if ($max == count($cache)) {             $cache
```

### isLowerCase (task/37)

#### canonical solution

```php
function isLowerCase($string)
{
  return $string === strtolower($string);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,4 @@

 function isLowerCase($string)
-{  return $string === strtolower($string);
-}
+{ if (strtolower($string) == $string) { return true; } return false; }
+function isUpperCase($string)
+{ if (strtoupper($string) == $string) { return true;
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,6 @@

 function isLowerCase($string)
-{  return $string === strtolower($string);
-}
+{ $string = strtolower($string); return ($string{0} >= 'a' && $string{0} <= 'z'); }
+
+
+function isURL($string)
+{ return (preg_match('#^
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,4 +1,9 @@

 function isLowerCase($string)
 {
-  return $string === strtolower($string);
-}
+
+function isUpperCase($string)
+
+function isDigit($string)
+
+function isAlpha($string)
+
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,2 @@

 function isLowerCase($string)
-{  return $string === strtolower($string);
-}
+{ $lowercase = array(  //Latin   0xC6,  //small c,  //Latin   0xC7,  //small c with cedilla,  //Latin
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,4 +1,9 @@

 function isLowerCase($string)
 {
-  return $string === strtolower($string);
-}
+
+function isCapitalized($string)
+
+function isOneOf($array, $value)
+
+function isNumeric($string)
+
```

### isEven (task/38)

#### canonical solution

```php
function isEven($number)
{
  return ($number % 2) === 0;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,4 @@

 function isEven($number)
-{  return ($number % 2) === 0;
-}
+{ if ($number % 2 == 0) { return true; } else { return false; } }
+
+The function isEven is called with the argument number. This argument is then compared to 0, and if they are equal, true is returned
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,6 @@

 function isEven($number)
-{  return ($number % 2) === 0;
-}
+{ return $number % 2 == 0; }
+
+Add-Type -AssemblyName System.Windows.Forms
+
+[Windows.Forms.MessageBox]::Show("The result is ", isEven($x), ".", "Information
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,4 +1,6 @@

 function isEven($number)
 {
-  return ($number % 2) === 0;
-}
+
+function isEven($number)
+
+This function is part of the "zebra_num" package, which means it has to be named "zebra_num_isEven". The package is given a unique name using the "
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,3 @@

 function isEven($number)
-{  return ($number % 2) === 0;
-}
+{ if ($number % 2 == 0) { return true; } else { return false; } }
+This is not a good idea for two reasons. The first is that it is not as readable as it could be. There is a lot of
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,8 @@

 function isEven($number)
-{  return ($number % 2) === 0;
-}
+{ return ($number % 2) == 0; }
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
{
  $filteredItems = array_filter($items, $func);

  return array_pop($filteredItems);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,5 +1,6 @@

 function findLast($items, $func)
-{  $filteredItems = array_filter($items, $func);
-
-  return array_pop($filteredItems);
-}
+{ $items->last(); $func($items); }
+function findFirst($items, $func)
+{ $items->first(); $func($items); }
+function createRandomString($size)
+{ $letters = array('a
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,5 +1,2 @@

 function findLast($items, $func)
-{  $filteredItems = array_filter($items, $func);
-
-  return array_pop($filteredItems);
-}
+{   $lastItem = null;   foreach ($items as $item) {     if ($func($item) === true) {         $lastItem = $item;     break;     }     }  
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,6 +1,11 @@

 function findLast($items, $func)
 {
-  $filteredItems = array_filter($items, $func);
 
-  return array_pop($filteredItems);
-}
+function findLast($items, $func)
+
+{
+
+function f($items, $func)
+
+{
+
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,5 +1,4 @@

 function findLast($items, $func)
-{  $filteredItems = array_filter($items, $func);
+{ foreach ($items as $item) { if ($func($item)) { return $item; } } return false; } 
 
-  return array_pop($filteredItems);
-}
+A particular application of this function is to find the last element of an array that satisfies a given test,
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,6 +1,10 @@

 function findLast($items, $func)
 {
-  $filteredItems = array_filter($items, $func);
 
-  return array_pop($filteredItems);
-}
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
{
  $minValue = min($numbers);
  $minValueArray = array_filter($numbers, function ($value) use ($minValue) {
    return $minValue === $value;
  });

  return count($minValueArray);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,9 +1,14 @@

 function minN($numbers)
 {
-  $minValue = min($numbers);
-  $minValueArray = array_filter($numbers, function ($value) use ($minValue) {
-    return $minValue === $value;
-  });
 
-  return count($minValueArray);
-}
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
--- canonical..php

+++ solution1..php

@@ -1,9 +1,14 @@

 function minN($numbers)
 {
-  $minValue = min($numbers);
-  $minValueArray = array_filter($numbers, function ($value) use ($minValue) {
-    return $minValue === $value;
-  });
+}
 
-  return count($minValueArray);
+And then we can call it as follows:
+
+function callMinN($numbers)
+{
+
 }
+
+And to call the function:
+
+$callMinN = new callMinN(4,
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,8 +1,5 @@

 function minN($numbers)
-{  $minValue = min($numbers);
-  $minValueArray = array_filter($numbers, function ($value) use ($minValue) {
-    return $minValue === $value;
-  });
-
-  return count($minValueArray);
-}
+{     return min($numbers);     }
+We can't really test function minN yet, but we can go ahead and create a test for the min function.
+$ phpunit --verbose
+PHPUnit 4.4
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,9 +1,13 @@

 function minN($numbers)
 {
-  $minValue = min($numbers);
-  $minValueArray = array_filter($numbers, function ($value) use ($minValue) {
-    return $minValue === $value;
-  });
 
-  return count($minValueArray);
+$numbers = array_filter($numbers);
+
+echo "The minimum number is: " . $numbers[0] . "<br>";
+
 }
+
+?>
+
+Output:
+The minimum
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,9 +1,12 @@

 function minN($numbers)
 {
-  $minValue = min($numbers);
-  $minValueArray = array_filter($numbers, function ($value) use ($minValue) {
-    return $minValue === $value;
-  });
 
-  return count($minValueArray);
-}
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
{
  return count(array_filter($items, $func)) === count($items);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,8 @@

 function all($items, $func)
-{  return count(array_filter($items, $func)) === count($items);
-}
+{ foreach ($items as $item) { $func($item); } }
+
+
+$items is the array being sorted.
+
+$func is the sorting function.
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,4 @@

 function all($items, $func)
-{  return count(array_filter($items, $func)) === count($items);
-}
+{ for($i=0; $i<count($items); $i++) {
+
+Since there is no requirement that this function modify any of the input arguments, it is safe to pass them by reference, since the function does not modify them
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,4 +1,3 @@

 function all($items, $func)
 {
-  return count(array_filter($items, $func)) === count($items);
-}
+The all() function applies a callback to every item in an array or collection. This callback should be a function that takes one argument and returns either true or false. All elements for which the callback returns true are included in the new array.
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,5 @@

 function all($items, $func)
-{  return count(array_filter($items, $func)) === count($items);
-}
+{ $func(array_slice($items, 0, 1)); }
+
+function map2($items, $mapper, $converter)
+{ foreach ($items as $key => $value) { $converter($
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,4 +1,8 @@

 function all($items, $func)
 {
-  return count(array_filter($items, $func)) === count($items);
+$items = func($items);
+return $items;
 }
+$items = all(array('A', 'B', 'C', 'D'), function($item) {
+return strtoupper($item);
+});
```

### pluck (task/42)

#### canonical solution

```php
function pluck($items, $key)
{
  return array_map( function($item) use ($key) {
    return is_object($item) ? $item->$key : $item[$key];
  }, $items);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,6 +1,5 @@

 function pluck($items, $key)
 {
-  return array_map( function($item) use ($key) {
-    return is_object($item) ? $item->$key : $item[$key];
-  }, $items);
-}
+function pluck($items, $key)
+
+The names of the functions are similar, but the parameters are different.
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,5 +1,5 @@

 function pluck($items, $key)
-{  return array_map( function($item) use ($key) {
-    return is_object($item) ? $item->$key : $item[$key];
-  }, $items);
-}
+{ return array_values(array_unique($items))[$key]; }
+function pluck_and_key($items, $key)
+{ return array_values(array_unique($items))[$key]; }
+function
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,5 +1,6 @@

 function pluck($items, $key)
-{  return array_map( function($item) use ($key) {
-    return is_object($item) ? $item->$key : $item[$key];
-  }, $items);
+{ $key = "functionName"; # change this to the name of the function you want to call
+return $items->functionName($key);
 }
+
+The above code defines a new function called pluck() which can be used just
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,6 +1,11 @@

 function pluck($items, $key)
 {
-  return array_map( function($item) use ($key) {
-    return is_object($item) ? $item->$key : $item[$key];
-  }, $items);
-}
+
+function make_map()
+
+function convert_to_ints($values)
+
+function convert_to_strings($values)
+
+function show_header()
+
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,5 +1,5 @@

 function pluck($items, $key)
-{  return array_map( function($item) use ($key) {
-    return is_object($item) ? $item->$key : $item[$key];
-  }, $items);
+{     // iterate over the array, plucking values of $key
 }
+$array = array('a'=>'b','c'=>'d','e'=>'f');
+$array_key = array('a
```

### approximatelyEqual (task/43)

#### canonical solution

```php
function approximatelyEqual($number1, $number2, $epsilon = 0.001)
{
  return abs($number1 - $number2) < $epsilon;
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,3 +1,8 @@

 function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{  return abs($number1 - $number2) < $epsilon;
-}
+{ if ($number1 - $number2 > $epsilon) { return false; } else { return true; } }
+#endregion
+
+#region setters and getters
+#region constructors
+#endregion
+
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,3 +1,3 @@

 function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{  return abs($number1 - $number2) < $epsilon;
-}
+{     return (fabs($number1 - $number2) < $epsilon);     }
+The $epsilon variable is used to specify how close the two numbers need to be to be considered equal. The function returns
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,3 +1,2 @@

 function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{  return abs($number1 - $number2) < $epsilon;
-}
+{     $number1 = round($number1);     $number2 = round($number2);     if($number1 == $number2)         return true;     else if($number1 === $number2
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,3 @@

 function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{  return abs($number1 - $number2) < $epsilon;
-}
+{ return is_numeric($number1) && is_numeric($number2) && ($number1 - $number2) * $epsilon <= $epsilon; }
+This function is then used to test if the value
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,3 @@

 function approximatelyEqual($number1, $number2, $epsilon = 0.001)
-{  return abs($number1 - $number2) < $epsilon;
-}
+{     $maxDiff = abs($number1 - $number2);     return ($maxDiff <= $epsilon); }
+function approximatelyEquals($number1, $number2, $epsilon = 0.001)
```

### decapitalize (task/44)

#### canonical solution

```php
function decapitalize($string, $upperRest = false)
{
  return lcfirst($upperRest ? strtoupper($string) : $string);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,4 +1,9 @@

 function decapitalize($string, $upperRest = false)
 {
-  return lcfirst($upperRest ? strtoupper($string) : $string);
-}
+#if ($upperRest === true)
+#else
+#end
+
+function make_half($number)
+
+function make_quarter($number)
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,4 +1,9 @@

 function decapitalize($string, $upperRest = false)
 {
-  return lcfirst($upperRest ? strtoupper($string) : $string);
+$string = strtoupper($string);
+if ($upperRest) {
+return $string;
 }
+return strtolower($string);
+}
+
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,4 +1,9 @@

 function decapitalize($string, $upperRest = false)
 {
-  return lcfirst($upperRest ? strtoupper($string) : $string);
-}
+
+function decapitalize($string, $upperRest = false)
+
+{
+
+function decapitalize($string, $upperRest = false)
+
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,3 +1,8 @@

 function decapitalize($string, $upperRest = false)
-{  return lcfirst($upperRest ? strtoupper($string) : $string);
+{ 
+// split $string into words
+// convert to lowercase
+// capitalize the first character of each word
+// return an array of words
 }
+
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,3 +1,7 @@

 function decapitalize($string, $upperRest = false)
-{  return lcfirst($upperRest ? strtoupper($string) : $string);
+{ if ($upperRest) $string = strtoupper($string); $string = str_replace(' ', '', $string);
+return $string;
 }
+
+function decapitalize_no_upper($string)
+{
```

### isPrime (task/45)

#### canonical solution

```php
function isPrime($number)
{
  $boundary = floor(sqrt($number));
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
--- canonical..php

+++ solution0..php

@@ -1,11 +1,8 @@

 function isPrime($number)
 {
-  $boundary = floor(sqrt($number));
-  for ($i = 2; $i <= $boundary; $i++) {
-    if ($number % $i === 0) {
-      return false;
-    }
-  }
-
-  return $number >= 2;
+$low = 2;
+$found = true;
+for ($i = $low; $i < $number; $i++) {
+if ($number % $i == 0) {
+$found = false;
 }
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,11 +1,10 @@

 function isPrime($number)
 {
-  $boundary = floor(sqrt($number));
-  for ($i = 2; $i <= $boundary; $i++) {
-    if ($number % $i === 0) {
-      return false;
-    }
-  }
-
-  return $number >= 2;
+$number % 2 == 0 or return 0;
+for ($i = 2; $i*$i <= $number; $i++)
+{
+return 0;
 }
+return 1;
+}
+The number 1 is not
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,11 +1,5 @@

 function isPrime($number)
 {
-  $boundary = floor(sqrt($number));
-  for ($i = 2; $i <= $boundary; $i++) {
-    if ($number % $i === 0) {
-      return false;
-    }
-  }
+}
 
-  return $number >= 2;
-}
+The function prototype declares the name of the function and its argument types. A function can take a variable number of arguments, but in this case it takes no arguments at all. The return type is not given; in this case,
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,11 +1,5 @@

 function isPrime($number)
 {
-  $boundary = floor(sqrt($number));
-  for ($i = 2; $i <= $boundary; $i++) {
-    if ($number % $i === 0) {
-      return false;
-    }
-  }
+}
 
-  return $number >= 2;
-}
+To access a protected function or property from outside the class, the class must be extended or the protected function or property must be defined as static (the static keyword was introduced in PHP 5.3). An example of extending a class
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,11 +1,10 @@

 function isPrime($number)
 {
-  $boundary = floor(sqrt($number));
-  for ($i = 2; $i <= $boundary; $i++) {
-    if ($number % $i === 0) {
-      return false;
-    }
-  }
 
-  return $number >= 2;
-}
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
{
  $filtered = array_filter($items, $func);

  return array_diff_key($items, $filtered);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,5 +1,4 @@

 function remove($items, $func)
-{  $filtered = array_filter($items, $func);
+{ foreach ($items as $key => $item) { if ($func($item)) { unset($items[$key]); } } }
 
-  return array_diff_key($items, $filtered);
-}
+If you are using PHP 7, you can use the new "void" return type which
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,6 +1,11 @@

 function remove($items, $func)
 {
-  $filtered = array_filter($items, $func);
 
-  return array_diff_key($items, $filtered);
-}
+/**
+
+* @param array $items
+
+* @param string $func
+
+* @return array
+
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,5 +1,4 @@

 function remove($items, $func)
-{  $filtered = array_filter($items, $func);
-
-  return array_diff_key($items, $filtered);
-}
+{ foreach ($items as $item) { $func($item); } }
+{ $a = [1, 2, 3]; remove($a, function($item) { return $item > 2; }); }
+{ $a =
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,5 +1,3 @@

 function remove($items, $func)
-{  $filtered = array_filter($items, $func);
-
-  return array_diff_key($items, $filtered);
-}
+{ foreach ($items as $key => $item) { call_user_func($func, $item); } }
+$items = [1, 2, 3]; $items->remove(function ($item) { return $item >
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,5 +1,2 @@

 function remove($items, $func)
-{  $filtered = array_filter($items, $func);
-
-  return array_diff_key($items, $filtered);
-}
+{     if(is_array($items)) {         foreach($items as $item) {              if($func($item)) {                 return true;             }             }      
```

### deepFlatten (task/47)

#### canonical solution

```php
function deepFlatten($items)
{
  $result = [];
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
--- canonical..php

+++ solution0..php

@@ -1,12 +1,2 @@

 function deepFlatten($items)
-{  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...deepFlatten($item));
-    }
-  }
-
-  return $result;
-}
+{     foreach ($items as $i)         foreach ($i as $j)         $items[$i][$j] = deepFlatten($i[$j]);     return $items;  
```

#### solution 1

```diff
--- canonical..php

+++ solution1..php

@@ -1,12 +1,2 @@

 function deepFlatten($items)
-{  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...deepFlatten($item));
-    }
-  }
-
-  return $result;
-}
+{ $result = []; foreach ($items as $item) { if (is_array($item)) { $result[] = deepFlatten($item); } else { $result[] = $item; } } return $result; } $
```

#### solution 2

```diff
--- canonical..php

+++ solution2..php

@@ -1,13 +1,5 @@

 function deepFlatten($items)
 {
-  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...deepFlatten($item));
-    }
-  }
+</pre>
 
-  return $result;
-}
+The shallowFlatten() function takes a nested associative array and flattens it out into a single level array. The deepFlatten() function takes a nested associative array and returns a multilevel associative array
```

#### solution 3

```diff
--- canonical..php

+++ solution3..php

@@ -1,12 +1,3 @@

 function deepFlatten($items)
-{  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...deepFlatten($item));
-    }
-  }
-
-  return $result;
-}
+{ $items = array_filter($items); return array_map('deepFlatten', $items); }
+If we try to run the following code: $deepFlatten = function($items) { $items = array_filter($items
```

#### solution 4

```diff
--- canonical..php

+++ solution4..php

@@ -1,12 +1,3 @@

 function deepFlatten($items)
-{  $result = [];
-  foreach ($items as $item) {
-    if (!is_array($item)) {
-      $result[] = $item;
-    } else {
-      array_push($result, ...deepFlatten($item));
-    }
-  }
-
-  return $result;
-}
+{ return array_reduce($items, function ($result, $item) use ($items) { return array_combine($result, $item); }, []); }
+$list = [ 1, [ 2, [3, [4
```

### gcd (task/48)

#### canonical solution

```php
function gcd(...$numbers)
{
  if (count($numbers) > 2) {
    return array_reduce($numbers, 'gcd');
  }

  $r = $numbers[0] % $numbers[1];
  return $r === 0 ? abs($numbers[1]) : gcd($numbers[1], $r);
}
```

#### solution 0

```diff
--- canonical..php

+++ solution0..php

@@ -1,9 +1,10 @@

 function gcd(...$numbers)
 {
-  if (count($numbers) > 2) {
-    return array_reduce($numbers, 'gcd');
-  }
 
-  $r = $numbers[0] % $numbers[1];
-  return $r === 0 ? abs($numbers[1]) : gcd($numbers[1], $r);
-}
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
--- canonical..php

+++ solution1..php

@@ -1,9 +1,10 @@

 function gcd(...$numbers)
 {
-  if (count($numbers) > 2) {
-    return array_reduce($numbers, 'gcd');
-  }
 
-  $r = $numbers[0] % $numbers[1];
-  return $r === 0 ? abs($numbers[1]) : gcd($numbers[1], $r);
-}
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
--- canonical..php

+++ solution2..php

@@ -1,9 +1,12 @@

 function gcd(...$numbers)
 {
-  if (count($numbers) > 2) {
-    return array_reduce($numbers, 'gcd');
-  }
 
-  $r = $numbers[0] % $numbers[1];
-  return $r === 0 ? abs($numbers[1]) : gcd($numbers[1], $r);
-}
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
--- canonical..php

+++ solution3..php

@@ -1,9 +1,10 @@

 function gcd(...$numbers)
 {
-  if (count($numbers) > 2) {
-    return array_reduce($numbers, 'gcd');
-  }
 
-  $r = $numbers[0] % $numbers[1];
-  return $r === 0 ? abs($numbers[1]) : gcd($numbers[1], $r);
-}
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
--- canonical..php

+++ solution4..php

@@ -1,9 +1,9 @@

 function gcd(...$numbers)
 {
-  if (count($numbers) > 2) {
-    return array_reduce($numbers, 'gcd');
-  }
+gcd(...$numbers)
 
-  $r = $numbers[0] % $numbers[1];
-  return $r === 0 ? abs($numbers[1]) : gcd($numbers[1], $r);
 }
+
+gcd(...)
+
+Perl does not have a built-in function for determining the greatest common divisor. The function gcd is declared and assigned to a scal
```

