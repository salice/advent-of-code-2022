
def part_a(input_path):
    f = open(input_path).read().strip()
    for idx in range(3,len(f)):
        window = f[idx - 3:idx + 1]
        if len(window) == len(set(window)):
            print(window)
            print(idx + 1)
            first_marker = idx + 1
            return first_marker


def part_b(input_path):
    f = open(input_path).read().strip()
    for idx in range(13,len(f)):
        window = f[idx - 13:idx + 1]
        if len(window) == len(set(window)):
            print(window)
            print(idx + 1)
            first_marker = idx + 1
            return first_marker





if __name__ == "__main__":
    input_path = "input/input6.txt"
    soln_a = part_a(input_path)
    print(f"part a solution is: {soln_a}")
    soln_b = part_b(input_path)
    print(f"part b solution is: {soln_b}")