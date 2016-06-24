class MazeRunner(object):
    
    def __init__(self, maze, start, finish):
        self.__maze = maze
        self.__rotation = (1,0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze)-1 \
            or y > len(self.__maze)-1 \
            or x < 0 or y < 0 \
            or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        #print_maze(self.__maze, self.__x, self.__y)
        return True
    
    def turn_left(self):
        left_rotation = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self
    
    def turn_right(self):
        right_rotation = {
            (1,0): (0,1),
            (0,-1): (1,0),
            (-1,0): (0,-1),
            (0,1): (-1,0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self
    
    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]
maze_example1 = {
    'm': [
        [0,1,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,1,0],
    ],
    's': (0,0),
    'f': (4,4)
}
maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])

    
def maze_controller(maze_runner):

    def go_right():
        maze_runner.turn_right()
        if maze_runner.go():
            maze_runner.turn_left()
            return 'right'
        else:
            maze_runner.turn_left()
            return False
    
    def go_left():
        maze_runner.turn_left()
        if maze_runner.go():
            maze_runner.turn_right()
            return 'left'
        else:
            maze_runner.turn_right()
            return False
    def go_back():
        maze_runner.turn_right()
        maze_runner.turn_right()
        if maze_runner.go():
            maze_runner.turn_right()
            maze_runner.turn_right()
            return 'back'
        else:
            maze_runner.turn_right()
            maze_runner.turn_right()
            return False
    
    def go_straight():
        if maze_runner.go():
            return 'straight'
        else:
            return False
    

    def my_way():
        print 'new step'
        if not maze_runner.found():
            if go_straight():
                print 'go_straight'
                my_way()
            if go_right():
                print 'go_right'
                my_way()
            if go_left():
                print 'go_left'
                my_way()
            else:
                print 'go_back'
                go_back()
                return False
        else:
            return 'found'
    print my_way()

maze_controller(maze_runner)




