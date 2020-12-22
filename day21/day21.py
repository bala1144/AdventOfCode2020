import itertools
import numpy as np
from collections import defaultdict
import copy
import re

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


def input_parser(input_file):
    """Read the input and get the inputs are parsing

    """
    with open(input_file) as f:
        input_list = f.read().split('\n')

    food = Dictlist()
    all_ingredients_set = []
    for line in input_list:
        allergens = set(line[:-1].split(" (contains ")[-1].split(", "))
        ingredients = set(line.split(" (contains ")[0].split(" "))
        all_ingredients_set.extend(list(ingredients))
        for x in allergens:
            food[x] = ingredients  

    return food, all_ingredients_set

def find_non_allergen_incredients(food_dict, all_ingredients_list):
    """ The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list

    Key rules :
    * Each allergen is found in exactly one ingredient.
    * Each ingredient contains zero or one allergen. 
    
    """
    # find the allergens ingredients based on the common element mapping
    allegern_ingredients = []
    allegern_ingredients_map = {}
    for keys in food_dict.keys():
        if len(food_dict[keys]) > 1:
            allegern_ingredients.extend( list( set.intersection(*food_dict[keys]) ) )
            allegern_ingredients_map[keys] = list( set.intersection(*food_dict[keys]) )
   
    # compute for the non-repeation set
    for keys in food_dict.keys():
        if len(food_dict[keys]) == 1:
            allegern = food_dict[keys][0] - set.intersection( food_dict[keys][0], set(allegern_ingredients) ) 
            allegern_ingredients.extend(allegern)
            allegern_ingredients_map[keys] = list(set.intersection(*food_dict[keys]) )

    
    # compose all the ingredients to one set
    all_ingredients_set = set(all_ingredients_list)
    non_allergen_set = all_ingredients_set - set(allegern_ingredients)
    num_of_non_allergen_occ = sum([ all_ingredients_list.count(x) for x in non_allergen_set])


    # part2
    refind_dict = {}
    allegren_set = set(allegern_ingredients)
    print('allegren_set', allegren_set)
    start_len = 1
    print('Number of Allgerns', len(food_dict.keys()) )
    while len(allegren_set):
        for keys, items in allegern_ingredients_map.items():             
            if len(items) == start_len and len(set.intersection(set(items), allegren_set)) > 0: 
                matched_ingred = set.intersection(set(items), allegren_set)
                matched_ingred = matched_ingred.pop()
                refind_dict[keys] = matched_ingred
                allegren_set.remove(matched_ingred)

        start_len = start_len + 1

        print('Number of Allgerns', len(food_dict.keys()) )
        print('refined dict', refind_dict)
        print('allegren_set', allegren_set)
    print('allegern_ingredients_map', allegern_ingredients_map)
    print('allegern_ingredients_map', len(allegern_ingredients_map))
    
    print('canonical string : ')
    print(','.join([refind_dict[x] for x in sorted( refind_dict.keys() )]))
    return num_of_non_allergen_occ


def main():
    # input_file = 'D:\Projects\AdventOfCode2020\day21\sample_input.txt'
    input_file = 'D:\Projects\AdventOfCode2020\day21\input.txt'
    food_dict, all_ingredients_set = input_parser(input_file)
    print('Number of non allergen ingredients',find_non_allergen_incredients(food_dict, all_ingredients_set))

if __name__ == "__main__":
    main()