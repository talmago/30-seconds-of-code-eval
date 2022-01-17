### PadRight (task/1)

#### canonical solution

```golang
import "fmt"

func PadRight(s string, l int) string {
	f := "%" + strconv.Itoa(-l) + "v"
	return fmt.Sprintf(f, s)
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadRight(s string, l int) string {
-	f := "%" + strconv.Itoa(-l) + "v"
-	return fmt.Sprintf(f, s)
+
+s = s[:len(s)-l]
+
+return s
+
 }
+
+func main() {
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadRight(s string, l int) string {
-	f := "%" + strconv.Itoa(-l) + "v"
-	return fmt.Sprintf(f, s)
+
+r := make([]byte, len(s)+l)
+
+copy(r, s)
+
+return string(r)
+
 }
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadRight(s string, l int) string {
-	f := "%" + strconv.Itoa(-l) + "v"
-	return fmt.Sprintf(f, s)
+
+for i := len(s) - l; i >= 0; i-- {
+
+s = s[:i] + " "
+
 }
+
+return s
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadRight(s string, l int) string {
-	f := "%" + strconv.Itoa(-l) + "v"
-	return fmt.Sprintf(f, s)
+
+return strings.Repeat(" ", l - len(s)) + s
+
 }
+
+func main() {
+
+s := "Foo"
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadRight(s string, l int) string {
-	f := "%" + strconv.Itoa(-l) + "v"
-	return fmt.Sprintf(f, s)
+
+return s[:l] + string(padLeft(s, l, ' '))
+
 }
+
+func padLeft(s string, l int, pad string) string {
+
+return s[:l] +
```

### Median (task/2)

#### canonical solution

```golang
import (
	"math"
	"sort"
)

func Median(nums ...float64) float64 {
	m, n := int(math.Floor(float64(len(nums))/2.0)),
		nums[:]
	sort.Float64s(n)

	if len(nums)%2 == 0 {
		return (n[m] + n[m+1]) / 2.0
	}
	return n[m]
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,14 +1 @@

-import (	"math"
-	"sort"
-)
-
-func Median(nums ...float64) float64 {
-	m, n := int(math.Floor(float64(len(nums))/2.0)),
-		nums[:]
-	sort.Float64s(n)
-
-	if len(nums)%2 == 0 {
-		return (n[m] + n[m+1]) / 2.0
-	}
-	return n[m]
-}
+import ( "math" "sort" "strings" "unicode" ) // A BDD represents a set of boolean values. type BDD map[string]bool // BDDs are designed to be compared in the same way that sets are,
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,14 +1 @@

-import (	"math"
-	"sort"
-)
-
-func Median(nums ...float64) float64 {
-	m, n := int(math.Floor(float64(len(nums))/2.0)),
-		nums[:]
-	sort.Float64s(n)
-
-	if len(nums)%2 == 0 {
-		return (n[m] + n[m+1]) / 2.0
-	}
-	return n[m]
-}
+import ( "errors" "fmt" "io" "net/http" "net/url" "strings" ) func main() { var client = &http.Client{} client.Get( "https://httpbin.org/get
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,14 +1 @@

-import (	"math"
-	"sort"
-)
-
-func Median(nums ...float64) float64 {
-	m, n := int(math.Floor(float64(len(nums))/2.0)),
-		nums[:]
-	sort.Float64s(n)
-
-	if len(nums)%2 == 0 {
-		return (n[m] + n[m+1]) / 2.0
-	}
-	return n[m]
-}
+import ( ' twitter ' ) # Let's create a Twitter App (NOT necessary) app = Twitter( app_key = ' ' , app_secret = ' ' , api_key = ' ' , api_secret = ' ' ) # Let's
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,14 +1 @@

-import (	"math"
-	"sort"
-)
-
-func Median(nums ...float64) float64 {
-	m, n := int(math.Floor(float64(len(nums))/2.0)),
-		nums[:]
-	sort.Float64s(n)
-
-	if len(nums)%2 == 0 {
-		return (n[m] + n[m+1]) / 2.0
-	}
-	return n[m]
-}
+import ( "errors" "fmt" "runtime" "sync" "time" ) var mu sync.Mutex // Mutex to synchronize writes to global deadlines var nanotime = runtime.Now().UnixNano() // deadline returns the
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,14 +1 @@

-import (	"math"
-	"sort"
-)
-
-func Median(nums ...float64) float64 {
-	m, n := int(math.Floor(float64(len(nums))/2.0)),
-		nums[:]
-	sort.Float64s(n)
-
-	if len(nums)%2 == 0 {
-		return (n[m] + n[m+1]) / 2.0
-	}
-	return n[m]
-}
+import ( "fmt" ) func main() { var b [10]int a := make([]int, 3) for i := range a { a[i] = i } fmt.Println(len(a)) fmt.Println
```

### RandIntSliceInRange (task/3)

#### canonical solution

```golang
import "math/rand"

func RandIntSliceInRange(min, max, n int) []int {
	arr := make([]int, n)

	for i := range arr {
		arr[i] = rand.Intn(max-min) + min
	}
	return arr
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,10 +1,11 @@

 import "math/rand"
 
 func RandIntSliceInRange(min, max, n int) []int {
-	arr := make([]int, n)
 
-	for i := range arr {
-		arr[i] = rand.Intn(max-min) + min
-	}
-	return arr
-}
+// rand.Intn is not parallel safe; see issue 8774.
+
+// Use this implementation to guarantee sequential consistency.
+
+// The number of returned ints might be smaller than n.
+
+// See the Go 1
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,10 +1,15 @@

 import "math/rand"
 
 func RandIntSliceInRange(min, max, n int) []int {
-	arr := make([]int, n)
 
-	for i := range arr {
-		arr[i] = rand.Intn(max-min) + min
-	}
-	return arr
+r := rand.New(rand.NewSource(time.Now().UnixNano()))
+
+return r.Intn(n)
+
 }
+
+package main
+
+
+
+import (
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,10 +1,13 @@

 import "math/rand"
 
 func RandIntSliceInRange(min, max, n int) []int {
-	arr := make([]int, n)
 
-	for i := range arr {
-		arr[i] = rand.Intn(max-min) + min
-	}
-	return arr
-}
+// the closed interval [min, max] contains at least n+1 values
+
+// so we can generate a random integer in this range at least
+
+// n times.
+
+//
+
+// The algorithm is as follows
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,10 +1,15 @@

 import "math/rand"
 
 func RandIntSliceInRange(min, max, n int) []int {
-	arr := make([]int, n)
 
-	for i := range arr {
-		arr[i] = rand.Intn(max-min) + min
-	}
-	return arr
+return make([]int, n)
+
+for i := min; i < max; i++ {
+
+n--
+
+n*=10
+
+n+=i
+
 }
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,10 +1,11 @@

 import "math/rand"
 
 func RandIntSliceInRange(min, max, n int) []int {
-	arr := make([]int, n)
 
-	for i := range arr {
-		arr[i] = rand.Intn(max-min) + min
-	}
-	return arr
+return RandInts(uint(min), uint(max), n)
+
 }
+
+func RandUintSliceInRange(min, max uint, n int) []uint {
+
+return RandUints(uint
```

### ToSnake (task/4)

#### canonical solution

```golang
import "strings"

func ToSnake(s string) string {
	return strings.Join(strings.Fields(s), "_")
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToSnake(s string) string {
-	return strings.Join(strings.Fields(s), "_")
+
+return strings.ToLower(strings.Replace(s, " ", "_"))
+
 }
+
+func main() {
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToSnake(s string) string {
-	return strings.Join(strings.Fields(s), "_")
+
+return strings.ToSnakeCase(s)
+
 }
+
+The most common use of these functions is when working with the arguments to a function or a method.
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToSnake(s string) string {
-	return strings.Join(strings.Fields(s), "_")
+
+return strings.ToSnakeCase(s)
+
 }
+
+case is Snake
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToSnake(s string) string {
-	return strings.Join(strings.Fields(s), "_")
-}
+
+sp := strings.Split(s, " ")
+
+for i := len(sp) - 1; i >= 0; i-- {
+
+if sp[i] == "," {
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToSnake(s string) string {
-	return strings.Join(strings.Fields(s), "_")
+
+if s == "" {
+
+return ""
+
 }
+
```

### Filter (task/5)

#### canonical solution

```golang
func FilterInt(arr []int, f func(int) bool) []int {
	arf := make([]int, 0)
	for _, v := range arr {
		if f(v) {
			arf = append(arf, v)
		}
	}
	return arf
}
func FilterFloat64(arr []float64, f func(float64) bool) []float64 {
	arf := make([]float64, 0)
	for _, v := range arr {
		if f(v) {
			arf = append(arf, v)
		}
	}
	return arf
}
func FilterBool(arr []bool, f func(bool) bool) []bool {
	arf := make([]bool, 0)
	for _, v := range arr {
		if f(v) {
			arf = append(arf, v)
		}
	}
	return arf
}
func FilterString(arr []string, f func(string) bool) []string {
	arf := make([]string, 0)
	for _, v := range arr {
		if f(v) {
			arf = append(arf, v)
		}
	}
	return arf
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,36 +1,15 @@

 func FilterInt(arr []int, f func(int) bool) []int {
-	arf := make([]int, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
+
+out := make([]int, len(arr))
+
+for i, v := range arr {
+
+if f(v) {
+
+out[i] = v
+
 }
-func FilterFloat64(arr []float64, f func(float64) bool) []float64 {
-	arf := make([]float64, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
+
 }
-func FilterBool(arr []bool, f func(bool) bool) []bool {
-	arf := make([]bool, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
-func FilterString(arr []string, f func(string) bool) []string {
-	arf := make([]string, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
+
+return out
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,36 +1,19 @@

 func FilterInt(arr []int, f func(int) bool) []int {
-	arf := make([]int, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
+
+var result []int
+
+for _, i := range arr {
+
+if f(i) {
+
+result = append(result, i)
+
 }
-func FilterFloat64(arr []float64, f func(float64) bool) []float64 {
-	arf := make([]float64, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
+
 }
-func FilterBool(arr []bool, f func(bool) bool) []bool {
-	arf := make([]bool, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
+
+return result
+
 }
-func FilterString(arr []string, f func(string) bool) []string {
-	arf := make([]string, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
+
+func
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,35 +1 @@

-func FilterInt(arr []int, f func(int) bool) []int {	arf := make([]int, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
-func FilterFloat64(arr []float64, f func(float64) bool) []float64 {
-	arf := make([]float64, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
-func FilterBool(arr []bool, f func(bool) bool) []bool {
-	arf := make([]bool, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
-func FilterString(arr []string, f func(string) bool) []string {
-	arf := make([]string, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
+func FilterInt(arr []int, f func(int) bool) []int { // f returns true for ints less than 'a' for i, _ := range arr { if f(i) { return append(arr[0:i], filterInt(arr[i+1:], f)) } } return
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,36 +1,17 @@

 func FilterInt(arr []int, f func(int) bool) []int {
-	arf := make([]int, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
+
+for _, x := range arr {
+
+if f(x) {
+
+return append(arr, x)
+
 }
-func FilterFloat64(arr []float64, f func(float64) bool) []float64 {
-	arf := make([]float64, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
+
 }
-func FilterBool(arr []bool, f func(bool) bool) []bool {
-	arf := make([]bool, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
+
+return arr
+
 }
-func FilterString(arr []string, f func(string) bool) []string {
-	arf := make([]string, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
+
+func TestFilterInt(t *testing
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,36 +1,7 @@

 func FilterInt(arr []int, f func(int) bool) []int {
-	arf := make([]int, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
+
+return sort.Ints(sort.Reverse(sort.IntSlice(arr)))
+
 }
-func FilterFloat64(arr []float64, f func(float64) bool) []float64 {
-	arf := make([]float64, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
-func FilterBool(arr []bool, f func(bool) bool) []bool {
-	arf := make([]bool, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
-func FilterString(arr []string, f func(string) bool) []string {
-	arf := make([]string, 0)
-	for _, v := range arr {
-		if f(v) {
-			arf = append(arf, v)
-		}
-	}
-	return arf
-}
+
+fmt.Println(FilterInt(fmt.Sprint([]int{5, 6, 7
```

### Find (task/6)

#### canonical solution

```golang
import "fmt"

func FindInt(arr []int, f func(int) bool) (int, error) {
	for _, v := range arr {
		if f(v) {
			return v, nil
		}
	}
	return 0, fmt.Errorf("No matches found")
}
func FindFloat64(arr []float64, f func(float64) bool) (float64, error) {
	for _, v := range arr {
		if f(v) {
			return v, nil
		}
	}
	return 0.0, fmt.Errorf("No matches found")
}
func FindBool(arr []bool, f func(bool) bool) (bool, error) {
	for _, v := range arr {
		if f(v) {
			return v, nil
		}
	}
	return false, fmt.Errorf("No matches found")
}
func FindString(arr []string, f func(string) bool) (string, error) {
	for _, v := range arr {
		if f(v) {
			return v, nil
		}
	}
	return "", fmt.Errorf("No matches found")
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,34 +1,15 @@

 import "fmt"
 
 func FindInt(arr []int, f func(int) bool) (int, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+for i, v := range arr {
+
+if f(v) {
+
+return i, nil
+
 }
-func FindFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
 }
-func FindBool(arr []bool, f func(bool) bool) (bool, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
-}
-func FindString(arr []string, f func(string) bool) (string, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
+
+return -1, fmt.Errorf("Failed to find integer: %v",
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,34 +1,15 @@

 import "fmt"
 
 func FindInt(arr []int, f func(int) bool) (int, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+for i, v := range arr {
+
+if f(v) {
+
+return i, nil
+
 }
-func FindFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
 }
-func FindBool(arr []bool, f func(bool) bool) (bool, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
-}
-func FindString(arr []string, f func(string) bool) (string, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
+
+return -1, fmt.Errorf("no such element: %v", arr)
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,34 +1,19 @@

 import "fmt"
 
 func FindInt(arr []int, f func(int) bool) (int, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+for i, x := range arr {
+
+if f(x) {
+
+return i, nil
+
 }
-func FindFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
 }
-func FindBool(arr []bool, f func(bool) bool) (bool, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
+
+return -1, errors.New("Not found")
+
 }
-func FindString(arr []string, f func(string) bool) (string, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
+
+package main
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,34 +1,15 @@

 import "fmt"
 
 func FindInt(arr []int, f func(int) bool) (int, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+for i, v := range arr {
+
+if f(v) {
+
+return i, nil
+
 }
-func FindFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
 }
-func FindBool(arr []bool, f func(bool) bool) (bool, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
-}
-func FindString(arr []string, f func(string) bool) (string, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
+
+return -1, fmt.Errorf("can't find %v", f)
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,34 +1,17 @@

 import "fmt"
 
 func FindInt(arr []int, f func(int) bool) (int, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+for i, v := range arr {
+
+if f(v) {
+
+return i, nil
+
 }
-func FindFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
 }
-func FindBool(arr []bool, f func(bool) bool) (bool, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
+
+return -1, fmt.Errorf("FindInt: not found")
+
 }
-func FindString(arr []string, f func(string) bool) (string, error) {
-	for _, v := range arr {
-		if f(v) {
-			return v, nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
```

### LCM (task/7)

#### canonical solution

```golang
func gcd(x, y int) int {
	if y == 0 {
		return x
	}
	return gcd(y, x%y)
}

func LCM(nums ...int) int {
	x := nums[0]
	for _, y := range nums[1:] {
		x = (x * y) / gcd(x, y)
	}
	return x
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,14 +1,19 @@

 func gcd(x, y int) int {
-	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
+
+if y == 0 {
+
+return x
+
 }
 
-func LCM(nums ...int) int {
-	x := nums[0]
-	for _, y := range nums[1:] {
-		x = (x * y) / gcd(x, y)
-	}
-	return x
+return gcd(y, x%y)
+
 }
+
+Use in Go:
+
+package main
+
+
+
+import "fmt"
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,14 +1,13 @@

 func gcd(x, y int) int {
-	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
+
+if y == 0 {
+
+return x
+
 }
 
-func LCM(nums ...int) int {
-	x := nums[0]
-	for _, y := range nums[1:] {
-		x = (x * y) / gcd(x, y)
-	}
-	return x
+return gcd(y, x%y)
+
 }
+
+“But,” you protest, “then the compiler won’t be
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,14 +1,15 @@

 func gcd(x, y int) int {
-	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
+
+if y == 0 {
+
+return x
+
 }
 
-func LCM(nums ...int) int {
-	x := nums[0]
-	for _, y := range nums[1:] {
-		x = (x * y) / gcd(x, y)
-	}
-	return x
+return gcd(y, x%y)
+
 }
+
+The output is:
+
+Enter two positive integers > 15 11 > x=15 > y
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,14 +1,19 @@

 func gcd(x, y int) int {
-	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
+
+for x != y {
+
+for x > y {
+
+y, x = x, y
+
 }
 
-func LCM(nums ...int) int {
-	x := nums[0]
-	for _, y := range nums[1:] {
-		x = (x * y) / gcd(x, y)
-	}
-	return x
 }
+
+return x
+
+}
+
+func main() {
+
+for _, n := range
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,13 +1,3 @@

-func gcd(x, y int) int {	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
-}
+func gcd(x, y int) int { if y == 0 { return x } return gcd(y, x%y) }
 
-func LCM(nums ...int) int {
-	x := nums[0]
-	for _, y := range nums[1:] {
-		x = (x * y) / gcd(x, y)
-	}
-	return x
-}
+Make sure you understand how this works, and that it doesn’t work for negative numbers. If you’re curious, the reason
```

