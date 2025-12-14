import typing
from functools import reduce
from operator import add, mul


class Column(typing.NamedTuple):
    idx: int
    operator: str


def get_columns(operator_line: str) -> list[Column]:
    columns: list[Column] = []
    for i in range(len(operator_line)):
        if operator_line[i] != " ":
            columns.append(Column(i, operator_line[i]))
    return columns


def main():
    with open("day6.txt") as f:
        lines = f.read().splitlines()
        # use last line (operators) to sus out columns
        columns = get_columns(lines[len(lines) - 1])

        print("")
        total_total = 0
        for x, col in enumerate(columns):
            items = []
            for row in range(0, len(lines) - 1):
                line = lines[row]
                if x == len(columns) - 1:
                    items.append(int(line[col.idx:]))
                else:
                    items.append(int(line[col.idx: columns[x + 1].idx]))

            if col.operator == '+':
                col_total = reduce(add, items)
            else:
                col_total = reduce(mul, items)
            total_total += col_total
        print(f"part 1 - {total_total}")


if __name__ == "__main__":
    main()
