from datetime import datetime


def parse_event_data(line):
    words = line.strip().split(" ")
    if words[2] == "wake":
        return {
            "type": "wake"
        }
    elif words[2] == "sleep":
        return {
            "type": "sleep"
        }
    else:
        return {
            "type": "shift",
            "guard_id": int(words[2])
        }


def parse_guard_events(lines):
    def parse_event(line):
        evt_data = parse_event_data(line)
        evt = {
            "datetime": datetime.strptime(line[:16], "%Y-%m-%d %H:%M"),
            **evt_data
        }
        return evt

    ev = list(map(parse_event, lines))
    return sorted(ev, key=lambda x: x["datetime"].timestamp())


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
            start_minute = ev["datetime"].time().minute
        else:
            end_minute = ev["datetime"].time().minute
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
    if tbl:
        return max(tbl, key=lambda m: tbl[m])
    else:
        return 0


def part_1(guard_events):
    guard_stats = aggregate_guard_stats(guard_events)
    laziest_guard = find_laziest_guard(guard_stats)
    best_minute = find_favorite_minute(laziest_guard)
    print("Laziest guard = {}".format(laziest_guard["guard_id"] * best_minute))


def find_most_predictable_guard(guard_stats):
    pred_id = max(guard_stats, key=lambda g: find_favorite_minute(guard_stats[g]))
    return guard_stats[pred_id]


def part_2(guard_events):
    guard_stats = aggregate_guard_stats(guard_events)
    predictable = find_most_predictable_guard(guard_stats)
    best_minute = find_favorite_minute(predictable)
    print("Predictable guard = {}".format(predictable["guard_id"] * best_minute))


def main():
    with open("./day4.txt") as lines:
        guard_events = parse_guard_events(lines)
        part_1(guard_events)
        part_2(guard_events)


if __name__ == "__main__":
    main()
