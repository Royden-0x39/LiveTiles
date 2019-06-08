# LiveTiles
My personal iteration of John Conway's Game of Life.

PROGRAM OPERATION:
  * Create a window with a grid
  * Assign attributes to the tiles in the grid:
    - 2 States: ON & OFF (highlighted Black & White, respectively)
    - Rules for next generation:
      a) ON tiles:
        1) if has 1 or 0 neighbors, turn OFF
        2) if has 4 or more neighbors, turn OFF
        3) if has 2 or 3 neighbors, remain ON
      b) OFF tiles:
        1) if has 3 neighbors, turn ON
        2) else, remain OFF
  * Initialize a clock: every generation, process all tiles on screen.

DEVELOPMENTS:
  * Generations controlled by: Clock, Button, or "Ctrl+Enter"
  * Select tiles manually:
    - mouse
    - arrow keys and "Enter" (the tile in question is outlined while 
        being selected; the outline disappears next generation)
  * Edge of screen: treat as a ring of OFF tiles?