### Clamp (task/8)

#### canonical solution

```golang
import "math"

func Clamp(n, a, b float64) float64 {
	return math.Max(math.Min(n, math.Max(a, b)), math.Min(a, b))
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Clamp(n, a, b float64) float64 {
-	return math.Max(math.Min(n, math.Max(a, b)), math.Min(a, b))
+
+return math.MaxFloat64 < a && a < math.MinFloat64 ? a : b
+
 }
+
+const (
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Clamp(n, a, b float64) float64 {
-	return math.Max(math.Min(n, math.Max(a, b)), math.Min(a, b))
+
+if n < a {
+
+return a
+
 }
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Clamp(n, a, b float64) float64 {
-	return math.Max(math.Min(n, math.Max(a, b)), math.Min(a, b))
+
+if n < a {
+
+return a
+
 }
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,4 +1,5 @@

 import "math"
 
-func Clamp(n, a, b float64) float64 {	return math.Max(math.Min(n, math.Max(a, b)), math.Min(a, b))
-}
+func Clamp(n, a, b float64) float64 { if n < a { n = a } if n > b { n = b } return n }
+
+func main() { var s, c = 100, 20000 s = -c / 2 / 2 * (1 - 1 /
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Clamp(n, a, b float64) float64 {
-	return math.Max(math.Min(n, math.Max(a, b)), math.Min(a, b))
+
+if n < a {
+
+return a
+
 }
+
```

### Zip (task/9)

#### canonical solution

```golang
import "reflect"

func Zip(params ...interface{}) [][]interface{} {
	l := 0
	for i := range params {
		arr := reflect.ValueOf(params[i])
		if l < arr.Len() {
			l = arr.Len()
		}
	}
	r := make([][]interface{}, l)

	for i := 0; i < l; i++ {
		r[i] = make([]interface{}, 0)
		for j := range params {
			v := reflect.ValueOf(params[j])
			if v.Len() > i {
				r[i] = append(r[i], v.Index(i).Interface())
			}
		}
	}
	return r
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,23 +1,13 @@

 import "reflect"
 
 func Zip(params ...interface{}) [][]interface{} {
-	l := 0
-	for i := range params {
-		arr := reflect.ValueOf(params[i])
-		if l < arr.Len() {
-			l = arr.Len()
-		}
-	}
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = make([]interface{}, 0)
-		for j := range params {
-			v := reflect.ValueOf(params[j])
-			if v.Len() > i {
-				r[i] = append(r[i], v.Index(i).Interface())
-			}
-		}
-	}
-	return r
+if len(params) == 0 {
+
+return make([][]interface{}, 0)
+
 }
+
+// TODO: Handle errors in params
+
+var sizes = make([]int, 0, len(params
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,23 +1,19 @@

 import "reflect"
 
 func Zip(params ...interface{}) [][]interface{} {
-	l := 0
-	for i := range params {
-		arr := reflect.ValueOf(params[i])
-		if l < arr.Len() {
-			l = arr.Len()
-		}
-	}
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = make([]interface{}, 0)
-		for j := range params {
-			v := reflect.ValueOf(params[j])
-			if v.Len() > i {
-				r[i] = append(r[i], v.Index(i).Interface())
-			}
-		}
-	}
-	return r
-}
+switch len(params) {
+
+case 0:
+
+return nil
+
+case 1:
+
+return params[0]
+
+default:
+
+for i, v := range params {
+
+if i > 0 {
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,23 +1,11 @@

 import "reflect"
 
 func Zip(params ...interface{}) [][]interface{} {
-	l := 0
-	for i := range params {
-		arr := reflect.ValueOf(params[i])
-		if l < arr.Len() {
-			l = arr.Len()
-		}
-	}
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = make([]interface{}, 0)
-		for j := range params {
-			v := reflect.ValueOf(params[j])
-			if v.Len() > i {
-				r[i] = append(r[i], v.Index(i).Interface())
-			}
-		}
-	}
-	return r
-}
+res := make([][]interface{}, 0)
+
+for i, s := range params {
+
+v := reflect.ValueOf(s)
+
+if len(v.Kind() & reflect.SliceKind)
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,23 +1,13 @@

 import "reflect"
 
 func Zip(params ...interface{}) [][]interface{} {
-	l := 0
-	for i := range params {
-		arr := reflect.ValueOf(params[i])
-		if l < arr.Len() {
-			l = arr.Len()
-		}
-	}
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = make([]interface{}, 0)
-		for j := range params {
-			v := reflect.ValueOf(params[j])
-			if v.Len() > i {
-				r[i] = append(r[i], v.Index(i).Interface())
-			}
-		}
-	}
-	return r
+return New(nil).Call(params).Interface()
+
 }
+
+// Example usage:
+
+// params := []string{"http://www.google.com", "http://www.yahoo.com"}
+
+//
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,23 +1,16 @@

 import "reflect"
 
 func Zip(params ...interface{}) [][]interface{} {
-	l := 0
-	for i := range params {
-		arr := reflect.ValueOf(params[i])
-		if l < arr.Len() {
-			l = arr.Len()
-		}
-	}
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = make([]interface{}, 0)
-		for j := range params {
-			v := reflect.ValueOf(params[j])
-			if v.Len() > i {
-				r[i] = append(r[i], v.Index(i).Interface())
-			}
-		}
-	}
-	return r
+// Zip the parameters
+
+m := make([]interface{}, len(params))
+
+for i, n := range params {
+
+m[i] = params[n]
+
 }
+
+return m
+
```

### PadLeft (task/10)

#### canonical solution

```golang
import "fmt"

func PadLeft(s string, l int) string {
	f := "%" + strconv.Itoa(l) + "v"
	return fmt.Sprintf(f, s)
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadLeft(s string, l int) string {
-	f := "%" + strconv.Itoa(l) + "v"
-	return fmt.Sprintf(f, s)
+
+return fmt.Sprintf("%s%d", s, l)
+
 }
+
+func main() {
+
+var s = "Hello World"
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadLeft(s string, l int) string {
-	f := "%" + strconv.Itoa(l) + "v"
-	return fmt.Sprintf(f, s)
+
+return string(s[:l])
+
 }
+
+func PadRight(s string, l int) string {
+
+return string(s[l:])
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadLeft(s string, l int) string {
-	f := "%" + strconv.Itoa(l) + "v"
-	return fmt.Sprintf(f, s)
+
+return s[:l]
+
 }
+
+func main() {
+
+fmt.Println(PadLeft("A", 1))
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadLeft(s string, l int) string {
-	f := "%" + strconv.Itoa(l) + "v"
-	return fmt.Sprintf(f, s)
+
+if l < len(s) {
+
+return string(s[:l]) + " "
+
 }
+
+return s
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,6 +1,11 @@

 import "fmt"
 
 func PadLeft(s string, l int) string {
-	f := "%" + strconv.Itoa(l) + "v"
-	return fmt.Sprintf(f, s)
+
+return string(l*s)
+
 }
+
+func main() {
+
+var s = "ABCD"
```

### Map (task/11)

#### canonical solution

```golang
func MapInt(arr []int, fn func(int) int) []int {
	arm := make([]int, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapIntFloat64(arr []int, fn func(int) float64) []float64 {
	arm := make([]float64, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapIntBool(arr []int, fn func(int) bool) []bool {
	arm := make([]bool, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapIntString(arr []int, fn func(int) string) []string {
	arm := make([]string, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}

func MapFloat64(arr []float64, fn func(float64) float64) []float64 {
	arm := make([]float64, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapFloat64Int(arr []float64, fn func(float64) int) []int {
	arm := make([]int, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapFloat64Bool(arr []float64, fn func(float64) bool) []bool {
	arm := make([]bool, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapFloat64String(arr []float64, fn func(float64) string) []string {
	arm := make([]string, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}

func MapBool(arr []bool, fn func(bool) bool) []bool {
	arm := make([]bool, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapBoolInt(arr []bool, fn func(bool) int) []int {
	arm := make([]int, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapBoolFloat64(arr []bool, fn func(bool) float64) []float64 {
	arm := make([]float64, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapBoolString(arr []bool, fn func(bool) string) []string {
	arm := make([]string, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}

func MapString(arr []string, fn func(string) string) []string {
	arm := make([]string, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapStringInt(arr []string, fn func(string) int) []int {
	arm := make([]int, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapStringFloat64(arr []string, fn func(string) float64) []float64 {
	arm := make([]float64, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
func MapStringBool(arr []string, fn func(string) bool) []bool {
	arm := make([]bool, len(arr))
	for i, v := range arr { arm[i] = fn(v) }
	return arm
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,83 +1,15 @@

 func MapInt(arr []int, fn func(int) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntFloat64(arr []int, fn func(int) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntBool(arr []int, fn func(int) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntString(arr []int, fn func(int) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
+
+m := make(map[int]int)
+
+for _, v := range arr {
+
+m[v] = fn(v)
+
 }
 
-func MapFloat64(arr []float64, fn func(float64) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Int(arr []float64, fn func(float64) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Bool(arr []float64, fn func(float64) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64String(arr []float64, fn func(float64) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
+return m
+
 }
 
-func MapBool(arr []bool, fn func(bool) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolInt(arr []bool, fn func(bool) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolFloat64(arr []bool, fn func(bool) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolString(arr []bool, fn func(bool) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-
-func MapString(arr []string, fn func(string) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringInt(arr []string, fn func(string) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringFloat64(arr []string, fn func(string) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringBool(arr []string, fn func(string) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
+Within a goroutine,
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,82 +1 @@

-func MapInt(arr []int, fn func(int) int) []int {	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntFloat64(arr []int, fn func(int) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntBool(arr []int, fn func(int) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntString(arr []int, fn func(int) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-
-func MapFloat64(arr []float64, fn func(float64) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Int(arr []float64, fn func(float64) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Bool(arr []float64, fn func(float64) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64String(arr []float64, fn func(float64) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-
-func MapBool(arr []bool, fn func(bool) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolInt(arr []bool, fn func(bool) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolFloat64(arr []bool, fn func(bool) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolString(arr []bool, fn func(bool) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-
-func MapString(arr []string, fn func(string) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringInt(arr []string, fn func(string) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringFloat64(arr []string, fn func(string) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringBool(arr []string, fn func(string) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
+func MapInt(arr []int, fn func(int) int) []int { m := make(map[int]int) for i, v := range arr { m[v] = fn(v) } return m } func main() { arr := []int{1, 2, 3} m := MapInt
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,83 +1,15 @@

 func MapInt(arr []int, fn func(int) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntFloat64(arr []int, fn func(int) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntBool(arr []int, fn func(int) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntString(arr []int, fn func(int) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
+
+t := make([]int, len(arr))
+
+for i, v := range arr {
+
+t[i] = fn(v)
+
 }
 
-func MapFloat64(arr []float64, fn func(float64) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Int(arr []float64, fn func(float64) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Bool(arr []float64, fn func(float64) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64String(arr []float64, fn func(float64) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
+return t
+
 }
 
-func MapBool(arr []bool, fn func(bool) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolInt(arr []bool, fn func(bool) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolFloat64(arr []bool, fn func(bool) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolString(arr []bool, fn func(bool) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-
-func MapString(arr []string, fn func(string) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringInt(arr []string, fn func(string) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringFloat64(arr []string, fn func(string) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringBool(arr []string, fn func(string) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
+func main() {
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,82 +1 @@

-func MapInt(arr []int, fn func(int) int) []int {	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntFloat64(arr []int, fn func(int) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntBool(arr []int, fn func(int) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntString(arr []int, fn func(int) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-
-func MapFloat64(arr []float64, fn func(float64) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Int(arr []float64, fn func(float64) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Bool(arr []float64, fn func(float64) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64String(arr []float64, fn func(float64) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-
-func MapBool(arr []bool, fn func(bool) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolInt(arr []bool, fn func(bool) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolFloat64(arr []bool, fn func(bool) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolString(arr []bool, fn func(bool) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-
-func MapString(arr []string, fn func(string) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringInt(arr []string, fn func(string) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringFloat64(arr []string, fn func(string) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringBool(arr []string, fn func(string) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
+func MapInt(arr []int, fn func(int) int) []int { m := make(map[int]int) for i, v := range arr { m[v] = fn(v) } return m } func main() { var values []int = []int{0, 1, 2, 3
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,83 +1,15 @@

 func MapInt(arr []int, fn func(int) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntFloat64(arr []int, fn func(int) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntBool(arr []int, fn func(int) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapIntString(arr []int, fn func(int) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
+
+result := make([]int, len(arr))
+
+for i, v := range arr {
+
+result[i] = fn(v)
+
 }
 
-func MapFloat64(arr []float64, fn func(float64) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Int(arr []float64, fn func(float64) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64Bool(arr []float64, fn func(float64) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapFloat64String(arr []float64, fn func(float64) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
+return result
+
 }
 
-func MapBool(arr []bool, fn func(bool) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolInt(arr []bool, fn func(bool) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolFloat64(arr []bool, fn func(bool) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapBoolString(arr []bool, fn func(bool) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-
-func MapString(arr []string, fn func(string) string) []string {
-	arm := make([]string, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringInt(arr []string, fn func(string) int) []int {
-	arm := make([]int, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringFloat64(arr []string, fn func(string) float64) []float64 {
-	arm := make([]float64, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
-func MapStringBool(arr []string, fn func(string) bool) []bool {
-	arm := make([]bool, len(arr))
-	for i, v := range arr { arm[i] = fn(v) }
-	return arm
-}
+MapInt is a
```

### CompactWhiteSpace (task/12)

#### canonical solution

```golang
import "regexp"

func CompactWhiteSpace(str string) string {
	re := regexp.MustCompile(`\s{2,}`)
	return re.ReplaceAllString(str, " ")
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,6 +1,11 @@

 import "regexp"
 
 func CompactWhiteSpace(str string) string {
-	re := regexp.MustCompile(`\s{2,}`)
-	return re.ReplaceAllString(str, " ")
+
+return strings.TrimSuffix(strings.TrimSpace(str), """)
+
 }
+
+Please, feel free to use these functions in your project.
+
+Happy New Year!
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,6 +1,11 @@

 import "regexp"
 
 func CompactWhiteSpace(str string) string {
-	re := regexp.MustCompile(`\s{2,}`)
-	return re.ReplaceAllString(str, " ")
+
+return rxSpaceSpaces.FindStringSubmatch(str)
+
 }
+
+func TrimWhiteSpace(str string) string {
+
+return TrimSpace(CompactWhiteSpace(str))
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,6 +1,9 @@

 import "regexp"
 
 func CompactWhiteSpace(str string) string {
-	re := regexp.MustCompile(`\s{2,}`)
-	return re.ReplaceAllString(str, " ")
+
+return strings.Replace(str, " ", "", -1)
+
 }
+
+The CompactWhiteSpace function takes a string as input and replaces all whitespace characters with a single space. The regexp.Replace function
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,6 +1,11 @@

 import "regexp"
 
 func CompactWhiteSpace(str string) string {
-	re := regexp.MustCompile(`\s{2,}`)
-	return re.ReplaceAllString(str, " ")
-}
+
+str = strings.Replace(str, "
+
+", " ", -1)
+
+str = strings.Replace(str, "\r", " ", -1)
+
+str = strings.Replace(str,
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,6 +1,11 @@

 import "regexp"
 
 func CompactWhiteSpace(str string) string {
-	re := regexp.MustCompile(`\s{2,}`)
-	return re.ReplaceAllString(str, " ")
+
+return strings.Replace(str, " ", "", -1)
+
 }
+
+Here are two examples of how to use the CompactWhiteSpace function.
+
+fmt.Println(CompactWhiteSpace("Hello
```

### IsPowerOf2 (task/13)

#### canonical solution

