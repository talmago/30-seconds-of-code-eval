#### PadRight (task/1)

```diff
-import "fmt"
-
-func PadRight(s string, l int) string {
+import "fmt"
+
+func PadRight(s string, l int) string {
+
+    s = s[:len(s)-l]
+    return s
+    }
+    func main() {
+    fmt.Println(PadRight("12345", 3))
+    fmt.Println(
```

#### PadRight (task/1)

```diff
-import "fmt"
-
-func PadRight(s string, l int) string {
+import "fmt"
+
+func PadRight(s string, l int) string {
+
+    r := make([]byte, len(s)+l)
+    copy(r, s)
+    return string(r)
+    }
+    func main() {
+    fmt.Println(PadRight("
```

#### PadRight (task/1)

```diff
-import "fmt"
-
-func PadRight(s string, l int) string {
+import "fmt"
+
+func PadRight(s string, l int) string {
+
+    for i := len(s) - l; i >= 0; i-- {
+    s = s[:i] + " "
+    }
+    return s
+    }
+    func Equal(a, b string
```

#### PadRight (task/1)

```diff
-import "fmt"
-
-func PadRight(s string, l int) string {
+import "fmt"
+
+func PadRight(s string, l int) string {
+
+    return strings.Repeat(" ", l - len(s)) + s
+    }
+    func main() {
+    s := "Foo"
+    s = PadRight(s, 32)
+    fmt.Print
```

#### PadRight (task/1)

```diff
-import "fmt"
-
-func PadRight(s string, l int) string {
+import "fmt"
+
+func PadRight(s string, l int) string {
+
+    return s[:l] + string(padLeft(s, l, ' '))
+    }
+    func padLeft(s string, l int, pad string) string {
+    return s[:l] +
```

#### Median (task/2)

```diff
-import (
+import (
+ "math" "sort" "strings" "unicode" ) // A BDD represents a set of boolean values. type BDD map[string]bool // BDDs are designed to be compared in the same way that sets are,
```

#### Median (task/2)

```diff
-import (
+import (
+ "errors" "fmt" "io" "net/http" "net/url" "strings" ) func main() { var client = &http.Client{} client.Get( "https://httpbin.org/get
```

#### Median (task/2)

```diff
-import (
+import (
+ ' twitter ' ) # Let's create a Twitter App (NOT necessary) app = Twitter( app_key = ' ' , app_secret = ' ' , api_key = ' ' , api_secret = ' ' ) # Let's
```

#### Median (task/2)

```diff
-import (
+import (
+ "errors" "fmt" "runtime" "sync" "time" ) var mu sync.Mutex // Mutex to synchronize writes to global deadlines var nanotime = runtime.Now().UnixNano() // deadline returns the
```

#### Median (task/2)

```diff
-import (
+import (
+ "fmt" ) func main() { var b [10]int a := make([]int, 3) for i := range a { a[i] = i } fmt.Println(len(a)) fmt.Println
```

#### RandIntSliceInRange (task/3)

```diff
-import "math/rand"
-
-func RandIntSliceInRange(min, max, n int) []int {
+import "math/rand"
+
+func RandIntSliceInRange(min, max, n int) []int {
+
+    // rand.Intn is not parallel safe; see issue 8774.
+    // Use this implementation to guarantee sequential consistency.
+    // The number of returned ints might be smaller than n.
+    // See the Go 1
```

#### RandIntSliceInRange (task/3)

```diff
-import "math/rand"
-
-func RandIntSliceInRange(min, max, n int) []int {
+import "math/rand"
+
+func RandIntSliceInRange(min, max, n int) []int {
+
+    r := rand.New(rand.NewSource(time.Now().UnixNano()))
+    return r.Intn(n)
+    }
+    package main
+    
+    import (
+    "fmt"
```

#### RandIntSliceInRange (task/3)

```diff
-import "math/rand"
-
-func RandIntSliceInRange(min, max, n int) []int {
+import "math/rand"
+
+func RandIntSliceInRange(min, max, n int) []int {
+
+    // the closed interval [min, max] contains at least n+1 values
+    // so we can generate a random integer in this range at least
+    // n times.
+    //
+    // The algorithm is as follows
```

#### RandIntSliceInRange (task/3)

```diff
-import "math/rand"
-
-func RandIntSliceInRange(min, max, n int) []int {
+import "math/rand"
+
+func RandIntSliceInRange(min, max, n int) []int {
+
+    return make([]int, n)
+    for i := min; i < max; i++ {
+    n--
+    n*=10
+    n+=i
+    }
+    return
+    }
```

#### RandIntSliceInRange (task/3)

```diff
-import "math/rand"
-
-func RandIntSliceInRange(min, max, n int) []int {
+import "math/rand"
+
+func RandIntSliceInRange(min, max, n int) []int {
+
+    return RandInts(uint(min), uint(max), n)
+    }
+    func RandUintSliceInRange(min, max uint, n int) []uint {
+    return RandUints(uint
```

#### ToSnake (task/4)

```diff
-import "strings"
-
-func ToSnake(s string) string {
+import "strings"
+
+func ToSnake(s string) string {
+
+    return strings.ToLower(strings.Replace(s, " ", "_"))
+    }
+    func main() {
+    fmt.Println(ToSnake("Hello World"))
+    }
+    Translation of:
```

#### ToSnake (task/4)

```diff
-import "strings"
-
-func ToSnake(s string) string {
+import "strings"
+
+func ToSnake(s string) string {
+
+    return strings.ToSnakeCase(s)
+    }
+    The most common use of these functions is when working with the arguments to a function or a method.
+    func Add(left, right int) int {
```

#### ToSnake (task/4)

```diff
-import "strings"
-
-func ToSnake(s string) string {
+import "strings"
+
+func ToSnake(s string) string {
+
+    return strings.ToSnakeCase(s)
+    }
+    case is Snake
+    // "snakecase" or "snake_case"
+    // ToSnakeCase is a snake-case conversion function.
```

#### ToSnake (task/4)

```diff
-import "strings"
-
-func ToSnake(s string) string {
+import "strings"
+
+func ToSnake(s string) string {
+
+    sp := strings.Split(s, " ")
+    for i := len(sp) - 1; i >= 0; i-- {
+    if sp[i] == "," {
+    return sp[i+
```

#### ToSnake (task/4)

```diff
-import "strings"
-
-func ToSnake(s string) string {
+import "strings"
+
+func ToSnake(s string) string {
+
+    if s == "" {
+    return ""
+    }
+    last := "^"
+    for i := 0; i < len(s); i++ {
+    c := s[i]
+    if c ==
```

#### Filter (task/5)

```diff
-func FilterInt(arr []int, f func(int) bool) []int {
+func FilterInt(arr []int, f func(int) bool) []int {
+
+    out := make([]int, len(arr))
+    for i, v := range arr {
+    if f(v) {
+    out[i] = v
+    }
+    }
+    return out
```

#### Filter (task/5)

```diff
-func FilterInt(arr []int, f func(int) bool) []int {
+func FilterInt(arr []int, f func(int) bool) []int {
+
+    var result []int
+    for _, i := range arr {
+    if f(i) {
+    result = append(result, i)
+    }
+    }
+    return result
+    }
+    func
```

#### Filter (task/5)

```diff
-func FilterInt(arr []int, f func(int) bool) []int {
+func FilterInt(arr []int, f func(int) bool) []int {
+ // f returns true for ints less than 'a' for i, _ := range arr { if f(i) { return append(arr[0:i], filterInt(arr[i+1:], f)) } } return
```

#### Filter (task/5)

```diff
-func FilterInt(arr []int, f func(int) bool) []int {
+func FilterInt(arr []int, f func(int) bool) []int {
+
+    for _, x := range arr {
+    if f(x) {
+    return append(arr, x)
+    }
+    }
+    return arr
+    }
+    func TestFilterInt(t *testing
```

#### Filter (task/5)

```diff
-func FilterInt(arr []int, f func(int) bool) []int {
+func FilterInt(arr []int, f func(int) bool) []int {
+
+    return sort.Ints(sort.Reverse(sort.IntSlice(arr)))
+    }
+    fmt.Println(FilterInt(fmt.Sprint([]int{5, 6, 7
```

#### Find (task/6)

```diff
-import "fmt"
-
-func FindInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindInt(arr []int, f func(int) bool) (int, error) {
+
+    for i, v := range arr {
+    if f(v) {
+    return i, nil
+    }
+    }
+    return -1, fmt.Errorf("Failed to find integer: %v",
```

#### Find (task/6)

```diff
-import "fmt"
-
-func FindInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindInt(arr []int, f func(int) bool) (int, error) {
+
+    for i, v := range arr {
+    if f(v) {
+    return i, nil
+    }
+    }
+    return -1, fmt.Errorf("no such element: %v", arr)
```

#### Find (task/6)

```diff
-import "fmt"
-
-func FindInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindInt(arr []int, f func(int) bool) (int, error) {
+
+    for i, x := range arr {
+    if f(x) {
+    return i, nil
+    }
+    }
+    return -1, errors.New("Not found")
+    }
+    package main
```

#### Find (task/6)

```diff
-import "fmt"
-
-func FindInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindInt(arr []int, f func(int) bool) (int, error) {
+
+    for i, v := range arr {
+    if f(v) {
+    return i, nil
+    }
+    }
+    return -1, fmt.Errorf("can't find %v", f)
```

#### Find (task/6)

```diff
-import "fmt"
-
-func FindInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindInt(arr []int, f func(int) bool) (int, error) {
+
+    for i, v := range arr {
+    if f(v) {
+    return i, nil
+    }
+    }
+    return -1, fmt.Errorf("FindInt: not found")
+    }
```

#### LCM (task/7)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+
+    if y == 0 {
+    return x
+    }
+    return gcd(y, x%y)
+    }
+    Use in Go:
+    package main
+    
+    import "fmt"
```

#### LCM (task/7)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+
+    if y == 0 {
+    return x
+    }
+    return gcd(y, x%y)
+    }
+    “But,” you protest, “then the compiler won’t be
```

#### LCM (task/7)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+
+    if y == 0 {
+    return x
+    }
+    return gcd(y, x%y)
+    }
+    The output is:
+    Enter two positive integers > 15 11 > x=15 > y
```

#### LCM (task/7)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+
+    for x != y {
+    for x > y {
+    y, x = x, y
+    }
+    }
+    return x
+    }
+    func main() {
+    for _, n := range
```

