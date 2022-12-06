from collections import deque

def init_stacks(stack_path):
    f = open(stack_path).readlines()
    reverse = f[::-1]
    num_arrays = [i for i in reverse[0] if len(i.strip())]
    stack_dict = {i: deque() for i in num_arrays}
    for i in reverse[1:]:
        elements = i.split(" ")
        index = 1
        skipped = 0
        for val in elements:
            if  len(val.strip()) > 0:
                if skipped:
                    index += skipped // 4
                stack_dict[str(index)].append(val.strip())
                index += 1
                skipped = 0
            else:
                skipped += 1
        index = 1
    return stack_dict

def part_a(input_path, stack_path):
    stacks = init_stacks(stack_path)
    f = open(input_path).read()
    moveset = [i for i in f.strip().split("\n")]
    for step in moveset:
        magnitude, direction = step.split(" from ")
        magnitude = int(magnitude.split(" ")[-1].strip())
        start, end = direction.split(" to ")
        start = start.strip()
        end = end.strip()
        for _ in range(magnitude):
            ele = stacks[start].pop()
            stacks[end].append(ele)
    
    final = ""
    for idx, _ in stacks.items():
        final += stacks[idx].pop()[1]
    return final

def part_b(input_path, stack_path):
    stacks = init_stacks(stack_path)
    f = open(input_path).read()
    moveset = [i for i in f.strip().split("\n")]
    for step in moveset:
        magnitude, direction = step.split(" from ")
        magnitude = int(magnitude.split(" ")[-1].strip())
        start, end = direction.split(" to ")
        start = start.strip()
        end = end.strip()
        temp= []
        for _ in range(magnitude):
            ele = stacks[start].pop()
            temp.append(ele)
        temp = temp[::-1]
        for val in temp:
            stacks[end].append(val)
        temp = []
    final = ""
    for idx, _ in stacks.items():
        final += stacks[idx].pop()[1]
    return final



if __name__ == "__main__":
    input_path = "input/input5.txt"
    stack_path = "input/input5init.txt"
    soln_a = part_a(input_path, stack_path)
    print(f"part a solution is: {soln_a}")
    soln_b = part_b(input_path, stack_path)
    print(f"part b solution is: {soln_b}")