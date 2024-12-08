from pathlib import Path

# Read input from a file
p = Path(__file__).with_name("input.txt")
with p.open("r") as f:
    lines = f.readlines()

def is_safe():
    total_safe = 0

    for line in lines:
        levels = list(map(int, line.split()))
        if is_sequence_safe(levels) or can_remove_one_for_safety(levels):
            total_safe += 1

    return total_safe

def is_sequence_safe(levels):
    """Check if a sequence is safe without modifications."""
    positive = False
    negative = False

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if not (-3 <= diff <= -1 or 1 <= diff <= 3):
            return False
        if diff > 0:
            positive = True
        if diff < 0:
            negative = True

    return not (positive and negative)

def can_remove_one_for_safety(levels):
    """Check if removing one level makes the sequence safe."""
    for i in range(len(levels)):
        modified = levels[:i] + levels[i + 1:]
        if is_sequence_safe(modified):
            return True
    return False

if __name__ == "__main__":
    print(is_safe())
