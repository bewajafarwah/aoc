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


def main1():
    fileName = 'd1.in'
    elf = readContents(fileName)
    max = -1
    for e in elf:
        if sum(e) > max:
            max = sum(e)
    print(max)

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
                mval = sum(e)
        max.append(mval)
        count += 1
    print(sum(max))

def check():
    inf = 'd1.in'
    ll = [[int(y) for y in x.split("\n")] for x in open(inf).read().strip().split('\n\n')]
    print(max([sum(x) for x in ll]))
    print(sum(sorted([sum(x) for x in ll])[-3:]))
if __name__ == "__main__":
    main1()
    main2()
    check()