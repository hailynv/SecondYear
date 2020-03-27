#ifndef _maze_h
#define _maze_h
#include <stdbool.h>

//---- Directional Constants ---------------------------------------------------
// You can use this to track the direction your solver is facing if you want
enum direction { NORTH, EAST, SOUTH, WEST };


// IMPORTANT: Since the upper left hand corner of the maze is given the
// coordinate (1, 1), the directions are not what you might expect from a
// 'normal' coordinate plane.  Namely, although right and left still correspond
// to positive and negative 'x' respectively, down is actually positive 'y' and
// up is negative 'y'.


//-----Functions you SHOULD use in your runner.c file---------------------------

// returns true if the coordinate supplied is within the bounds of the maze and
// false otherwise.
bool maze_is_coord_in_bounds(int x, int y);

// Returns the character in the maze at a given coordinate.  A return value of
// '#' represents a wall, 'S' represents the starting place of the robot, 'E'
// represents the exit and ' ' represents an open space.
char maze_get_char(int x, int y);

// This function can be used to set a character in the maze to something new.
// It will not set a square that's filled with a wall to something new though.
bool maze_set_char(int x, int y, char new_val);


//-----Functions you may use for debugging, but not in your final submission----

// This function prints the maze as it currently is
void maze_print(void);



//-----Functions you should NOT use in your runner.c file-----------------------

// Initializes the maze according to the width and height passed in.  The width
// and height should both be greater than 8 and odd.  The width should also be
// less than 80 and the height should be less than 26.  IMPORTANT: The start of
// the maze is always in the upper left of the maze at (1, 1)
bool maze_init(int width, int height);

#endif
