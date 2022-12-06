
def part_a(input_path):
    f = open(input_path).read()
    data = [i for i in f.strip().split("\n")]
    overlap_pairs = 0
    for pair in data:
        group_1, group_2 = pair.split(",")
        group_1_lower, group_1_upper = group_1.split("-")
        group_2_lower, group_2_upper = group_2.split("-")
        group_1_range = set(range(int(group_1_lower), int(group_1_upper) + 1))
        group_2_range = set(range(int(group_2_lower), int(group_2_upper) + 1))
        if group_1_range.issubset(group_2_range) or group_2_range.issubset(group_1_range):
            overlap_pairs += 1
    print(overlap_pairs)
    return overlap_pairs

def part_b(input_path):
    f = open(input_path).read()
    data = [i for i in f.strip().split("\n")]
    overlap_pairs = 0
    for pair in data:
        group_1, group_2 = pair.split(",")
        group_1_lower, group_1_upper = group_1.split("-")
        group_2_lower, group_2_upper = group_2.split("-")
        group_1_range = set(range(int(group_1_lower), int(group_1_upper) + 1))
        group_2_range = set(range(int(group_2_lower), int(group_2_upper) + 1))
        if group_1_range.intersection(group_2_range):
            overlap_pairs += 1
    return overlap_pairs





if __name__ == "__main__":
    input_path = "input/input4.txt"
    test = "input/test4.txt"
    soln_a = part_a(input_path)
    # part_a(test)
    print(f"solution to part a is: {soln_a}")
    soln_b = part_b(input_path)
    # print(part_b(test))
    print(f"solution to part b is: {soln_b}")