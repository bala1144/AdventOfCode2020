import itertools
import numpy as np
from collections import defaultdict
import copy
import re

def input_parser(input_file):
    """Read the input and get the inputs are parsing

    """
    with open(input_file) as f:
        input_list = f.read().split('\n\n')
    
    players_dict = {}
    for line in input_list:
        line = line.split('\n')
        players_dict[int(re.search(r"\d", line[0]).group())] = list(map(int, line[1:]))
    
    return players_dict

def simulate_combat_game(players_dict):
    """ Game Rules 
    
    Before the game starts, split the cards so each player has their
    own deck (your puzzle input). Then, the game consists of a series of
    rounds: both players draw their top card, and the player with the 
    higher-valued card wins the round. The winner keeps both cards, placing
    them on the bottom of their own deck so that the winner's card is above
    the other card. If this causes a player to have all of the cards, 
    they win, and the game ends


    """
    print(players_dict)
    i = 2
    while True:

        values = [ players_dict[key].pop(0) for key in sorted(players_dict.keys()) ]
        
        # rearrange list the set the max at the first
        max_val =  max(values)
        max_index = values.index(max(values))
        values.remove(max_val)
        values.insert(0,max_val)
        players_dict[max_index+1].extend(values)
        # print(i,players_dict,values)
        if any( [ len(values) == 0 for key, values in players_dict.items()]):
            break
        
        i += 1
    for j, values in enumerate(players_dict.values()):
        if len(values) != 0:
            print('winning set', values)
            score = sum([ int(x) * (i+1) for i, x in enumerate(values[::-1])] )
            print('Winning Player ', j+1 , 'score', score)

def recursive_combat_game(p1,p2, score=False):
    """Recursive version of the combat game is played
    """
    p1_seen = set()
    p2_seen = set()
    i = 0
    while True:

        p1_seq = ' '.join(map(str, p1))
        p2_seq = ' '.join(map(str, p2))
        if p1_seq in p1_seen or p2_seq in p2_seen :
            return 1, False # winner, score
        else: 
            p1_seen.add(p1_seq)
            p2_seen.add(p2_seq)

        p1c = p1.pop(0)
        p2c = p2.pop(0)
        # player recursive game find the winner
        if p1c <= len(p1) and p2c <= len(p2):
            p1_sub = p1.copy()[:p1c]
            p2_sub = p2.copy()[:p2c]
            winner, _ =  recursive_combat_game(p1_sub, p2_sub)
        else:
            winner = 1 if p1c > p2c else 2

        if winner == 1 :
            # append the first player
            p1.extend([p1c,p2c])
            win_set = p1      
        elif winner == 2:
            # append the second player
            p2.extend([p2c,p1c])
            win_set = p2

        i+=1  
        if len(p1) == 0 or len(p2) == 0:
            if score:
                score = sum([ (i+1) * item for i, item in enumerate(win_set[::-1]) ])
            # game ended  
            return winner, score 

def main():
    # input_file = 'D:\Projects\AdventOfCode2020\day22\sample_input.txt'
    input_file = 'D:\Projects\AdventOfCode2020\day22\input.txt'
    players_dict = input_parser(input_file)
    # simulate_combat_game(players_dict)
    winner, score = recursive_combat_game(players_dict[1], players_dict[2], score=True)
    print('part 2 winning score', score)


if __name__ == "__main__":
    main()