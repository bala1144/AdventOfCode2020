from itertools import combinations
from memoization import cached

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')
    
    input_list = list(map(int, input_list))
    return input_list

def find_differences(input_list):

    input_list.sort()
    diff_list = list(map(int.__sub__, input_list[1:] , input_list[:-1]))
    # print(diff_list)

    diff_extract =  { i:diff_list.count(i) for i in set(diff_list) }
    # print(diff_extract)
    return diff_extract


def check_combination_list(comb_list, maxEle):
    valid_list = 0
    # must contain the first and last element
    if 0 in comb_list and maxEle in comb_list:
        comb_list = sorted(comb_list)
        
        diff_list = list(map(int.__sub__, comb_list[1:] , comb_list[:-1]))
        # print(diff_list)
        diff_set = set(diff_list)
        # print(diff_set)
        intersection_set =  set.intersection(diff_set, set(range(4,maxEle)))
        # print('intersection_set', intersection_set)
        if len(intersection_set) == 0:
            # print('valid set')
            # print(comb_list)
            valid_list = 1

    return valid_list


@cached()
def recursive_find_distinct_adapter_arrangments(input_list, start, maxElement):

    current_possible_list = []
    if maxElement not in input_list:
        return 1

    num_possiblities = 0   
    for i in [1,2,3]:
        next_elem  = start + i
        if next_elem in input_list:
            # grow the combination tree
            next_list = input_list.copy()
            next_list.remove(next_elem)
            num_possiblities += recursive_find_distinct_adapter_arrangments(next_list, next_elem, maxElement)

    return num_possiblities
        

def find_distinct_adapter_arrangments(input_list):
    input_list.append(0) # add 0
    input_list.append(max(input_list) + 3) # add max adapter
    
    num_of_combination = 0
    for i in range(len(input_list) - 3):
        combintion_result = combinations(input_list, len(input_list) - i )
        current_set_result = [check_combination_list(combination, max(input_list)) for combination in combintion_result]
        num_of_combination += sum(current_set_result)
        print('Len', len(input_list) - i, 'total comb', len(current_set_result), 'Sum of valid' ,sum(current_set_result), 'Cum sum', num_of_combination)
        if sum(current_set_result) == 0:
            break
    
    print('Number of valid distinct combinations', num_of_combination)

def main():
    input_file = 'D:\Projects\AdventOfCode2020\day10\input.txt'
    input_list = input_parser(input_file)
    # print(input_list)
    input_list.append(0) # add 0
    input_list.append(max(input_list) + 3) # add max adapter 
    input_list.sort()

    diff_extract = find_differences(input_list)
    print('the product of 3 dif and 1 diff',(diff_extract[3]) * (diff_extract[1]) )

    # find_distinct_adapter_arrangments(input_list)
    num_possiblities = recursive_find_distinct_adapter_arrangments(input_list, 0 , max(input_list))
    print('Number of valid possiblities',num_possiblities )


def puzzle_2_ref_fn():
    numbers = {int(i) for i in open('D:\Projects\AdventOfCode2020\day10\sample_input1.txt')}
    print('Numbers', numbers)
    numbers_paths_map = {n:0 for n in numbers}         
    print('numbers_paths_map', numbers_paths_map)                            
    last = pivot = 0                                                                
    ordered = []                                                                    
    numbers_paths_map[0] = 1                                                        

    while len(numbers) != len(ordered):                                             
        ordered.append(pivot)                                                       
        for value in [1, 2, 3]:                                                     
            if pivot+value in numbers:                                              
                pivot += value                                                      
                break
    
    for value in ordered:                                                           
        for j in [1, 2, 3]:                                                        
            if value+j in numbers:  
                                                            
                numbers_paths_map[value+j] += numbers_paths_map[value]             
                last = numbers_paths_map[value+j]

                print('Ordered', ordered)
                print('Val', value, 'j', j,  'In Num', value+j )  
                print('numbers_paths_map', numbers_paths_map)                            
                print('last', last)  
                print() 
    print(last)     




if __name__ == "__main__":
    # main()
    def puzzle_2_ref_fn()