import re 

def input_parser(input_file):
    """
    sample : 
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929
    .
    .
    .

    
    """
    with open(input_file) as f:
        input_list = f.read().split('\n\n')

    passport_datas = []
    for row in input_list:
        data_dict = { field.split(':')[0] :field.split(':')[1]  for field in row.split()} # convert the row records to dict
        passport_datas.append(data_dict)

    return passport_datas

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
check_byr = lambda data : 1 if 1920 <= int(data['byr']) and (int(data['byr']) <= 2002) and (len(data['byr']) >= 4) else 0

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
check_iyr = lambda data : 1 if 2010 <= int(data['iyr']) and int(data['iyr']) <= 2020 and len(data['iyr']) >= 4 else 0

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
check_eyr = lambda data : 1 if 2020 <= int(data['eyr']) and int(data['eyr']) <= 2030 and len(data['eyr']) >= 4 else 0

def check_hgt(data):
    # a number followed by either cm or in: 
    # print('hgt_data', data)
    hgt_data = data['hgt']
    
    if ('cm' not in hgt_data) and ('in' not in hgt_data):
        return 0

    # If cm, the number must be at least 150 and at most 19
    if ( 'cm' in hgt_data ) :
        return 1  if ( 150 <= int(hgt_data.split('cm')[0]) ) and ( int(hgt_data.split('cm')[0]) <= 193 ) else 0

    #If in, the number must be at least 59 and at most 76.
    if ( 'in' in hgt_data ):
        return 1 if ( 59 <= int(hgt_data.split('in')[0]) ) and ( int(hgt_data.split('in')[0]) <= 76 ) else 0
        
check_hcl = lambda data : 1 if re.search("^(#[\da-f]{6})$", data['hcl']) else 0

# exactly one of: amb blu brn gry grn hzl oth.
check_ecl = lambda data : 1 if ( len(data['ecl']) == 3 ) and (data['ecl'] in [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) else 0

# pid (Passport ID) - a nine-digit number, including leading zeroes.
check_pid = lambda data : 1 if len(data['pid']) == 9 and ( data['pid'].isdecimal() ) else 0

check_valid_record = lambda data : check_byr(data) * check_iyr(data) * check_eyr(data) * check_hgt(data) * check_hcl(data) * check_ecl(data) * check_pid(data)


def main():
    input_file = 'D:\Projects\AdventOfCode2020\day4\input.txt'
    # input_file = 'D:\Projects\AdventOfCode2020\day4\sample_input_invalid.txt'
    passport_datas = input_parser(input_file)

    # # puzzle 1
    # valid_data = 0
    # for data in passport_datas:
    #     valid_data += len(data) == 8
    #     valid_data += (len(data) == 7) and ('cid' not in  data.keys())
    
    # print('number of valid data', valid_data)

    # puzzle 2
    valid_data = 0
    for data in passport_datas:
        if len(data) == 8 or ( (len(data) == 7) and ('cid' not in  data.keys()) ) :
            valid_data += check_valid_record(data)
    
    print('number of valid data', valid_data)


if __name__ == "__main__":
    main()
