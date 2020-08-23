"""
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.
"""


def boxBlur(image):
    transformed = [[0] * (len(image[0]) - 2)  for i in range(len(image) - 2)]
    
    for r in range(len(image)):
        for c in range(len(image[0])):
            if r > 0 and c > 0 and r < len(image) - 1 and c < len(image[0]) - 1:
                total = \
                    image[r + 0][c + 1] + \
                    image[r - 1][c + 1] + \
                    image[r + 1][c + 1] + \
                    image[r + 0][c + 0] + \
                    image[r + 1][c + 0] + \
                    image[r - 1][c + 0] + \
                    image[r - 1][c - 1] + \
                    image[r + 0][c - 1] + \
                    image[r + 1][c - 1]
                    
                transformed[r - 1][c - 1] = total // 9
    
    return transformed
    
    
