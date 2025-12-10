def get_joltage(bank: str, no_of_flips: int):
    length = len(bank)
    start = 0
    joltage_digits = []
    for flip in range(no_of_flips):
        this_max = 0
        for chk in range(start, length - no_of_flips + flip + 1):
            chk_digit = int(bank[chk])
            if chk_digit > this_max:  # strict gt
                this_max = chk_digit
                start = chk + 1
        joltage_digits.append(this_max)
    return int(''.join(map(str, joltage_digits)))


def sum_up_joltage(lines: list[str], part, flips):
    total_j = 0
    for bank in lines:
        total_j += get_joltage(bank, flips)
    print(f"Part {part} - total joltage = {total_j}")


def main():
    with open("day3.txt") as f:
        lines = f.read().splitlines()
        sum_up_joltage(lines, 1, 2)
        sum_up_joltage(lines, 2, 12)


if __name__ == '__main__':
    main()
