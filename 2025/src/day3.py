def get_joltage(bank: str):
    max_val = 0
    for x in range(0, len(bank) - 1):
        for y in range(x + 1, len(bank)):
            max_val = max(max_val, int(bank[x] + bank[y]))
    return max_val


def main():
    with open("day3.txt") as f:
        lines = f.read().splitlines()
        total_j = 0
        for bank in lines:
            total_j += get_joltage(bank)

        print(f"part 1 - total joltage = {total_j}")


if __name__ == '__main__':
    main()
