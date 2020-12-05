

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')
    
    seat_id_set = set()
    
    for seat in input_list:
        seat_id_set.add(int(seat.translate("".maketrans("FLBR", "0011")),2))

    return seat_id_set

def main():
    input_file = 'D:\Projects\AdventOfCode2020\day5\input.txt'
    seat_id_set = input_parser(input_file)

    # puzzle 1
    # print('max of seat id', max(seat_id_set) )
    
    # puzzle 2 find the missing set
    print( set(range(min(seat_id_set), max(seat_id_set))) - seat_id_set )
    print('')
if __name__ == "__main__":
    main()

