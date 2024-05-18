import fire

from pmg import generate
from pmg import algorithms

def main(
    row = 3,
    col = 3
        ):
    generator = generate()

    maze = generator.grid_init(row, col)

    print(maze)

if __name__ == '__main__':
    fire.Fire(main) 
