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

# Day10

c++ refreshing

```
#include <iostream>
#include <string>

int main()
{
    int *a ;
    std::cout << "A print " <<  a << std::endl;
    
    a  = new int(2);
    std::cout << "a new assignment " <<  a << std::endl;
    std::cout << "a address " <<  &a << std::endl;
    std::cout << "a address value " <<  *&a << std::endl;
    std::cout << "a address value value " <<  **&a << std::endl;
    
    // array using pointers
    
    int *arr = (int *)calloc(10, 10 * sizeof(int));
    std::cout << "Size of int " << sizeof(int) << std::endl; 
    std::cout << "Size of arr " << sizeof(arr) << std::endl; 
    std::cout << " print arr "<< arr << std::endl; 
    std::cout << " arr val "<< *arr << std::endl;
    std::cout << " Address of arr val "<< &arr << std::endl; 
    std::cout << " val Address of arr val "<< *&arr << std::endl;
    
}

output:
A print 0x400c50
a new assignment 0x225bc20
a address 0x7ffd6e961d80
a address value 0x225bc20
a address value value 2
Size of int 4
Size of arr 8
 print arr 0x225bc40
 arr val 0
 Address of arr val 0x7ffd6e961d88
 val Address of arr val 0x225bc40
```

### Day14

* Regular expression in python : using regexes allows to match multiple set of patterns which is not possible with string manipulation methods provided, We can also specify portion of the regular expression to be repeated reguarly

```
sample input : 
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
-----------------

for line in input_list: 
    if 'mask' in line:
        instruction_list.append(re.search("[X01]+", line).group())
    elif 'mem' in line:
        instruction_list.append(tuple(map(int,re.findall(r"\d+", line))))
    else:
        raise RuntimeError('Invalid instruction')

-----------------

* First regex will return XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X, it creates a class for X,0,1 with repetition.
* Second regex will return all the digits in the line  : (8,11)
        
```