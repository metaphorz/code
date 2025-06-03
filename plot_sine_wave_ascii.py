"""Generate an ASCII-art plot of a sine wave."""
import math

# width and height of ASCII plot
cols = 60
rows = 20

# generate x values from 0 to 2*pi
for i in range(rows):
    x = i / (rows - 1) * 2 * math.pi
    y = math.sin(x)
    # transform y from [-1, 1] to [0, cols-1]
    col = int((y + 1) / 2 * (cols - 1))
    line = [' '] * cols
    line[col] = '*'
    print(''.join(line))
