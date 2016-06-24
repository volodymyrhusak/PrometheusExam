

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
    my_way=[[]]

    def go_right():
        maze_runner.right()
        if maze_runner.go():
            maze_runner.left()
            return 'right'
        else:
            maze_runner.left()
            return False

    def go_left():
        maze_runner.left()
        if maze_runner.go():
            maze_runner.right()
            return 'left'
        else:
            maze_runner.right()
            return False

    def go_back():
        maze_runner.right()
        maze_runner.right()
        if maze_runner.go():
            maze_runner.right()
            maze_runner.right()
            return 'back'
        else:
            maze_runner.right()
            maze_runner.right()
            return False
    
    def go_straight():
        if maze_runner.go():
            return 'straight'
        else:
            return False

    def check_back_after():
        if step=='straight':
            maze_runner.right()
            maze_runner.right()
            maze_runner.go()
            maze_runner.right()
            maze_runner.right()
            return True
        elif step=='left':
            maze_runner.right()
            maze_runner.go()
            maze_runner.left()
            return True
        elif step=='rigth':
            maze_runner.left()                
            maze_runner.go()
            maze_runner.right()
            return True
        elif step=='back':
            maze_runner.go()
            return True
        else:
            return False



    def examining():
        if maze_runner.found():
            return 'found'
        else:
            if last_turn=='start':
                
                step_1=check_back_after(go_back())

                step_2=check_back_after(go_left())
                step_3=check_back_after(go_right())
                step_4=check_back_after(go_straight())

                
                
            if last_turn=='straight':

            if last_turn=='left':

            if last_turn=='right'
            if last_turn=='back'


 goStraightList=[]
    print 'goStraightList'

    def go_back():
        maze_runner.turn_left()
        for x in xrange(1,1000):
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


maze_controller(maze_runner)

print maze_runner.found()