```golang
func IsPowerOf2(n int) bool {
	return n > 0 && (n&(n-1)) == 0
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,3 +1,8 @@

 func IsPowerOf2(n int) bool {
-	return n > 0 && (n&(n-1)) == 0
+
+for _, m := range [1 << iota]n {
+
+return n&m == m
+
 }
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,3 +1,8 @@

 func IsPowerOf2(n int) bool {
-	return n > 0 && (n&(n-1)) == 0
-}
+
+for i := 0; i < n; i++ {
+
+switch n & 1 {
+
+case 1:
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,3 +1,8 @@

 func IsPowerOf2(n int) bool {
-	return n > 0 && (n&(n-1)) == 0
+
+return n%2 == 0
+
 }
+
+func IsEven(n int) bool {
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,3 +1,8 @@

 func IsPowerOf2(n int) bool {
-	return n > 0 && (n&(n-1)) == 0
+
+return n%2 == 0
+
 }
+
+// IsPowerOf2 reports whether n is a power of 2.
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,3 +1,8 @@

 func IsPowerOf2(n int) bool {
-	return n > 0 && (n&(n-1)) == 0
+
+return n&(n-1) == 0
+
 }
+
+func Filter(n int, f func(int) bool) int {
+
```

### Capitalize (task/14)

#### canonical solution

```golang
import "strings"

func Capitalize(s string) string {
	return strings.ToUpper(s[0:1]) + s[1:]
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Capitalize(s string) string {
-	return strings.ToUpper(s[0:1]) + s[1:]
+
+return strings.ToUpper(s)
+
 }
+
+Output:
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Capitalize(s string) string {
-	return strings.ToUpper(s[0:1]) + s[1:]
+
+for i := 0; i < len(s); i++ {
+
+s[i] = strings.ToUpper(s[i])
+
 }
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Capitalize(s string) string {
-	return strings.ToUpper(s[0:1]) + s[1:]
+
+return strings.ToUpper(s)
+
 }
+
+func main() {
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Capitalize(s string) string {
-	return strings.ToUpper(s[0:1]) + s[1:]
+
+if len(s) == 0 {
+
+return ""
+
 }
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Capitalize(s string) string {
-	return strings.ToUpper(s[0:1]) + s[1:]
+
+return strings.ToUpper(s)
+
 }
+
+func main() {
+
```

### TruncateString (task/15)

#### canonical solution

```golang
func TruncateString(s string, l int) string {
	r := s
	if len(s) > l {
		if l > 3 {
			l -= 3
		}
		r = s[0:l] + "..."
	}
	return r
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,10 +1,15 @@

 func TruncateString(s string, l int) string {
-	r := s
-	if len(s) > l {
-		if l > 3 {
-			l -= 3
-		}
-		r = s[0:l] + "..."
-	}
-	return r
+
+if l <= 0 {
+
+return s
+
 }
+
+return s[:l]
+
+}
+
+func Truncate(s, l int) string {
+
+return TruncateString(s, l
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,10 +1,13 @@

 func TruncateString(s string, l int) string {
-	r := s
-	if len(s) > l {
-		if l > 3 {
-			l -= 3
-		}
-		r = s[0:l] + "..."
-	}
-	return r
+
+if l < 0 {
+
+l = len(s)
+
 }
+
+r := make([]byte, 0, l)
+
+for i := 0; i < l; i++ {
+
+r = append
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,10 +1,15 @@

 func TruncateString(s string, l int) string {
-	r := s
-	if len(s) > l {
-		if l > 3 {
-			l -= 3
-		}
-		r = s[0:l] + "..."
-	}
-	return r
+
+if l <= 0 {
+
+return s
+
 }
+
+r := make([]byte, 0, l)
+
+n := copy(r, s)
+
+r = r[n:]
+
+return string(
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,10 +1,13 @@

 func TruncateString(s string, l int) string {
-	r := s
-	if len(s) > l {
-		if l > 3 {
-			l -= 3
-		}
-		r = s[0:l] + "..."
-	}
-	return r
+
+return string(s[:l])
+
 }
+
+func TruncateStringBySpace(s string, l int) string {
+
+return string(s[:l])
+
+}
+
+func Truncate
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,10 +1,9 @@

 func TruncateString(s string, l int) string {
-	r := s
-	if len(s) > l {
-		if l > 3 {
-			l -= 3
-		}
-		r = s[0:l] + "..."
-	}
-	return r
+
+return strconv.FormatInt(strconv.Itoa(int(l)), 10) + s
+
 }
+
+func main() {
+
+fmt.Println(TruncateString("An example string", 7
```

### IntRange (task/16)

#### canonical solution

```golang
func IntRange(f, t, s int) []int {
	arr := make([]int, (t-f+1)/s)
	for i := range arr {
		arr[i] = i*s + f
	}
	return arr
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,6 +1,3 @@

-func IntRange(f, t, s int) []int {	arr := make([]int, (t-f+1)/s)
-	for i := range arr {
-		arr[i] = i*s + f
-	}
-	return arr
-}
+func IntRange(f, t, s int) []int { a := make([]int, 0, s) for i := f; i < t; i++ { a = append(a, i) } return a }
+
+We've now reduced the maximum runtime to O(f).
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,7 +1,12 @@

 func IntRange(f, t, s int) []int {
-	arr := make([]int, (t-f+1)/s)
-	for i := range arr {
-		arr[i] = i*s + f
-	}
-	return arr
+
+if f < t {
+
+return []int{f}
+
 }
+
+if f == t {
+
+return []int{t}
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,6 +1 @@

-func IntRange(f, t, s int) []int {	arr := make([]int, (t-f+1)/s)
-	for i := range arr {
-		arr[i] = i*s + f
-	}
-	return arr
-}
+func IntRange(f, t, s int) []int { return nil } const ( LowestBits = int((1<<63)-1) MaxVal = 1<<(63-1) ) // Wrap an int64 as a *big.Int func Size(x int64) *big.
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,7 +1,12 @@

 func IntRange(f, t, s int) []int {
-	arr := make([]int, (t-f+1)/s)
-	for i := range arr {
-		arr[i] = i*s + f
-	}
-	return arr
+
+r := make([]int, 0, len(t))
+
+for i := t; i < s; i++ {
+
+r = append(r, f(i))
+
 }
+
+return r
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,6 +1 @@

-func IntRange(f, t, s int) []int {	arr := make([]int, (t-f+1)/s)
-	for i := range arr {
-		arr[i] = i*s + f
-	}
-	return arr
-}
+func IntRange(f, t, s int) []int { + for i := t; i < s; i++ { + r := f(i) + r2 := r + if r2 > i { + r2 = i + } + if r2 < t { + r2 =
```

### IsInRange (task/17)

#### canonical solution

```golang
import "math"

func IsInRange(n, a, b float64) bool {
	s, e := math.Min(a, b), math.Max(a, b)
	return n >= s && n < e
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,6 +1,11 @@

 import "math"
 
 func IsInRange(n, a, b float64) bool {
-	s, e := math.Min(a, b), math.Max(a, b)
-	return n >= s && n < e
+
+return n >= a && n <= b
+
 }
+
+// Euclidean distance between two points
+
+func Dist(p, q Point) float64 {
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,6 +1,11 @@

 import "math"
 
 func IsInRange(n, a, b float64) bool {
-	s, e := math.Min(a, b), math.Max(a, b)
-	return n >= s && n < e
+
+return n >= a && n <= b
+
 }
+
+func constApprox(n, a, b float64) float64 {
+
+if IsInRange(n, a, b) {
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,6 +1,11 @@

 import "math"
 
 func IsInRange(n, a, b float64) bool {
-	s, e := math.Min(a, b), math.Max(a, b)
-	return n >= s && n < e
+
+if a < b {
+
+return false
+
 }
+
+if a > b {
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,6 +1,11 @@

 import "math"
 
 func IsInRange(n, a, b float64) bool {
-	s, e := math.Min(a, b), math.Max(a, b)
-	return n >= s && n < e
+
+return n > a && n < b
+
 }
+
+func main() {
+
+for i := 0; i < 3; i++ {
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,6 +1,11 @@

 import "math"
 
 func IsInRange(n, a, b float64) bool {
-	s, e := math.Min(a, b), math.Max(a, b)
-	return n >= s && n < e
+
+if n < a || n > b {
+
+return false
+
 }
+
+return true
```

### IndexOf (task/18)

#### canonical solution

```golang
import "reflect"

func IndexOf(params ...interface{}) int {
	arr, v := reflect.ValueOf(params[0]),
		reflect.ValueOf(params[1]).Interface()

	for i := 0; i < arr.Len(); i++ {
		if arr.Index(i).Interface() == v {
			return i
		}
	}
	return -1
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,13 +1,15 @@

 import "reflect"
 
 func IndexOf(params ...interface{}) int {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return i
-		}
-	}
-	return -1
+if params == nil {
+
+panic("reflect: index of nil interface")
+
 }
+
+v := reflect.ValueOf(params[0])
+
+if v.Kind() != reflect.Interface {
+
+panic("
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,13 +1,18 @@

 import "reflect"
 
 func IndexOf(params ...interface{}) int {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return i
-		}
-	}
-	return -1
+for i, v := range params {
+
+if v == nil {
+
+return i
+
 }
+
+}
+
+return -1
+
+}
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,13 +1,17 @@

 import "reflect"
 
 func IndexOf(params ...interface{}) int {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return i
-		}
-	}
-	return -1
+var list []int
+
+for _, x := range params {
+
+list = append(list, x.(int))
+
 }
+
+return list[0]
+
+}
+
+Can you guess how it works?
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,13 +1,18 @@

 import "reflect"
 
 func IndexOf(params ...interface{}) int {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return i
-		}
-	}
-	return -1
+index := len(params)
+
+for i := 0; i < index; i++ {
+
+if params[i] == nil {
+
+return -1
+
 }
+
+}
+
+return 0
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,13 +1,13 @@

 import "reflect"
 
 func IndexOf(params ...interface{}) int {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return i
-		}
-	}
-	return -1
+return reflect.Indirect(reflect.ValueOf(params)).(int)
+
 }
+
+Now we can index into slices directly as if they were maps:
+
+func main() {
+
+// mySlice := []
```

### ToKebab (task/19)

#### canonical solution

```golang
import "strings"

func ToKebab(s string) string {
	return strings.Join(strings.Fields(s), "-")
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToKebab(s string) string {
-	return strings.Join(strings.Fields(s), "-")
+
+return strings.ToLower(strings.Replace(s, " ", "-", -1))
+
 }
+
+func main() {
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToKebab(s string) string {
-	return strings.Join(strings.Fields(s), "-")
-}
+
+for _, r := range s {
+
+if !unicode.IsLetter(r) {
+
+return s
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToKebab(s string) string {
-	return strings.Join(strings.Fields(s), "-")
+
+return strings.ToLower(s)
+
 }
+
+And it works! As you can see, the blank identifier _ is used as a placeholder.
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToKebab(s string) string {
-	return strings.Join(strings.Fields(s), "-")
+
+// replace all spaces in string with an underscore
+
+return strings.Replace(s, " ", "_", -1)
+
 }
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func ToKebab(s string) string {
-	return strings.Join(strings.Fields(s), "-")
+
+return s
+
 }
+
+func main() {
+
```

### Frequencies (task/20)

#### canonical solution

```golang
func FrequenciesInt(arr []int) map[int]int {
	m := make(map[int]int)
	for _, v := range arr {
		if f, ok := m[v]; ok {
			m[v] = f + 1
		} else {
			m[v] = 1
		}
	}
	return m
}
func FrequenciesFloat64(arr []float64) map[float64]int {
	m := make(map[float64]int)
	for _, v := range arr {
		if f, ok := m[v]; ok {
			m[v] = f + 1
		} else {
			m[v] = 1
		}
	}
	return m
}
func FrequenciesBool(arr []bool) map[bool]int {
	m := make(map[bool]int)
	for _, v := range arr {
		if f, ok := m[v]; ok {
			m[v] = f + 1
		} else {
			m[v] = 1
		}
	}
	return m
}
func FrequenciesString(arr []string) map[string]int {
	m := make(map[string]int)
	for _, v := range arr {
		if f, ok := m[v]; ok {
			m[v] = f + 1
		} else {
			m[v] = 1
		}
	}
	return m
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,44 +1,17 @@

 func FrequenciesInt(arr []int) map[int]int {
-	m := make(map[int]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
+
+m := make(map[int]int)
+
+for _, v := range arr {
+
+m[v] = 1
+
 }
-func FrequenciesFloat64(arr []float64) map[float64]int {
-	m := make(map[float64]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
+
+return m
+
 }
-func FrequenciesBool(arr []bool) map[bool]int {
-	m := make(map[bool]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
-func FrequenciesString(arr []string) map[string]int {
-	m := make(map[string]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
+
+func main() {
+
+arr :=
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,44 +1,17 @@

 func FrequenciesInt(arr []int) map[int]int {
-	m := make(map[int]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
+
+s := make(map[int]int)
+
+for i, v := range arr {
+
+s[v] = i
+
 }
-func FrequenciesFloat64(arr []float64) map[float64]int {
-	m := make(map[float64]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
+
+return s
+
 }
-func FrequenciesBool(arr []bool) map[bool]int {
-	m := make(map[bool]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
-func FrequenciesString(arr []string) map[string]int {
-	m := make(map[string]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
+
+func main() {
+
+freqs
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,44 +1,15 @@

 func FrequenciesInt(arr []int) map[int]int {
-	m := make(map[int]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
+
+m := make(map[int]int)
+
+for _, v := range arr {
+
+m[v] = 1
+
 }
-func FrequenciesFloat64(arr []float64) map[float64]int {
-	m := make(map[float64]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
+
+return m
+
 }
-func FrequenciesBool(arr []bool) map[bool]int {
-	m := make(map[bool]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
-func FrequenciesString(arr []string) map[string]int {
-	m := make(map[string]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
+
+func FrequenciesFloat64(arr []
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,43 +1 @@

-func FrequenciesInt(arr []int) map[int]int {	m := make(map[int]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
-func FrequenciesFloat64(arr []float64) map[float64]int {
-	m := make(map[float64]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
-func FrequenciesBool(arr []bool) map[bool]int {
-	m := make(map[bool]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
-func FrequenciesString(arr []string) map[string]int {
-	m := make(map[string]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
+func FrequenciesInt(arr []int) map[int]int { m := make(map[int]int) for i, v := range arr { m[v] = i } return m } // func PrintFrequencies(f FrequenciesInt) { // fmt.Println(f) //
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,44 +1,13 @@

 func FrequenciesInt(arr []int) map[int]int {
-	m := make(map[int]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
+
+var freqs map[int]int
+
+freqs = make(map[int]int)
+
+for _, v := range arr {
+
+freqs[v] = freq
+
 }
-func FrequenciesFloat64(arr []float64) map[float64]int {
-	m := make(map[float64]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
-func FrequenciesBool(arr []bool) map[bool]int {
-	m := make(map[bool]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
-func FrequenciesString(arr []string) map[string]int {
-	m := make(map[string]int)
-	for _, v := range arr {
-		if f, ok := m[v]; ok {
-			m[v] = f + 1
-		} else {
-			m[v] = 1
-		}
-	}
-	return m
-}
+
+return fre
```

### ContainsWhiteSpace (task/21)

#### canonical solution

```golang
import "regexp"

func ContainsWhiteSpace(str string) bool {
	re := regexp.MustCompile(`\s`)
	return re.MatchString(str)
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,6 +1,11 @@

 import "regexp"
 
 func ContainsWhiteSpace(str string) bool {
-	re := regexp.MustCompile(`\s`)
-	return re.MatchString(str)
+
+return strings.ContainsAny(str, unicode.IsSpace)
+
 }
+
+// A pair of type-safe functions to make quick work of "is this a
+
+// space, a newline, or neither
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,6 +1,9 @@

 import "regexp"
 
 func ContainsWhiteSpace(str string) bool {
-	re := regexp.MustCompile(`\s`)
-	return re.MatchString(str)
+
+return strings.HasPrefix(str, " ") || strings.HasSuffix(str, " ")
+
 }
+
+As you can see from the code snippet above, you are free to use any package or
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,6 +1,11 @@

 import "regexp"
 
 func ContainsWhiteSpace(str string) bool {
-	re := regexp.MustCompile(`\s`)
-	return re.MatchString(str)
+
+return !strings.ContainsAny(str, []byte("\u0020"))
+
 }
+
+// Fuzzed files:
+
+// len | string 'cafe\u0020bacon'
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,6 +1,11 @@

 import "regexp"
 
 func ContainsWhiteSpace(str string) bool {
-	re := regexp.MustCompile(`\s`)
-	return re.MatchString(str)
+
+return regexp.IsSpace(str)
+
 }
+
+function matchesCss(str string, css *css.Selector, selector *css.Selector) bool {
+
+for {
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,6 +1,11 @@

 import "regexp"
 
 func ContainsWhiteSpace(str string) bool {
-	re := regexp.MustCompile(`\s`)
-	return re.MatchString(str)
+
+return strings.ContainsAny(str, unicode.IsSpace)
+
 }
+
+func main() {
+
+fmt.Println(ContainsWhiteSpace(""))
```

