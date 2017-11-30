
class Robot:

    x = None
    y = None
    facing = None
    map_size = None

    def __init__(self, x, y, facing, map_size):
        self.x = x
        self.y = y
        self.facing = facing
        self.map_size = map_size

    def rotate_left(self):

        if self.facing == 'N':
            self.facing = 'W'
        elif self.facing == 'E':
            self.facing = 'N'
        elif self.facing == 'S':
            self.facing = 'E'
        elif self.facing == 'W':
            self.facing = 'S'

    def rotate_right(self):

        if self.facing == 'N':
            self.facing = 'E'
        elif self.facing == 'E':
            self.facing = 'S'
        elif self.facing == 'S':
            self.facing = 'W'
        elif self.facing == 'W':
            self.facing = 'N'

    def move(self):
        if self.facing == 'N':
            self.y += 1
        elif self.facing == 'S':
            self.y -= 1
        elif self.facing == 'W':
            self.x -= 1
        elif self.facing == 'E':
            self.x += 1
        if self.x < 0 or self.y < 0 or self.x > self.map_size[0] or self.y > self.map_size[1]:
            raise ValueError('Position of Robot is out of bounds.')

    def show_current_location(self):
        return self.x, " ", self.y, " ", self.facing



if __name__ == "__main__":
    map_size = input().split()
    width = int(map_size[0])
    height = int(map_size[1])
    map_size = (width, height)

    x_pos, y_pos, facing = input().split()
    instructions = input()

    my_robot = Robot(int(x_pos), int(y_pos), facing, map_size)

    my_list = list (instructions)
    # my_list[:0] = instructions
    print(my_list)

    for elem in my_list:
        if elem == 'M':
            my_robot.move()
        elif elem == 'L':
            my_robot.rotate_left()
        elif elem == 'R':
            my_robot.rotate_right()
        print(my_robot.show_current_location())

    print(my_robot.show_current_location())

