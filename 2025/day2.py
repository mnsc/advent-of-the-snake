import re

with open("day2.txt") as f:
    ranges = f.read().split(",")
    total_part1 = 0
    total_part2 = 0
    for r in ranges:
        (lower, upper) = r.split("-")
        for int_a in range(int(lower), int(upper) + 1):
            str_a = str(int_a)
            if re.match(r"^(\d+)\1$", str_a):
                total_part1 += int_a
            if re.match(r"^(\d+)\1+$", str_a):
                total_part2 += int_a

    print(f"part 1 - {total_part1}")
    print(f"part 2 - {total_part2}")