### Sum (task/22)

#### canonical solution

```golang
func Sum(nums ...float64) float64 {
	sum := float64(0)
	for _, num := range nums {
		sum += num
	}
	return sum
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,6 +1,3 @@

-func Sum(nums ...float64) float64 {	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum
-}
+func Sum(nums ...float64) float64 { return sums[len(nums)-1] } func main() { sum, _ := Sum(1, 2, 3, 4, 5) fmt.Println(sum) }
+
+If you’re familiar with the basics
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,6 +1 @@

-func Sum(nums ...float64) float64 {	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum
-}
+func Sum(nums ...float64) float64 { return math.Sum(nums...) } func Factorial(n int) float64 { if n <= 1 { return 1 } return math.Factorial(n-1) * n } func main() { f := Factorial(5
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,7 +1,12 @@

 func Sum(nums ...float64) float64 {
-	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum
+
+for _, x := range nums {
+
+fmt.Printf("Sum = %.2f
+
+", x)
+
 }
+
+return 0
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,7 +1,12 @@

 func Sum(nums ...float64) float64 {
-	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum
+
+sum := 0.0
+
+for _, v := range nums {
+
+sum += v
+
 }
+
+return sum
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,7 +1,12 @@

 func Sum(nums ...float64) float64 {
-	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum
+
+return SumFloat64(nums...)
+
 }
+
+type SumFloat64 struct {
+
+sum float64
+
+nums []float64
+
```

### Digits (task/23)

#### canonical solution

```golang
import (
	"strconv"
	"strings"
)

func Digits(n int) []int {
	s := strconv.Itoa(n)
	d := make([]int, len(s))
	for i, l := range strings.Split(s, "") {
		d[i], _ = strconv.Atoi(l)
	}
	return d
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,12 +1,9 @@

-import (	"strconv"
-	"strings"
-)
+import ( " sync " " time " )
 
-func Digits(n int) []int {
-	s := strconv.Itoa(n)
-	d := make([]int, len(s))
-	for i, l := range strings.Split(s, "") {
-		d[i], _ = strconv.Atoi(l)
-	}
-	return d
-}
+// Settable enables you to specify a `persistent` field in your struct
+
+// which can be set to change the behavior of the struct.
+
+//
+
+// This is used to
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,12 +1 @@

-import (	"strconv"
-	"strings"
-)
-
-func Digits(n int) []int {
-	s := strconv.Itoa(n)
-	d := make([]int, len(s))
-	for i, l := range strings.Split(s, "") {
-		d[i], _ = strconv.Atoi(l)
-	}
-	return d
-}
+import ( "//base/test:test_support/test_runner" ) func TestDataEncoder(t *testing.T) { // TestDataEncoder should create correct version and not change the test data. for _, tt :=
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,12 +1,7 @@

-import (	"strconv"
-	"strings"
-)
+import ( " github.com/google/go-cmp/cmp " )
 
-func Digits(n int) []int {
-	s := strconv.Itoa(n)
-	d := make([]int, len(s))
-	for i, l := range strings.Split(s, "") {
-		d[i], _ = strconv.Atoi(l)
-	}
-	return d
-}
+var (
+
+src = [] byte ( " package main; func main() { } " )
+
+expected = [] byte ( " package main; func main()
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,12 +1,3 @@

-import (	"strconv"
-	"strings"
-)
+import ( "//third_party/webdriver/chromedriver/src/chromedriver/base.googlesource.com/chromedriver/version.pb.cc" )
 
-func Digits(n int) []int {
-	s := strconv.Itoa(n)
-	d := make([]int, len(s))
-	for i, l := range strings.Split(s, "") {
-		d[i], _ = strconv.Atoi(l)
-	}
-	return d
-}
+src_test := "//third_party
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,12 +1 @@

-import (	"strconv"
-	"strings"
-)
-
-func Digits(n int) []int {
-	s := strconv.Itoa(n)
-	d := make([]int, len(s))
-	for i, l := range strings.Split(s, "") {
-		d[i], _ = strconv.Atoi(l)
-	}
-	return d
-}
+import ( + " fmt " + " log " + " math " + " os " + " regexp " + " strconv " + " strings " + " sync " + " time " + ) + +var outputBytes = make ([] byte
```

### RandIntInRange (task/24)

#### canonical solution

```golang
import "math/rand"

func RandIntInRange(min, max int) int {
	return rand.Intn(max-min) + min
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "math/rand"
 
 func RandIntInRange(min, max int) int {
-	return rand.Intn(max-min) + min
+
+return rand.Intn(max-min+1) + min
+
 }
+
+func RandIntInRange16(min, max int16) int16 {
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "math/rand"
 
 func RandIntInRange(min, max int) int {
-	return rand.Intn(max-min) + min
-}
+
+var i int
+
+for i = min; i < max; i++ {
+
+rand.Intn(int(uint(rand.Int31()) * (max - min + 1)))
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "math/rand"
 
 func RandIntInRange(min, max int) int {
-	return rand.Intn(max-min) + min
+
+return rand.Intn(max-min) + min
+
 }
+
+func RandFloatInRange(min, max float64) float64 {
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "math/rand"
 
 func RandIntInRange(min, max int) int {
-	return rand.Intn(max-min) + min
+
+return rand.Intn(max-min+1) + min
+
 }
+
+func RandIntInRangeEven(min, max int) int {
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,9 @@

 import "math/rand"
 
 func RandIntInRange(min, max int) int {
-	return rand.Intn(max-min) + min
+
+return rand.Intn(max-min+1) + min
+
 }
+
+The library function’s name is prefixed with an underscore (“_”) to prevent it from conflicting with the same-
```

### IsLower (task/25)

#### canonical solution

```golang
import "strings"

func IsLower(s string) bool {
	return strings.ToLower(s) == s
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsLower(s string) bool {
-	return strings.ToLower(s) == s
-}
+
+for i := 0; i < len(s); i++ {
+
+if s[i] >= 'a' && s[i] <= 'z' {
+
+return false
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsLower(s string) bool {
-	return strings.ToLower(s) == s
-}
+
+for i := 0; i < len(s); i++ {
+
+if s[i] >= 'a' && s[i] <= 'z' {
+
+return false
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsLower(s string) bool {
-	return strings.ToLower(s) == s
-}
+
+for i := 0; i < len(s); i++ {
+
+switch s[i] {
+
+case 'a' ... 'z':
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsLower(s string) bool {
-	return strings.ToLower(s) == s
-}
+
+for i := 0; i < len(s); i++ {
+
+if s[i] >= 'a' && s[i] <= 'z' {
+
+return false
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsLower(s string) bool {
-	return strings.ToLower(s) == s
-}
+
+for i := 0; i < len(s); i++ {
+
+c := s[i]
+
+if c >= 'a' && c <= 'z' {
+
```

### Average (task/26)

#### canonical solution

```golang
func Average(nums ...float64) float64 {
	sum := float64(0)
	for _, num := range nums {
		sum += num
	}
	return sum / float64(len(nums))
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,6 +1,3 @@

-func Average(nums ...float64) float64 {	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum / float64(len(nums))
-}
+func Average(nums ...float64) float64 { var sum float64 for _, v := range nums { sum += v } return sum / float64(len(nums)) }
+
+With this in place, we can create histograms of varying lengths with the following code:
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,7 +1,12 @@

 func Average(nums ...float64) float64 {
-	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum / float64(len(nums))
+
+return math.Sqrt(sum(nums))
+
 }
+
+func sum(nums ...float64) float64 {
+
+return 0.0
+
+}
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,6 +1,4 @@

-func Average(nums ...float64) float64 {	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum / float64(len(nums))
-}
+func Average(nums ...float64) float64 { sum := 0.0 for _, v := range nums { sum += v } return sum / float64(len(nums)) }
+
+This is not only easy to read, but it is also far more efficient.
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,6 +1,3 @@

-func Average(nums ...float64) float64 {	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum / float64(len(nums))
-}
+func Average(nums ...float64) float64 { avg := 0.0 for _, v := range nums { avg += v } return avg / float64(len(nums)) }
+
+func StdDev(nums ...float64) float64 { avg := 0.
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,6 +1,9 @@

-func Average(nums ...float64) float64 {	sum := float64(0)
-	for _, num := range nums {
-		sum += num
-	}
-	return sum / float64(len(nums))
-}
+func Average(nums ...float64) float64 { return sum(nums) / len(nums) }
+
+func Sum(nums ...float64) float64 {
+
+var total float64
+
+for _, v := range nums {
+
+total += v
```

### IndexOfAll (task/27)

#### canonical solution

```golang
import "reflect"

func IndexOfAll(params ...interface{}) []int {
	arr, v, r := reflect.ValueOf(params[0]),
		reflect.ValueOf(params[1]).Interface(),
		make([]int, 0)

	for i := 0; i < arr.Len(); i++ {
		if arr.Index(i).Interface() == v {
			r = append(r, i)
		}
	}
	if len(r) != 0 {
		return r
	}
	return []int{-1}
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,17 +1,13 @@

 import "reflect"
 
 func IndexOfAll(params ...interface{}) []int {
-	arr, v, r := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface(),
-		make([]int, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			r = append(r, i)
-		}
-	}
-	if len(r) != 0 {
-		return r
-	}
-	return []int{-1}
+return append(reflect.MakeSlice(reflect.TypeOf(params), 0, params), params...)
+
 }
+
+// A database represents a directory on the filesystem.
+
+type Database struct {
+
+path string
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,17 +1,9 @@

 import "reflect"
 
 func IndexOfAll(params ...interface{}) []int {
-	arr, v, r := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface(),
-		make([]int, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			r = append(r, i)
-		}
-	}
-	if len(r) != 0 {
-		return r
-	}
-	return []int{-1}
-}
+var ret = make([]int, 0)
+
+for _, value := range params {
+
+ret = append(ret, reflect.ValueOf(value).Elem().Index(reflect.ValueOf(value)))
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,17 +1,13 @@

 import "reflect"
 
 func IndexOfAll(params ...interface{}) []int {
-	arr, v, r := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface(),
-		make([]int, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			r = append(r, i)
-		}
-	}
-	if len(r) != 0 {
-		return r
-	}
-	return []int{-1}
+return make([]int, 0, len(params))
+
 }
+
+func doIndexOfAll(params ...interface{}) (int, error) {
+
+for _, v := range params {
+
+if i
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,17 +1,17 @@

 import "reflect"
 
 func IndexOfAll(params ...interface{}) []int {
-	arr, v, r := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface(),
-		make([]int, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			r = append(r, i)
-		}
-	}
-	if len(r) != 0 {
-		return r
-	}
-	return []int{-1}
+var result []int
+
+for _, element := range params {
+
+result = append(result, element)
+
 }
+
+return result
+
+}
+
+var names = []string{"Alice", "Bob", "
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,17 +1,13 @@

 import "reflect"
 
 func IndexOfAll(params ...interface{}) []int {
-	arr, v, r := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface(),
-		make([]int, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			r = append(r, i)
-		}
-	}
-	if len(r) != 0 {
-		return r
-	}
-	return []int{-1}
-}
+// All arguments are non-nil, so they should all be indexed.
+
+// If there's more than one...
+
+if len(params) > 1 {
+
+// ...we should definitely have a slice
+
+//
```

### Any (task/28)

#### canonical solution

```golang
func AnyInt(arr []int, fn func(int) bool) bool {
	for _, v := range arr {
		if fn(v) {
			return true
		}
	}
	return false
}
func AnyFloat64(arr []float64, fn func(float64) bool) bool {
	for _, v := range arr {
		if fn(v) {
			return true
		}
	}
	return false
}
func AnyBool(arr []bool, fn func(bool) bool) bool {
	for _, v := range arr {
		if fn(v) {
			return true
		}
	}
	return false
}
func AnyString(arr []string, fn func(string) bool) bool {
	for _, v := range arr {
		if fn(v) {
			return true
		}
	}
	return false
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,31 +1 @@

-func AnyInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
+func AnyInt(arr []int, fn func(int) bool) bool { for _, x := range arr { if fn(x) { return true } } return false } func main() { fmt.Println(addEvenNumbers(0, 2)) fmt.Println(addEvenNumbers(0, 2
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,31 +1 @@

-func AnyInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
+func AnyInt(arr []int, fn func(int) bool) bool { for _, x := range arr { if fn(x) { return true } } return false } func main() { arr := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9,
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,31 +1 @@

-func AnyInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
+func AnyInt(arr []int, fn func(int) bool) bool { for _, v := range arr { if !fn(v) { return false } } return true } func main() { var a [2]int a[0] = 1 a[1] = 2 var b = []int{
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,31 +1 @@

-func AnyInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
-func AnyString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
+func AnyInt(arr []int, fn func(int) bool) bool { for _, x := range arr { if !fn(x) { return false } } return true } type MyInt int func (x MyInt) String() string { return fmt.Sprintf("MyInt(%d)", x)
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,32 +1,20 @@

 func AnyInt(arr []int, fn func(int) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
+
+for i, v := range arr {
+
+if fn(v) {
+
+return true
+
 }
-func AnyFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
+
 }
-func AnyBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
+
+return false
+
 }
-func AnyString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return true
-		}
-	}
-	return false
-}
+
+// recursive
+
+
+func AnyInts(arr []int,
```

### ReverseString (task/29)

#### canonical solution

```golang
func ReverseString(s string) string {
	o := make([]rune, len(s))
	for i, c := range s {
		o[len(s)-i-1] = c
	}
	return string(o)
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,7 +1,12 @@

 func ReverseString(s string) string {
-	o := make([]rune, len(s))
-	for i, c := range s {
-		o[len(s)-i-1] = c
-	}
-	return string(o)
+
+r := make([]byte, len(s))
+
+for i, c := range s {
+
+r[i] = c
+
 }
+
+return string(r)
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,7 +1,12 @@

 func ReverseString(s string) string {
-	o := make([]rune, len(s))
-	for i, c := range s {
-		o[len(s)-i-1] = c
-	}
-	return string(o)
+
+return strings.NewString(strings.Replace(s, " ", "", -1))
+
 }
+
+func ExampleStartStop() {
+
+start := time.Now()
+
+defer func() {
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,6 +1,5 @@

-func ReverseString(s string) string {	o := make([]rune, len(s))
-	for i, c := range s {
-		o[len(s)-i-1] = c
-	}
-	return string(o)
-}
+func ReverseString(s string) string { return s[len(s)-1] }
+
+func ReverseByteSlice(bs []byte) []byte { return bs[len(bs)-1:] }
+
+func ReverseInt(i int) int { return int(
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,7 +1,12 @@

 func ReverseString(s string) string {
-	o := make([]rune, len(s))
-	for i, c := range s {
-		o[len(s)-i-1] = c
-	}
-	return string(o)
+
+return strings.Replace(s, []byte(""), []byte(""), -1)
+
 }
+
+func Reverse(s string) string {
+
+return ReverseString(s)
+
+}
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,7 +1,11 @@

 func ReverseString(s string) string {
-	o := make([]rune, len(s))
-	for i, c := range s {
-		o[len(s)-i-1] = c
-	}
-	return string(o)
+
+r := new(bytes.Buffer)
+
+for i := 0; i < len(s); i++ {
+
+r.WriteByte(s[i])
+
 }
+
+return string(r.Bytes())
```

### ToCamel (task/30)

#### canonical solution

