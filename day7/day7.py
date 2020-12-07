from collections import defaultdict

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')

    outer_colour_dict = defaultdict(lambda: {})
    for line in input_list:
        if 'no other bags' not in line: 
            outer_colour, right = line.split(' bags contain')
            outer_colour = outer_colour.replace(" ", "")
            # we can do the same operation with filter by spliting with white space and filtering out bags, bag

            inner_colours = right.replace(" ", "").replace('bags', "").replace('bag', "").strip('.').split(',')
            # inner_colours =  ['1brightwhite', '2mutedyellow'] for a input line of light red bags contain 1 bright white bag, 2 muted yellow bags.

            inner_colours_dict = { colour[1:]: int(colour[0])  for colour in inner_colours}

            outer_colour_dict[outer_colour] = inner_colours_dict

    return outer_colour_dict

def find_number_of_outer_bags(outer_colour_dict, search_bag):

    # search for the "search bag" in the outer_colour_dict.values()
    # if is the present then search add the key to the search bag

    search_bag_list = [search_bag]
    result = []
    while search_bag_list:
        current_search_bag  = search_bag_list.pop()
        for key, inner_bags_dict in outer_colour_dict.items():
            # check if current_search_bag is in the values
            if current_search_bag in inner_bags_dict.keys():
                search_bag_list.append(key)
                result.append(key)

    print('Number of outerbags', len(set(result)))

def find_number_of_inside_bags(outer_colour_dict, search_bag):

    count = 0
    inner_bags_dict = outer_colour_dict[search_bag]
    # print(search_bag, inner_bags_dict, count)
    for key, nobags in inner_bags_dict.items():
        count += nobags + nobags * find_number_of_inside_bags(outer_colour_dict, key)
    return count

def main():
    input_file = 'D:\Projects\AdventOfCode2020\day7\input.txt'
    outer_colour_dict = input_parser(input_file)
    
    # puzzle 1
    search_bag="shiny gold"
    # find_number_of_outer_bags(outer_colour_dict, search_bag.replace(" ", ""))

    # puzzle 2
    print('number of inner_bags', find_number_of_inside_bags(outer_colour_dict, search_bag.replace(" ", "")))
    

if __name__ == "__main__":
    main()

