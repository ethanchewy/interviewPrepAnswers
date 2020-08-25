"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.
"""
def sudoku2(grid):
    row_viewed = {}
    columns_viewed = {}
    
    start_row_count = {}
    start_col_count = {}
    
    subgrids_viewed = {}
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == ".":
                continue
                
            if row in row_viewed:
                if grid[row][col] in row_viewed[row]:
                    return False
                row_viewed[row][grid[row][col]] = 0
            else:
                row_viewed[row] = {grid[row][col]:0}

            if col in columns_viewed:
                if grid[row][col] in columns_viewed[col]:
                    return False
                columns_viewed[col][grid[row][col]] = 0
            else:
                columns_viewed[col] = {grid[row][col]:0}
            
            # We group squares based on their ranges square 0 => 1-9, square 1 => 10-18, etc.
            # Remember that square grids are 0 indexed
            square_grid_location =  (row // 3)*(len(grid[0])//3) + col // 3
            
            if square_grid_location in subgrids_viewed:
                if grid[row][col] in subgrids_viewed[square_grid_location]:
                    return False
                subgrids_viewed[square_grid_location][grid[row][col]] = 0
            else: 
                subgrids_viewed[square_grid_location] = {grid[row][col]:0}
                
    return True
                
            
                
            
                