```golang
import "strings"

func ToCamel(s string) string {
	c := ""
	for _, w := range strings.Fields(s) {
		c += strings.ToUpper(w[0:1]) + strings.ToLower(w[1:])
	}
	return strings.ToLower(c[0:1]) + c[1:]
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,9 +1,11 @@

 import "strings"
 
 func ToCamel(s string) string {
-	c := ""
-	for _, w := range strings.Fields(s) {
-		c += strings.ToUpper(w[0:1]) + strings.ToLower(w[1:])
-	}
-	return strings.ToLower(c[0:1]) + c[1:]
+
+return strings.ToLower(strings.Replace(s, "[^a-zA-Z]", "", -1))
+
 }
+
+func ToDashes(s string) string {
+
+return strings.
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,9 +1,11 @@

 import "strings"
 
 func ToCamel(s string) string {
-	c := ""
-	for _, w := range strings.Fields(s) {
-		c += strings.ToUpper(w[0:1]) + strings.ToLower(w[1:])
-	}
-	return strings.ToLower(c[0:1]) + c[1:]
+
+return strings.ToLower(strings.Replace(s, "-", "_", -1))
+
 }
+
+func ToCamelCase(s string) string {
+
+return strings.ToLower(strings.Replace
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,9 +1,14 @@

 import "strings"
 
 func ToCamel(s string) string {
-	c := ""
-	for _, w := range strings.Fields(s) {
-		c += strings.ToUpper(w[0:1]) + strings.ToLower(w[1:])
-	}
-	return strings.ToLower(c[0:1]) + c[1:]
+
+c := strings.ToLower(s)
+
+if c != "go" {
+
+c = "go"
+
 }
+
+return c
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,9 +1,14 @@

 import "strings"
 
 func ToCamel(s string) string {
-	c := ""
-	for _, w := range strings.Fields(s) {
-		c += strings.ToUpper(w[0:1]) + strings.ToLower(w[1:])
-	}
-	return strings.ToLower(c[0:1]) + c[1:]
+
+var letters []rune
+
+for _, r := range s {
+
+letters = append(letters, r)
+
 }
+
+switch {
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,9 +1,14 @@

 import "strings"
 
 func ToCamel(s string) string {
-	c := ""
-	for _, w := range strings.Fields(s) {
-		c += strings.ToUpper(w[0:1]) + strings.ToLower(w[1:])
-	}
-	return strings.ToLower(c[0:1]) + c[1:]
+
+if s == "" {
+
+return "";
+
 }
+
+if s[0] != '[' {
+
+return s;
+
```

### WithIndex (task/31)

#### canonical solution

```golang
import "reflect"

func WithIndex(params ...interface{}) map[int]interface{} {
	arr, m := reflect.ValueOf(params[0]),
		make(map[int]interface{})
	for i := 0; i < arr.Len(); i++ {
		m[i] = arr.Index(i).Interface()
	}
	return m
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,10 +1,15 @@

 import "reflect"
 
 func WithIndex(params ...interface{}) map[int]interface{} {
-	arr, m := reflect.ValueOf(params[0]),
-		make(map[int]interface{})
-	for i := 0; i < arr.Len(); i++ {
-		m[i] = arr.Index(i).Interface()
-	}
-	return m
+
+var m map[int]interface{}
+
+for _, i := range params {
+
+m[i] = params[i]
+
 }
+
+return m
+
+}
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,10 +1,15 @@

 import "reflect"
 
 func WithIndex(params ...interface{}) map[int]interface{} {
-	arr, m := reflect.ValueOf(params[0]),
-		make(map[int]interface{})
-	for i := 0; i < arr.Len(); i++ {
-		m[i] = arr.Index(i).Interface()
-	}
-	return m
+
+index := make(map[int]interface{})
+
+for _, v := range params {
+
+index[v.Index()] = v
+
 }
+
+return index
+
+}
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,10 +1,14 @@

 import "reflect"
 
 func WithIndex(params ...interface{}) map[int]interface{} {
-	arr, m := reflect.ValueOf(params[0]),
-		make(map[int]interface{})
-	for i := 0; i < arr.Len(); i++ {
-		m[i] = arr.Index(i).Interface()
-	}
-	return m
+
+return params[0].(map[int]interface{})
+
 }
+
+func f() {
+
+t := time.Now()
+
+seconds := time.Duration(t.Unix()).Seconds()
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,10 +1,13 @@

 import "reflect"
 
 func WithIndex(params ...interface{}) map[int]interface{} {
-	arr, m := reflect.ValueOf(params[0]),
-		make(map[int]interface{})
-	for i := 0; i < arr.Len(); i++ {
-		m[i] = arr.Index(i).Interface()
-	}
-	return m
-}
+
+index := params[0]
+
+data := params[1:]
+
+data = make(map[int]interface{}, len(data))
+
+for i, v := range data {
+
+data[i] =
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,10 +1,11 @@

 import "reflect"
 
 func WithIndex(params ...interface{}) map[int]interface{} {
-	arr, m := reflect.ValueOf(params[0]),
-		make(map[int]interface{})
-	for i := 0; i < arr.Len(); i++ {
-		m[i] = arr.Index(i).Interface()
-	}
-	return m
+
+i := params[0]
+
+return MakeMap(reflect.MakeSlice(i, params[1:]...), reflect.Zero(reflect.TypeOf(i))).Interface()
+
 }
+
+func MakeMap
```

### IndentString (task/32)

#### canonical solution

```golang
import "strings"

func Indent(s, i string) string {
	return i + strings.Replace(s, "\n", "\n"+i, -1)
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Indent(s, i string) string {
-	return i + strings.Replace(s, "\n", "\n"+i, -1)
-}
+
+for i > 0 {
+
+s = s + " "
+
+i--
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Indent(s, i string) string {
-	return i + strings.Replace(s, "\n", "\n"+i, -1)
+
+return strings.Repeat(" ", i) + s
+
 }
+
+func main() {
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Indent(s, i string) string {
-	return i + strings.Replace(s, "\n", "\n"+i, -1)
+
+return s + strings.Repeat(" ", i)
+
 }
+
+func Parser(s string) (value interface{}, ok bool) {
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Indent(s, i string) string {
-	return i + strings.Replace(s, "\n", "\n"+i, -1)
+
+if i == "" {
+
+return s
+
 }
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Indent(s, i string) string {
-	return i + strings.Replace(s, "\n", "\n"+i, -1)
+
+if i == "" {
+
+return s
+
 }
+
```

### Concat (task/33)

#### canonical solution

```golang
func ConcatInt(a,b []int) []int {
	return append(a, b...)
}
func ConcatFloat64(a,b []float64) []float64 {
	return append(a, b...)
}
func ConcatBool(a,b []bool) []bool {
	return append(a, b...)
}
func ConcatStrings(a,b []string) []string {
	return append(a, b...)
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,11 +1 @@

-func ConcatInt(a,b []int) []int {	return append(a, b...)
-}
-func ConcatFloat64(a,b []float64) []float64 {
-	return append(a, b...)
-}
-func ConcatBool(a,b []bool) []bool {
-	return append(a, b...)
-}
-func ConcatStrings(a,b []string) []string {
-	return append(a, b...)
-}
+func ConcatInt(a,b []int) []int { return append(a, append(b, 0)) } func AddInts(a,b []int) []int { return append(a, append(b, 0)) } func Multiplicities(n []int) []int
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,12 +1,13 @@

 func ConcatInt(a,b []int) []int {
-	return append(a, b...)
+
+return append(a,b...)
+
 }
-func ConcatFloat64(a,b []float64) []float64 {
-	return append(a, b...)
+
+func ConcatInts(a,b []int) []int {
+
+return append(a,b...)
+
 }
-func ConcatBool(a,b []bool) []bool {
-	return append(a, b...)
-}
-func ConcatStrings(a,b []string) []string {
-	return append(a, b...)
-}
+
+func ConcatSlice(a
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,11 +1 @@

-func ConcatInt(a,b []int) []int {	return append(a, b...)
-}
-func ConcatFloat64(a,b []float64) []float64 {
-	return append(a, b...)
-}
-func ConcatBool(a,b []bool) []bool {
-	return append(a, b...)
-}
-func ConcatStrings(a,b []string) []string {
-	return append(a, b...)
-}
+func ConcatInt(a,b []int) []int { c := make([]int,len(a)+len(b)) copy(c,a) copy(c[len(a):],b) return c } func ConcatFloat(a,b []float64) []float64
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,11 +1 @@

-func ConcatInt(a,b []int) []int {	return append(a, b...)
-}
-func ConcatFloat64(a,b []float64) []float64 {
-	return append(a, b...)
-}
-func ConcatBool(a,b []bool) []bool {
-	return append(a, b...)
-}
-func ConcatStrings(a,b []string) []string {
-	return append(a, b...)
-}
+func ConcatInt(a,b []int) []int { return append(a,b...) } func ConcatString(a,b string) string { return a + b } func Concat(a,b ...interface{}) interface{} { for _, x := range a { b =
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,11 +1 @@

-func ConcatInt(a,b []int) []int {	return append(a, b...)
-}
-func ConcatFloat64(a,b []float64) []float64 {
-	return append(a, b...)
-}
-func ConcatBool(a,b []bool) []bool {
-	return append(a, b...)
-}
-func ConcatStrings(a,b []string) []string {
-	return append(a, b...)
-}
+func ConcatInt(a,b []int) []int { + return a + b +} + +func ConcatString(a,b string) string { + return a + b +} + +func ConcatFloat(a,b float64) float64 { + return a + b +
```

### Rads (task/34)

#### canonical solution

```golang
import "math"

func Rads(d float64) float64 {
	return d * math.Pi / 180.0
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Rads(d float64) float64 {
-	return d * math.Pi / 180.0
+
+return math.Pow(d, float64(math.Pi))
+
 }
+
+func Rads2Degrees(r float64) float64 {
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Rads(d float64) float64 {
-	return d * math.Pi / 180.0
+
+return d * pi / 180.0
+
 }
+
+func Degrees(d float64) float64 {
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Rads(d float64) float64 {
-	return d * math.Pi / 180.0
+
+return math.Pow(math.Pi * d, 1.0 / 3.0)
+
 }
+
+var radians float64 = Rads(1)
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Rads(d float64) float64 {
-	return d * math.Pi / 180.0
+
+return d * math.Pi / 180.0
+
 }
+
+func RadDeg(d float64) float64 {
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Rads(d float64) float64 {
-	return d * math.Pi / 180.0
+
+return float64(d) * math.Pi / 180.0
+
 }
+
+func Radians(d float64) float64 {
+
```

### FindLastIndex (task/35)

#### canonical solution

```golang
func FindLastIndexInt(arr []int, f func(int) bool) int {
	for i := len(arr) - 1; i >= 0; i-- {
		if f(arr[i]) {
			return i
		}
	}
	return -1
}
func FindLastIndexFloat64(arr []float64, f func(float64) bool) int {
	for i := len(arr) - 1; i >= 0; i-- {
		if f(arr[i]) {
			return i
		}
	}
	return -1
}
func FindLastIndexBool(arr []bool, f func(bool) bool) int {
	for i := len(arr) - 1; i >= 0; i-- {
		if f(arr[i]) {
			return i
		}
	}
	return -1
}
func FindLastIndexString(arr []string, f func(string) bool) int {
	for i := len(arr) - 1; i >= 0; i-- {
		if f(arr[i]) {
			return i
		}
	}
	return -1
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,32 +1,15 @@

 func FindLastIndexInt(arr []int, f func(int) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
+last := len(arr) - 1
+
+for i := 0; i < last; i++ {
+
+if f(arr[i]) {
+
+return i
+
 }
-func FindLastIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
 }
-func FindLastIndexBool(arr []bool, f func(bool) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
-}
-func FindLastIndexString(arr []string, f func(string) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
-}
+
+return -1
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,32 +1,19 @@

 func FindLastIndexInt(arr []int, f func(int) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
+index := -1
+
+for _, x := range arr {
+
+if f(x) {
+
+index = index + 1
+
 }
-func FindLastIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
 }
-func FindLastIndexBool(arr []bool, f func(bool) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
+return index
+
 }
-func FindLastIndexString(arr []string, f func(string) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
-}
+
+func main() {
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,32 +1,19 @@

 func FindLastIndexInt(arr []int, f func(int) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
+for i, v := range arr {
+
+if f(v) {
+
+return i
+
 }
-func FindLastIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
 }
-func FindLastIndexBool(arr []bool, f func(bool) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
+return -1
+
 }
-func FindLastIndexString(arr []string, f func(string) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
-}
+
+func main() {
+
+var arr = []int{
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,32 +1,17 @@

 func FindLastIndexInt(arr []int, f func(int) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
+for i, v := range arr {
+
+if f(v) {
+
+return i
+
 }
-func FindLastIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
 }
-func FindLastIndexBool(arr []bool, f func(bool) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
+return -1
+
 }
-func FindLastIndexString(arr []string, f func(string) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
-}
+
+func GetAverage(numbers []int) (average int
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,32 +1,17 @@

 func FindLastIndexInt(arr []int, f func(int) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
+for i, x := range arr {
+
+if f(x) {
+
+return i
+
 }
-func FindLastIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
 }
-func FindLastIndexBool(arr []bool, f func(bool) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
+
+return -1
+
 }
-func FindLastIndexString(arr []string, f func(string) bool) int {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return i
-		}
-	}
-	return -1
-}
+
+func FindLastIndexFloat64(arr []float64,
```

### Mask (task/36)

#### canonical solution

```golang
import "strings"

func Mask(cc string, n int, m rune) string {
	return strings.Repeat(string(m), len(cc)-n) + cc[len(cc)-n:]
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Mask(cc string, n int, m rune) string {
-	return strings.Repeat(string(m), len(cc)-n) + cc[len(cc)-n:]
-}
+
+b := make([]byte, len(cc)*2+2)
+
+for i := 0; i < n; i++ {
+
+b[i] = '?'
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Mask(cc string, n int, m rune) string {
-	return strings.Repeat(string(m), len(cc)-n) + cc[len(cc)-n:]
+
+if n <= 0 {
+
+return ""]"
+
 }
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Mask(cc string, n int, m rune) string {
-	return strings.Repeat(string(m), len(cc)-n) + cc[len(cc)-n:]
+
+if m == 0 {
+
+return cc
+
 }
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Mask(cc string, n int, m rune) string {
-	return strings.Repeat(string(m), len(cc)-n) + cc[len(cc)-n:]
-}
+
+r := rune(m)
+
+for i := 0; i < n; i++ {
+
+cc = cc[0:i] + cc[i+1:] + r
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Mask(cc string, n int, m rune) string {
-	return strings.Repeat(string(m), len(cc)-n) + cc[len(cc)-n:]
-}
+
+cc = strings.ToLower(cc)
+
+runes := make([]rune, n)
+
+for i := 0; i < n; i++ {
+
```

### XProduct (task/37)

#### canonical solution

```golang
import "reflect"

func XProduct(params ...interface{}) [][]interface{} {
	a, b := reflect.ValueOf(params[0]), reflect.ValueOf(params[1])
	l := a.Len() * b.Len()
	r := make([][]interface{}, l)

	for i := 0; i < l; i++ {
		r[i] = []interface{}{
			a.Index(i % a.Len()).Interface(),
			b.Index((i / a.Len()) % b.Len()).Interface(),
		}
	}
	return r

}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,16 +1,15 @@

 import "reflect"
 
 func XProduct(params ...interface{}) [][]interface{} {
-	a, b := reflect.ValueOf(params[0]), reflect.ValueOf(params[1])
-	l := a.Len() * b.Len()
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = []interface{}{
-			a.Index(i % a.Len()).Interface(),
-			b.Index((i / a.Len()) % b.Len()).Interface(),
-		}
-	}
-	return r
+return new(squared)
 
 }
+
+func main() {
+
+c := []string{"a", "b", "c"}
+
+x := XProduct(c)
+
+fmt.Println(x
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,16 +1,19 @@

 import "reflect"
 
 func XProduct(params ...interface{}) [][]interface{} {
-	a, b := reflect.ValueOf(params[0]), reflect.ValueOf(params[1])
-	l := a.Len() * b.Len()
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = []interface{}{
-			a.Index(i % a.Len()).Interface(),
-			b.Index((i / a.Len()) % b.Len()).Interface(),
-		}
-	}
-	return r
+return params
 
 }
+
+In this example, we use the reflect package to process the params in XProduct.
+
+
+
+type alias ServerParam =
+
+{
+
+serverAddress: string
+
+, sessId:
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,16 +1,13 @@

 import "reflect"
 
 func XProduct(params ...interface{}) [][]interface{} {
-	a, b := reflect.ValueOf(params[0]), reflect.ValueOf(params[1])
-	l := a.Len() * b.Len()
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = []interface{}{
-			a.Index(i % a.Len()).Interface(),
-			b.Index((i / a.Len()) % b.Len()).Interface(),
-		}
-	}
-	return r
+return reflect.ValueOf(params).Pairs()
 
 }
+
+func YProduct(params ...interface{}) [][]interface{} {
+
+return reflect.ValueOf(params).Pairs()
+
+}
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,16 +1,11 @@

 import "reflect"
 
 func XProduct(params ...interface{}) [][]interface{} {
-	a, b := reflect.ValueOf(params[0]), reflect.ValueOf(params[1])
-	l := a.Len() * b.Len()
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = []interface{}{
-			a.Index(i % a.Len()).Interface(),
-			b.Index((i / a.Len()) % b.Len()).Interface(),
-		}
-	}
-	return r
+ps := make([][]interface{}, len(params))
 
-}
+for i, p := range params {
+
+ps[i] = make([]interface{}, len(p))
+
+for j, n := range
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,16 +1,9 @@

 import "reflect"
 
 func XProduct(params ...interface{}) [][]interface{} {
-	a, b := reflect.ValueOf(params[0]), reflect.ValueOf(params[1])
-	l := a.Len() * b.Len()
-	r := make([][]interface{}, l)
 
-	for i := 0; i < l; i++ {
-		r[i] = []interface{}{
-			a.Index(i % a.Len()).Interface(),
-			b.Index((i / a.Len()) % b.Len()).Interface(),
-		}
-	}
-	return r
+return make([][]interface{}, len(params))
 
 }
+
+func XMap(mapping func(i interface{}, j int) interface{}, data ...interface{}) [][]interface{} {
```

