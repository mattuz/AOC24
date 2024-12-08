from pathlib import Path
import re

# Read input from a file
p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

def multiply():
    pattern = r"mul\((\d+),(\d+)\)"
    product = 0
    for line in lines:
        matches = re.findall(pattern, line)
        res = [(int(x), int(y)) for x,y in matches]
        for (x, y) in res:
            product += x*y
    print(product)

        

if __name__ == "__main__":
    multiply()