import copy

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')
    
    input_list = list(map(int, input_list))
    return input_list

def find_sum_set_N_pairs(preamble_set, N):

    found_pair = False
    for x in preamble_set:
        if abs( x - N) in preamble_set and (N/2 != N):
            found_pair =  True
            break 
    
    return found_pair

def find_seq_add_to_N(input_list, N):
    
    start = 0
    end = 2

    while(1):

        net_sum = sum(input_list[start:end])

        if net_sum > N:
            start += 1
        elif net_sum < N:
            end += 1
        else:
            break

    print('Matching set ', input_list[start:end] )
    print('Find the sum of match', max(input_list[start:end])+min(input_list[start:end]))

def find_odd_number(input_list, preamble_len = 5):

    # create the first set
    remaining_set = input_list[preamble_len:]
    i = 0
    for num in remaining_set:
        preamble_set  = input_list[i : i + preamble_len]
        if not find_sum_set_N_pairs(preamble_set, num):
            break
        i += 1
    
    print('The unpaired number', num)
    return num

def main():
    input_file = 'D:\Projects\AdventOfCode2020\day9\input.txt'
    input_list = input_parser(input_file)

    # puzzle 1
    N = find_odd_number(input_list, preamble_len=25)

    # puzzle 2
    find_seq_add_to_N(input_list, N)

if __name__ == "__main__":
    main()