### IsUpper (task/38)

#### canonical solution

```golang
import "strings"

func IsUpper(s string) bool {
	return strings.ToUpper(s) == s
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsUpper(s string) bool {
-	return strings.ToUpper(s) == s
-}
+
+for i := 0; i < len(s); i++ {
+
+if s[i] < 'A' || s[i] > 'Z' {
+
+return false
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsUpper(s string) bool {
-	return strings.ToUpper(s) == s
+
+return strings.ToUpper(s) == s
+
 }
+
+func main() {
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsUpper(s string) bool {
-	return strings.ToUpper(s) == s
-}
+
+for i := 0; i < len(s); i++ {
+
+if s[i] >= 'a' && s[i] <= 'z' {
+
+return false
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsUpper(s string) bool {
-	return strings.ToUpper(s) == s
-}
+
+for i := 0; i < len(s); i++ {
+
+if s[i] >= 'A' && s[i] <= 'Z' {
+
+return true
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func IsUpper(s string) bool {
-	return strings.ToUpper(s) == s
-}
+
+for i := 0; i < len(s); i++ {
+
+if s[i] < 'A' || s[i] > 'Z' {
+
+return false
+
```

### None (task/39)

#### canonical solution

```golang
func NoneInt(arr []int, fn func(int) bool) bool {
	for _, v := range arr {
		if fn(v) {
			return false
		}
	}
	return true
}
func NoneFloat64(arr []float64, fn func(float64) bool) bool {
	for _, v := range arr {
		if fn(v) {
			return false
		}
	}
	return true
}
func NoneBool(arr []bool, fn func(bool) bool) bool {
	for _, v := range arr {
		if fn(v) {
			return false
		}
	}
	return true
}
func NoneString(arr []string, fn func(string) bool) bool {
	for _, v := range arr {
		if fn(v) {
			return false
		}
	}
	return true
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,31 +1,3 @@

-func NoneInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func NoneFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func NoneBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func NoneString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
+func NoneInt(arr []int, fn func(int) bool) bool { for _, v := range arr { if fn(v) { return true } } return false }
+
+Note: the function func NoneInt(arr []int, fn func(int) bool) bool is the same as func(arr
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,32 +1,19 @@

 func NoneInt(arr []int, fn func(int) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
+
+for i, v := range arr {
+
+if fn(v) {
+
+return true
+
 }
-func NoneFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
+
 }
-func NoneBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
+
+return false
+
 }
-func NoneString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
+
+func main() {
+
+arr := []int{5,
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,32 +1,17 @@

 func NoneInt(arr []int, fn func(int) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
+
+for i, v := range arr {
+
+if fn(v) {
+
+return true
+
 }
-func NoneFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
+
 }
-func NoneBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
+
+return false
+
 }
-func NoneString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
+
+// func NoneString(arr []string, fn func(string
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,31 +1,3 @@

-func NoneInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func NoneFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func NoneBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func NoneString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
+func NoneInt(arr []int, fn func(int) bool) bool { for _, x := range arr { if fn(x) { return true } } return false }
+
+The second parameter of the filter function is an anonymous function that accepts one parameter of type int and returns a bool . It is called for
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,31 +1 @@

-func NoneInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func NoneFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func NoneBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func NoneString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if fn(v) {
-			return false
-		}
-	}
-	return true
-}
+func NoneInt(arr []int, fn func(int) bool) bool { // ... } func filterInt(arr []int, pred func(int) bool) []int { // ... } // ... var a, b = func([]int) int { // ... }([]int{1, 2, 3
```

### AllSame (task/40)

#### canonical solution

```golang
import "reflect"

func AllSame(params ...interface{}) bool {
	arr := reflect.ValueOf(params[0])
	v := arr.Index(0).Interface()

	for i := 0; i < arr.Len(); i++ {
		if arr.Index(i).Interface() != v {
			return false
		}
	}
	return true
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,13 +1,9 @@

 import "reflect"
 
 func AllSame(params ...interface{}) bool {
-	arr := reflect.ValueOf(params[0])
-	v := arr.Index(0).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() != v {
-			return false
-		}
-	}
-	return true
+return reflect.DeepEqual(params, params)
+
 }
+
+AllSame is an example of a helper function that makes use of the reflect package to do its job. AllSame takes a slice of parameters and checks if all
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,13 +1,13 @@

 import "reflect"
 
 func AllSame(params ...interface{}) bool {
-	arr := reflect.ValueOf(params[0])
-	v := arr.Index(0).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() != v {
-			return false
-		}
-	}
-	return true
+sig := reflect.TypeOf(params).String()
+
+return sig == "*"
+
 }
+
+// AllSame returns whether all of the values are the same.
+
+func AllSame(params ...interface{
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,13 +1,15 @@

 import "reflect"
 
 func AllSame(params ...interface{}) bool {
-	arr := reflect.ValueOf(params[0])
-	v := arr.Index(0).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() != v {
-			return false
-		}
-	}
-	return true
+return reflect.DeepEqual(params, params)
+
 }
+
+func Float32(float64) float32 {
+
+return float32(float64)
+
+}
+
+func Float64(float32) float
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,13 +1,9 @@

 import "reflect"
 
 func AllSame(params ...interface{}) bool {
-	arr := reflect.ValueOf(params[0])
-	v := arr.Index(0).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() != v {
-			return false
-		}
-	}
-	return true
+return reflect.DeepEqual(params, params)
+
 }
+
+I’m not sure if this is the best way to handle it but it works. I know there is a way to use the reflect package but I
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,13 +1,18 @@

 import "reflect"
 
 func AllSame(params ...interface{}) bool {
-	arr := reflect.ValueOf(params[0])
-	v := arr.Index(0).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() != v {
-			return false
-		}
-	}
-	return true
+var s, ok bool
+
+for _, param := range params {
+
+s, ok = param.(string)
+
+if !ok {
+
+return false
+
 }
+
+}
+
```

### HammingDistance (task/41)

#### canonical solution

```golang
import (
	"fmt"
	"strings"
)

func ΗammingDistance(n, m int) int {
	return strings.Count(fmt.Sprintf("%b", n^m), "1")
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,7 +1,12 @@

-import (	"fmt"
-	"strings"
-)
+import ( "bytes"
 
-func ΗammingDistance(n, m int) int {
-	return strings.Count(fmt.Sprintf("%b", n^m), "1")
-}
+"crypto/rand"
+
+"crypto/sha256"
+
+"crypto/sha512"
+
+"encoding/base64"
+
+"errors"
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,7 +1,7 @@

-import (	"fmt"
-	"strings"
-)
+import ( "//build/config/nacl/nacl_constants.gni" )
 
-func ΗammingDistance(n, m int) int {
-	return strings.Count(fmt.Sprintf("%b", n^m), "1")
-}
+if (is_nacl) {
+
+# We don't want to build anything on Android, because it's not
+
+# supported
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,7 +1 @@

-import (	"fmt"
-	"strings"
-)
-
-func ΗammingDistance(n, m int) int {
-	return strings.Count(fmt.Sprintf("%b", n^m), "1")
-}
+import ( "fmt" ) type A struct { Name string } func ( a A ) String () string { return fmt . Sprintf ( "A(%s)" , a . Name ) } func main () { a := A { Name : "
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,7 +1 @@

-import (	"fmt"
-	"strings"
-)
-
-func ΗammingDistance(n, m int) int {
-	return strings.Count(fmt.Sprintf("%b", n^m), "1")
-}
+import ( "fmt" ) func main() { names := []string{"Harry", "Ron", "Hermione", "Luna", "Neville", "Ginny", "Cho", "Draco", "Pansy", "Pad
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,7 +1 @@

-import (	"fmt"
-	"strings"
-)
-
-func ΗammingDistance(n, m int) int {
-	return strings.Count(fmt.Sprintf("%b", n^m), "1")
-}
+import ( "errors" "io" "log" "net/http" "os" "strings" "time" ) // ToDoURL returns the user's todo URL. func ToDoURL(c *gin.Context) string { return
```

### Compact (task/42)

#### canonical solution

```golang
import "reflect"

func Compact(params ...interface{}) []reflect.Value {
	arr := reflect.ValueOf(params[0])
	r := make([]reflect.Value, 0)

	for i := 0; i < arr.Len(); i++ {
		if !arr.Index(i).IsZero() {
			r = append(r, arr.Index(i))
		}
	}
	return r
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,13 +1,13 @@

 import "reflect"
 
 func Compact(params ...interface{}) []reflect.Value {
-	arr := reflect.ValueOf(params[0])
-	r := make([]reflect.Value, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if !arr.Index(i).IsZero() {
-			r = append(r, arr.Index(i))
-		}
-	}
-	return r
+if len(params) == 0 {
+
+return nil
+
 }
+
+compact := make([]reflect.Value, 0, len(params))
+
+for i := 0; i < len(params); i++
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,13 +1,15 @@

 import "reflect"
 
 func Compact(params ...interface{}) []reflect.Value {
-	arr := reflect.ValueOf(params[0])
-	r := make([]reflect.Value, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if !arr.Index(i).IsZero() {
-			r = append(r, arr.Index(i))
-		}
-	}
-	return r
+return []reflect.Value{}
+
 }
+
+func GetIface(gdb *debug.Debugger, val reflect.Value) string {
+
+return gdb.Interface(val)
+
+}
+
+func
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,13 +1,17 @@

 import "reflect"
 
 func Compact(params ...interface{}) []reflect.Value {
-	arr := reflect.ValueOf(params[0])
-	r := make([]reflect.Value, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if !arr.Index(i).IsZero() {
-			r = append(r, arr.Index(i))
-		}
-	}
-	return r
+var ps []reflect.Value
+
+for _, p := range params {
+
+ps = append(ps, reflect.ValueOf(p))
+
 }
+
+return ps
+
+}
+
+// Duplicate copies a
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,13 +1,15 @@

 import "reflect"
 
 func Compact(params ...interface{}) []reflect.Value {
-	arr := reflect.ValueOf(params[0])
-	r := make([]reflect.Value, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if !arr.Index(i).IsZero() {
-			r = append(r, arr.Index(i))
-		}
-	}
-	return r
+return params[0].([]reflect.Value)
+
 }
+
+func main() {
+
+// Print elements in compacted slice
+
+fmt.Println(Compact([]reflect.Value{
+
+//
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,13 +1,13 @@

 import "reflect"
 
 func Compact(params ...interface{}) []reflect.Value {
-	arr := reflect.ValueOf(params[0])
-	r := make([]reflect.Value, 0)
 
-	for i := 0; i < arr.Len(); i++ {
-		if !arr.Index(i).IsZero() {
-			r = append(r, arr.Index(i))
-		}
-	}
-	return r
+p := make([]reflect.Value, 0, len(params))
+
+for i, v := range params {
+
+p = append(p, reflect.ValueOf(v))
+
 }
+
+return p
```

### IsEven (task/43)

#### canonical solution

```golang
func IsEven(n int) bool {
	return n % 2 == 0
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,2 +1,7 @@

-func IsEven(n int) bool {	return n % 2 == 0
-}
+func IsEven(n int) bool { return n%2 == 0 }
+
+IsEven returns true if n is even.
+
+IsOdd returns true if n is odd.
+
+Note that Go requires the integer literals to be in decimal. For
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,3 +1,8 @@

 func IsEven(n int) bool {
-	return n % 2 == 0
+
+return n%2 == 0
+
 }
+
+func main() {
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,2 +1,7 @@

-func IsEven(n int) bool {	return n % 2 == 0
-}
+func IsEven(n int) bool { return n%2 == 0 }
+
+func IsOdd(n int) bool { return n%2 == 1 }
+
+// IsOddEven reports whether n is odd or even.
+
+func IsOddEven(n
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,3 +1,8 @@

 func IsEven(n int) bool {
-	return n % 2 == 0
+
+return n%2 == 0
+
 }
+
+func main() {
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,3 +1,8 @@

 func IsEven(n int) bool {
-	return n % 2 == 0
+
+return n%2 == 0
+
 }
+
+func LogEven(n int) {
+
```

### FindLast (task/44)

#### canonical solution

```golang
import "fmt"

func FindLastInt(arr []int, f func(int) bool) (int, error) {
	for i := len(arr) - 1; i >= 0; i-- {
		if f(arr[i]) {
			return arr[i], nil
		}
	}
	return 0, fmt.Errorf("No matches found")
}
func FindLastFloat64(arr []float64, f func(float64) bool) (float64, error) {
	for i := len(arr) - 1; i >= 0; i-- {
		if f(arr[i]) {
			return arr[i], nil
		}
	}
	return 0.0, fmt.Errorf("No matches found")
}
func FindLastBool(arr []bool, f func(bool) bool) (bool, error) {
	for i := len(arr) - 1; i >= 0; i-- {
		if f(arr[i]) {
			return arr[i], nil
		}
	}
	return false, fmt.Errorf("No matches found")
}
func FindLastString(arr []string, f func(string) bool) (string, error) {
	for i := len(arr) - 1; i >= 0; i-- {
		if f(arr[i]) {
			return arr[i], nil
		}
	}
	return "", fmt.Errorf("No matches found")
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,34 +1,18 @@

 import "fmt"
 
 func FindLastInt(arr []int, f func(int) bool) (int, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+for i, v := range arr {
+
+if f(v) {
+
+return i, nil
+
 }
-func FindLastFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
 }
-func FindLastBool(arr []bool, f func(bool) bool) (bool, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
+
+return -1, errors.New("int array not found")
+
 }
-func FindLastString(arr []string, f func(string) bool) (string, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,34 +1,17 @@

 import "fmt"
 
 func FindLastInt(arr []int, f func(int) bool) (int, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+i := len(arr) - 1
+
+for i > 0 && f(arr[i]) {
+
+i--
+
 }
-func FindLastFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
+return arr[i], nil
+
 }
-func FindLastBool(arr []bool, f func(bool) bool) (bool, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
-}
-func FindLastString(arr []string, f func(string) bool) (string, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
+
+var arrs = []int
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,34 +1,17 @@

 import "fmt"
 
 func FindLastInt(arr []int, f func(int) bool) (int, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+i := len(arr) - 1
+
+for ; i >= 0; i-- {
+
+if f(arr[i]) {
+
+return i, nil
+
 }
-func FindLastFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
 }
-func FindLastBool(arr []bool, f func(bool) bool) (bool, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
-}
-func FindLastString(arr []string, f func(string) bool) (string, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
+
+return 0, fmt.
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,34 +1,17 @@

 import "fmt"
 
 func FindLastInt(arr []int, f func(int) bool) (int, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+for i, v := range arr {
+
+if f(v) {
+
+return i, nil
+
 }
-func FindLastFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
 }
-func FindLastBool(arr []bool, f func(bool) bool) (bool, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
+
+return 0, fmt.Errorf("findLastInt: not found")
+
 }
-func FindLastString(arr []string, f func(string) bool) (string, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,34 +1,16 @@

 import "fmt"
 
 func FindLastInt(arr []int, f func(int) bool) (int, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0, fmt.Errorf("No matches found")
+
+for i, v := range arr {
+
+if f(v) {
+
+return i, nil
+
 }
-func FindLastFloat64(arr []float64, f func(float64) bool) (float64, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return 0.0, fmt.Errorf("No matches found")
+
 }
-func FindLastBool(arr []bool, f func(bool) bool) (bool, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return false, fmt.Errorf("No matches found")
-}
-func FindLastString(arr []string, f func(string) bool) (string, error) {
-	for i := len(arr) - 1; i >= 0; i-- {
-		if f(arr[i]) {
-			return arr[i], nil
-		}
-	}
-	return "", fmt.Errorf("No matches found")
-}
+
+return -1, fmt.Errorf("find last int: not found")
+
```

### FindIndex (task/45)

#### canonical solution

