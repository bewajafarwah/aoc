def readContents(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()

    height = []
    for line in lines:
        h = []
        for i in line.strip():
            h.append(int(i))
        height.append(h)

    return height

def part1(fileName):
    height = readContents(fileName)
    x, y = len(height), len(height[0])
    
    lowp = []
    for r in range(x):
        for c in range(y):
            count = 0
            cur = height[r][c]
            if c + 1 < y:
                if cur < height[r][c + 1]:
                    count += 1
            else:
                count += 1

            if c - 1 >= 0:
                if cur < height[r][c - 1]:
                    count += 1
            else:
                count += 1

            if r + 1 < x:        
                if cur < height[r + 1][c]:
                    count += 1
            else:
                count += 1

            if r - 1 >= 0:
                if cur < height[r - 1 ][c]:
                    count += 1
            else:
                count += 1
            if count == 4:
                lowp.append((r, c, height[r][c]))

    risk = 0
    for r, c, value in lowp:
        risk += (value + 1)

    return risk

def part2():
    pass

if __name__ == '__main__':
    fileName = 'd9.txt'
    print(f'Ans 1: {part1(fileName)}')
