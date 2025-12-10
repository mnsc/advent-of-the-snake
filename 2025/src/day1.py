
def main():
    with open("day1.txt") as f:
        position = 50
        total_position = 50
        zero_count = 0
        passing_zero_count = 0
        lines = f.read().splitlines()
        for line in lines:
            print("---")
            before_div = total_position // 100
            direction = line[0]
            distance = int(line[1:])
            print(f"line: {line} is direction: {direction} and distance: {distance}")
            if direction == "R":
                position += distance
                total_position += distance
            elif direction == "L":
                position -= distance
                total_position -= distance
            else:
                raise ValueError("WTF!?!!")

            position = position % 100
            print(f"New position is: {position} with total_position: {total_position}")
            after_div = total_position // 100
            if position == 0:
                zero_count += 1

            passing_zero_count += abs(before_div - after_div)

            print(f"before: {before_div} after: {after_div} -> {passing_zero_count}")

    print(f"Part 1 - {zero_count}")
    # WIP too many if:s to consider for now print(f"Part 2 - {passing_zero_count}")

if __name__ == '__main__':
    main()