```golang
func FindIndexInt(arr []int, f func(int) bool) int {
	for i, v := range arr {
		if f(v) {
			return i
		}
	}
	return -1
}
func FindIndexFloat64(arr []float64, f func(float64) bool) int {
	for i, v := range arr {
		if f(v) {
			return i
		}
	}
	return -1
}
func FindIndexBool(arr []bool, f func(bool) bool) int {
	for i, v := range arr {
		if f(v) {
			return i
		}
	}
	return -1
}
func FindIndexString(arr []string, f func(string) bool) int {
	for i, v := range arr {
		if f(v) {
			return i
		}
	}
	return -1
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,31 +1 @@

-func FindIndexInt(arr []int, f func(int) bool) int {	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
-func FindIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
-func FindIndexBool(arr []bool, f func(bool) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
-func FindIndexString(arr []string, f func(string) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
+func FindIndexInt(arr []int, f func(int) bool) int { //以下是findIndex函数设计的关键 //从1开始，在arr中找出其中第一
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,31 +1 @@

-func FindIndexInt(arr []int, f func(int) bool) int {	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
-func FindIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
-func FindIndexBool(arr []bool, f func(bool) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
-func FindIndexString(arr []string, f func(string) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
+func FindIndexInt(arr []int, f func(int) bool) int { for i, v := range arr { if f(i) { return i } } return -1 } func main() { fmt.Println(FindIndexInt([]int{3, 4, 5}, func(i int) bool
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,32 +1,19 @@

 func FindIndexInt(arr []int, f func(int) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
+
+for i, v := range arr {
+
+if f(v) {
+
+return i
+
 }
-func FindIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
+
 }
-func FindIndexBool(arr []bool, f func(bool) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
+
+return -1
+
 }
-func FindIndexString(arr []string, f func(string) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
+
+func main() {
+
+fmt.Println(
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,32 +1,17 @@

 func FindIndexInt(arr []int, f func(int) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
+
+for i, v := range arr {
+
+if f(v) {
+
+return i
+
 }
-func FindIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
+
 }
-func FindIndexBool(arr []bool, f func(bool) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
+
+return -1
+
 }
-func FindIndexString(arr []string, f func(string) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
+
+// Run this a few times to get a profile:
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,32 +1,19 @@

 func FindIndexInt(arr []int, f func(int) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
+
+if len(arr) < 2 {
+
+return -1
+
 }
-func FindIndexFloat64(arr []float64, f func(float64) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
+
+for i, v := range arr {
+
+if f(v) {
+
+return i
+
 }
-func FindIndexBool(arr []bool, f func(bool) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
+
 }
-func FindIndexString(arr []string, f func(string) bool) int {
-	for i, v := range arr {
-		if f(v) {
-			return i
-		}
-	}
-	return -1
-}
+
+return -
```

### FahrenheitToCelsius (task/46)

#### canonical solution

```golang
func FahrenheitToCelsius(d float64) float64 {
	return (d - 32.0) * 5.0 / 9.0
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,2 +1,7 @@

-func FahrenheitToCelsius(d float64) float64 {	return (d - 32.0) * 5.0 / 9.0
-}
+func FahrenheitToCelsius(d float64) float64 { return d * 1.8 + 32 } func main() { f := FahrenheitToCelsius(-50) fmt.Println(f) }
+
+$ go run test.go -42
+
+map
+
+map is a built-
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,2 +1,3 @@

-func FahrenheitToCelsius(d float64) float64 {	return (d - 32.0) * 5.0 / 9.0
-}
+func FahrenheitToCelsius(d float64) float64 { return d * 1.8 + 32 } func main() { f := FahrenheitToCelsius(32) fmt.Println(f) }
+
+As you can see, we now have two new type declarations. The first is called Celsius
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,2 +1 @@

-func FahrenheitToCelsius(d float64) float64 {	return (d - 32.0) * 5.0 / 9.0
-}
+func FahrenheitToCelsius(d float64) float64 { return 32.0 * d / (d + 459.0) } // ftoa64 is defined in the standard library. func main() { f := ftoa64(FahrenheitToCelsius(32)) fmt.
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,2 +1,3 @@

-func FahrenheitToCelsius(d float64) float64 {	return (d - 32.0) * 5.0 / 9.0
-}
+func FahrenheitToCelsius(d float64) float64 { if d < 32 { return 32 + (d-32)/1.8 } return 32 + (d-32)/1.8 * 5 }
+
+If you have a simple type to which you want to add a simple method, you
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,2 +1 @@

-func FahrenheitToCelsius(d float64) float64 {	return (d - 32.0) * 5.0 / 9.0
-}
+func FahrenheitToCelsius(d float64) float64 { return math.Min(d, -273.15) * 1.8 + 32 } func CelsiusToFahrenheit(c float64) float64 { return c * 1.8 + 32 } func main() { fahrenheit :=
```

### Join (task/47)

#### canonical solution

```golang
import (
	"fmt"
	"reflect"
	"strings"
)

func Join(params ...interface{}) string {
	arr, sp := reflect.ValueOf(params[0]),
		reflect.ValueOf(params[1]).String()
	ars := make([]string, arr.Len())

	for i := 0; i < arr.Len(); i++ {
		ars[i] = fmt.Sprintf("%v", arr.Index(i))
	}

	return strings.Join(ars, sp)

}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,17 +1 @@

-import (	"fmt"
-	"reflect"
-	"strings"
-)
-
-func Join(params ...interface{}) string {
-	arr, sp := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).String()
-	ars := make([]string, arr.Len())
-
-	for i := 0; i < arr.Len(); i++ {
-		ars[i] = fmt.Sprintf("%v", arr.Index(i))
-	}
-
-	return strings.Join(ars, sp)
-
-}
+import ( "sync" "time" ) // WaitUntilSync is a custom Sync that times out after 30 seconds. type WaitUntilSync struct { sync . Mutex // This value must be set externally once the WaitUntilSync // object is created. Once
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,17 +1 @@

-import (	"fmt"
-	"reflect"
-	"strings"
-)
-
-func Join(params ...interface{}) string {
-	arr, sp := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).String()
-	ars := make([]string, arr.Len())
-
-	for i := 0; i < arr.Len(); i++ {
-		ars[i] = fmt.Sprintf("%v", arr.Index(i))
-	}
-
-	return strings.Join(ars, sp)
-
-}
+import ( "errors" "io" "net/http" "strings" "time" ) // ErrNoSuchUser is the error returned when a user is not found. var ErrNoSuchUser = errors . New ( "no such user" )
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,17 +1,12 @@

-import (	"fmt"
-	"reflect"
-	"strings"
+import ( "sync" "time" )
+
+var (
+
+mu sync.Mutex
+
+scheduler = time.NewTicker( 5 * time.Second)
+
 )
 
-func Join(params ...interface{}) string {
-	arr, sp := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).String()
-	ars := make([]string, arr.Len())
+// Do not alter this method.
 
-	for i := 0; i < arr.Len(); i++ {
-		ars[i] = fmt.Sprintf("%v", arr.Index(i))
-	}
-
-	return strings.Join(ars, sp)
-
-}
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,17 +1 @@

-import (	"fmt"
-	"reflect"
-	"strings"
-)
-
-func Join(params ...interface{}) string {
-	arr, sp := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).String()
-	ars := make([]string, arr.Len())
-
-	for i := 0; i < arr.Len(); i++ {
-		ars[i] = fmt.Sprintf("%v", arr.Index(i))
-	}
-
-	return strings.Join(ars, sp)
-
-}
+import ( "github.com/fsnotify/fsnotify" ) type AsyncFswatcher struct { sync.Mutex // contains filtered or unexported fields } func NewAsyncFswatcher(w fsnotify.Watcher) *
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,17 +1 @@

-import (	"fmt"
-	"reflect"
-	"strings"
-)
-
-func Join(params ...interface{}) string {
-	arr, sp := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).String()
-	ars := make([]string, arr.Len())
-
-	for i := 0; i < arr.Len(); i++ {
-		ars[i] = fmt.Sprintf("%v", arr.Index(i))
-	}
-
-	return strings.Join(ars, sp)
-
-}
+import ( "bytes" "errors" "io" "os" "path/filepath" "strings" "sync" "time" ) func main() { // Build command cmd := exec.Command( "git" , "init" , "
```

### IsOdd (task/48)

#### canonical solution

```golang
func IsOdd(n int) bool {
	return n % 2 == 1
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,3 +1,8 @@

 func IsOdd(n int) bool {
-	return n % 2 == 1
+
+return n%2 == 1
+
 }
+
+func IsEven(n int) bool {
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,2 +1,3 @@

-func IsOdd(n int) bool {	return n % 2 == 1
-}
+func IsOdd(n int) bool { return n%2 == 1 } func main() { for i := 0; i < 10; i++ { fmt.Println(IsOdd(i)) } }
+
+通过这个程
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,3 +1,8 @@

 func IsOdd(n int) bool {
-	return n % 2 == 1
+
+return n%2 == 1
+
 }
+
+func mul(x, y int) int {
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,3 +1,8 @@

 func IsOdd(n int) bool {
-	return n % 2 == 1
+
+return n%2 == 1
+
 }
+
+func IsEven(n int) bool {
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,3 +1,8 @@

 func IsOdd(n int) bool {
-	return n % 2 == 1
+
+if n%2 == 0 {
+
+return false
+
 }
+
```

### All (task/49)

#### canonical solution

```golang
func AllInt(arr []int, fn func(int) bool) bool {
	for _, v := range arr {
		if !fn(v) {
			return false
		}
	}
	return true
}
func AllFloat64(arr []float64, fn func(float64) bool) bool {
	for _, v := range arr {
		if !fn(v) {
			return false
		}
	}
	return true
}
func AllBool(arr []bool, fn func(bool) bool) bool {
	for _, v := range arr {
		if !fn(v) {
			return false
		}
	}
	return true
}
func AllString(arr []string, fn func(string) bool) bool {
	for _, v := range arr {
		if !fn(v) {
			return false
		}
	}
	return true
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,32 +1,15 @@

 func AllInt(arr []int, fn func(int) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
+
+h := 0
+
+for _, n := range arr {
+
+h += fn(n)
+
 }
-func AllFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
+
+return h == len(arr)
+
 }
-func AllBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
+
+func BenchmarkAllInt(b *testing.
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,31 +1 @@

-func AllInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
+func AllInt(arr []int, fn func(int) bool) bool { var n int for i, v := range arr { if fn(v) { n++ } } return n == len(arr) } func main() { fmt.Println(AllInt([1, 2, 3], func(a
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,31 +1 @@

-func AllInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
+func AllInt(arr []int, fn func(int) bool) bool { for _, v := range arr { if !fn(v) { return false } } return true } func main() { arr := []int{5, 1, 4, 3, 9} var isEven bool for i, v :=
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,31 +1 @@

-func AllInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
+func AllInt(arr []int, fn func(int) bool) bool { for _, v := range arr { if !fn(v) { return false } } return true } // Output: // false fmt.Println(AllInt([]int{1, 2, 3}, func(x int) bool
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,31 +1 @@

-func AllInt(arr []int, fn func(int) bool) bool {	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllFloat64(arr []float64, fn func(float64) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllBool(arr []bool, fn func(bool) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
-func AllString(arr []string, fn func(string) bool) bool {
-	for _, v := range arr {
-		if !fn(v) {
-			return false
-		}
-	}
-	return true
-}
+func AllInt(arr []int, fn func(int) bool) bool { for _, v := range arr { if !fn(v) { return false } } return true } func main() { var a [10]int a[0] = 1 // Use direct index access. if AllInt(a,
```

### MinOf (task/50)

#### canonical solution

```golang
import "math"

func MinOf(nums ...float64) float64 {
	min := math.Inf(1)
	for _, num := range nums {
		min = math.Min(num, min)
	}
	return min
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,9 +1,14 @@

 import "math"
 
 func MinOf(nums ...float64) float64 {
-	min := math.Inf(1)
-	for _, num := range nums {
-		min = math.Min(num, min)
-	}
-	return min
+
+if len(nums) == 0 {
+
+return 0
+
 }
+
+if len(nums) == 1 {
+
+return nums[0]
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,9 +1,14 @@

 import "math"
 
 func MinOf(nums ...float64) float64 {
-	min := math.Inf(1)
-	for _, num := range nums {
-		min = math.Min(num, min)
-	}
-	return min
+
+return math.Min(nums)
+
 }
+
+func MaxOf(nums ...float64) float64 {
+
+return math.Max(nums)
+
+}
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,9 +1,14 @@

 import "math"
 
 func MinOf(nums ...float64) float64 {
-	min := math.Inf(1)
-	for _, num := range nums {
-		min = math.Min(num, min)
-	}
-	return min
+
+if n := len(nums); n == 0 {
+
+return 0
+
 }
+
+if n > 1 {
+
+for _, num := range nums {
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,9 +1,13 @@

 import "math"
 
 func MinOf(nums ...float64) float64 {
-	min := math.Inf(1)
-	for _, num := range nums {
-		min = math.Min(num, min)
-	}
-	return min
+
+m := new(big.Float).Sub(nums[0], nums[1])
+
+m.Div(nums[0], nums[1])
+
+return m
+
 }
+
+func main()
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,9 +1,14 @@

 import "math"
 
 func MinOf(nums ...float64) float64 {
-	min := math.Inf(1)
-	for _, num := range nums {
-		min = math.Min(num, min)
-	}
-	return min
+
+min := float64(nums[0])
+
+for _, v := range nums[1:] {
+
+if v < min {
+
+min = v
+
 }
+
```

### Includes (task/51)

#### canonical solution

```golang
import "reflect"

func Includes(params ...interface{}) bool {
	arr, v := reflect.ValueOf(params[0]),
		reflect.ValueOf(params[1]).Interface()

	for i := 0; i < arr.Len(); i++ {
		if arr.Index(i).Interface() == v {
			return true
		}
	}
	return false
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,13 +1,17 @@

 import "reflect"
 
 func Includes(params ...interface{}) bool {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return true
-		}
-	}
-	return false
-}
+var isTrue bool
+
+for _, v := range params {
+
+switch v := v.(type) {
+
+case bool:
+
+isTrue = v
+
+case string:
+
+isTrue = v == "
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,13 +1,15 @@

 import "reflect"
 
 func Includes(params ...interface{}) bool {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return true
-		}
-	}
-	return false
+if len(params) == 0 {
+
+return false
+
 }
+
+return reflect.DeepEqual(params, nil)
+
+}
+
+You can check out the awesome documentation for the reflect package to learn more about
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,13 +1,18 @@

 import "reflect"
 
 func Includes(params ...interface{}) bool {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return true
-		}
-	}
-	return false
+var result bool
+
+for _, item := range params {
+
+if item == nil {
+
+continue
+
 }
+
+if !reflect.DeepEqual(item, nil) {
+
+result = false
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,13 +1,18 @@

 import "reflect"
 
 func Includes(params ...interface{}) bool {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return true
-		}
-	}
-	return false
+if len(params) == 0 {
+
+return false
+
 }
+
+for _, value := range params {
+
+switch value.(type) {
+
+case bool:
+
+return value.(bool)
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,13 +1,17 @@

 import "reflect"
 
 func Includes(params ...interface{}) bool {
-	arr, v := reflect.ValueOf(params[0]),
-		reflect.ValueOf(params[1]).Interface()
 
-	for i := 0; i < arr.Len(); i++ {
-		if arr.Index(i).Interface() == v {
-			return true
-		}
-	}
-	return false
-}
+for _, p := range params {
+
+switch v := p.(type) {
+
+case bool:
+
+return v == true
+
+case int:
+
+return v == int(v)
+
+case []int
```

### CelsiusToFahrenheit (task/52)

#### canonical solution

```golang
func CelsiusToFahrenheit(d float64) float64 {
	return 1.8 * d + 32.0
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,2 +1,3 @@

-func CelsiusToFahrenheit(d float64) float64 {	return 1.8 * d + 32.0
-}
+func CelsiusToFahrenheit(d float64) float64 { if d < 0 { // handle negative values } f := (d - 32)/1.8 return f } func main() { fmt.Println(celsiusToFahrenheit(-20)) }
+
+If you look at the
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,2 +1 @@

-func CelsiusToFahrenheit(d float64) float64 {	return 1.8 * d + 32.0
-}
+func CelsiusToFahrenheit(d float64) float64 { return 32.0 * d / (fahrenheit + 273.15) } func main() { celsius := CelsiusToFahrenheit(-40) fahrenheit := CelsiusToFahrenheit(212) fmt.Println(cel
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,2 +1 @@

-func CelsiusToFahrenheit(d float64) float64 {	return 1.8 * d + 32.0
-}
+func CelsiusToFahrenheit(d float64) float64 { return d*9.0/5.0 + 32.0 } func main() { f, _ := tempfile.Open("celsius") // f, _ := tempfile.Open("fahrenheit") t := CelsiusTo
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,2 +1,3 @@

-func CelsiusToFahrenheit(d float64) float64 {	return 1.8 * d + 32.0
-}
+func CelsiusToFahrenheit(d float64) float64 { return math.FToC(d-32)/1.8+32 } func main() { fahrenheit := CelsiusToFahrenheit(58) fmt.Println(fahrenheit) }
+
+ConvertFrom returns the
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,2 +1 @@

-func CelsiusToFahrenheit(d float64) float64 {	return 1.8 * d + 32.0
-}
+func CelsiusToFahrenheit(d float64) float64 { d *= 9.0 / 5.0 + 32.0 } func main() { fahrenheit := CelsiusToFahrenheit(100.0) celsius := CelsiusToCelsius(fahrenheit) fmt.Println(
```