#### LCM (task/7)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+ if y == 0 { return x } return gcd(y, x%y) }
+    Make sure you understand how this works, and that it doesn’t work for negative numbers. If you’re curious, the reason
```

#### Clamp (task/8)

```diff
-import "math"
-
-func Clamp(n, a, b float64) float64 {
+import "math"
+
+func Clamp(n, a, b float64) float64 {
+
+    return math.MaxFloat64 < a && a < math.MinFloat64 ? a : b
+    }
+    const (
+    minCubicEval = 1e3
+    maxCubicEval = 1e
```

#### Clamp (task/8)

```diff
-import "math"
-
-func Clamp(n, a, b float64) float64 {
+import "math"
+
+func Clamp(n, a, b float64) float64 {
+
+    if n < a {
+    return a
+    }
+    if n > b {
+    return b
+    }
+    return n
+    }
+    func main() {
+    fmt.Println(Cl
```

#### Clamp (task/8)

```diff
-import "math"
-
-func Clamp(n, a, b float64) float64 {
+import "math"
+
+func Clamp(n, a, b float64) float64 {
+
+    if n < a {
+    return a
+    }
+    if n > b {
+    return b
+    }
+    return n
+    }
+    }
+    func main() {
+    d := []float
```

#### Clamp (task/8)

```diff
-import "math"
-
-func Clamp(n, a, b float64) float64 {
+import "math"
+
+func Clamp(n, a, b float64) float64 {
+ if n < a { n = a } if n > b { n = b } return n }
+    func main() { var s, c = 100, 20000 s = -c / 2 / 2 * (1 - 1 /
```

#### Clamp (task/8)

```diff
-import "math"
-
-func Clamp(n, a, b float64) float64 {
+import "math"
+
+func Clamp(n, a, b float64) float64 {
+
+    if n < a {
+    return a
+    }
+    if n > b {
+    return b
+    }
+    return n
+    }
+    type Matrix struct {
+    M *Matrix
+    Rows
```

#### Zip (task/9)

```diff
-import "reflect"
-
-func Zip(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func Zip(params ...interface{}) [][]interface{} {
+
+    if len(params) == 0 {
+    return make([][]interface{}, 0)
+    }
+    // TODO: Handle errors in params
+    var sizes = make([]int, 0, len(params
```

#### Zip (task/9)

```diff
-import "reflect"
-
-func Zip(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func Zip(params ...interface{}) [][]interface{} {
+
+    switch len(params) {
+    case 0:
+    return nil
+    case 1:
+    return params[0]
+    default:
+    for i, v := range params {
+    if i > 0 {
```

#### Zip (task/9)

```diff
-import "reflect"
-
-func Zip(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func Zip(params ...interface{}) [][]interface{} {
+
+    res := make([][]interface{}, 0)
+    for i, s := range params {
+    v := reflect.ValueOf(s)
+    if len(v.Kind() & reflect.SliceKind)
```

#### Zip (task/9)

```diff
-import "reflect"
-
-func Zip(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func Zip(params ...interface{}) [][]interface{} {
+
+    return New(nil).Call(params).Interface()
+    }
+    // Example usage:
+    // params := []string{"http://www.google.com", "http://www.yahoo.com"}
+    //
```

#### Zip (task/9)

```diff
-import "reflect"
-
-func Zip(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func Zip(params ...interface{}) [][]interface{} {
+
+    // Zip the parameters
+    m := make([]interface{}, len(params))
+    for i, n := range params {
+    m[i] = params[n]
+    }
+    return m
```

#### PadLeft (task/10)

```diff
-import "fmt"
-
-func PadLeft(s string, l int) string {
+import "fmt"
+
+func PadLeft(s string, l int) string {
+
+    return fmt.Sprintf("%s%d", s, l)
+    }
+    func main() {
+    var s = "Hello World"
+    fmt.Println(PadLeft(s, 12))
```

#### PadLeft (task/10)

```diff
-import "fmt"
-
-func PadLeft(s string, l int) string {
+import "fmt"
+
+func PadLeft(s string, l int) string {
+
+    return string(s[:l])
+    }
+    func PadRight(s string, l int) string {
+    return string(s[l:])
+    }
+    type value struct {
+    f float
```

#### PadLeft (task/10)

```diff
-import "fmt"
-
-func PadLeft(s string, l int) string {
+import "fmt"
+
+func PadLeft(s string, l int) string {
+
+    return s[:l]
+    }
+    func main() {
+    fmt.Println(PadLeft("A", 1))
+    fmt.Println(PadLeft("A", 5))
+    f
```

#### PadLeft (task/10)

```diff
-import "fmt"
-
-func PadLeft(s string, l int) string {
+import "fmt"
+
+func PadLeft(s string, l int) string {
+
+    if l < len(s) {
+    return string(s[:l]) + " "
+    }
+    return s
+    }
+    func main() {
+    fmt.Println(PadLeft("
```

#### PadLeft (task/10)

```diff
-import "fmt"
-
-func PadLeft(s string, l int) string {
+import "fmt"
+
+func PadLeft(s string, l int) string {
+
+    return string(l*s)
+    }
+    func main() {
+    var s = "ABCD"
+    fmt.Println(s.PadLeft(10, '.'))
+    }
```

#### Map (task/11)

```diff
-func MapInt(arr []int, fn func(int) int) []int {
+func MapInt(arr []int, fn func(int) int) []int {
+
+    m := make(map[int]int)
+    for _, v := range arr {
+    m[v] = fn(v)
+    }
+    return m
+    }
+    Within a goroutine,
```

#### Map (task/11)

```diff
-func MapInt(arr []int, fn func(int) int) []int {
+func MapInt(arr []int, fn func(int) int) []int {
+ m := make(map[int]int) for i, v := range arr { m[v] = fn(v) } return m } func main() { arr := []int{1, 2, 3} m := MapInt
```

#### Map (task/11)

```diff
-func MapInt(arr []int, fn func(int) int) []int {
+func MapInt(arr []int, fn func(int) int) []int {
+
+    t := make([]int, len(arr))
+    for i, v := range arr {
+    t[i] = fn(v)
+    }
+    return t
+    }
+    func main() {
```

#### Map (task/11)

```diff
-func MapInt(arr []int, fn func(int) int) []int {
+func MapInt(arr []int, fn func(int) int) []int {
+ m := make(map[int]int) for i, v := range arr { m[v] = fn(v) } return m } func main() { var values []int = []int{0, 1, 2, 3
```

#### Map (task/11)

```diff
-func MapInt(arr []int, fn func(int) int) []int {
+func MapInt(arr []int, fn func(int) int) []int {
+
+    result := make([]int, len(arr))
+    for i, v := range arr {
+    result[i] = fn(v)
+    }
+    return result
+    }
+    MapInt is a
```

#### CompactWhiteSpace (task/12)

```diff
-import "regexp"
-
-func CompactWhiteSpace(str string) string {
+import "regexp"
+
+func CompactWhiteSpace(str string) string {
+
+    return strings.TrimSuffix(strings.TrimSpace(str), """)
+    }
+    Please, feel free to use these functions in your project.
+    Happy New Year!
```

#### CompactWhiteSpace (task/12)

```diff
-import "regexp"
-
-func CompactWhiteSpace(str string) string {
+import "regexp"
+
+func CompactWhiteSpace(str string) string {
+
+    return rxSpaceSpaces.FindStringSubmatch(str)
+    }
+    func TrimWhiteSpace(str string) string {
+    return TrimSpace(CompactWhiteSpace(str))
+    }
```

#### CompactWhiteSpace (task/12)

```diff
-import "regexp"
-
-func CompactWhiteSpace(str string) string {
+import "regexp"
+
+func CompactWhiteSpace(str string) string {
+
+    return strings.Replace(str, " ", "", -1)
+    }
+    The CompactWhiteSpace function takes a string as input and replaces all whitespace characters with a single space. The regexp.Replace function
```

#### CompactWhiteSpace (task/12)

```diff
-import "regexp"
-
-func CompactWhiteSpace(str string) string {
+import "regexp"
+
+func CompactWhiteSpace(str string) string {
+
+    str = strings.Replace(str, "
+    ", " ", -1)
+    str = strings.Replace(str, "\r", " ", -1)
+    str = strings.Replace(str,
```

#### CompactWhiteSpace (task/12)

```diff
-import "regexp"
-
-func CompactWhiteSpace(str string) string {
+import "regexp"
+
+func CompactWhiteSpace(str string) string {
+
+    return strings.Replace(str, " ", "", -1)
+    }
+    Here are two examples of how to use the CompactWhiteSpace function.
+    fmt.Println(CompactWhiteSpace("Hello
```

#### IsPowerOf2 (task/13)

```diff
-func IsPowerOf2(n int) bool {
+func IsPowerOf2(n int) bool {
+
+    for _, m := range [1 << iota]n {
+    return n&m == m
+    }
+    return false
+    }
+    func isOdd(n int) bool {
+    return n
```

#### IsPowerOf2 (task/13)

```diff
-func IsPowerOf2(n int) bool {
+func IsPowerOf2(n int) bool {
+
+    for i := 0; i < n; i++ {
+    switch n & 1 {
+    case 1:
+    return false
+    }
+    }
+    return true
+    }
+    // IsBigPowerOf
```

#### IsPowerOf2 (task/13)

```diff
-func IsPowerOf2(n int) bool {
+func IsPowerOf2(n int) bool {
+
+    return n%2 == 0
+    }
+    func IsEven(n int) bool {
+    return n%2 == 0
+    }
+    func IsMultipleOf3(n int) bool {
+    return n
```

#### IsPowerOf2 (task/13)

```diff
-func IsPowerOf2(n int) bool {
+func IsPowerOf2(n int) bool {
+
+    return n%2 == 0
+    }
+    // IsPowerOf2 reports whether n is a power of 2.
+    func main() {
+    fmt.Println(IsPowerOf2(2))
```

#### IsPowerOf2 (task/13)

```diff
-func IsPowerOf2(n int) bool {
+func IsPowerOf2(n int) bool {
+
+    return n&(n-1) == 0
+    }
+    func Filter(n int, f func(int) bool) int {
+    for i := 0; i < n; i++ {
+    if f
```

#### Capitalize (task/14)

```diff
-import "strings"
-
-func Capitalize(s string) string {
+import "strings"
+
+func Capitalize(s string) string {
+
+    return strings.ToUpper(s)
+    }
+    Output:
```

#### Capitalize (task/14)

```diff
-import "strings"
-
-func Capitalize(s string) string {
+import "strings"
+
+func Capitalize(s string) string {
+
+    for i := 0; i < len(s); i++ {
+    s[i] = strings.ToUpper(s[i])
+    }
+    return s
+    }
+    That’s it
```

#### Capitalize (task/14)

```diff
-import "strings"
-
-func Capitalize(s string) string {
+import "strings"
+
+func Capitalize(s string) string {
+
+    return strings.ToUpper(s)
+    }
+    func main() {
+    // Local variables:
+    var s string = "Hello, world!"
+    fmt.Println(Capitalize(s))
```

#### Capitalize (task/14)

```diff
-import "strings"
-
-func Capitalize(s string) string {
+import "strings"
+
+func Capitalize(s string) string {
+
+    if len(s) == 0 {
+    return ""
+    }
+    for i := 0; i < len(s); i++ {
+    if s[i] < 'a' || s[i] >
```

#### Capitalize (task/14)

```diff
-import "strings"
-
-func Capitalize(s string) string {
+import "strings"
+
+func Capitalize(s string) string {
+
+    return strings.ToUpper(s)
+    }
+    func main() {
+    fmt.Println(Capitalize("now"))
+    }
+    Output:
+    NOW
+    The top-level name
```

#### TruncateString (task/15)

```diff
-func TruncateString(s string, l int) string {
+func TruncateString(s string, l int) string {
+
+    if l <= 0 {
+    return s
+    }
+    return s[:l]
+    }
+    func Truncate(s, l int) string {
+    return TruncateString(s, l
```

#### TruncateString (task/15)

```diff
-func TruncateString(s string, l int) string {
+func TruncateString(s string, l int) string {
+
+    if l < 0 {
+    l = len(s)
+    }
+    r := make([]byte, 0, l)
+    for i := 0; i < l; i++ {
+    r = append
```

#### TruncateString (task/15)

```diff
-func TruncateString(s string, l int) string {
+func TruncateString(s string, l int) string {
+
+    if l <= 0 {
+    return s
+    }
+    r := make([]byte, 0, l)
+    n := copy(r, s)
+    r = r[n:]
+    return string(
```

#### TruncateString (task/15)

```diff
-func TruncateString(s string, l int) string {
+func TruncateString(s string, l int) string {
+
+    return string(s[:l])
+    }
+    func TruncateStringBySpace(s string, l int) string {
+    return string(s[:l])
+    }
+    func Truncate
```

#### TruncateString (task/15)

```diff
-func TruncateString(s string, l int) string {
+func TruncateString(s string, l int) string {
+
+    return strconv.FormatInt(strconv.Itoa(int(l)), 10) + s
+    }
+    func main() {
+    fmt.Println(TruncateString("An example string", 7
```

#### IntRange (task/16)

```diff
-func IntRange(f, t, s int) []int {
+func IntRange(f, t, s int) []int {
+ a := make([]int, 0, s) for i := f; i < t; i++ { a = append(a, i) } return a }
+    We've now reduced the maximum runtime to O(f).
```

#### IntRange (task/16)

```diff
-func IntRange(f, t, s int) []int {
+func IntRange(f, t, s int) []int {
+
+    if f < t {
+    return []int{f}
+    }
+    if f == t {
+    return []int{t}
+    }
+    return []int{f, t}
+    }
```

#### IntRange (task/16)

```diff
-func IntRange(f, t, s int) []int {
+func IntRange(f, t, s int) []int {
+ return nil } const ( LowestBits = int((1<<63)-1) MaxVal = 1<<(63-1) ) // Wrap an int64 as a *big.Int func Size(x int64) *big.
```

#### IntRange (task/16)

```diff
-func IntRange(f, t, s int) []int {
+func IntRange(f, t, s int) []int {
+
+    r := make([]int, 0, len(t))
+    for i := t; i < s; i++ {
+    r = append(r, f(i))
+    }
+    return r
```

#### IntRange (task/16)

```diff
-func IntRange(f, t, s int) []int {
+func IntRange(f, t, s int) []int {
+ + for i := t; i < s; i++ { + r := f(i) + r2 := r + if r2 > i { + r2 = i + } + if r2 < t { + r2 =
```

#### IsInRange (task/17)

```diff
-import "math"
-
-func IsInRange(n, a, b float64) bool {
+import "math"
+
+func IsInRange(n, a, b float64) bool {
+
+    return n >= a && n <= b
+    }
+    // Euclidean distance between two points
+    func Dist(p, q Point) float64 {
+    d := p.x - q.x
+    d
```

#### IsInRange (task/17)

```diff
-import "math"
-
-func IsInRange(n, a, b float64) bool {
+import "math"
+
+func IsInRange(n, a, b float64) bool {
+
+    return n >= a && n <= b
+    }
+    func constApprox(n, a, b float64) float64 {
+    if IsInRange(n, a, b) {
+    return n
```

#### IsInRange (task/17)

```diff
-import "math"
-
-func IsInRange(n, a, b float64) bool {
+import "math"
+
+func IsInRange(n, a, b float64) bool {
+
+    if a < b {
+    return false
+    }
+    if a > b {
+    return true
+    }
+    if n < a {
+    return false
+    }
+    if n > b {
```

#### IsInRange (task/17)

```diff
-import "math"
-
-func IsInRange(n, a, b float64) bool {
+import "math"
+
+func IsInRange(n, a, b float64) bool {
+
+    return n > a && n < b
+    }
+    func main() {
+    for i := 0; i < 3; i++ {
+    if IsInRange(i, 0, 1) {
+    f
```

#### IsInRange (task/17)

```diff
-import "math"
-
-func IsInRange(n, a, b float64) bool {
+import "math"
+
+func IsInRange(n, a, b float64) bool {
+
+    if n < a || n > b {
+    return false
+    }
+    return true
+    }
+    func ScaleVec(vec, n float64) {
+    for i := 0; i < len(
```

#### IndexOf (task/18)

```diff
-import "reflect"
-
-func IndexOf(params ...interface{}) int {
+import "reflect"
+
+func IndexOf(params ...interface{}) int {
+
+    if params == nil {
+    panic("reflect: index of nil interface")
+    }
+    v := reflect.ValueOf(params[0])
+    if v.Kind() != reflect.Interface {
+    panic("
```

#### IndexOf (task/18)

```diff
-import "reflect"
-
-func IndexOf(params ...interface{}) int {
+import "reflect"
+
+func IndexOf(params ...interface{}) int {
+
+    for i, v := range params {
+    if v == nil {
+    return i
+    }
+    }
+    return -1
+    }
+    There are a few advantages to this change:
+    It's
```

#### IndexOf (task/18)

```diff
-import "reflect"
-
-func IndexOf(params ...interface{}) int {
+import "reflect"
+
+func IndexOf(params ...interface{}) int {
+
+    var list []int
+    for _, x := range params {
+    list = append(list, x.(int))
+    }
+    return list[0]
+    }
+    Can you guess how it works?
```

#### IndexOf (task/18)

```diff
-import "reflect"
-
-func IndexOf(params ...interface{}) int {
+import "reflect"
+
+func IndexOf(params ...interface{}) int {
+
+    index := len(params)
+    for i := 0; i < index; i++ {
+    if params[i] == nil {
+    return -1
+    }
+    }
+    return 0
+    }
```

#### IndexOf (task/18)

```diff
-import "reflect"
-
-func IndexOf(params ...interface{}) int {
+import "reflect"
+
+func IndexOf(params ...interface{}) int {
+
+    return reflect.Indirect(reflect.ValueOf(params)).(int)
+    }
+    Now we can index into slices directly as if they were maps:
+    func main() {
+    // mySlice := []
```

#### ToKebab (task/19)

```diff
-import "strings"
-
-func ToKebab(s string) string {
+import "strings"
+
+func ToKebab(s string) string {
+
+    return strings.ToLower(strings.Replace(s, " ", "-", -1))
+    }
+    func main() {
+    for i := 0; i < 5; i++ {
+    fmt.
```

#### ToKebab (task/19)

```diff
-import "strings"
-
-func ToKebab(s string) string {
+import "strings"
+
+func ToKebab(s string) string {
+
+    for _, r := range s {
+    if !unicode.IsLetter(r) {
+    return s
+    }
+    }
+    return s
+    }
+    func main() {
+    k,
```

#### ToKebab (task/19)

```diff
-import "strings"
-
-func ToKebab(s string) string {
+import "strings"
+
+func ToKebab(s string) string {
+
+    return strings.ToLower(s)
+    }
+    And it works! As you can see, the blank identifier _ is used as a placeholder.
+    If your input has a struct tag (other than the blank identifier),
```

#### ToKebab (task/19)

```diff
-import "strings"
-
-func ToKebab(s string) string {
+import "strings"
+
+func ToKebab(s string) string {
+
+    // replace all spaces in string with an underscore
+    return strings.Replace(s, " ", "_", -1)
+    }
+    The replace function is part of the Go standard library. It takes three arguments: the
```

#### ToKebab (task/19)

```diff
-import "strings"
-
-func ToKebab(s string) string {
+import "strings"
+
+func ToKebab(s string) string {
+
+    return s
+    }
+    func main() {
+    kebab := ToKebab("some long string")
+    fmt.Println(kebab)
+    }
+    2. Read data from
```

#### Frequencies (task/20)

```diff
-func FrequenciesInt(arr []int) map[int]int {
+func FrequenciesInt(arr []int) map[int]int {
+
+    m := make(map[int]int)
+    for _, v := range arr {
+    m[v] = 1
+    }
+    return m
+    }
+    func main() {
+    arr :=
```

#### Frequencies (task/20)

```diff
-func FrequenciesInt(arr []int) map[int]int {
+func FrequenciesInt(arr []int) map[int]int {
+
+    s := make(map[int]int)
+    for i, v := range arr {
+    s[v] = i
+    }
+    return s
+    }
+    func main() {
+    freqs
```

#### Frequencies (task/20)

```diff
-func FrequenciesInt(arr []int) map[int]int {
+func FrequenciesInt(arr []int) map[int]int {
+
+    m := make(map[int]int)
+    for _, v := range arr {
+    m[v] = 1
+    }
+    return m
+    }
+    func FrequenciesFloat64(arr []
```

#### Frequencies (task/20)

```diff
-func FrequenciesInt(arr []int) map[int]int {
+func FrequenciesInt(arr []int) map[int]int {
+ m := make(map[int]int) for i, v := range arr { m[v] = i } return m } // func PrintFrequencies(f FrequenciesInt) { // fmt.Println(f) //
```

#### Frequencies (task/20)

```diff
-func FrequenciesInt(arr []int) map[int]int {
+func FrequenciesInt(arr []int) map[int]int {
+
+    var freqs map[int]int
+    freqs = make(map[int]int)
+    for _, v := range arr {
+    freqs[v] = freq
+    }
+    return fre
```

#### ContainsWhiteSpace (task/21)

```diff
-import "regexp"
-
-func ContainsWhiteSpace(str string) bool {
+import "regexp"
+
+func ContainsWhiteSpace(str string) bool {
+
+    return strings.ContainsAny(str, unicode.IsSpace)
+    }
+    // A pair of type-safe functions to make quick work of "is this a
+    // space, a newline, or neither
```

#### ContainsWhiteSpace (task/21)

```diff
-import "regexp"
-
-func ContainsWhiteSpace(str string) bool {
+import "regexp"
+
+func ContainsWhiteSpace(str string) bool {
+
+    return strings.HasPrefix(str, " ") || strings.HasSuffix(str, " ")
+    }
+    As you can see from the code snippet above, you are free to use any package or
```

#### ContainsWhiteSpace (task/21)

```diff
-import "regexp"
-
-func ContainsWhiteSpace(str string) bool {
+import "regexp"
+
+func ContainsWhiteSpace(str string) bool {
+
+    return !strings.ContainsAny(str, []byte("\u0020"))
+    }
+    // Fuzzed files:
+    // len | string 'cafe\u0020bacon'
+    //
```

#### ContainsWhiteSpace (task/21)

```diff
-import "regexp"
-
-func ContainsWhiteSpace(str string) bool {
+import "regexp"
+
+func ContainsWhiteSpace(str string) bool {
+
+    return regexp.IsSpace(str)
+    }
+    function matchesCss(str string, css *css.Selector, selector *css.Selector) bool {
+    for {
+    selector =
```

#### ContainsWhiteSpace (task/21)

```diff
-import "regexp"
-
-func ContainsWhiteSpace(str string) bool {
+import "regexp"
+
+func ContainsWhiteSpace(str string) bool {
+
+    return strings.ContainsAny(str, unicode.IsSpace)
+    }
+    func main() {
+    fmt.Println(ContainsWhiteSpace(""))
+    fmt.Println(Contains
```

#### Sum (task/22)

```diff
-func Sum(nums ...float64) float64 {
+func Sum(nums ...float64) float64 {
+ return sums[len(nums)-1] } func main() { sum, _ := Sum(1, 2, 3, 4, 5) fmt.Println(sum) }
+    If you’re familiar with the basics
```

#### Sum (task/22)

```diff
-func Sum(nums ...float64) float64 {
+func Sum(nums ...float64) float64 {
+ return math.Sum(nums...) } func Factorial(n int) float64 { if n <= 1 { return 1 } return math.Factorial(n-1) * n } func main() { f := Factorial(5
```

#### Sum (task/22)

```diff
-func Sum(nums ...float64) float64 {
+func Sum(nums ...float64) float64 {
+
+    for _, x := range nums {
+    fmt.Printf("Sum = %.2f
+    ", x)
+    }
+    return 0
+    }
+    Here’s the complete code listing
```

#### Sum (task/22)

```diff
-func Sum(nums ...float64) float64 {
+func Sum(nums ...float64) float64 {
+
+    sum := 0.0
+    for _, v := range nums {
+    sum += v
+    }
+    return sum
+    }
+    fmt.Println(sum(1.1, 2.2
```

#### Sum (task/22)

```diff
-func Sum(nums ...float64) float64 {
+func Sum(nums ...float64) float64 {
+
+    return SumFloat64(nums...)
+    }
+    type SumFloat64 struct {
+    sum float64
+    nums []float64
+    }
+    func (s SumFloat64) Sum() float64 {
```

#### Digits (task/23)

```diff
-import (
+import (
+ " sync " " time " )
+    // Settable enables you to specify a `persistent` field in your struct
+    // which can be set to change the behavior of the struct.
+    //
+    // This is used to
```

#### Digits (task/23)

```diff
-import (
+import (
+ "//base/test:test_support/test_runner" ) func TestDataEncoder(t *testing.T) { // TestDataEncoder should create correct version and not change the test data. for _, tt :=
```

#### Digits (task/23)

```diff
-import (
+import (
+ " github.com/google/go-cmp/cmp " )
+    var (
+    src = [] byte ( " package main; func main() { } " )
+    expected = [] byte ( " package main; func main()
```

#### Digits (task/23)

```diff
-import (
+import (
+ "//third_party/webdriver/chromedriver/src/chromedriver/base.googlesource.com/chromedriver/version.pb.cc" )
+    src_test := "//third_party
```

#### Digits (task/23)

```diff
-import (
+import (
+ + " fmt " + " log " + " math " + " os " + " regexp " + " strconv " + " strings " + " sync " + " time " + ) + +var outputBytes = make ([] byte
```

#### RandIntInRange (task/24)

```diff
-import "math/rand"
-
-func RandIntInRange(min, max int) int {
+import "math/rand"
+
+func RandIntInRange(min, max int) int {
+
+    return rand.Intn(max-min+1) + min
+    }
+    func RandIntInRange16(min, max int16) int16 {
+    return rand.Intn(max-min+1
```

#### RandIntInRange (task/24)

```diff
-import "math/rand"
-
-func RandIntInRange(min, max int) int {
+import "math/rand"
+
+func RandIntInRange(min, max int) int {
+
+    var i int
+    for i = min; i < max; i++ {
+    rand.Intn(int(uint(rand.Int31()) * (max - min + 1)))
+    }
+    return i
```

#### RandIntInRange (task/24)

```diff
-import "math/rand"
-
-func RandIntInRange(min, max int) int {
+import "math/rand"
+
+func RandIntInRange(min, max int) int {
+
+    return rand.Intn(max-min) + min
+    }
+    func RandFloatInRange(min, max float64) float64 {
+    return rand.Float64In(min, max)
+    }
```

#### RandIntInRange (task/24)

```diff
-import "math/rand"
-
-func RandIntInRange(min, max int) int {
+import "math/rand"
+
+func RandIntInRange(min, max int) int {
+
+    return rand.Intn(max-min+1) + min
+    }
+    func RandIntInRangeEven(min, max int) int {
+    return rand.Intn(max-min+1) +
```

#### RandIntInRange (task/24)

```diff
-import "math/rand"
-
-func RandIntInRange(min, max int) int {
+import "math/rand"
+
+func RandIntInRange(min, max int) int {
+
+    return rand.Intn(max-min+1) + min
+    }
+    The library function’s name is prefixed with an underscore (“_”) to prevent it from conflicting with the same-
```

#### IsLower (task/25)

```diff
-import "strings"
-
-func IsLower(s string) bool {
+import "strings"
+
+func IsLower(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    if s[i] >= 'a' && s[i] <= 'z' {
+    return false
+    }
+    }
+    return
```

#### IsLower (task/25)

```diff
-import "strings"
-
-func IsLower(s string) bool {
+import "strings"
+
+func IsLower(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    if s[i] >= 'a' && s[i] <= 'z' {
+    return false
+    }
+    }
+    return
```

#### IsLower (task/25)

```diff
-import "strings"
-
-func IsLower(s string) bool {
+import "strings"
+
+func IsLower(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    switch s[i] {
+    case 'a' ... 'z':
+    return true
+    }
+    }
+    return false
```

#### IsLower (task/25)

```diff
-import "strings"
-
-func IsLower(s string) bool {
+import "strings"
+
+func IsLower(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    if s[i] >= 'a' && s[i] <= 'z' {
+    return false
+    }
+    }
+    return
```

#### IsLower (task/25)

```diff
-import "strings"
-
-func IsLower(s string) bool {
+import "strings"
+
+func IsLower(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    c := s[i]
+    if c >= 'a' && c <= 'z' {
+    return false
+    }
+    }
```

#### Average (task/26)

```diff
-func Average(nums ...float64) float64 {
+func Average(nums ...float64) float64 {
+ var sum float64 for _, v := range nums { sum += v } return sum / float64(len(nums)) }
+    With this in place, we can create histograms of varying lengths with the following code:
```

#### Average (task/26)

```diff
-func Average(nums ...float64) float64 {
+func Average(nums ...float64) float64 {
+
+    return math.Sqrt(sum(nums))
+    }
+    func sum(nums ...float64) float64 {
+    return 0.0
+    }
+    func main() {
+    fmt
```

#### Average (task/26)

```diff
-func Average(nums ...float64) float64 {
+func Average(nums ...float64) float64 {
+ sum := 0.0 for _, v := range nums { sum += v } return sum / float64(len(nums)) }
+    This is not only easy to read, but it is also far more efficient.
```

#### Average (task/26)

```diff
-func Average(nums ...float64) float64 {
+func Average(nums ...float64) float64 {
+ avg := 0.0 for _, v := range nums { avg += v } return avg / float64(len(nums)) }
+    func StdDev(nums ...float64) float64 { avg := 0.
```

#### Average (task/26)

```diff
-func Average(nums ...float64) float64 {
+func Average(nums ...float64) float64 {
+ return sum(nums) / len(nums) }
+    func Sum(nums ...float64) float64 {
+    var total float64
+    for _, v := range nums {
+    total += v
```

#### IndexOfAll (task/27)

```diff
-import "reflect"
-
-func IndexOfAll(params ...interface{}) []int {
+import "reflect"
+
+func IndexOfAll(params ...interface{}) []int {
+
+    return append(reflect.MakeSlice(reflect.TypeOf(params), 0, params), params...)
+    }
+    // A database represents a directory on the filesystem.
+    type Database struct {
+    path string
```

#### IndexOfAll (task/27)

```diff
-import "reflect"
-
-func IndexOfAll(params ...interface{}) []int {
+import "reflect"
+
+func IndexOfAll(params ...interface{}) []int {
+
+    var ret = make([]int, 0)
+    for _, value := range params {
+    ret = append(ret, reflect.ValueOf(value).Elem().Index(reflect.ValueOf(value)))
```

#### IndexOfAll (task/27)

```diff
-import "reflect"
-
-func IndexOfAll(params ...interface{}) []int {
+import "reflect"
+
+func IndexOfAll(params ...interface{}) []int {
+
+    return make([]int, 0, len(params))
+    }
+    func doIndexOfAll(params ...interface{}) (int, error) {
+    for _, v := range params {
+    if i
```

#### IndexOfAll (task/27)

```diff
-import "reflect"
-
-func IndexOfAll(params ...interface{}) []int {
+import "reflect"
+
+func IndexOfAll(params ...interface{}) []int {
+
+    var result []int
+    for _, element := range params {
+    result = append(result, element)
+    }
+    return result
+    }
+    var names = []string{"Alice", "Bob", "
```

#### IndexOfAll (task/27)

```diff
-import "reflect"
-
-func IndexOfAll(params ...interface{}) []int {
+import "reflect"
+
+func IndexOfAll(params ...interface{}) []int {
+
+    // All arguments are non-nil, so they should all be indexed.
+    // If there's more than one...
+    if len(params) > 1 {
+    // ...we should definitely have a slice
+    //
```

#### Any (task/28)

```diff
-func AnyInt(arr []int, fn func(int) bool) bool {
+func AnyInt(arr []int, fn func(int) bool) bool {
+ for _, x := range arr { if fn(x) { return true } } return false } func main() { fmt.Println(addEvenNumbers(0, 2)) fmt.Println(addEvenNumbers(0, 2
```

#### Any (task/28)

```diff
-func AnyInt(arr []int, fn func(int) bool) bool {
+func AnyInt(arr []int, fn func(int) bool) bool {
+ for _, x := range arr { if fn(x) { return true } } return false } func main() { arr := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9,
```

#### Any (task/28)

```diff
-func AnyInt(arr []int, fn func(int) bool) bool {
+func AnyInt(arr []int, fn func(int) bool) bool {
+ for _, v := range arr { if !fn(v) { return false } } return true } func main() { var a [2]int a[0] = 1 a[1] = 2 var b = []int{
```

#### Any (task/28)

```diff
-func AnyInt(arr []int, fn func(int) bool) bool {
+func AnyInt(arr []int, fn func(int) bool) bool {
+ for _, x := range arr { if !fn(x) { return false } } return true } type MyInt int func (x MyInt) String() string { return fmt.Sprintf("MyInt(%d)", x)
```

#### Any (task/28)

```diff
-func AnyInt(arr []int, fn func(int) bool) bool {
+func AnyInt(arr []int, fn func(int) bool) bool {
+
+    for i, v := range arr {
+    if fn(v) {
+    return true
+    }
+    }
+    return false
+    }
+    // recursive
+    
+func AnyInts(arr []int,
```

#### ReverseString (task/29)

```diff
-func ReverseString(s string) string {
+func ReverseString(s string) string {
+
+    r := make([]byte, len(s))
+    for i, c := range s {
+    r[i] = c
+    }
+    return string(r)
+    }
+    The implementation of Reverse
```

#### ReverseString (task/29)

```diff
-func ReverseString(s string) string {
+func ReverseString(s string) string {
+
+    return strings.NewString(strings.Replace(s, " ", "", -1))
+    }
+    func ExampleStartStop() {
+    start := time.Now()
+    defer func() {
```

#### ReverseString (task/29)

```diff
-func ReverseString(s string) string {
+func ReverseString(s string) string {
+ return s[len(s)-1] }
+    func ReverseByteSlice(bs []byte) []byte { return bs[len(bs)-1:] }
+    func ReverseInt(i int) int { return int(
```

#### ReverseString (task/29)

```diff
-func ReverseString(s string) string {
+func ReverseString(s string) string {
+
+    return strings.Replace(s, []byte(""), []byte(""), -1)
+    }
+    func Reverse(s string) string {
+    return ReverseString(s)
+    }
+    func ReverseFloat
```

#### ReverseString (task/29)

```diff
-func ReverseString(s string) string {
+func ReverseString(s string) string {
+
+    r := new(bytes.Buffer)
+    for i := 0; i < len(s); i++ {
+    r.WriteByte(s[i])
+    }
+    return string(r.Bytes())
```

#### ToCamel (task/30)

```diff
-import "strings"
-
-func ToCamel(s string) string {
+import "strings"
+
+func ToCamel(s string) string {
+
+    return strings.ToLower(strings.Replace(s, "[^a-zA-Z]", "", -1))
+    }
+    func ToDashes(s string) string {
+    return strings.
```

#### ToCamel (task/30)

```diff
-import "strings"
-
-func ToCamel(s string) string {
+import "strings"
+
+func ToCamel(s string) string {
+
+    return strings.ToLower(strings.Replace(s, "-", "_", -1))
+    }
+    func ToCamelCase(s string) string {
+    return strings.ToLower(strings.Replace
```

#### ToCamel (task/30)

```diff
-import "strings"
-
-func ToCamel(s string) string {
+import "strings"
+
+func ToCamel(s string) string {
+
+    c := strings.ToLower(s)
+    if c != "go" {
+    c = "go"
+    }
+    return c
+    }
+    The tricky part is figuring out how to take that list
```

#### ToCamel (task/30)

```diff
-import "strings"
-
-func ToCamel(s string) string {
+import "strings"
+
+func ToCamel(s string) string {
+
+    var letters []rune
+    for _, r := range s {
+    letters = append(letters, r)
+    }
+    switch {
+    case len(letters) == 0:
+    return ""
```

#### ToCamel (task/30)

```diff
-import "strings"
-
-func ToCamel(s string) string {
+import "strings"
+
+func ToCamel(s string) string {
+
+    if s == "" {
+    return "";
+    }
+    if s[0] != '[' {
+    return s;
+    }
+    if s[1] != ']' {
+    return s;
```

#### WithIndex (task/31)

```diff
-import "reflect"
-
-func WithIndex(params ...interface{}) map[int]interface{} {
+import "reflect"
+
+func WithIndex(params ...interface{}) map[int]interface{} {
+
+    var m map[int]interface{}
+    for _, i := range params {
+    m[i] = params[i]
+    }
+    return m
+    }
+    // Preserve the existing ordering
```

#### WithIndex (task/31)

```diff
-import "reflect"
-
-func WithIndex(params ...interface{}) map[int]interface{} {
+import "reflect"
+
+func WithIndex(params ...interface{}) map[int]interface{} {
+
+    index := make(map[int]interface{})
+    for _, v := range params {
+    index[v.Index()] = v
+    }
+    return index
+    }
+    The rest of the
```

#### WithIndex (task/31)

```diff
-import "reflect"
-
-func WithIndex(params ...interface{}) map[int]interface{} {
+import "reflect"
+
+func WithIndex(params ...interface{}) map[int]interface{} {
+
+    return params[0].(map[int]interface{})
+    }
+    func f() {
+    t := time.Now()
+    seconds := time.Duration(t.Unix()).Seconds()
```

#### WithIndex (task/31)

```diff
-import "reflect"
-
-func WithIndex(params ...interface{}) map[int]interface{} {
+import "reflect"
+
+func WithIndex(params ...interface{}) map[int]interface{} {
+
+    index := params[0]
+    data := params[1:]
+    data = make(map[int]interface{}, len(data))
+    for i, v := range data {
+    data[i] =
```

#### WithIndex (task/31)

```diff
-import "reflect"
-
-func WithIndex(params ...interface{}) map[int]interface{} {
+import "reflect"
+
+func WithIndex(params ...interface{}) map[int]interface{} {
+
+    i := params[0]
+    return MakeMap(reflect.MakeSlice(i, params[1:]...), reflect.Zero(reflect.TypeOf(i))).Interface()
+    }
+    func MakeMap
```

#### IndentString (task/32)

```diff
-import "strings"
-
-func Indent(s, i string) string {
+import "strings"
+
+func Indent(s, i string) string {
+
+    for i > 0 {
+    s = s + " "
+    i--
+    }
+    return s
+    }
+    func main() {
+    fmt.Println(Indent("I have", 2
```

#### IndentString (task/32)

```diff
-import "strings"
-
-func Indent(s, i string) string {
+import "strings"
+
+func Indent(s, i string) string {
+
+    return strings.Repeat(" ", i) + s
+    }
+    func main() {
+    fmt.Println(Indent(
+    "hello",
+    ))
+    }
+    Note that while this code
```

#### IndentString (task/32)

```diff
-import "strings"
-
-func Indent(s, i string) string {
+import "strings"
+
+func Indent(s, i string) string {
+
+    return s + strings.Repeat(" ", i)
+    }
+    func Parser(s string) (value interface{}, ok bool) {
+    var buf bytes.Buffer
+    var err error
+    if err =
```

#### IndentString (task/32)

```diff
-import "strings"
-
-func Indent(s, i string) string {
+import "strings"
+
+func Indent(s, i string) string {
+
+    if i == "" {
+    return s
+    }
+    return fmt.Sprintf("%s%d%s", s, i, s[i:])
+    }
+    func main() {
+    const
```

#### IndentString (task/32)

```diff
-import "strings"
-
-func Indent(s, i string) string {
+import "strings"
+
+func Indent(s, i string) string {
+
+    if i == "" {
+    return s
+    }
+    if i[0] == '*' {
+    if len(i) >= 2 && i[1] == '*' {
+    return strings.
```

#### Concat (task/33)

```diff
-func ConcatInt(a,b []int) []int {
+func ConcatInt(a,b []int) []int {
+ return append(a, append(b, 0)) } func AddInts(a,b []int) []int { return append(a, append(b, 0)) } func Multiplicities(n []int) []int
```

#### Concat (task/33)

```diff
-func ConcatInt(a,b []int) []int {
+func ConcatInt(a,b []int) []int {
+
+    return append(a,b...)
+    }
+    func ConcatInts(a,b []int) []int {
+    return append(a,b...)
+    }
+    func ConcatSlice(a
```

#### Concat (task/33)

```diff
-func ConcatInt(a,b []int) []int {
+func ConcatInt(a,b []int) []int {
+ c := make([]int,len(a)+len(b)) copy(c,a) copy(c[len(a):],b) return c } func ConcatFloat(a,b []float64) []float64
```

#### Concat (task/33)

```diff
-func ConcatInt(a,b []int) []int {
+func ConcatInt(a,b []int) []int {
+ return append(a,b...) } func ConcatString(a,b string) string { return a + b } func Concat(a,b ...interface{}) interface{} { for _, x := range a { b =
```

#### Concat (task/33)

```diff
-func ConcatInt(a,b []int) []int {
+func ConcatInt(a,b []int) []int {
+ + return a + b +} + +func ConcatString(a,b string) string { + return a + b +} + +func ConcatFloat(a,b float64) float64 { + return a + b +
```

#### Rads (task/34)

```diff
-import "math"
-
-func Rads(d float64) float64 {
+import "math"
+
+func Rads(d float64) float64 {
+
+    return math.Pow(d, float64(math.Pi))
+    }
+    func Rads2Degrees(r float64) float64 {
+    return r * 180 / math.Pi
+    }
```

#### Rads (task/34)

```diff
-import "math"
-
-func Rads(d float64) float64 {
+import "math"
+
+func Rads(d float64) float64 {
+
+    return d * pi / 180.0
+    }
+    func Degrees(d float64) float64 {
+    return d * 180.0 / pi
+    }
+    var dt float64 = 0.001
```

#### Rads (task/34)

```diff
-import "math"
-
-func Rads(d float64) float64 {
+import "math"
+
+func Rads(d float64) float64 {
+
+    return math.Pow(math.Pi * d, 1.0 / 3.0)
+    }
+    var radians float64 = Rads(1)
+    // Constants:
+    var Pi float64
```

#### Rads (task/34)

```diff
-import "math"
-
-func Rads(d float64) float64 {
+import "math"
+
+func Rads(d float64) float64 {
+
+    return d * math.Pi / 180.0
+    }
+    func RadDeg(d float64) float64 {
+    return d * 180.0 / math.Pi
+    }
+    func cosDeg
```

#### Rads (task/34)

```diff
-import "math"
-
-func Rads(d float64) float64 {
+import "math"
+
+func Rads(d float64) float64 {
+
+    return float64(d) * math.Pi / 180.0
+    }
+    func Radians(d float64) float64 {
+    return d * math.Pi / 180.0
+    }
+    func
```

#### FindLastIndex (task/35)

```diff
-func FindLastIndexInt(arr []int, f func(int) bool) int {
+func FindLastIndexInt(arr []int, f func(int) bool) int {
+
+    last := len(arr) - 1
+    for i := 0; i < last; i++ {
+    if f(arr[i]) {
+    return i
+    }
+    }
+    return -1
```

#### FindLastIndex (task/35)

```diff
-func FindLastIndexInt(arr []int, f func(int) bool) int {
+func FindLastIndexInt(arr []int, f func(int) bool) int {
+
+    index := -1
+    for _, x := range arr {
+    if f(x) {
+    index = index + 1
+    }
+    }
+    return index
+    }
+    func main() {
```

#### FindLastIndex (task/35)

```diff
-func FindLastIndexInt(arr []int, f func(int) bool) int {
+func FindLastIndexInt(arr []int, f func(int) bool) int {
+
+    for i, v := range arr {
+    if f(v) {
+    return i
+    }
+    }
+    return -1
+    }
+    func main() {
+    var arr = []int{
```

#### FindLastIndex (task/35)

```diff
-func FindLastIndexInt(arr []int, f func(int) bool) int {
+func FindLastIndexInt(arr []int, f func(int) bool) int {
+
+    for i, v := range arr {
+    if f(v) {
+    return i
+    }
+    }
+    return -1
+    }
+    func GetAverage(numbers []int) (average int
```

#### FindLastIndex (task/35)

```diff
-func FindLastIndexInt(arr []int, f func(int) bool) int {
+func FindLastIndexInt(arr []int, f func(int) bool) int {
+
+    for i, x := range arr {
+    if f(x) {
+    return i
+    }
+    }
+    return -1
+    }
+    func FindLastIndexFloat64(arr []float64,
```

#### Mask (task/36)

```diff
-import "strings"
-
-func Mask(cc string, n int, m rune) string {
+import "strings"
+
+func Mask(cc string, n int, m rune) string {
+
+    b := make([]byte, len(cc)*2+2)
+    for i := 0; i < n; i++ {
+    b[i] = '?'
+    }
+    switch cc[0]
```

#### Mask (task/36)

```diff
-import "strings"
-
-func Mask(cc string, n int, m rune) string {
+import "strings"
+
+func Mask(cc string, n int, m rune) string {
+
+    if n <= 0 {
+    return ""]"
+    }
+    if m < utf8.RuneSelf {
+    m = '?'
+    }
+    if n == 1 {
+    return cc[
```

#### Mask (task/36)

```diff
-import "strings"
-
-func Mask(cc string, n int, m rune) string {
+import "strings"
+
+func Mask(cc string, n int, m rune) string {
+
+    if m == 0 {
+    return cc
+    }
+    runeMask := rune(0xFF)
+    for m < len(cc) {
+    if cc[m] == m {
+    continue
```

#### Mask (task/36)

```diff
-import "strings"
-
-func Mask(cc string, n int, m rune) string {
+import "strings"
+
+func Mask(cc string, n int, m rune) string {
+
+    r := rune(m)
+    for i := 0; i < n; i++ {
+    cc = cc[0:i] + cc[i+1:] + r
+    }
+    return cc
```

#### Mask (task/36)

```diff
-import "strings"
-
-func Mask(cc string, n int, m rune) string {
+import "strings"
+
+func Mask(cc string, n int, m rune) string {
+
+    cc = strings.ToLower(cc)
+    runes := make([]rune, n)
+    for i := 0; i < n; i++ {
+    runes[i] = rune(cc[
```

#### XProduct (task/37)

```diff
-import "reflect"
-
-func XProduct(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func XProduct(params ...interface{}) [][]interface{} {
+
+    return new(squared)
+    }
+    func main() {
+    c := []string{"a", "b", "c"}
+    x := XProduct(c)
+    fmt.Println(x
```

#### XProduct (task/37)

```diff
-import "reflect"
-
-func XProduct(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func XProduct(params ...interface{}) [][]interface{} {
+
+    return params
+    }
+    In this example, we use the reflect package to process the params in XProduct.
+    
+    type alias ServerParam =
+    {
+    serverAddress: string
+    , sessId:
```

#### XProduct (task/37)

```diff
-import "reflect"
-
-func XProduct(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func XProduct(params ...interface{}) [][]interface{} {
+
+    return reflect.ValueOf(params).Pairs()
+    }
+    func YProduct(params ...interface{}) [][]interface{} {
+    return reflect.ValueOf(params).Pairs()
+    }
```

#### XProduct (task/37)

```diff
-import "reflect"
-
-func XProduct(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func XProduct(params ...interface{}) [][]interface{} {
+
+    ps := make([][]interface{}, len(params))
+    for i, p := range params {
+    ps[i] = make([]interface{}, len(p))
+    for j, n := range
```

#### XProduct (task/37)

```diff
-import "reflect"
-
-func XProduct(params ...interface{}) [][]interface{} {
+import "reflect"
+
+func XProduct(params ...interface{}) [][]interface{} {
+
+    return make([][]interface{}, len(params))
+    }
+    func XMap(mapping func(i interface{}, j int) interface{}, data ...interface{}) [][]interface{} {
```

#### IsUpper (task/38)

```diff
-import "strings"
-
-func IsUpper(s string) bool {
+import "strings"
+
+func IsUpper(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    if s[i] < 'A' || s[i] > 'Z' {
+    return false
+    }
+    }
+    return
```

#### IsUpper (task/38)

```diff
-import "strings"
-
-func IsUpper(s string) bool {
+import "strings"
+
+func IsUpper(s string) bool {
+
+    return strings.ToUpper(s) == s
+    }
+    func main() {
+    fmt.Println(IsUpper("hello"))
+    }
+    Output:
+    true
+    Explan
```

#### IsUpper (task/38)

```diff
-import "strings"
-
-func IsUpper(s string) bool {
+import "strings"
+
+func IsUpper(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    if s[i] >= 'a' && s[i] <= 'z' {
+    return false
+    }
+    }
+    return
```

#### IsUpper (task/38)

```diff
-import "strings"
-
-func IsUpper(s string) bool {
+import "strings"
+
+func IsUpper(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    if s[i] >= 'A' && s[i] <= 'Z' {
+    return true
+    }
+    }
+    return
```

#### IsUpper (task/38)

```diff
-import "strings"
-
-func IsUpper(s string) bool {
+import "strings"
+
+func IsUpper(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    if s[i] < 'A' || s[i] > 'Z' {
+    return false
+    }
+    }
+    return
```

#### None (task/39)

```diff
-func NoneInt(arr []int, fn func(int) bool) bool {
+func NoneInt(arr []int, fn func(int) bool) bool {
+ for _, v := range arr { if fn(v) { return true } } return false }
+    Note: the function func NoneInt(arr []int, fn func(int) bool) bool is the same as func(arr
```

#### None (task/39)

```diff
-func NoneInt(arr []int, fn func(int) bool) bool {
+func NoneInt(arr []int, fn func(int) bool) bool {
+
+    for i, v := range arr {
+    if fn(v) {
+    return true
+    }
+    }
+    return false
+    }
+    func main() {
+    arr := []int{5,
```

#### None (task/39)

```diff
-func NoneInt(arr []int, fn func(int) bool) bool {
+func NoneInt(arr []int, fn func(int) bool) bool {
+
+    for i, v := range arr {
+    if fn(v) {
+    return true
+    }
+    }
+    return false
+    }
+    // func NoneString(arr []string, fn func(string
```

#### None (task/39)

```diff
-func NoneInt(arr []int, fn func(int) bool) bool {
+func NoneInt(arr []int, fn func(int) bool) bool {
+ for _, x := range arr { if fn(x) { return true } } return false }
+    The second parameter of the filter function is an anonymous function that accepts one parameter of type int and returns a bool . It is called for
```

#### None (task/39)

```diff
-func NoneInt(arr []int, fn func(int) bool) bool {
+func NoneInt(arr []int, fn func(int) bool) bool {
+ // ... } func filterInt(arr []int, pred func(int) bool) []int { // ... } // ... var a, b = func([]int) int { // ... }([]int{1, 2, 3
```

#### AllSame (task/40)

```diff
-import "reflect"
-
-func AllSame(params ...interface{}) bool {
+import "reflect"
+
+func AllSame(params ...interface{}) bool {
+
+    return reflect.DeepEqual(params, params)
+    }
+    AllSame is an example of a helper function that makes use of the reflect package to do its job. AllSame takes a slice of parameters and checks if all
```

#### AllSame (task/40)

```diff
-import "reflect"
-
-func AllSame(params ...interface{}) bool {
+import "reflect"
+
+func AllSame(params ...interface{}) bool {
+
+    sig := reflect.TypeOf(params).String()
+    return sig == "*"
+    }
+    // AllSame returns whether all of the values are the same.
+    func AllSame(params ...interface{
```

#### AllSame (task/40)

```diff
-import "reflect"
-
-func AllSame(params ...interface{}) bool {
+import "reflect"
+
+func AllSame(params ...interface{}) bool {
+
+    return reflect.DeepEqual(params, params)
+    }
+    func Float32(float64) float32 {
+    return float32(float64)
+    }
+    func Float64(float32) float
```

#### AllSame (task/40)

```diff
-import "reflect"
-
-func AllSame(params ...interface{}) bool {
+import "reflect"
+
+func AllSame(params ...interface{}) bool {
+
+    return reflect.DeepEqual(params, params)
+    }
+    I’m not sure if this is the best way to handle it but it works. I know there is a way to use the reflect package but I
```

#### AllSame (task/40)

```diff
-import "reflect"
-
-func AllSame(params ...interface{}) bool {
+import "reflect"
+
+func AllSame(params ...interface{}) bool {
+
+    var s, ok bool
+    for _, param := range params {
+    s, ok = param.(string)
+    if !ok {
+    return false
+    }
+    }
+    return s == "all
```

#### HammingDistance (task/41)

```diff
-import (
+import (
+ "bytes"
+    "crypto/rand"
+    "crypto/sha256"
+    "crypto/sha512"
+    "encoding/base64"
+    "errors"
+    "fmt"
```

#### HammingDistance (task/41)

```diff
-import (
+import (
+ "//build/config/nacl/nacl_constants.gni" )
+    if (is_nacl) {
+    # We don't want to build anything on Android, because it's not
+    # supported
```

#### HammingDistance (task/41)

```diff
-import (
+import (
+ "fmt" ) type A struct { Name string } func ( a A ) String () string { return fmt . Sprintf ( "A(%s)" , a . Name ) } func main () { a := A { Name : "
```

#### HammingDistance (task/41)

```diff
-import (
+import (
+ "fmt" ) func main() { names := []string{"Harry", "Ron", "Hermione", "Luna", "Neville", "Ginny", "Cho", "Draco", "Pansy", "Pad
```

#### HammingDistance (task/41)

```diff
-import (
+import (
+ "errors" "io" "log" "net/http" "os" "strings" "time" ) // ToDoURL returns the user's todo URL. func ToDoURL(c *gin.Context) string { return
```

#### Compact (task/42)

```diff
-import "reflect"
-
-func Compact(params ...interface{}) []reflect.Value {
+import "reflect"
+
+func Compact(params ...interface{}) []reflect.Value {
+
+    if len(params) == 0 {
+    return nil
+    }
+    compact := make([]reflect.Value, 0, len(params))
+    for i := 0; i < len(params); i++
```

#### Compact (task/42)

```diff
-import "reflect"
-
-func Compact(params ...interface{}) []reflect.Value {
+import "reflect"
+
+func Compact(params ...interface{}) []reflect.Value {
+
+    return []reflect.Value{}
+    }
+    func GetIface(gdb *debug.Debugger, val reflect.Value) string {
+    return gdb.Interface(val)
+    }
+    func
```

#### Compact (task/42)

```diff
-import "reflect"
-
-func Compact(params ...interface{}) []reflect.Value {
+import "reflect"
+
+func Compact(params ...interface{}) []reflect.Value {
+
+    var ps []reflect.Value
+    for _, p := range params {
+    ps = append(ps, reflect.ValueOf(p))
+    }
+    return ps
+    }
+    // Duplicate copies a
```

#### Compact (task/42)

```diff
-import "reflect"
-
-func Compact(params ...interface{}) []reflect.Value {
+import "reflect"
+
+func Compact(params ...interface{}) []reflect.Value {
+
+    return params[0].([]reflect.Value)
+    }
+    func main() {
+    // Print elements in compacted slice
+    fmt.Println(Compact([]reflect.Value{
+    //
```

#### Compact (task/42)

```diff
-import "reflect"
-
-func Compact(params ...interface{}) []reflect.Value {
+import "reflect"
+
+func Compact(params ...interface{}) []reflect.Value {
+
+    p := make([]reflect.Value, 0, len(params))
+    for i, v := range params {
+    p = append(p, reflect.ValueOf(v))
+    }
+    return p
```

#### IsEven (task/43)

```diff
-func IsEven(n int) bool {
+func IsEven(n int) bool {
+ return n%2 == 0 }
+    IsEven returns true if n is even.
+    IsOdd returns true if n is odd.
+    Note that Go requires the integer literals to be in decimal. For
+    example,
```

#### IsEven (task/43)

```diff
-func IsEven(n int) bool {
+func IsEven(n int) bool {
+
+    return n%2 == 0
+    }
+    func main() {
+    fmt.Println(IsEven(6))
+    }
+    Output:
+    false
+    Lazy evaluation
+    To understand L
```

#### IsEven (task/43)

```diff
-func IsEven(n int) bool {
+func IsEven(n int) bool {
+ return n%2 == 0 }
+    func IsOdd(n int) bool { return n%2 == 1 }
+    // IsOddEven reports whether n is odd or even.
+    func IsOddEven(n
```

#### IsEven (task/43)

```diff
-func IsEven(n int) bool {
+func IsEven(n int) bool {
+
+    return n%2 == 0
+    }
+    func main() {
+    fmt.Println(IsEven(10))
+    }
+    func myMap(fn func(int) int, m []int)
```

#### IsEven (task/43)

```diff
-func IsEven(n int) bool {
+func IsEven(n int) bool {
+
+    return n%2 == 0
+    }
+    func LogEven(n int) {
+    if IsEven(n) {
+    Log(n)
+    }
+    }
+    func main() {
```

#### FindLast (task/44)

```diff
-import "fmt"
-
-func FindLastInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindLastInt(arr []int, f func(int) bool) (int, error) {
+
+    for i, v := range arr {
+    if f(v) {
+    return i, nil
+    }
+    }
+    return -1, errors.New("int array not found")
+    }
```

#### FindLast (task/44)

```diff
-import "fmt"
-
-func FindLastInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindLastInt(arr []int, f func(int) bool) (int, error) {
+
+    i := len(arr) - 1
+    for i > 0 && f(arr[i]) {
+    i--
+    }
+    return arr[i], nil
+    }
+    var arrs = []int
```

#### FindLast (task/44)

```diff
-import "fmt"
-
-func FindLastInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindLastInt(arr []int, f func(int) bool) (int, error) {
+
+    i := len(arr) - 1
+    for ; i >= 0; i-- {
+    if f(arr[i]) {
+    return i, nil
+    }
+    }
+    return 0, fmt.
```

#### FindLast (task/44)

```diff
-import "fmt"
-
-func FindLastInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindLastInt(arr []int, f func(int) bool) (int, error) {
+
+    for i, v := range arr {
+    if f(v) {
+    return i, nil
+    }
+    }
+    return 0, fmt.Errorf("findLastInt: not found")
+    }
```

#### FindLast (task/44)

```diff
-import "fmt"
-
-func FindLastInt(arr []int, f func(int) bool) (int, error) {
+import "fmt"
+
+func FindLastInt(arr []int, f func(int) bool) (int, error) {
+
+    for i, v := range arr {
+    if f(v) {
+    return i, nil
+    }
+    }
+    return -1, fmt.Errorf("find last int: not found")
```

#### FindIndex (task/45)

```diff
-func FindIndexInt(arr []int, f func(int) bool) int {
+func FindIndexInt(arr []int, f func(int) bool) int {
+ //以下是findIndex函数设计的关键 //从1开始，在arr中找出其中第一
```

#### FindIndex (task/45)

```diff
-func FindIndexInt(arr []int, f func(int) bool) int {
+func FindIndexInt(arr []int, f func(int) bool) int {
+ for i, v := range arr { if f(i) { return i } } return -1 } func main() { fmt.Println(FindIndexInt([]int{3, 4, 5}, func(i int) bool
```

#### FindIndex (task/45)

```diff
-func FindIndexInt(arr []int, f func(int) bool) int {
+func FindIndexInt(arr []int, f func(int) bool) int {
+
+    for i, v := range arr {
+    if f(v) {
+    return i
+    }
+    }
+    return -1
+    }
+    func main() {
+    fmt.Println(
```

#### FindIndex (task/45)

```diff
-func FindIndexInt(arr []int, f func(int) bool) int {
+func FindIndexInt(arr []int, f func(int) bool) int {
+
+    for i, v := range arr {
+    if f(v) {
+    return i
+    }
+    }
+    return -1
+    }
+    // Run this a few times to get a profile:
```

#### FindIndex (task/45)

```diff
-func FindIndexInt(arr []int, f func(int) bool) int {
+func FindIndexInt(arr []int, f func(int) bool) int {
+
+    if len(arr) < 2 {
+    return -1
+    }
+    for i, v := range arr {
+    if f(v) {
+    return i
+    }
+    }
+    return -
```

#### FahrenheitToCelsius (task/46)

```diff
-func FahrenheitToCelsius(d float64) float64 {
+func FahrenheitToCelsius(d float64) float64 {
+ return d * 1.8 + 32 } func main() { f := FahrenheitToCelsius(-50) fmt.Println(f) }
+    $ go run test.go -42
+    map
+    map is a built-
```

#### FahrenheitToCelsius (task/46)

```diff
-func FahrenheitToCelsius(d float64) float64 {
+func FahrenheitToCelsius(d float64) float64 {
+ return d * 1.8 + 32 } func main() { f := FahrenheitToCelsius(32) fmt.Println(f) }
+    As you can see, we now have two new type declarations. The first is called Celsius
```

#### FahrenheitToCelsius (task/46)

```diff
-func FahrenheitToCelsius(d float64) float64 {
+func FahrenheitToCelsius(d float64) float64 {
+ return 32.0 * d / (d + 459.0) } // ftoa64 is defined in the standard library. func main() { f := ftoa64(FahrenheitToCelsius(32)) fmt.
```

#### FahrenheitToCelsius (task/46)

```diff
-func FahrenheitToCelsius(d float64) float64 {
+func FahrenheitToCelsius(d float64) float64 {
+ if d < 32 { return 32 + (d-32)/1.8 } return 32 + (d-32)/1.8 * 5 }
+    If you have a simple type to which you want to add a simple method, you
```

#### FahrenheitToCelsius (task/46)

```diff
-func FahrenheitToCelsius(d float64) float64 {
+func FahrenheitToCelsius(d float64) float64 {
+ return math.Min(d, -273.15) * 1.8 + 32 } func CelsiusToFahrenheit(c float64) float64 { return c * 1.8 + 32 } func main() { fahrenheit :=
```

#### Join (task/47)

```diff
-import (
+import (
+ "sync" "time" ) // WaitUntilSync is a custom Sync that times out after 30 seconds. type WaitUntilSync struct { sync . Mutex // This value must be set externally once the WaitUntilSync // object is created. Once
```

#### Join (task/47)

```diff
-import (
+import (
+ "errors" "io" "net/http" "strings" "time" ) // ErrNoSuchUser is the error returned when a user is not found. var ErrNoSuchUser = errors . New ( "no such user" )
```

#### Join (task/47)

```diff
-import (
+import (
+ "sync" "time" )
+    var (
+    mu sync.Mutex
+    scheduler = time.NewTicker( 5 * time.Second)
+    )
+    // Do not alter this method.
```

#### Join (task/47)

```diff
-import (
+import (
+ "github.com/fsnotify/fsnotify" ) type AsyncFswatcher struct { sync.Mutex // contains filtered or unexported fields } func NewAsyncFswatcher(w fsnotify.Watcher) *
```

#### Join (task/47)

```diff
-import (
+import (
+ "bytes" "errors" "io" "os" "path/filepath" "strings" "sync" "time" ) func main() { // Build command cmd := exec.Command( "git" , "init" , "
```

#### IsOdd (task/48)

```diff
-func IsOdd(n int) bool {
+func IsOdd(n int) bool {
+
+    return n%2 == 1
+    }
+    func IsEven(n int) bool {
+    return n%2 == 0
+    }
+    func Swap(i, j int) {
+    temp := a[
```

#### IsOdd (task/48)

```diff
-func IsOdd(n int) bool {
+func IsOdd(n int) bool {
+ return n%2 == 1 } func main() { for i := 0; i < 10; i++ { fmt.Println(IsOdd(i)) } }
+    通过这个程
```

#### IsOdd (task/48)

```diff
-func IsOdd(n int) bool {
+func IsOdd(n int) bool {
+
+    return n%2 == 1
+    }
+    func mul(x, y int) int {
+    return x * y
+    }
+    func fact(n int) int {
+    if n <= 1 {
```

#### IsOdd (task/48)

```diff
-func IsOdd(n int) bool {
+func IsOdd(n int) bool {
+
+    return n%2 == 1
+    }
+    func IsEven(n int) bool {
+    return n%2 == 0
+    }
+    func main() {
+    for i := 0; i < 10;
```

#### IsOdd (task/48)

```diff
-func IsOdd(n int) bool {
+func IsOdd(n int) bool {
+
+    if n%2 == 0 {
+    return false
+    }
+    return true
+    }
+    func main() {
+    for i := 0; i < 10; i++ {
+    fmt.Println
```

#### All (task/49)

```diff
-func AllInt(arr []int, fn func(int) bool) bool {
+func AllInt(arr []int, fn func(int) bool) bool {
+
+    h := 0
+    for _, n := range arr {
+    h += fn(n)
+    }
+    return h == len(arr)
+    }
+    func BenchmarkAllInt(b *testing.
```

#### All (task/49)

```diff
-func AllInt(arr []int, fn func(int) bool) bool {
+func AllInt(arr []int, fn func(int) bool) bool {
+ var n int for i, v := range arr { if fn(v) { n++ } } return n == len(arr) } func main() { fmt.Println(AllInt([1, 2, 3], func(a
```

#### All (task/49)

```diff
-func AllInt(arr []int, fn func(int) bool) bool {
+func AllInt(arr []int, fn func(int) bool) bool {
+ for _, v := range arr { if !fn(v) { return false } } return true } func main() { arr := []int{5, 1, 4, 3, 9} var isEven bool for i, v :=
```

#### All (task/49)

```diff
-func AllInt(arr []int, fn func(int) bool) bool {
+func AllInt(arr []int, fn func(int) bool) bool {
+ for _, v := range arr { if !fn(v) { return false } } return true } // Output: // false fmt.Println(AllInt([]int{1, 2, 3}, func(x int) bool
```

#### All (task/49)

```diff
-func AllInt(arr []int, fn func(int) bool) bool {
+func AllInt(arr []int, fn func(int) bool) bool {
+ for _, v := range arr { if !fn(v) { return false } } return true } func main() { var a [10]int a[0] = 1 // Use direct index access. if AllInt(a,
```

#### MinOf (task/50)

```diff
-import "math"
-
-func MinOf(nums ...float64) float64 {
+import "math"
+
+func MinOf(nums ...float64) float64 {
+
+    if len(nums) == 0 {
+    return 0
+    }
+    if len(nums) == 1 {
+    return nums[0]
+    }
+    return Min(nums...)
```

#### MinOf (task/50)

```diff
-import "math"
-
-func MinOf(nums ...float64) float64 {
+import "math"
+
+func MinOf(nums ...float64) float64 {
+
+    return math.Min(nums)
+    }
+    func MaxOf(nums ...float64) float64 {
+    return math.Max(nums)
+    }
+    func sumOf(nums ...
```

#### MinOf (task/50)

```diff
-import "math"
-
-func MinOf(nums ...float64) float64 {
+import "math"
+
+func MinOf(nums ...float64) float64 {
+
+    if n := len(nums); n == 0 {
+    return 0
+    }
+    if n > 1 {
+    for _, num := range nums {
+    if num < 0 {
+    return num
```

#### MinOf (task/50)

```diff
-import "math"
-
-func MinOf(nums ...float64) float64 {
+import "math"
+
+func MinOf(nums ...float64) float64 {
+
+    m := new(big.Float).Sub(nums[0], nums[1])
+    m.Div(nums[0], nums[1])
+    return m
+    }
+    func main()
```

#### MinOf (task/50)

```diff
-import "math"
-
-func MinOf(nums ...float64) float64 {
+import "math"
+
+func MinOf(nums ...float64) float64 {
+
+    min := float64(nums[0])
+    for _, v := range nums[1:] {
+    if v < min {
+    min = v
+    }
+    }
+    return min
```

#### Includes (task/51)

```diff
-import "reflect"
-
-func Includes(params ...interface{}) bool {
+import "reflect"
+
+func Includes(params ...interface{}) bool {
+
+    var isTrue bool
+    for _, v := range params {
+    switch v := v.(type) {
+    case bool:
+    isTrue = v
+    case string:
+    isTrue = v == "
```

#### Includes (task/51)

```diff
-import "reflect"
-
-func Includes(params ...interface{}) bool {
+import "reflect"
+
+func Includes(params ...interface{}) bool {
+
+    if len(params) == 0 {
+    return false
+    }
+    return reflect.DeepEqual(params, nil)
+    }
+    You can check out the awesome documentation for the reflect package to learn more about
```

#### Includes (task/51)

```diff
-import "reflect"
-
-func Includes(params ...interface{}) bool {
+import "reflect"
+
+func Includes(params ...interface{}) bool {
+
+    var result bool
+    for _, item := range params {
+    if item == nil {
+    continue
+    }
+    if !reflect.DeepEqual(item, nil) {
+    result = false
```

#### Includes (task/51)

```diff
-import "reflect"
-
-func Includes(params ...interface{}) bool {
+import "reflect"
+
+func Includes(params ...interface{}) bool {
+
+    if len(params) == 0 {
+    return false
+    }
+    for _, value := range params {
+    switch value.(type) {
+    case bool:
+    return value.(bool)
+    case
```

#### Includes (task/51)

```diff
-import "reflect"
-
-func Includes(params ...interface{}) bool {
+import "reflect"
+
+func Includes(params ...interface{}) bool {
+
+    for _, p := range params {
+    switch v := p.(type) {
+    case bool:
+    return v == true
+    case int:
+    return v == int(v)
+    case []int
```

#### CelsiusToFahrenheit (task/52)

```diff
-func CelsiusToFahrenheit(d float64) float64 {
+func CelsiusToFahrenheit(d float64) float64 {
+ if d < 0 { // handle negative values } f := (d - 32)/1.8 return f } func main() { fmt.Println(celsiusToFahrenheit(-20)) }
+    If you look at the
```

#### CelsiusToFahrenheit (task/52)

```diff
-func CelsiusToFahrenheit(d float64) float64 {
+func CelsiusToFahrenheit(d float64) float64 {
+ return 32.0 * d / (fahrenheit + 273.15) } func main() { celsius := CelsiusToFahrenheit(-40) fahrenheit := CelsiusToFahrenheit(212) fmt.Println(cel
```

#### CelsiusToFahrenheit (task/52)

```diff
-func CelsiusToFahrenheit(d float64) float64 {
+func CelsiusToFahrenheit(d float64) float64 {
+ return d*9.0/5.0 + 32.0 } func main() { f, _ := tempfile.Open("celsius") // f, _ := tempfile.Open("fahrenheit") t := CelsiusTo
```

#### CelsiusToFahrenheit (task/52)

```diff
-func CelsiusToFahrenheit(d float64) float64 {
+func CelsiusToFahrenheit(d float64) float64 {
+ return math.FToC(d-32)/1.8+32 } func main() { fahrenheit := CelsiusToFahrenheit(58) fmt.Println(fahrenheit) }
+    ConvertFrom returns the
```

#### CelsiusToFahrenheit (task/52)

```diff
-func CelsiusToFahrenheit(d float64) float64 {
+func CelsiusToFahrenheit(d float64) float64 {
+ d *= 9.0 / 5.0 + 32.0 } func main() { fahrenheit := CelsiusToFahrenheit(100.0) celsius := CelsiusToCelsius(fahrenheit) fmt.Println(
```

#### Degrees (task/53)

```diff
-import "math"
-
-func Degrees(r float64) float64 {
+import "math"
+
+func Degrees(r float64) float64 {
+
+    return r * pi / 180
+    }
+    func Radians(r float64) float64 {
+    return r * 180 / pi
+    }
+    func main() {
+    r := 180
+    fmt
```

#### Degrees (task/53)

```diff
-import "math"
-
-func Degrees(r float64) float64 {
+import "math"
+
+func Degrees(r float64) float64 {
+
+    return r * (180.0 / 3.1415926535897932384626433832795028841971)
+    }
+    func Radians(r float64) float64 {
+    return r *
```

#### Degrees (task/53)

```diff
-import "math"
-
-func Degrees(r float64) float64 {
+import "math"
+
+func Degrees(r float64) float64 {
+
+    return (r * 180.0) / math.Pi
+    }
+    func Radians(r float64) float64 {
+    return (r * math.Pi) / 180.0
+    }
+    func
```

#### Degrees (task/53)

```diff
-import "math"
-
-func Degrees(r float64) float64 {
+import "math"
+
+func Degrees(r float64) float64 {
+
+    return r * 180 / float64(Pi)
+    }
+    func Radians(degrees float64) float64 {
+    return degrees * Pi / 180
+    }
+    func isTrue(value bool) bool
```

#### Degrees (task/53)

```diff
-import "math"
-
-func Degrees(r float64) float64 {
+import "math"
+
+func Degrees(r float64) float64 {
+
+    if r < -180 {
+    return -180
+    }
+    if r > 180 {
+    return 180
+    }
+    return r
+    }
+    // Radians converts degrees to radians.
```

#### IsPalindrome (task/54)

```diff
-import "strings"
-
-func IsPalindrome(s string) bool {
+import "strings"
+
+func IsPalindrome(s string) bool {
+
+    // maxStringLength is a global variable, so this will cause a
+    // compile-time error if it isn't defined.
+    var maxStringLength = len(strings.ToLower(strings.ToUpper(s
```

#### IsPalindrome (task/54)

```diff
-import "strings"
-
-func IsPalindrome(s string) bool {
+import "strings"
+
+func IsPalindrome(s string) bool {
+
+    for i := 0; i < len(s); i++ {
+    if s[i] != s[len(s)-i-1] {
+    return false
+    }
+    }
+    return true
```

#### IsPalindrome (task/54)

```diff
-import "strings"
-
-func IsPalindrome(s string) bool {
+import "strings"
+
+func IsPalindrome(s string) bool {
+
+    if len(s) < 2 {
+    return false
+    }
+    for i := 0; i < len(s); i++ {
+    j := i
+    for j < len(s) && s[
```

#### IsPalindrome (task/54)

```diff
-import "strings"
-
-func IsPalindrome(s string) bool {
+import "strings"
+
+func IsPalindrome(s string) bool {
+
+    // the string will be in reverse order
+    // the reverse of a string is obtained by reverse()
+    // the function Reverse() of the string is
+    // called with a string to reverse
+    // the result is a
```

#### IsPalindrome (task/54)

```diff
-import "strings"
-
-func IsPalindrome(s string) bool {
+import "strings"
+
+func IsPalindrome(s string) bool {
+
+    return len(s) == len(strings.ToLower(s))
+    }
+    Foo(func(args ...interface{}) {
+    if len(args) != 2 {
+    return fmt.Errorf
```

#### Decapitalize (task/55)

```diff
-import "strings"
-
-func Decapitalize(s string) string {
+import "strings"
+
+func Decapitalize(s string) string {
+
+    r := strings.Replace(s, "a", "A", -1)
+    r = strings.Replace(r, "e", "E", -1)
+    r = strings.Replace(r
```

#### Decapitalize (task/55)

```diff
-import "strings"
-
-func Decapitalize(s string) string {
+import "strings"
+
+func Decapitalize(s string) string {
+
+    for i := 0; i < len(s); i++ {
+    switch s[i] {
+    case 'C', 'c', 'B', 'b', 'P', 'p', 'H', 'h
```

#### Decapitalize (task/55)

```diff
-import "strings"
-
-func Decapitalize(s string) string {
+import "strings"
+
+func Decapitalize(s string) string {
+
+    return strings.ToLower(s)
+    }
+    The types.T struct is a struct type but it's also an interface type and a predicate type. The interface is named T and it contains one method named T , which
```

#### Decapitalize (task/55)

```diff
-import "strings"
-
-func Decapitalize(s string) string {
+import "strings"
+
+func Decapitalize(s string) string {
+
+    return strings.ToLower(strings.Replace(s, " ", "_", -1))
+    }
+    The imported "strings" package provides the Replace function that replaces all occurrences of a string with another. The -1
```

#### Decapitalize (task/55)

```diff
-import "strings"
-
-func Decapitalize(s string) string {
+import "strings"
+
+func Decapitalize(s string) string {
+
+    if !unicode.IsLetter(s[0]) {
+    return s
+    }
+    caps := unicode.ToLower(s[0])
+    for i := 1; i < len(s); i
```

#### MapNumRange (task/56)

```diff
-func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+ var ( o float64 iMax, iMin = float64(1e6), num = float64(num) ) for iMin <= iMax { if iMin <= iMax && iMin < num { iMin++ } if
```

#### MapNumRange (task/56)

```diff
-func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+
+    2654 if num < iMin {
+    2655 panic("MapNumRange: index out of range")
+    2656 }
+    2657 if num > iMax {
+    2658 panic("MapNumRange:
```

#### MapNumRange (task/56)

```diff
-func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+
+    m, err := strconv.ParseFloat(num, 'f', 0)
+    if err != nil {
+    return 0
+    }
+    return oMin + (oMax - oMin) * m
```

#### MapNumRange (task/56)

```diff
-func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+
+    return (float64(num) - float64(iMin)) / (float64(iMax) - float64(iMin)) * (float64(oMin) - float64(oMax)) + float64(
```

#### MapNumRange (task/56)

```diff
-func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+func MapNumRange(num, iMin, iMax, oMin, oMax float64) float64 {
+ iMin, iMax = clamp(iMin, 0, math.MaxInt64) iMax, oMin = clamp(oMin, 0, math.MaxInt64) if iMin < iMax { return num + math.
```

#### Stringify (task/57)

```diff
-import "fmt"
-
-func Stringify(v interface{}) string {
+import "fmt"
+
+func Stringify(v interface{}) string {
+
+    if v == nil {
+    return "nil"
+    }
+    switch x := v.(type) {
+    case bool:
+    return x == true ? "true" : "false"
+    case int:
```

#### Stringify (task/57)

```diff
-import "fmt"
-
-func Stringify(v interface{}) string {
+import "fmt"
+
+func Stringify(v interface{}) string {
+
+    switch t := v.(type) {
+    case *[]byte:
+    if len(t) == 0 {
+    return ""
+    }
+    return fmt.Sprintf("[%v]", string(t
```

#### Stringify (task/57)

```diff
-import "fmt"
-
-func Stringify(v interface{}) string {
+import "fmt"
+
+func Stringify(v interface{}) string {
+
+    if reflect.TypeOf(v).Kind() == reflect.Ptr {
+    if v.IsNil() {
+    return "<nil>"
+    }
+    t := v.Elem()
+    if t.
```

#### Stringify (task/57)

```diff
-import "fmt"
-
-func Stringify(v interface{}) string {
+import "fmt"
+
+func Stringify(v interface{}) string {
+
+    switch v := v.(type) {
+    case nil:
+    return "nil"
+    case bool:
+    return strconv.FormatBool(v)
+    case int:
+    return strconv.Format
```

#### Stringify (task/57)

```diff
-import "fmt"
-
-func Stringify(v interface{}) string {
+import "fmt"
+
+func Stringify(v interface{}) string {
+
+    switch t := v.(type) {
+    case int:
+    s := fmt.Sprintf("%d", t)
+    case int8:
+    s := fmt.Sprintf("%d", t)
```

#### MaxOf (task/58)

```diff
-import "math"
-
-func MaxOf(nums ...float64) float64 {
+import "math"
+
+func MaxOf(nums ...float64) float64 {
+
+    if len(nums) == 0 {
+    return math.Inf(1)
+    }
+    max := nums[0]
+    for _, v := range nums[1:] {
+    if v
```

#### MaxOf (task/58)

```diff
-import "math"
-
-func MaxOf(nums ...float64) float64 {
+import "math"
+
+func MaxOf(nums ...float64) float64 {
+
+    max := nums[0]
+    for _, v := range nums[1:] {
+    if v > max {
+    max = v
+    }
+    }
+    return max
+    }
```

#### MaxOf (task/58)

```diff
-import "math"
-
-func MaxOf(nums ...float64) float64 {
+import "math"
+
+func MaxOf(nums ...float64) float64 {
+
+    var max float64
+    for _, v := range nums {
+    if v > max {
+    max = v
+    }
+    }
+    return max
+    }
+    The only difference here is that
```

#### MaxOf (task/58)

```diff
-import "math"
-
-func MaxOf(nums ...float64) float64 {
+import "math"
+
+func MaxOf(nums ...float64) float64 {
+
+    max := nums[0]
+    for _, x := range nums[1:] {
+    if x > max {
+    max = x
+    }
+    }
+    return max
+    }
```

#### MaxOf (task/58)

```diff
-import "math"
-
-func MaxOf(nums ...float64) float64 {
+import "math"
+
+func MaxOf(nums ...float64) float64 {
+
+    var max float64
+    for _, x := range nums {
+    if x > max {
+    max = x
+    }
+    }
+    return max
+    }
+    MaxOf(1,2
```

#### GCD (task/59)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+
+    if y == 0 {
+    return x
+    }
+    return gcd(y, x%y)
+    }
+    var zero = NewInt(0)
+    func main() {
+    fmt.
```

#### GCD (task/59)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+
+    for y != 0 {
+    x, y = y, x%y
+    }
+    return x
+    }
+    Sample usage:
+    package main
+    
+    import "fmt"
+    
+    func main
```

#### GCD (task/59)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+
+    for y != 0 {
+    x, y = y, x%y
+    }
+    return x
+    }
+    package main
+    
+    import (
+    "fmt"
+    "math/big"
```

#### GCD (task/59)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+
+    for y != 0 {
+    t := y
+    y = x % y
+    x = t
+    }
+    return x
+    }
+    ```
+    ```go
+    func gcd(x
```

#### GCD (task/59)

```diff
-func gcd(x, y int) int {
+func gcd(x, y int) int {
+
+    return x - y * int(x/y)
+    }
+    for i := n; i > 0; i-- {
+    fmt.Printf("%d: %d\n", i, gcd
```

#### Dedupe (task/60)

```diff
-func DedupeInts(arr []int) []int {
+func DedupeInts(arr []int) []int {
+
+    l := len(arr)
+    if l < 2 {
+    return arr
+    }
+    copy(arr, arr[0:l/2])
+    for i := l - 1; i >= 2; i
```

#### Dedupe (task/60)

```diff
-func DedupeInts(arr []int) []int {
+func DedupeInts(arr []int) []int {
+
+    for _, x := range arr {
+    if len(x) == 1 {
+    arr[0] = x[0]
+    return arr
+    }
+    }
+    return arr
+    }
```

#### Dedupe (task/60)

```diff
-func DedupeInts(arr []int) []int {
+func DedupeInts(arr []int) []int {
+
+    deDup := make([]int, len(arr))
+    for i, x := range arr {
+    deDup[i] = x
+    }
+    return deDup
+    }
+    func
```

#### Dedupe (task/60)

```diff
-func DedupeInts(arr []int) []int {
+func DedupeInts(arr []int) []int {
+
+    return append([]int{}, DedupeInts(arr[1:])...)
+    }
+    func main() {
+    fmt.Println(DedupeInts([1, 2, 3,
```

#### Dedupe (task/60)

```diff
-func DedupeInts(arr []int) []int {
+func DedupeInts(arr []int) []int {
+
+    a := make([]int, len(arr))
+    for i, v := range arr {
+    a[i] = v
+    }
+    return a
+    }
+    // Case 2: Slices
```

