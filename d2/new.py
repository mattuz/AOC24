from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

def is_safe():
    sum = 0
    for line in lines:
        test = line.split(" ")
        nlist = []
        for num in test:
            nlist.append(int(num))
        ok = True
        first = True
        prev = 0
        positive = False
        negative = False
        for num in nlist:
            if first:
                first = False
                prev = num
                continue
            else:   
                comp = num-prev
                if comp > 0:
                    positive = True
                elif comp < 0:
                    negative = True
                prev = num
            if not (-3 <= comp <= -1 or 1 <= comp <= 3) or (positive and negative):
                ok = False
        if ok == True:
            sum += 1
        else:
            if dampener(nlist):
                sum += 1
    return sum
            
def dampener(mylist):
    saved = 0
    for index, number in enumerate(mylist):
        clist = mylist.copy()
        del clist[index]

        ok = True
        first = True
        prev = 0
        positive = False
        negative = False
        for num in clist:
            if first:
                first = False
                prev = num
                continue
            else:   
                comp = num-prev
                if comp > 0:
                    positive = True
                elif comp < 0:
                    negative = True
                
                prev = num
            if not (-3 <= comp <= -1 or 1 <= comp <= 3) or (positive and negative):
                ok = False
        if ok == True:
            saved += 1
    if saved == 1:
        print("SAVED!!! ", mylist)
        return True
    else:
        return False



if __name__ == "__main__":
    print(is_safe())
