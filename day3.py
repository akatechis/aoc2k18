def parse_claim(line):
    tokens = line.split(" ")
    claim = {
        "claim_id": int(tokens[0]),
        "x": int(tokens[1]),
        "y": int(tokens[2]),
        "w": int(tokens[3]),
        "h": int(tokens[4])
    }
    return claim


def apply_claims(claims):
    tiles = {}
    for cl in claims:
        x, y, w, h = cl["x"], cl["y"], cl["w"], cl["h"]
        for a in range(x, x + w):
            for b in range(y, y + h):
                key = (a, b)
                if key not in tiles:
                    tiles[key] = "C"
                else:
                    tiles[key] = "X"
    return tiles


def count_conflicted_tiles(tiles):
    def tile_conflicted(tile):
        return tile is "X"
    return len(list(filter(tile_conflicted, tiles.values())))


def part_1(claims):
    tiles = apply_claims(claims)
    count = count_conflicted_tiles(tiles)
    print("Number of conflicted tiles = {}".format(count))


def claim_is_conflicted(tiles, claim):
    x, y, w, h = claim["x"], claim["y"], claim["w"], claim["h"]
    for a in range(x, x + w):
        for b in range(y, y + h):
            key = (a, b)
            if tiles[key] is "X":
                return True
    return False


def find_conflict_free_claim(tiles, claims):
    for cl in claims:
        if not claim_is_conflicted(tiles, cl):
            return cl


def part_2(claims):
    tiles = apply_claims(claims)
    conflict_free = find_conflict_free_claim(tiles, claims)
    print("Conflict free claim = {}".format(conflict_free["claim_id"]))


def main():
    with open("day3.txt") as lines:
        claims = list(map(parse_claim, lines))
        part_1(claims)
        part_2(claims)


def print_tiles(tiles, w, h):
    for y in range(0, h):
        for x in range(0, w):
            key = (x, y)
            if key not in tiles:
                print(".", end="")
            else:
                print(tiles[key], end="")
        print()


if __name__ == '__main__':
    main()
