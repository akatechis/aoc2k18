def part_1(lines):
    fr = 0
    for step in lines:
        fr += int(step)
    print("Final frequency = {}".format(fr))


def part_2(lines):
    dupe = dupe_freq(lines)
    print("Duplicate frequency = {}".format(dupe))


def dupe_freq(lines):
    fr = 0
    freq_seen = {fr}

    while True:
        for step in lines:
            fr += int(step)
            if fr in freq_seen:
                return fr
            freq_seen.add(fr)


def main():
    with open("./day1.txt") as lines:
        lines = list(lines)
        part_1(lines)
        part_2(lines)


if __name__ == '__main__':
    main()
