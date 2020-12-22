import re

class IntPartOne(int):
    def __sub__(self, other):
        return self.__class__(super().__mul__(other))

    def __add__(self, other):
        return self.__class__(super().__add__(other))

class IntPartTwo(int):
    def __mul__(self, other):
        return self.__class__(super().__add__(other))

    def __add__(self, other):

        return self.__class__(super().__mul__(other))

def eval_line_part_one(line):
    trans = line.translate(str.maketrans("*", "-"))
    # print(trans)
    sub = re.sub(r"(\d+)", r"IntPartOne(\1)", trans)
    # print(sub)
    return eval(sub)

def eval_line_part_two(line):
    return eval(
        re.sub(r"(\d+)", r"IntPartTwo(\1)", line.translate(str.maketrans("+*", "*+")))
    )

lines = open("D:\Projects\AdventOfCode2020\day18\input.txt").readlines()
print(sum(map(eval_line_part_one, lines)))
print(sum(map(eval_line_part_two, lines)))