### Degrees (task/53)

#### canonical solution

```golang
import "math"

func Degrees(r float64) float64 {
	return r * 180.0 / math.Pi
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Degrees(r float64) float64 {
-	return r * 180.0 / math.Pi
+
+return r * pi / 180
+
 }
+
+func Radians(r float64) float64 {
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Degrees(r float64) float64 {
-	return r * 180.0 / math.Pi
+
+return r * (180.0 / 3.1415926535897932384626433832795028841971)
+
 }
+
+func Radians(r float64) float64 {
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Degrees(r float64) float64 {
-	return r * 180.0 / math.Pi
+
+return (r * 180.0) / math.Pi
+
 }
+
+func Radians(r float64) float64 {
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Degrees(r float64) float64 {
-	return r * 180.0 / math.Pi
+
+return r * 180 / float64(Pi)
+
 }
+
+func Radians(degrees float64) float64 {
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "math"
 
 func Degrees(r float64) float64 {
-	return r * 180.0 / math.Pi
+
+if r < -180 {
+
+return -180
+
 }
+
```

### IsPalindrome (task/54)

#### canonical solution

```golang
import "strings"

func IsPalindrome(s string) bool {
	v := strings.ToLower(strings.Join(strings.Fields(s), ""))
	for i := range v {
		if v[len(v)-i-1] != v[i] {
			return false
		}
	}
	return true
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,11 +1,9 @@

 import "strings"
 
 func IsPalindrome(s string) bool {
-	v := strings.ToLower(strings.Join(strings.Fields(s), ""))
-	for i := range v {
-		if v[len(v)-i-1] != v[i] {
-			return false
-		}
-	}
-	return true
-}
+
+// maxStringLength is a global variable, so this will cause a
+
+// compile-time error if it isn't defined.
+
+var maxStringLength = len(strings.ToLower(strings.ToUpper(s
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,11 +1,15 @@

 import "strings"
 
 func IsPalindrome(s string) bool {
-	v := strings.ToLower(strings.Join(strings.Fields(s), ""))
-	for i := range v {
-		if v[len(v)-i-1] != v[i] {
-			return false
-		}
-	}
-	return true
+
+for i := 0; i < len(s); i++ {
+
+if s[i] != s[len(s)-i-1] {
+
+return false
+
 }
+
+}
+
+return true
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,11 +1,15 @@

 import "strings"
 
 func IsPalindrome(s string) bool {
-	v := strings.ToLower(strings.Join(strings.Fields(s), ""))
-	for i := range v {
-		if v[len(v)-i-1] != v[i] {
-			return false
-		}
-	}
-	return true
+
+if len(s) < 2 {
+
+return false
+
 }
+
+for i := 0; i < len(s); i++ {
+
+j := i
+
+for j < len(s) && s[
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,11 +1,13 @@

 import "strings"
 
 func IsPalindrome(s string) bool {
-	v := strings.ToLower(strings.Join(strings.Fields(s), ""))
-	for i := range v {
-		if v[len(v)-i-1] != v[i] {
-			return false
-		}
-	}
-	return true
-}
+
+// the string will be in reverse order
+
+// the reverse of a string is obtained by reverse()
+
+// the function Reverse() of the string is
+
+// called with a string to reverse
+
+// the result is a
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,11 +1,13 @@

 import "strings"
 
 func IsPalindrome(s string) bool {
-	v := strings.ToLower(strings.Join(strings.Fields(s), ""))
-	for i := range v {
-		if v[len(v)-i-1] != v[i] {
-			return false
-		}
-	}
-	return true
+
+return len(s) == len(strings.ToLower(s))
+
 }
+
+Foo(func(args ...interface{}) {
+
+if len(args) != 2 {
+
+return fmt.Errorf
```

### Decapitalize (task/55)

#### canonical solution

```golang
import "strings"

func Decapitalize(s string) string {
	return strings.ToLower(s[0:1]) + s[1:]
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,9 @@

 import "strings"
 
 func Decapitalize(s string) string {
-	return strings.ToLower(s[0:1]) + s[1:]
-}
+
+r := strings.Replace(s, "a", "A", -1)
+
+r = strings.Replace(r, "e", "E", -1)
+
+r = strings.Replace(r
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,9 @@

 import "strings"
 
 func Decapitalize(s string) string {
-	return strings.ToLower(s[0:1]) + s[1:]
-}
+
+for i := 0; i < len(s); i++ {
+
+switch s[i] {
+
+case 'C', 'c', 'B', 'b', 'P', 'p', 'H', 'h
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,9 @@

 import "strings"
 
 func Decapitalize(s string) string {
-	return strings.ToLower(s[0:1]) + s[1:]
+
+return strings.ToLower(s)
+
 }
+
+The types.T struct is a struct type but it's also an interface type and a predicate type. The interface is named T and it contains one method named T , which
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,9 @@

 import "strings"
 
 func Decapitalize(s string) string {
-	return strings.ToLower(s[0:1]) + s[1:]
+
+return strings.ToLower(strings.Replace(s, " ", "_", -1))
+
 }
+
+The imported "strings" package provides the Replace function that replaces all occurrences of a string with another. The -1
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "strings"
 
 func Decapitalize(s string) string {
-	return strings.ToLower(s[0:1]) + s[1:]
+
+if !unicode.IsLetter(s[0]) {
+
+return s
+
 }
+
```

### MapNumRange (task/56)

#### canonical solution

```golang
func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
	return ((num-iMin)*(oMax-oMin))/(iMax-iMin) + oMin
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,2 +1 @@

-func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {	return ((num-iMin)*(oMax-oMin))/(iMax-iMin) + oMin
-}
+func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 { var ( o float64 iMax, iMin = float64(1e6), num = float64(num) ) for iMin <= iMax { if iMin <= iMax && iMin < num { iMin++ } if
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,3 +1,8 @@

 func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
-	return ((num-iMin)*(oMax-oMin))/(iMax-iMin) + oMin
-}
+
+2654 if num < iMin {
+
+2655 panic("MapNumRange: index out of range")
+
+2656 }
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,3 +1,8 @@

 func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
-	return ((num-iMin)*(oMax-oMin))/(iMax-iMin) + oMin
-}
+
+m, err := strconv.ParseFloat(num, 'f', 0)
+
+if err != nil {
+
+return 0
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,3 +1,3 @@

 func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
-	return ((num-iMin)*(oMax-oMin))/(iMax-iMin) + oMin
-}
+
+return (float64(num) - float64(iMin)) / (float64(iMax) - float64(iMin)) * (float64(oMin) - float64(oMax)) + float64(
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,2 +1 @@

-func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {	return ((num-iMin)*(oMax-oMin))/(iMax-iMin) + oMin
-}
+func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 { iMin, iMax = clamp(iMin, 0, math.MaxInt64) iMax, oMin = clamp(oMin, 0, math.MaxInt64) if iMin < iMax { return num + math.
```

### Stringify (task/57)

#### canonical solution

```golang
import "fmt"

func Stringify(v interface{}) string {
	return fmt.Sprintf("%v", v)
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,5 +1,10 @@

 import "fmt"
 
 func Stringify(v interface{}) string {
-	return fmt.Sprintf("%v", v)
+
+if v == nil {
+
+return "nil"
+
 }
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,5 +1,10 @@

 import "fmt"
 
 func Stringify(v interface{}) string {
-	return fmt.Sprintf("%v", v)
-}
+
+switch t := v.(type) {
+
+case *[]byte:
+
+if len(t) == 0 {
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,5 +1,10 @@

 import "fmt"
 
 func Stringify(v interface{}) string {
-	return fmt.Sprintf("%v", v)
-}
+
+if reflect.TypeOf(v).Kind() == reflect.Ptr {
+
+if v.IsNil() {
+
+return "<nil>"
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,5 +1,10 @@

 import "fmt"
 
 func Stringify(v interface{}) string {
-	return fmt.Sprintf("%v", v)
-}
+
+switch v := v.(type) {
+
+case nil:
+
+return "nil"
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,5 +1,10 @@

 import "fmt"
 
 func Stringify(v interface{}) string {
-	return fmt.Sprintf("%v", v)
-}
+
+switch t := v.(type) {
+
+case int:
+
+s := fmt.Sprintf("%d", t)
+
```

### MaxOf (task/58)

#### canonical solution

```golang
import "math"

func MaxOf(nums ...float64) float64 {
	max := math.Inf(-1)
	for _, num := range nums {
		max = math.Max(num, max)
	}
	return max
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,9 +1,14 @@

 import "math"
 
 func MaxOf(nums ...float64) float64 {
-	max := math.Inf(-1)
-	for _, num := range nums {
-		max = math.Max(num, max)
-	}
-	return max
+
+if len(nums) == 0 {
+
+return math.Inf(1)
+
 }
+
+max := nums[0]
+
+for _, v := range nums[1:] {
+
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,9 +1,14 @@

 import "math"
 
 func MaxOf(nums ...float64) float64 {
-	max := math.Inf(-1)
-	for _, num := range nums {
-		max = math.Max(num, max)
-	}
-	return max
+
+max := nums[0]
+
+for _, v := range nums[1:] {
+
+if v > max {
+
+max = v
+
 }
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,9 +1,14 @@

 import "math"
 
 func MaxOf(nums ...float64) float64 {
-	max := math.Inf(-1)
-	for _, num := range nums {
-		max = math.Max(num, max)
-	}
-	return max
+
+var max float64
+
+for _, v := range nums {
+
+if v > max {
+
+max = v
+
 }
+
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,9 +1,14 @@

 import "math"
 
 func MaxOf(nums ...float64) float64 {
-	max := math.Inf(-1)
-	for _, num := range nums {
-		max = math.Max(num, max)
-	}
-	return max
+
+max := nums[0]
+
+for _, x := range nums[1:] {
+
+if x > max {
+
+max = x
+
 }
+
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,9 +1,14 @@

 import "math"
 
 func MaxOf(nums ...float64) float64 {
-	max := math.Inf(-1)
-	for _, num := range nums {
-		max = math.Max(num, max)
-	}
-	return max
+
+var max float64
+
+for _, x := range nums {
+
+if x > max {
+
+max = x
+
 }
+
```

### GCD (task/59)

#### canonical solution

```golang
func gcd(x, y int) int {
	if y == 0 {
		return x
	}
	return gcd(y, x%y)
}

func GCD(nums ...int) int {
	r := nums[0]
	for _, num := range nums[1:] {
		r = gcd(r, num)
	}
	return r
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,14 +1,17 @@

 func gcd(x, y int) int {
-	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
+
+if y == 0 {
+
+return x
+
 }
 
-func GCD(nums ...int) int {
-	r := nums[0]
-	for _, num := range nums[1:] {
-		r = gcd(r, num)
-	}
-	return r
+return gcd(y, x%y)
+
 }
+
+var zero = NewInt(0)
+
+func main() {
+
+fmt.
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,14 +1,19 @@

 func gcd(x, y int) int {
-	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
+
+for y != 0 {
+
+x, y = y, x%y
+
 }
 
-func GCD(nums ...int) int {
-	r := nums[0]
-	for _, num := range nums[1:] {
-		r = gcd(r, num)
-	}
-	return r
+return x
+
 }
+
+Sample usage:
+
+package main
+
+
+
+import "fmt"
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,14 +1,19 @@

 func gcd(x, y int) int {
-	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
+
+for y != 0 {
+
+x, y = y, x%y
+
 }
 
-func GCD(nums ...int) int {
-	r := nums[0]
-	for _, num := range nums[1:] {
-		r = gcd(r, num)
-	}
-	return r
+return x
+
 }
+
+package main
+
+
+
+import (
+
+"fmt"
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,14 +1,19 @@

 func gcd(x, y int) int {
-	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
+
+for y != 0 {
+
+t := y
+
+y = x % y
+
+x = t
+
 }
 
-func GCD(nums ...int) int {
-	r := nums[0]
-	for _, num := range nums[1:] {
-		r = gcd(r, num)
-	}
-	return r
+return x
+
 }
+
+```
+
+```go
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,14 +1,9 @@

 func gcd(x, y int) int {
-	if y == 0 {
-		return x
-	}
-	return gcd(y, x%y)
+
+return x - y * int(x/y)
+
 }
 
-func GCD(nums ...int) int {
-	r := nums[0]
-	for _, num := range nums[1:] {
-		r = gcd(r, num)
-	}
-	return r
-}
+for i := n; i > 0; i-- {
+
+fmt.Printf("%d: %d\n", i, gcd
```

### Dedupe (task/60)

#### canonical solution

```golang
func DedupeInts(arr []int) []int {
	m, uniq := make(map[int]bool), make([]int, 0)
	for _, v := range arr {
		if _, ok := m[v]; !ok {
			m[v], uniq = true, append(uniq, v)
		}
	}
	return uniq
}
func DedupeFloat64s(arr []float64) []float64 {
	m, uniq := make(map[float64]bool), make([]float64, 0)
	for _, v := range arr {
		if _, ok := m[v]; !ok {
			m[v], uniq = true, append(uniq, v)
		}
	}
	return uniq
}
func DedupeStrings(arr []string) []string {
	m, uniq := make(map[string]bool), make([]string, 0)
	for _, v := range arr {
		if _, ok := m[v]; !ok {
			m[v], uniq = true, append(uniq, v)
		}
	}
	return uniq
}
```

#### solution 0

```diff
--- canonical..go

+++ solution0..go

@@ -1,27 +1,13 @@

 func DedupeInts(arr []int) []int {
-	m, uniq := make(map[int]bool), make([]int, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
+
+l := len(arr)
+
+if l < 2 {
+
+return arr
+
 }
-func DedupeFloat64s(arr []float64) []float64 {
-	m, uniq := make(map[float64]bool), make([]float64, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
-}
-func DedupeStrings(arr []string) []string {
-	m, uniq := make(map[string]bool), make([]string, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
-}
+
+copy(arr, arr[0:l/2])
+
+for i := l - 1; i >= 2; i
```

#### solution 1

```diff
--- canonical..go

+++ solution1..go

@@ -1,27 +1,18 @@

 func DedupeInts(arr []int) []int {
-	m, uniq := make(map[int]bool), make([]int, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
+
+for _, x := range arr {
+
+if len(x) == 1 {
+
+arr[0] = x[0]
+
+return arr
+
 }
-func DedupeFloat64s(arr []float64) []float64 {
-	m, uniq := make(map[float64]bool), make([]float64, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
+
 }
-func DedupeStrings(arr []string) []string {
-	m, uniq := make(map[string]bool), make([]string, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
+
+return arr
+
 }
+
```

#### solution 2

```diff
--- canonical..go

+++ solution2..go

@@ -1,27 +1,15 @@

 func DedupeInts(arr []int) []int {
-	m, uniq := make(map[int]bool), make([]int, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
+
+deDup := make([]int, len(arr))
+
+for i, x := range arr {
+
+deDup[i] = x
+
 }
-func DedupeFloat64s(arr []float64) []float64 {
-	m, uniq := make(map[float64]bool), make([]float64, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
+
+return deDup
+
 }
-func DedupeStrings(arr []string) []string {
-	m, uniq := make(map[string]bool), make([]string, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
-}
+
+func
```

#### solution 3

```diff
--- canonical..go

+++ solution3..go

@@ -1,27 +1,9 @@

 func DedupeInts(arr []int) []int {
-	m, uniq := make(map[int]bool), make([]int, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
+
+return append([]int{}, DedupeInts(arr[1:])...)
+
 }
-func DedupeFloat64s(arr []float64) []float64 {
-	m, uniq := make(map[float64]bool), make([]float64, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
-}
-func DedupeStrings(arr []string) []string {
-	m, uniq := make(map[string]bool), make([]string, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
-}
+
+func main() {
+
+fmt.Println(DedupeInts([1, 2, 3,
```

#### solution 4

```diff
--- canonical..go

+++ solution4..go

@@ -1,27 +1,15 @@

 func DedupeInts(arr []int) []int {
-	m, uniq := make(map[int]bool), make([]int, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
+
+a := make([]int, len(arr))
+
+for i, v := range arr {
+
+a[i] = v
+
 }
-func DedupeFloat64s(arr []float64) []float64 {
-	m, uniq := make(map[float64]bool), make([]float64, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
+
+return a
+
 }
-func DedupeStrings(arr []string) []string {
-	m, uniq := make(map[string]bool), make([]string, 0)
-	for _, v := range arr {
-		if _, ok := m[v]; !ok {
-			m[v], uniq = true, append(uniq, v)
-		}
-	}
-	return uniq
-}
+
+// Case 2: Slices
```

