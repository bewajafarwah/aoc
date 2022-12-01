def readContents(fileName):
    lines = open(fileName, 'r').readlines()
    line = lines[0].split(',')
    state = [0] * 9
    for l in line:
        state[int(l)] += 1
    return state

def printState(state):
    disp = []
    for i in range(len(state)):
        for j in range(state[i]):
            disp.append(i)
    print(disp)
    print()

def main():
    fileName = 'd6.txt'
    state = readContents(fileName)

    days = 256

    for _ in range(days):
        add = 0
        for i in range(len(state)):
            if i == 0:
                if state[0] > 0:
                    add= state[0]
                    state[0] = 0
                    state
            else:
                if(state[i] > 0):
                    temp = state[i]
                    state[i] = 0
                    state[i - 1] += temp
        state[8] += add
        state[6] += add
        
        

    count = 0

    for i in range(len(state)):
        count += state[i]
    print(count)


if __name__ == "__main__":
    main()