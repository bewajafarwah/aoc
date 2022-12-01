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


def main():
    fileName = 'd7.txt'
    pos = readContents(fileName)
    
    print(pos)

    fuels = {}
    for current in range(max(pos)):
        fuel = 0
        for key in pos:
            fuel += (abs(key - current) * pos[key])
        fuels[current] = fuel
        
    minfuel = np.inf
    minkey = -1
    for key, value in fuels.items():
        if value < minfuel:
            minfuel = value
            minkey = key

    print(minkey, minfuel)
    

def withStats():
    from statistics import median

    with open('d4e.txt', 'r') as f:
        data = [int(i) for i in f.readline().strip().split(',')]
       
    print(data)
    med = median(data)
    print(med)

if __name__ == "__main__":
    #main()
    withStats()