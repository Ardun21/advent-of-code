from typing import Tuple

class Shape():
    def __init__(self):
        self.points = 0
        self.beats = None
        self.loses = None

class Rock(Shape):
    def __init__(self):
        self.points = 1
        self.beats = Scissors
        self.loses = Paper

class Paper(Shape):
    def __init__(self):
        self.points = 2
        self.beats = Rock
        self.loses = Scissors

class Scissors(Shape):
    def __init__(self):
        self.points = 3
        self.beats = Paper
        self.loses = Rock

shapes = {
    'A': {
        'shape': Rock,
        'X': Scissors,
        'Y': Rock,
        'Z': Paper 
    },
    'B': {
        'shape': Paper,
        'X': Rock,
        'Y': Paper,
        'Z': Scissors
    },
    'C': {
        'shape': Scissors,
        'X': Paper,
        'Y': Scissors,
        'Z': Rock
    }
}

def shape_from_string(s):
    if s == 'A' or s == 'X':
        return Rock()
    elif s == 'B' or s == 'Y':
        return Paper()
    elif s == 'C' or s == 'Z':
        return Scissors()

def shapes_from_strings(s1, s2):
    return shapes[s1]['shape'](), shapes[s1][s2]()

def main():
    with open('input/day2.txt') as f:
        score_part1, score_part2 = 0, 0
        for line in f:
            p1, p2 = line.split()
            result = r_p_s(shape_from_string(p1), shape_from_string(p2))
            score_part1 += result[1] + result[2]

            result = r_p_s(*shapes_from_strings(p1, p2))
            score_part2 += result[1] + result[2]

    print(f'Score for Part 1: {score_part1}\nScore for Part 2: {score_part2}')

def r_p_s(p1: Shape, p2: Shape) -> Tuple[int, int, int]:
    tp1, tp2 = type(p1), type(p2)
    if tp1 == tp2:
        return (p1.points, p2.points, 3)
    elif tp2 == p1.loses:
        return (p1.points, p2.points, 6)
    else:
        return (p1.points, p2.points, 0)


if __name__ == '__main__':
    main()