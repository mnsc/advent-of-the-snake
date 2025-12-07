with open("day2.txt") as f:
    ranges = f.read().split(",")
    total = 0
    for r in ranges:
        (lower, upper) = r.split("-")
        #print(f"{lower}-{upper}")
        for int_a in range(int(lower), int(upper) + 1):
            str_a = str(int_a)
            len_a = len(str_a)
            if len_a % 2 == 0:
                firsthalf = str_a[:len_a // 2]
                secondhalf = str_a[len_a // 2:]
                # print(f"checking {str_a} first {firsthalf} second {secondhalf}")
                if firsthalf == secondhalf:
                    print(f"Invalid {str_a}")
                    total += int_a
    print(f"total {total}")

