// PAY NO MIND TO ANYTHING FROM HERE
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include "mazelib.h"

static int xy_to_index(int, int);

static int width;
static int height;
static char *maze;
static bool initializing = false;
// TO HERE


////////////////////////////////////////////////////////////////////////////////
// BEGIN: THINGS YOU SHOULD LOOK AT                                           //
////////////////////////////////////////////////////////////////////////////////

// returns "true" if x and y are both in-bounds as defined by:
// 0 <= x < width and 0 <= y <= height
// This function is not strictly necessary to complete the project
bool maze_is_coord_in_bounds( int x, int y ) {
  return 0 <= x && x < width && 0 <= y && y < height;
}


/*
  maze_get_char returns the character in 'maze' at the passed index
*/
char maze_get_char(int x, int y) {
  return maze[xy_to_index(x, y)];
}

/*
  maze_set_char sets the character in 'maze' at the passed index to the passed
  character.  It returns true if the character was actually replaced, and false
  otherwise.
*/
bool maze_set_char(int x, int y, char replacement) {
  char c = maze_get_char(x, y);
  if((c == '#' || c == 'S' || c == 'E') && !initializing) {
    return false;
  }
  maze[xy_to_index(x, y)] = replacement;
  return true;
}




////////////////////////////////////////////////////////////////////////////////
// BEGIN: STUFF YOU DON'T NEED TO LOOK AT OR UNDERSTAND FOR THE PROJECT       //
////////////////////////////////////////////////////////////////////////////////



static void shuffle_dirs(enum direction*);
static void reset(void);
static bool are_valid_maze_dimensions(int, int);
static void set_offsets_for_dir(int*, int*, enum direction);
static void maze_visit(int, int);


// maze_init allocates the memory for the maze array based on width and height
bool maze_init(int w, int h) {
  if(!are_valid_maze_dimensions(w, h)) {
    return false;
  }
  width = w;
  height = h;
  srand(time(NULL));
  maze = malloc(sizeof(*maze) * width * height);
  reset();
  initializing = true;
  maze_visit(1, 1);
  maze_set_char(1, 1, 'S');
  maze_set_char(width-2, height-2, 'E');
  initializing = false;
  return true;
}

/*
  maze_print displays the maze to the screen.
*/
void maze_print(void) {
  for(int y = 0; y < height; y++) {
    for(int x = 0; x < width; x++) {
      printf("%c", maze_get_char(x,y));
    }
    printf("\n");
  }
  printf("\n");
}

/*
  maze_visit starts at a given index and recursively maze_visits every direction in a
  randomized order. Recursion ends at a particular location when all the
  directions have been maze_visited.
*/
static void maze_visit(int x, int y) {
  maze_set_char(x, y, ' ');

  enum direction dirs[4] = {NORTH, EAST, SOUTH, WEST};
  shuffle_dirs(dirs);

  for (int i=0; i < 4; i++) {
    // dx and dy will be offsets from the current location based on the direction at i
    int dx = 0;
    int dy = 0;
    set_offsets_for_dir(&dx, &dy, dirs[i]);

    // get the (x, y) coordinates for the maze cell 2 spots away in the given direction
    int x2 = x + 2*dx;
    int y2 = y + 2*dy;

    // If the location at (x2, y2) is in bounds and it hasn't been visited yet, visit it
    if(maze_is_coord_in_bounds(x2, y2) && maze_get_char(x2, y2) == '#') {
      maze_set_char(x2-dx, y2-dy, ' ');
      maze_visit(x2, y2);
    }
  }
}

static bool are_valid_maze_dimensions(int w, int h) {
  return w % 2 == 1 &&
    h % 2 == 1 &&
    w > 8 &&
    h > 8 &&
    w < 80 &&
    h < 26;
}

// reset fills the maze with blocks ('#' characters).
static void reset(void) {
  for(int i = 0; i < width*height; i++)
    {
      maze[i] = '#';
    }
}

static int xy_to_index(int x, int y) {
  return y*width + x;
}

static void shuffle_dirs(enum direction *dirs) {
  for(int i = 0; i < 4; i++) {
    int r = rand() & 3; // Random number between 0 and 3
    // swap directions at r and i
    int temp = dirs[r];
    dirs[r] = dirs[i];
    dirs[i] = temp;
  }
}

static void set_offsets_for_dir(int *dx, int *dy, enum direction dir) {
  switch (dir) {
  case NORTH: 
    *dy = -1;
    break;
  case SOUTH: 
    *dy = 1; 
    break;
  case EAST:  
    *dx = 1; 
    break;
  case WEST:  
    *dx = -1; 
    break;
  }
}
