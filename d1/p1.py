from pathlib import Path

p = Path(__file__).with_name("input1.txt")
with p.open("r") as f:
    lines = f.readlines()

def list_sorter():
    both = []
    l1 = []
    l2 = []
    for line in lines:
        both = line.split("   ")
        l1.append(both[0])
        l2.append(both[1])
    l1.sort()
    l2.sort()
    return l1, l2

def distance_calc(l1, l2):
    sum = 0
    for i in range(len(l1)):
        diff = abs(int(l1[i])-int(l2[i]))
        sum += diff
    return sum


if __name__ == "__main__":
    l1, l2 = list_sorter()
    print(distance_calc(l1,l2))