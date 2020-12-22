import itertools
import numpy as np
from collections import defaultdict
import copy

def input_parser(input_file):
    """Read the input and get the inputs are parsing

    """
    with open(input_file) as f:
        input_list = f.read().split('\n')
    print(input_list)

    for line in input_list:
        print( list(line.replace(" ", "")) )


def evaluate_expr():
    pass

def main():
    input_file = 'D:\Projects\AdventOfCode2020\day18\sample_input.txt'
    # input_file = 'D:\Projects\AdventOfCode2020\day17\input.txt'
    input_parser(input_file)

if __name__ == "__main__":
    main()