from utils.readers import read_file_as_strings
from typing import List


def part1(data: List[str]) -> int:
    total = 0
    for line in data:
        first = second = None
        for c in line:
            if c in "1234567890":
                first = c if not first else first
                second = c
        total += int(first + second)
    return total


def part2(data: List[str]) -> List[str]:
    numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    clean = []
    for line in data:
        temp = ''
        for i in range(len(line)):
            c = line[i]
            if c in 'otfsen':
                for word in words:
                    if line[i:i+len(word)] == word:
                        temp += numbers[word]
            else:
                temp += c
        clean.append(temp)
    return clean


def main():
    data = read_file_as_strings('data.txt')
    print(f"p1: {part1(data)}")
    convert = part2(data)
    print(f"p2: {part1(convert)}")


if __name__ == "__main__":
    main()
