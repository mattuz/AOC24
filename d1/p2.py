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
        l1.append(int(both[0]))
        l2.append(int(both[1]))
    return l1, l2

def similarity_calc(l1, l2):
    sum = 0
    for i in range(len(l1)):
        num = l1[i]
        amount = l2.count(num)
        sum += num * amount
    return sum


if __name__ == "__main__":
    l1, l2 = list_sorter()
    print(similarity_calc(l1,l2))