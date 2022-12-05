with open('input/day4.txt') as f:
    c1 = 0
    c2 = 0
    for line in f:
        e1, e2 = line.strip().split(',')
        e1_start, e1_end = [int(x) for x in e1.split('-')]
        e2_start, e2_end = [int(x) for x in e2.split('-')]

        if e1_start <= e2_start and e2_end <= e1_end:
            c1 += 1
        elif e2_start <= e1_start and e1_end <= e2_end:
            c1 += 1

        if e2_start <= e1_start <= e2_end:
            c2 += 1
        elif e2_start <= e1_end <= e2_end:
            c2 += 1
        elif e1_start <= e2_start <= e1_end:
            c2 += 1
        elif e1_start <= e2_end <= e1_end:
            c2 += 1

    print(c1)
    print(c2)