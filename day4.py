def parse_guard_events(lines):
    def parse_event(line):
        dt = line[:16]
        timestamp = int(dt[:16].replace("-","").replace(" ","").replace(":",""))
        evt = { "timestamp": timestamp, "minutes": int(dt[14:16]) }
        words = line.strip().split(" ")
        if words[2] == "wake":
            evt["type"] = "wake"
        elif words[2] == "sleep":
            evt["type"] = "sleep"
        else:
            evt["type"] = "shift"
            evt["guard_id"] = int(words[2])

        return evt

    ev = list(map(parse_event, lines))
    return sorted(ev, key=lambda x: x["timestamp"])


def aggregate_guard_stats(guard_events):
    stats = {}
    guard = None
    start_minute = None
    for ev in guard_events:
        if ev["type"] == "shift":
            guard_id = ev["guard_id"]
            if guard_id not in stats:
                guard = {
                    "guard_id": guard_id,
                    "total_slept": 0,
                    "sleep_breakdown": {}
                }
                stats[guard_id] = guard
            else:
                guard = stats[guard_id]
        elif ev["type"] == "sleep":
            start_minute = ev["minutes"]
        else:
            end_minute = ev["minutes"]
            for minute in range(start_minute, end_minute):
                guard["total_slept"] += 1
                if minute not in guard["sleep_breakdown"]:
                    guard["sleep_breakdown"][minute] = 1
                else:
                    guard["sleep_breakdown"][minute] += 1
    return stats


def find_laziest_guard(guard_stats):
    laziest_id = max(guard_stats, key=lambda g: guard_stats[g]["total_slept"])
    return guard_stats[laziest_id]


def find_favorite_minute(guard_stat):
    tbl = guard_stat["sleep_breakdown"]
    return max(tbl, key=lambda m: tbl[m])


def part_1(guard_events):
    guard_stats = aggregate_guard_stats(guard_events)
    laziest_guard = find_laziest_guard(guard_stats)
    best_minute = find_favorite_minute(laziest_guard)
    print("Laziest guard = {}".format(laziest_guard["guard_id"] * best_minute))


def find_most_predictable_guard(guard_stats):
    all_minutes = {}
    for guard in guard_stats.values():
        guard_id = guard["guard_id"]
        for minute in guard["sleep_breakdown"]:
            key = "{}-{}".format(guard_id, minute)
            all_minutes[key] = guard["sleep_breakdown"][minute]
    p = max(all_minutes, key=lambda k: all_minutes[k]).split("-")
    return (int(p[0]), int(p[1]))


def part_2(guard_events):
    guard_stats = aggregate_guard_stats(guard_events)
    (guard_id, fav_minute) = find_most_predictable_guard(guard_stats)
    print("Predictable guard = {}".format(guard_id * fav_minute))


def main():
    with open("./day4.txt") as lines:
        guard_events = parse_guard_events(lines)
        part_1(guard_events)
        part_2(guard_events)


if __name__ == "__main__":
    main()

