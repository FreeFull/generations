def star_wars(x, y, elem, neighbours):
    """Star Wars preset of the Generations family. (345/2/4)"""
    red_count = 0
    for neighbour in neighbours:
        if neighbour == 3:
            red_count += 1

    if elem == 3: # The cell is alive
        if red_count in [3,4,5]:
            return 3
        else:
            return 2
    elif elem > 0: # The cell is decaying
        return elem - 1
    elif red_count == 2: # The cell is dead, but will be brought to life
        return 3
    else: # The cell is dead
        return 0

class Automaton:
    def __init__(self, x_size, y_size, rule = star_wars):
        self.x_size = x_size;
        self.y_size = y_size;
        self.rule = rule;

        self.buf = [[0]*x_size for _ in range(y_size)]
        self.back_buf = [[0]*x_size for _ in range(y_size)]

    def step(self):
        """Advances the simulation by one step"""
        for (y,row) in enumerate(self.buf):
            for (x,elem) in enumerate(row):
                self.back_buf[y][x] = self.rule(x, y, elem, self.neighbours(x,y))

        self.buf, self.back_buf = self.back_buf, self.buf

    def neighbours(self, x, y):
        """Returns all the cells in the neighbourhood of the specified cell."""
        return (
            self.buf[(y+dy) % self.y_size][(x+dx) % self.x_size]
            for dx in [-1,0,1]
            for dy in [-1,0,1]
            if (dx,dy) != (0,0)
            )

    def show(self):
        """Prints out the contents of buf, for debugging."""
        for row in self.buf:
            for elem in row:
                print(elem, end='')
            print()
