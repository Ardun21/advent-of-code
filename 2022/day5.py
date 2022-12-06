import re

s1 = ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P']
s2 = ['M', 'Q', 'H']
s3 = ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L']
s4 = ['Z', 'T', 'F', 'Q', 'M', 'W', 'G']
s5 = ['M', 'T', 'H', 'P']
s6 = ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T']
s7 = ['M', 'N', 'B', 'F', 'V', 'R']
s8 = ['P', 'L', 'H', 'M', 'R', 'G', 'S']
s9 = ['P', 'D', 'B', 'C', 'N']

stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

with open('input/day5.txt') as f:
    for line in f:
        move_count, src, dest = [int(x) for x in re.sub(r'(move |from |to )', '', line.strip()).split(' ')]
        src_stack = stacks[src - 1]
        dest_stack = stacks[dest - 1]
        crates_to_move = src_stack[-move_count:]
        # crates_to_move.reverse() # uncomment for 'CrateMover 9000' behavior

        stacks[src - 1] = src_stack[:-move_count]
        stacks[dest - 1] = dest_stack + crates_to_move

    print(''.join([x[-1] for x in stacks]))
