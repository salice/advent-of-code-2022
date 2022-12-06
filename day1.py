
def calories_per_elf(input_path):
    f = open(input_path).read()
    data = [i for i in f.strip().split("\n")]
    list_lists = []
    cache_list = []
    for i in data:
        if len(i) > 0:
            cache_list.append(int(i))
        else:
            list_lists.append(cache_list)
            cache_list = []
    return [sum(i) for i in list_lists]


def part_a(input_path):
    calories = calories_per_elf(input_path)
    max_val = max(calories)
    return max_val

def part_b(input_path):
    snacks = calories_per_elf(input_path)
    top_three = sorted(snacks, reverse=True)[:3]
    return sum(top_three)


if __name__ == "__main__":
    input_path = "input/input1a.txt"
    solution_a = part_a(input_path)
    print(f"part a solution is: {solution_a}")
    solution_b = part_b(input_path)
    print(f"part b solution is: {solution_b}")
    