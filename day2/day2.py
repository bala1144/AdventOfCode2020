

def input_parser(input_file):
    """
    input format : every line entries like 
    17-19 p: pwpzpfbrcpppjppbmppp
    10-11 b: bbbbbbbbbbbj 

    ouput : list(17,19,b,bbbbbbbbbbbj) for all lines
    """
    # convert the inputFile to list   
    condition_list = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.split('\n')[0].split()
            minMax = tuple(map(int, line[0].split('-'))) 
            reqChar = line[1][0]
            passwd = line[2]
            condition_list.append([minMax, reqChar, passwd])

    return condition_list

def check_valid_passwords(input_file):
    condition_list = input_parser(input_file)
    # print(condition_list)

    count = 0
    puzzle_2 = 0
    for (min,Max), reqChar, passwd in condition_list:
        
        # # puzzle 1
        # if passwd.count(reqChar) >= min and  passwd.count(reqChar) <= Max:
        #     count = count + 1
        #     print(min,Max,reqChar, passwd) 

        # puzzle 2
        if (passwd[min-1] == reqChar) ^ (passwd[Max-1] == reqChar):
            puzzle_2 = puzzle_2 + 1 
            
    print('total valid passwords', puzzle_2)

def main():
    input_file = 'D:\Projects\AdventOfCode2020\day2\input.txt'
    check_valid_passwords(input_file)

if __name__ == "__main__":
    main()