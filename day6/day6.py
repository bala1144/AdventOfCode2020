

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n\n')

    return input_list

def main():
    input_file = 'D:\Projects\AdventOfCode2020\day6\input.txt'
    input_list = input_parser(input_file)

    # puzzle 1
    print('The count of answers ', sum([len(set(answer.replace('\n', ''))) for answer in input_list]))

    # puzzle 2
    print('The count of answers ', sum([ len(set.intersection(*map(set, answer.split('\n')))) for answer in input_list]))
    
    # split up for better understanding
    # for answer in input_list :
    #   group_set = map(answer.split('\n')) # split everything into set and create all them into group
    #   intersection_set = set.intersection(*group_set) # intersection amoung all the sets
    

if __name__ == "__main__":
    main()

