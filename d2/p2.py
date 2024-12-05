from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

def is_safe():
    sum = 0
    for line in lines:
        test = line.split(" ")
        nlist = []
        ok = True
        for num in test:
            nlist.append(int(num))
        first = True
        prev = 0
        positive = False
        negative = False
        saved = 0
        print("checking: ", nlist)
        for index, num in enumerate(nlist):
            if first:
                first = False
                prev = num
                continue
            else:   
                comp = num-prev
                if comp >0:
                    positive = True
                else:
                    negative = True
                prev = num
            if not (-3 <= comp <= -1 or 1 <= comp <= 3) or (positive and negative):
                ok = problem_dampener(nlist, index)
                if ok:
                    print("saved!")
                    saved += 1
                    if saved > 1:
                        ok = False
        if ok == True:
            sum += 1
            print("Was ok! Total is now: ", sum)
    return sum
            
def problem_dampener(list, index):
    nlist = list.copy()
    del nlist[index]
    first = True
    prev = 0
    positive = False
    negative = False
    ok = True
    for curr in nlist:
        if first:
            first = False
            prev = curr
            continue
        else:   
            comp = curr-prev
            if comp >0:
                positive = True
            else:
                negative = True
            prev = curr
        if not (-3 <= comp <= -1 or 1 <= comp <= 3) or (positive and negative):
            ok = False
    return ok

if __name__ == "__main__":
    print(is_safe())
