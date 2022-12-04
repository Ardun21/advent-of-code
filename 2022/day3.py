from string import ascii_lowercase

def get_priority(x):
    if x in ascii_lowercase:
        return ascii_lowercase.index(x) + 1
    else:
        return 26 + ascii_lowercase.index(x.lower()) + 1

def main():
    with open('input/day3.txt') as f:
        total_priority = 0
        for line in f:
            line = line.strip()
            cut = len(line) // 2
            comp1, comp2 = set(line[:cut]), set(line[cut:])
            total_priority += get_priority(list(comp1.intersection(comp2))[0])
            
        f.seek(0)

        badge_priority = 0
        group = []
        for line in f:
            group.append(line.strip())
            if len(group) == 3:
                bag1, bag2, bag3 = set(group[0]), set(group[1]), set(group[2])
                badge_priority += get_priority(list(bag1.intersection(bag2, bag3))[0])
                group = []

        print(f'Part 1: {total_priority}')
        print(f'Part 2: {badge_priority}')

if __name__ == '__main__':
    main()