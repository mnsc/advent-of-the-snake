def main():
    with open("day4.txt") as f:
        lines = f.read().splitlines()
        floor_map = [list(line) for line in lines]
        free_rolls = 0
        for r, row in enumerate(floor_map):
            for c in range(len(row)):
                surrounding = 0
                if r > 0:
                    if c > 0 and floor_map[r - 1][c - 1] == '@':
                        surrounding += 1
                    if floor_map[r - 1][c] == '@':
                        surrounding += 1
                    if c < len(row) - 1 and floor_map[r - 1][c + 1] == '@':
                        surrounding += 1
                if r < len(floor_map) - 1:
                    if c > 0 and floor_map[r + 1][c - 1] == '@':
                        surrounding += 1
                    if c < len(row) - 1 and floor_map[r + 1][c + 1] == '@':
                        surrounding += 1
                    if floor_map[r + 1][c] == '@':
                        surrounding += 1
                if c > 0 and floor_map[r][c - 1] == '@':
                    surrounding += 1
                if c < len(row) - 1 and floor_map[r][c + 1] == '@':
                    surrounding += 1

                if floor_map[r][c] == '@' and surrounding < 4:
                    free_rolls += 1
                    print(surrounding, end='')
                else:
                    print(floor_map[r][c], end='')
            print("")

        print("-" * 20)
        print(f"part 1 - {free_rolls}")

if __name__ == '__main__':
    main()
