
def main():
    pass

if __name__ == "__main__":
    main()


def create_empty_maze(rows, cols):
    return [['#' for _ in range(cols)] for _ in range(rows)]
import random

DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def generate_maze(maze, r, c):
    maze[r][c] = ' '
    random.shuffle(DIRS)
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == '#':
            wall_r, wall_c = r + dr // 2, c + dc // 2
            maze[wall_r][wall_c] = ' '
            generate_maze(maze, nr, nc)
def set_start_end(maze):
    maze[1][1] = 'S'  # Стартовая точка
    maze[-2][-2] = 'E'  # Конечная точка

def print_maze(maze):
    for row in maze:
        print(''.join(row))
