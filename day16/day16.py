import re
from operator import methodcaller

def find_invalid_ticket_sum(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n\n')

        conditional_range = list(map(int,re.findall("\d+",input_list[0])))
        my_tickets = list(map(int,re.findall("\d+",input_list[1])))
        other_tickets = list(map(int,re.findall("\d+",input_list[2])))

        # valid range list
        valid_tickets = []
        for i in range(0,len(conditional_range), 2):
            valid_tickets.extend(list(range(conditional_range[i], conditional_range[i+1]+1)))    
        valid_tickets = set(valid_tickets)

    return sum([x for x in other_tickets if x not in valid_tickets])

def all_conditions_fieldwise(input_list):

    # extract only the condition for the departure seperatly
    condition_dict_ranges = []
    condition_dict_names = []
    for line in input_list[0].split('\n'):
            ranges = list(map(int,re.findall("\d+",line)))
            field_list = []
            for i in range(0,len(ranges), 2):
                field_list.extend(list(range(ranges[i], ranges[i+1]+1))) 
            condition_dict_ranges.append(field_list)
            condition_dict_names.append(line[:line.find(':')])
    
    return condition_dict_names, condition_dict_ranges

def find_field(input_file, field='departure'):
    with open(input_file) as f:
        input_list = f.read().split('\n\n')
        print(input_list)
    condition_dict_names, condition_dict_ranges = all_conditions_fieldwise(input_list)

    # extarct the valid tickets records
    my_tickets = list(map(int,re.findall("\d+",input_list[1])))
    other_tickets =  [ list(map(int,re.findall("\d+",line))) for line in input_list[2].split('\n')[1:] ]
    other_tickets.append(my_tickets)

    # create the list for all the valid ticket
    conditional_range = list(map(int,re.findall("\d+",input_list[0])))
    all_valid_number_possibilites = []
    for i in range(0,len(conditional_range), 2):
        all_valid_number_possibilites.extend(list(range(conditional_range[i], conditional_range[i+1]+1)))    
    all_valid_number_possibilites = set(all_valid_number_possibilites)

    valid_tickets = []
    for ticket in other_tickets: # check all the fields are from the valid number possibilites
        if all(num in all_valid_number_possibilites for num in ticket):
            valid_tickets.append(ticket)

    # # using the valid tickets find the column
    depature_cols = {}
    while len(depature_cols) != len(valid_tickets[0]): # run until labels are assigned for all the cols
        for name,valid_options in zip(condition_dict_names, condition_dict_ranges):
            col_list = []
            for i, col in enumerate(zip(*valid_tickets)):
                if all(num in valid_options for num in col):
                    col_list.append(i)
                if len(col_list) <= 1: # continue; more then one label is assigned to the col
                    break
            if len(col_list) == 1:
                depature_cols[name] = col_list[0]
                condition_dict_names.remove(name)
                condition_dict_ranges.remove(valid_options)
                print('assinged', name)
                print('Total', depature_cols.keys())
                print('remaining', len(valid_tickets[0]) - len(depature_cols))
                print('remaining condition', len(condition_dict_ranges), len(condition_dict_names))

    print('depature cols',depature_cols )
    print('other tickets len', len(other_tickets))
    print('Valid ticket len', len(valid_tickets))

def main():
    # input_file = 'D:\Projects\AdventOfCode2020\day16\sample_input.txt'
    input_file = 'D:\Projects\AdventOfCode2020\day16\input.txt'

    # puzzle 1
    # print('Sum of the invalid other tickets', find_invalid_ticket_sum(input_file))

    # puzzle 2
    print('Sum of the invalid other tickets', find_field(input_file))

if __name__ == "__main__":
    main()