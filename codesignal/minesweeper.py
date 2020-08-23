"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.
"""

def minesweeper(matrix):
    # Instantiate the whole matrix with 0s first
    result = [[0] * (len(matrix[0])) for i in range(len(matrix))]
    
    # O (# of items in matrix)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]:
                # increment surrounding blocks
                if row - 1 >= 0:
                    result[row - 1][col] += 1
                    if col - 1 >= 0:
                        result[row - 1][col - 1] += 1
                    if col + 1 < len(matrix[0]):
                        result[row - 1][col + 1] += 1
                    
                if col - 1 >= 0:
                    result[row][col - 1] += 1
                    
                if row + 1 < len(matrix):
                    result[row + 1][col] += 1
                    if col + 1 < len(matrix[0]):
                        result[row + 1][col + 1] += 1
                    if col - 1 >= 0:
                        result[row + 1][col - 1] += 1
                
                if col + 1 < len(matrix[0]):
                    result[row][col + 1] += 1
    
    return result
                
                    
                
