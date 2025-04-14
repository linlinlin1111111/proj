
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
def find_path(maze, r, c, visited):
    if maze[r][c] == 'E':
        return True
    if maze[r][c] == '#' or visited[r][c]:
        return False

    visited[r][c] = True
    if maze[r][c] != 'S':
        maze[r][c] = '.'

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if find_path(maze, r + dr, c + dc, visited):
            return True

    if maze[r][c] != 'S':
        maze[r][c] = ' '
    return False
def main():
    rows, cols = 15, 15  # Размер лабиринта
    maze = create_empty_maze(rows, cols)
    generate_maze(maze, 1, 1)
    set_start_end(maze)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    find_path(maze, 1, 1, visited)
    print_maze(maze)

if __name__ == "__main__":
    main()
