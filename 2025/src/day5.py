def main():
    with open("day5.txt") as f:
        lines = f.read().splitlines()
        ingredients = set()
        parse_fresh = True
        fresh_ingredient_ranges = []
        fresh_ingredients = 0
        for line in lines:
            if line == "":
                parse_fresh = False
                continue

            if parse_fresh:
                (lower, upper) = line.split("-")
                fresh_ingredient_ranges.append((int(lower), int(upper)))
            else:
                available = int(line)
                if check_fresh(available, fresh_ingredient_ranges):
                    fresh_ingredients += 1
                    continue

        print(ingredients)
        print(f"part 1 - {fresh_ingredients}")


def check_fresh(available, fresh_ingredient_ranges) -> bool:
    for (lower, upper) in fresh_ingredient_ranges:
        if lower <= available <= upper:
            return True
    return False


if __name__ == "__main__":
    main()
