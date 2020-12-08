# Learning during the event - for future reference

## Day5

* use of `<string>.translate("".maketrans("FLBR", "0011"))` translate the string in

```
sample_string = "FFLBRF"
print(sample_string.translate("".maketrans("FLBR", "0011")))
# the characters in the string are replaced by the mapping from "0011"
# output 000110

```

* use of  `int(string,2) ` will change the base . e.g. int(110,2) -> 6

 ## Day6

 * use map(), reduce() with function like set(), list() etc
 * using * to access the elements in the set like *set()   


## Day7

* Using `defaultdict()` over dict{} will allow the handle te keyword missing error.

## Day8

* using `copy.deepcopy()` to copy next list or 2D list array [ [] , [] ]
```
>>> import copy
>>> a = [[1,2],[3,4]]
>>> a
[[1, 2], [3, 4]]
>>> b = a.copy()
>>> b[0][0] = 100
>>> b      
[[100, 2], [3, 4]]
>>> a
[[100, 2], [3, 4]]
>>> c = copy.deepcopy(b)
>>> c [0][0] = 0
>>> c
[[0, 2], [3, 4]]
>>> b
[[100, 2], [3, 4]]
>>> a
[[100, 2], [3, 4]]
```