from pathlib import Path
import re

# Read input from a file
p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

def multiply():
    pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
    product = 0
    res  = []
    cdo = 0
    for line in lines:
        matches = re.findall(pattern, line)
    for match in matches:
        if match[0] and match[1]:
            res.append((int(match[0]), int(match[1])))
        elif match[2]:
            cdo +=1
            res.append("do")
        elif match[3]:
            res.append("don't")
    do = True
    for item in res:
        if item == "do":
            do = True
        elif item == "don't":
            do = False
        else:
            if do:
                x, y = item
                product += x*y                

        #res = [(int(x), int(y)) for x,y in matches]
        #for (x, y) in res:
        #    product += x*y
    print(product)

        

if __name__ == "__main__":
    multiply()