def readContents(fileName):
    lines = open(fileName, 'r').readlines()
    line = lines[0].split(',')
    state = []
    for l in line:
        state.append(int(l))
    return state

def main():
    fileName = 'd6e.txt'
    state = readContents(fileName)

    days = 256

    for _ in range(days):
        newfishcount = 0
        for i in range(len(state)):
            if state[i] == 0:
                newfishcount += 1
                state[i] = 6
            else:
                state[i]-=1
        for i in range(newfishcount):
            state.append(8)
        

    print(len(state))


if __name__ == "__main__":
    main()