# My personal learning during the event - for personal reference

* Day5
    1) use of `<string>.translate("".maketrans("FLBR", "0011"))` translate the string in

```
sample_string = "FFLBRF"
print(sample_string.translate("".maketrans("FLBR", "0011")))
# the characters in the string are replaced by the mapping from "0011"
# output 000110

```

    2) use of  `int(string,2) ` will change the base . e.g. int(110,2) -> 6

    