def readContents(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()

    elf = []
    e = []
    for line in lines:
        if line == '\n':
            elf.append(e)
            e = []
            continue
        e.append(int(line.strip()))

    elf.append(e)
    return elf


def main():
    fileName = 'd1.in'
    elf = readContents(fileName)
    max = -1
    for e in elf:
        if sum(e) > max:
            max = sum(e)
    print(sum(max))

def main2():
    fileName = 'd1.in'
    elf = readContents(fileName)

    max = []
    mval = -1
    count = 0
    while count != 3:
        mval = -1
        for e in elf:
            if mval < sum(e) and sum(e) not in max:
                print(count, mval, sum(e))
                mval = sum(e)
        max.append(mval)
        count += 1
    print(sum(max))
if __name__ == "__main__":
    main2()