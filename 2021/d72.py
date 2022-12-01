import numpy as np

def readContents(fileName):
    line = open(fileName, 'r').readline().split(',')
    pos = {}
    for l in line:
        if int(l) in pos:
            pos[int(l)] += 1
        else:
            pos[int(l)]  = 1
    return pos

def ap(n):
    return int((n * (n + 1)) / 2)


def main():
    fileName = 'd7.txt'
    pos = readContents(fileName)

    fuels = {}
    for current in range(max(pos)):
        fuel = 0
        for key in pos:
            fuel += (ap(abs(key - current)) * pos[key])
        fuels[current] = fuel
        
    minfuel = np.inf
    minkey = -1
    for key, value in fuels.items():
        if value < minfuel:
            minfuel = value
            minkey = key

    print(minkey, minfuel)
    

if __name__ == "__main__":
    main()