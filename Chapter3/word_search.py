from csp import Constraint, CSP
from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase

Grid = List[List[str]]


class GridLocation(NamedTuple):
    row: int
    column: int


def generate_grid(rows: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]


def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))


def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height = len(grid)
    width = len(grid[0])
    length = len(word)
    for row in range(height):
        for col in range(width):
            columns = range(col, col + length + 1)
            rows = range(row, row + length + 1)
            if col + length <= width:
                domain.append([GridLocation(row, c) for c in columns])
                if row + length <= height:
                    domain.append([GridLocation(row, col + (r - row))
                                   for r in rows])
            if row + length <= height:
                domain.append([GridLocation(r, col) for r in rows])
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row))
                                   for r in rows])
    return domain


class WordConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words: List[str]) -> None:
        super().__init__(words)
        self.words: List[str] = words

    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        all_locations = [locs for value in assignment.values()
                         for locs in value]
        return len(set(all_locations)) == len(all_locations)


if __name__ == "__main__":
    grid = generate_grid(9, 9)
    words = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    csp = CSP(words, locations)
    csp.add_constraint(WordConstraint(words))
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (
                    grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)
