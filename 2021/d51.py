import numpy as np

def readContents(fileName):
    lines = open(fileName, 'r').readlines()

    start_coords = []
    end_coords = []

    minx = np.inf
    maxy = -np.inf


    for line in lines:

        strcoord = line.strip().split('->')
        x1, y1 = strcoord[0].strip().split(',')
        x2, y2 = strcoord[1].strip().split(',')

        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)


        if x1 == x2 or y1 == y2:
            if x1 < minx:
                minx = x1
            if x2 < minx:
                minx = x2
            if y2 > maxy:
                maxy = y2
            if y1 > maxy:
                maxy = y1


            if x1 < x2:#or y1 < y2:
                start_coords.append((x1, y1))
                end_coords.append((x2, y2))
            else:
                start_coords.append((x2, y2))
                end_coords.append((x1, y1))

    return start_coords, end_coords, minx, maxy

def printGrid(grid):
    for g in grid:
        print(g)
    print()

def main():
    fileName = 'd5.txt'
    start_coords, end_coords, minx, maxy = readContents(fileName)
    grid = np.zeros((maxy + 1, maxy + 1))

    for i in range(len(start_coords)):
        sx = end_coords[i][0] - start_coords[i][0]
        sy = end_coords[i][1] - start_coords[i][1]

        x1, y1 = start_coords[i]
        x2, y2 = end_coords[i]
        
        if sx == 0:
            ix = 0
            if sy > 0:
                iy = 1
            else:
                iy = -1
        else:
            if sx > 0:
                ix = 1
            else:
                ix = -1
            iy = 0
        
        for j in range(max(abs(sx), abs(sy)) + 1):
            tx = x1 + (j*ix)
            ty = y1 + (j*iy)
            grid[tx][ty] += 1


    count = 0
    for i in range(maxy + 1):
        for j in range(maxy + 1):
            if grid[i][j] > 1:
                count += 1

    #print(grid.T)
    print(count)


if __name__ == '__main__':
    main()