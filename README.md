# LiveTiles
My personal iteration of John Conway's Game of Life.

## PROGRAM OPERATION:

  * Create a window with a grid
  * Assign attributes to the tiles in the grid:
    - 2 States: ON & OFF (highlighted Black & White, respectively)
    - Rules for next generation:
      - ON tiles:
        - if has 1 or 0 neighbors, turn OFF
        - if has 4 or more neighbors, turn OFF
        - if has 2 or 3 neighbors, remain ON
      - OFF tiles:
        - if has 3 neighbors, turn ON
        - else, remain OFF
  * Initialize a clock: every generation, process all tiles on screen.

## DEVELOPMENTS:

  * Generations controlled by: Clock, Button, or "Ctrl+Enter"
  * Select tiles manually:
    - mouse
    - arrow keys and "Enter" (the tile in question is outlined while 
        being selected; the outline disappears next generation)
  * Edge of screen: treat as a ring of OFF tiles?
