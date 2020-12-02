import itertools as it

def findSum2N(input_list, N):

    # sort the list 
    input_list = sorted(input_list)  

    # sort the input list
    start_ptr = 0
    end_ptr = len(input_list)-1

    for i in range(len(input_list)):

        N_sum = input_list[start_ptr] +  input_list[end_ptr]
        if N == N_sum:
            print('Combinations ',  input_list[end_ptr], input_list[start_ptr])
            break
        elif N > N_sum:
            start_ptr = start_ptr + 1
        else:
            end_ptr = end_ptr - 1


def find_mNum_Sum2N(input_list, N):

    all_set = set()

    for num1, num2 in it.combinations(input_list, 2):
        if N - num1 - num2 in all_set:
            print(num1 * num2 * (N - num1 - num2))
            break
        all_set.add(num1)
        all_set.add(num2)


def main():
    N=2020
    inputFile='D:\Projects\AdventOfCode2020\day1\input.txt'
    
    print('N', N)

    # convert the inputFile to list   
    with open(inputFile) as f:
        input_list = list(map(int, f.read().split('\n')[:-1]))

     
    print('InputList',input_list )

    # findSum2N(input_list, N)
    find_mNum_Sum2N(input_list, N)

if __name__ == "__main__":
    main()