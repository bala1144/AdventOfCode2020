import unittest
from day8 import fix_infinite_loop_instruction, find_first_infintite_loop_instruction, input_parser

class day8Class(unittest.TestCase):

    def setUp(self):
        sample_input = 'D:\Projects\AdventOfCode2020\day8\sample_input.txt'
        self.parsed_input = input_parser(sample_input)


    def test_puzzle1(self):
        accumulator, _ = find_first_infintite_loop_instruction(self.parsed_input)
        self.assertEqual(accumulator, 5)

    
    def test_puzzle2(self):
        accumulator = fix_infinite_loop_instruction(self.parsed_input)
        self.assertEqual(accumulator, 8)
        
if __name__ == '__main__':
    unittest.main()