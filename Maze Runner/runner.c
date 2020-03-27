#include <stdbool.h>
#include <stdio.h>
#include "mazelib.h"

/*
    ####################
    ### USEFUL NOTES ###
    ####################

### GO UP ###
North = (x, y-1)
### GO RIGHT ###
East = (x+1, y)
### GO DOWN ###
South = (x, y+1)
### GO LEFT ###
West = (x-1, y)

turn left: facing = (facing + 3) % 4
turn right: facing + 1 
                N (0)
                 -y
                  |
                  |
 W (3) -x --------|-------- +x E (1)
                  |
                  |
                 +y
                S (2)

*/ 

enum direction facing;


bool isWall(int x, int y) {
    if(maze_get_char(x,y) == '#') {
        return true;
    }
    return false;  
}

bool isExit(int x, int y) {
    if(maze_get_char(x,y) == 'E') {
        return true;
    }
    return false;  
}

bool isSpace(int x, int y) {
    if(maze_get_char(x,y) == ' ') {
        return true;
    }
    return false;
}

bool isPeriod(int x, int y) {
    if(maze_get_char(x,y) == '.') {
        return true;
    }
    return false;
}

bool isSmallO(int x, int y) {
    if(maze_get_char(x,y) == 'o') {
        return true;
    }
    return false;
}

bool isBigO(int x, int y) {
    if(maze_get_char(x,y) == 'O') {
        return true;
    }
    return false;
}

void dropCrumb(int x, int y) {
    if(isSpace(x,y)) {
        maze_set_char(x,y,'.');
    }
    if(isPeriod(x,y)) {
        maze_set_char(x,y,'o');
    }
    if(isSmallO(x,y)) {
        maze_set_char(x,y,'O');
    }
    if(isBigO(x,y)) {
        maze_set_char(x,y,'@');
    }
    return; 
}

void turnLeft(void) {
    facing = (facing + 3) % 4;
}

void turnRight(void) {
    facing = (facing + 1) % 4;
}

void moveForward(int x, int y) {
    if(facing == NORTH) { 
        y = y - 1;
    }
    if(facing == EAST) {
        x = x + 1;
    }
    if(facing == SOUTH) {
        y = y + 1;
    }
    if(facing == WEST) {
        x = x - 1;
    }
    //whatever direction you're facing depends on what 'moving forward' means
    return;
}

bool isFacingWall(int x, int y) {
    if (facing == NORTH) {
        if (isWall(x,y - 1)) {
            return true;
        }
    }
    if (facing == EAST) {
        if (isWall(x+1,y)) {
            return true;
        }
    }
    if (facing == SOUTH) {
        if (isWall(x,y + 1)) {
            return true;
        }
    }
    if (facing == WEST) {
        if (isWall(x -1 ,y)) {
            return true;
        }
    }
    return false; 
    //takes whatever direction you're facing and checks the coordinate in 'front' of you
}

bool isLeftWall(int x, int y) {
    turnLeft();
    moveForward(x,y);
    if(isWall(x,y)) {
        return true;
    }
    return false;
}

void runner_solve(void) {

   int x = 1;
   int y = 1;
   enum direction facing = SOUTH;

    while(!isExit(x,y)) {
        if(isFacingWall(x,y)) {
            turnRight();
        }
        if(!isFacingWall(x,y)) {
            dropCrumb(x,y);
            moveForward(x,y);     
        }
        if(isLeftWall(x,y)) {
            turnLeft();
            dropCrumb(x,y);
            moveForward(x,y);
        }
    }
    return;

}

void runner_init(void) {
    return;
}