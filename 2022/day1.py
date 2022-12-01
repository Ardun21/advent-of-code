from typing import List

class Elf:
    def __init__(self, items: List[int]):
        self.items = items
        self.total_calories = sum(i for i in self.items)

def sum_first_n(l, n) -> int:
    return sum(i.total_calories for i in l[0:n])

def main():
    elves = []
    with open("input/day1-1.txt") as f:
        items = []
        for line in f:
            if line.strip():
                items.append(int(line))
            else:
                elves.append(Elf(items))
                items = []

    elves = sorted(elves, key = lambda e: e.total_calories, reverse=True)

    # get total cals for top elf
    print(sum_first_n(elves, 1))

    # get total cals for top 3 elves
    print(sum_first_n(elves, 3))

if __name__ == "__main__":
    main()