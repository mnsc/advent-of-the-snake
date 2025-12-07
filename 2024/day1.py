def main():
    with open("day1.txt") as indata:
        left_list = []
        right_list = []
        for line in indata:
            (left, right) = line.split()
            left_list.append(int(left))
            right_list.append(int(right))

        left_list = sorted(left_list)
        right_list = sorted(right_list)
        if len(left_list) != len(right_list):
            raise ValueError("Wat")
        part1 = zip(left_list, right_list)
        part1_total = 0
        for (l, r) in part1:
            part1_total += abs(l - r)
        print(f"Part 1 - total: {part1_total}")

        right_pos = 0
        similarity_index = 0
        for l in left_list:
            loop_right = True
            while loop_right:
                r = right_list[right_pos]
                if r == l:
                    similarity_index += r
                    right_pos += 1
                elif r < l:
                    right_pos += 1
                else:
                    loop_right = False

                if len(right_list) <= right_pos:
                    loop_right = False

        print(f"Part 2 - similarity index: {similarity_index}")


if __name__ == '__main__':
    main()
