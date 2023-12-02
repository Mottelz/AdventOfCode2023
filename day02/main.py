from utils.readers import read_file_as_strings
from typing import List


def parse_game(raw_game: str) -> dict:
    totals = {'red': 0, 'green': 0, 'blue': 0}
    for game_round in raw_game.split(';'):
        temp = parse_round(game_round)
        for k in temp.keys():
            totals[k] = max(int(temp[k]), int(totals[k]))
    return totals


def parse_round(raw_round):
    count = {'red': 0, 'green': 0, 'blue': 0}
    for stones in raw_round.split(','):
        temp = stones.strip().split(' ')
        stone, val = temp[1], int(temp[0])
        count[stone] += val
    return count


def part1and2(data: List[str]) -> int:
    part1 = 0
    part2 = 0
    for game in data:
        val, raw_game = game.split(':')
        parsed = parse_game(raw_game)
        p1_max = {'red': 12, 'green': 13, 'blue': 14}
        part2 += parsed['red'] * parsed['green'] * parsed['blue']
        if parsed['red'] <= p1_max['red'] and \
            parsed['blue'] <= p1_max['blue'] and \
            parsed['green'] <= p1_max['green']:
            part1 += int(val.split(' ')[1])
    return part1, part2


def main():
    data = read_file_as_strings('data.txt')
    s1, s2 = part1and2(data)
    print(f"Part 1: {s1}\nPart 2: {s2}")


if __name__ == '__main__':
    main()
