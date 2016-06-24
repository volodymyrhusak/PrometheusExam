

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
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ],
    's': (0,5),
    'f': (10,5)
}

maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])



def maze_controller(maze_runner):
    goStraightList=[]
    print 'goStraightList'

    def go_back():
        maze_runner.turn_left()
        for x in xrange(1,1000):
            print ''
            if len(goStraightList)==0:
                maze_runner.turn_right()
                return True
            elif goStraightList[-1]==1:
                maze_runner.go()
                goStraightList.pop()
            elif goStraightList[-1]==2:
                maze_runner.turn_right()
                goStraightList.pop()
            elif goStraightList[-1]==3:
                goStraightList.pop()
                if maze_runner.go():
                    if maze_runner.found():
                        break
                    goStraightList.append(4)
                    goStraightList.append(1)
                    return True
            elif goStraightList[-1]==4:
                goStraightList.pop()
                maze_runner.turn_right()



        
    
    def go_straight():
        for x in xrange(1,1000):
            if maze_runner.found():
                break
            if maze_runner.go():
                goStraightList.append(1)
            else:
                if len(goStraightList)==0 or  goStraightList[-1]==1  :
                    maze_runner.turn_right()
                    goStraightList.append(3)
                    if maze_runner.go():
                        if maze_runner.found():
                            break
                        goStraightList.append(1)
                
                elif goStraightList[-1]==3:
                    goStraightList.pop()
                    maze_runner.turn_left()
                    maze_runner.turn_left()
                    goStraightList.append(2)
                    if maze_runner.go():
                        if maze_runner.found():
                            break 
                        goStraightList.append(1)
                
                elif goStraightList[-1]==2:
                    goStraightList.pop()
                    go_back()
    go_straight()


maze_controller(maze_runner)

print maze_runner.found()









    # print maze_runner.go()
    # print maze_runner.go()
    # maze_runner.turn_left()
    # print maze_runner.go()
