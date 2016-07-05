#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        [0,0,0,0,1,0,1,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,1,0,0,0,1,0,1],
        [1,0,1,0,0,0,1,0,1,0,1],
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


last_turn='start'

def maze_controller(maze_runner):
    my_way=[]
    my_crossroads=[]

    def go_right():
        '''turn rigth and look in the same direction '''
        maze_runner.turn_right()
        if maze_runner.go():
            maze_runner.turn_left()
            return 'right'
        else:
            maze_runner.turn_left()
            return False

    def go_left():
        '''turn lest and look in the same direction '''
        maze_runner.turn_left()
        if maze_runner.go():
            maze_runner.turn_right()
            return 'left'
        else:
            maze_runner.turn_right()
            return False

    def go_up():
        '''go up and look in the same direction '''
        maze_runner.turn_right()
        maze_runner.turn_right()
        if maze_runner.go():
            maze_runner.turn_right()
            maze_runner.turn_right()
            return 'up'
        else:
            maze_runner.turn_right()
            maze_runner.turn_right()
            return False
    
    def go_down():
        '''go down and look in the same direction '''
        if maze_runner.go():
            return 'down'
        else:
            return False

    def check_back_after(step):
        '''return coor after examining '''
        if step=='down':
            maze_runner.turn_right()
            maze_runner.turn_right()
            maze_runner.go()
            maze_runner.turn_right()
            maze_runner.turn_right()
            return 'down'
        elif step=='left':
            maze_runner.turn_right()
            maze_runner.go()
            maze_runner.turn_left()
            return 'left'
        elif step=='right':
            maze_runner.turn_left()                
            maze_runner.go()
            maze_runner.turn_right()
            return 'right'
        elif step=='up':
            maze_runner.go()
            return 'up'
        else:
            return False



    def examining_crossroads(last_turn):
        '''examining for crossroads'''
        if maze_runner.found():
            return 'found'
        else:
            if last_turn=='start':              
                step_1=check_back_after(go_up())
                step_2=check_back_after(go_left())
                step_3=check_back_after(go_right())
                step_4=check_back_after(go_down())
                my_crossroads.append([step_1,step_2,step_3,step_4])
                return [step_1,step_2,step_3,step_4]

            elif last_turn=='down':
                step_2=check_back_after(go_left())
                step_3=check_back_after(go_right())
                step_4=check_back_after(go_down())
                my_crossroads.append(['previous',step_2,step_3,step_4])
                return ['previous',step_2,step_3,step_4]

            elif last_turn=='left':
                step_1=check_back_after(go_up())
                step_2=check_back_after(go_left())
                step_4=check_back_after(go_down())
                my_crossroads.append([step_1,step_2,'previous',step_4])
                return [step_1,step_2,'previous',step_4]

            elif last_turn=='right':
                step_1=check_back_after(go_up())
                step_3=check_back_after(go_right())
                step_4=check_back_after(go_down())
                my_crossroads.append([step_1,'previous',step_3,step_4])
                return [step_1,'previous',step_3,step_4]

            elif last_turn=='up':
                step_1=check_back_after(go_up())
                step_2=check_back_after(go_left())
                step_3=check_back_after(go_right())
                my_crossroads.append([step_1,step_2,step_3,'previous'])
                return [step_1,step_2,step_3,'previous']
            else:
                return False

    def go_back(examining):
        pass
            








    def go(examining=None):
        global last_turn
        examining=examining_crossroads(last_turn)
        print examining
        if  examining=='found':
            return 'found'
            
        elif examining:
            for x in examining:
                print 'x ='+ str(x)
                if x=='down':
                    print 'go_down' 
                    go_down()
                    my_crossroads[-1][0]=False
                    last_turn='down'
                    if go(examining)=='found':
                        return 'found'
                elif x=='left':
                    print 'go_left'
                    go_left()
                    my_crossroads[-1][1]=False
                    last_turn='left'
                    if go(examining)=='found':
                        return 'found'
                elif x=='right':
                    print 'go_right'
                    go_right()
                    my_crossroads[-1][2]=False
                    last_turn='right'
                    if go(examining)=='found':
                        return 'found'
                elif x=='up':
                    print 'go_up'
                    go_up()
                    my_crossroads[-1][3]=False
                    last_turn='up'
                    if go(examining)=='found':
                        return 'found'
                elif x=='previous':
                    pass
            # go_back(examining)
            print 'check_back_after' 
            check_back_after(last_turn)
    go()
                        



 # godownList=[]
 #    print 'godownList'

 #    def go_up():
 #        maze_runner.turn_left()
 #        for x in xrange(1,1000):
 #            if len(godownList)==0:
 #                maze_runner.turn_right()
 #                return True
 #            elif godownList[-1]==1:
 #                maze_runner.go()
 #                godownList.pop()
 #            elif godownList[-1]==2:
 #                maze_runner.turn_right()
 #                godownList.pop()
 #            elif godownList[-1]==3:
 #                godownList.pop()
 #                if maze_runner.go():
 #                    if maze_runner.found():
 #                        break
 #                    godownList.append(4)
 #                    godownList.append(1)
 #                    return True
 #            elif godownList[-1]==4:
 #                godownList.pop()
 #                maze_runner.turn_right()



        
    
 #    def go():
 #        for x in xrange(1,1000):
 #            examining()




        
 #            if maze_runner.found():
 #                break
 #            if maze_runner.go():
 #                godownList.append(1)
 #            else:
 #                if len(godownList)==0 or  godownList[-1]==1  :
 #                    maze_runner.turn_right()
 #                    godownList.append(3)
 #                    if maze_runner.go():
 #                        if maze_runner.found():
 #                            break
 #                        godownList.append(1)
                
 #                elif godownList[-1]==3:
 #                    godownList.pop()
 #                    maze_runner.turn_left()
 #                    maze_runner.turn_left()
 #                    godownList.append(2)
 #                    if maze_runner.go():
 #                        if maze_runner.found():
 #                            break 
 #                        godownList.append(1)
                
 #                elif godownList[-1]==2:
 #                    godownList.pop()
 #                    go_up()


maze_controller(maze_runner)

print 'maze_runner.found()' + str(maze_runner.found())

