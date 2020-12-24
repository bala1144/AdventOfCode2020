import math 

def simulate_cup_game(input, num_round=10): 
    
    curr_num = input[0]
    num_elem = len(input)
    max_num = max(input)
    min_num = min(input)


    for round in range(1, num_round+1):

        # get the position
        # print(round, input)
        curr_num_idx = input.index(curr_num)
        next_num = input[(curr_num_idx + 4) % len(input)]

        # pop nxt 3 elements
        next_elems = [ input.pop( (input.index(curr_num)+1) % len(input)) for x in range(3)]

        # find the insert position
        find = True
        insert_num = curr_num - 1 
        if insert_num < min_num:
            insert_num = max_num
        while find:
            if insert_num not in next_elems:
                find = False
            else:
                insert_num = insert_num - 1 
                if insert_num < min_num:
                    insert_num = max_num

        curr_num = next_num

        # insert nxt to insert position
        insert_elem_idx = input.index(insert_num)
        for i, num in enumerate(next_elems):
            idx = (insert_elem_idx+i+1)
            input.insert( idx , num )

    return input

def part1(input, num_round=10):

    input = list(map(int, list(input)))
    num_elem = len(input)
    final_list = simulate_cup_game(input,num_round )

    # wrap the list to find the out string
    start_index = final_list.index(1)
    print(''.join( [str(final_list[ (start_index + x) % num_elem] ) for x in range(1, num_elem) ] ) )

def part2(input, num_round=10):

    crab_max_cup = 1000000
    crab_num_round = 10000000

    input = list(map(int, list(input)))
    max_val = max(input)
    
    # create list from max_val to 1000000 for second crab game
    input.extend(list(range(max_val+1,crab_max_cup+1)))
    num_elem = len(input)

    # simulate the game
    final_list = simulate_cup_game(input, crab_num_round )

    start_index = final_list.index(1)
    nxt_2_elems = final_list[ (start_index + 1) % num_elem : (start_index + 3) % num_elem ]
    print('two cups that will end up immediately clockwise of cup 1',  nxt_2_elems )
    print('product of next 2 cups',  math.prod(nxt_2_elems) )

def fast_part2(input):
    print(input)
    crab_max_cup = 1000000
    crab_num_round = 10000000

    input = list(map(int, list(input)))
    max_val = max(input)
    
    # create list from max_val to 1000000 for second crab game
    input.extend(list(range(max_val+1,crab_max_cup+1)))

    print(math.prod(play(input, 10000000)[1:3]))

# ************* code from https://github.com/MareinK/advent-of-code *******************#
# for learning using links improves the speed of access for the linked list setup
def play(cups, n):

    links = [None] * (len(cups) + 1)

    # creating the circuler linked list setup
    for c1, c2 in zip(cups, cups[1:] + [cups[0]]):
        links[c1] = c2

    max_num = max(cups)
    current = cups[0]

    for _ in range(n):
        
        picks = (links[current], links[links[current]], links[links[links[current]]])
        destination = current

        while destination in (current,) + picks:
            destination = max_num if destination == 1 else destination - 1

        links[current], links[destination], links[picks[-1]] = (
            links[links[links[links[current]]]],
            links[current],
            links[destination],
        )

        current = links[current]

    result = [1]
    while len(result) < len(cups):
        result.append(links[result[-1]])
    
    return result


def main():
    # sample_input = '389125467'
    sample_input = '925176834'

    # part1(sample_input,num_round=100)
    # part2(sample_input,num_round=100)
    fast_part2(sample_input)

if __name__ == "__main__":
    main()