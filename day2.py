def count_char_frequency(box_id):
    chars = {}
    for char in box_id:
        chars.setdefault(char, 0)
        chars[char] += 1
    return chars


def count_repeating_chars(box_ids, target_frequency):
    def matches(box_id):
        return target_frequency in count_char_frequency(box_id).values()
    matches = filter(matches, box_ids)
    return len(list(matches))


def part_1(box_ids):
    two_chars = count_repeating_chars(box_ids, 2)
    three_chars = count_repeating_chars(box_ids, 3)
    chk = two_chars * three_chars
    print("Checksum = {}".format(chk))


def box_ids_are_close_enough(left, right):
    diffs = 0
    for (a, b) in zip(list(left), list(right)):
        if a is not b:
            diffs += 1
    return diffs is 1


def extract_common_chars(left, right):
    common = ""
    for (a, b) in zip(list(left), list(right)):
        if a is b:
            common += a
    return common


def part_2(box_ids):
    for left_ptr in range(0, len(box_ids)):
        for right_ptr in range(left_ptr + 1, len(box_ids)):
            left = box_ids[left_ptr]
            right = box_ids[right_ptr]
            if box_ids_are_close_enough(left, right):
                common = extract_common_chars(left, right)
                print("Found a match: ({}, {})".format(left, right))
                print("Common characters: {}".format(common))


def main():
    with open("day2.txt") as lines:
        box_ids = list(lines)
        part_1(box_ids)
        part_2(box_ids)


if __name__ == '__main__':
    main()
