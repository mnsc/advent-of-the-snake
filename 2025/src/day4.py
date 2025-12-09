def main():
    with open("day4.txt") as f:
        lines = f.read().splitlines()
        floor_map = [list(line) for line in lines]

        for x in floor_map:
            for y in x:
                print(y, end='')
            print("")


if __name__ == '__main__':
    main()