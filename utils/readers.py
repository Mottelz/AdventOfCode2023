from typing import List


def read_file_as_strings(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        out = []
        for line in file:
            temp = line.replace('\n', '')
            out.append(temp)
    return out
