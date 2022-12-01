def readContents(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
    
    inputs = []
    outputs = []

    for line in lines:
        inp, out = line.strip().split('|')
        input = []
        output = []
        for i in inp.strip().split(' '):
            input.append(''.join(sorted(i)))
        for j in out.strip().split(' '):
            output.append(''.join(sorted(j)))
        # inputs.append(inp.strip().split(' '))
        # outputs.append(out.strip().split(' '))
        inputs.append(input)
        outputs.append(output)
    

    return inputs, outputs


def part1(outputs):
    count = 0
    lens = [7, 4, 2, 3]

    for out in outputs:
        for digit in out:
            if len(digit) in lens:
                count += 1

    return count


def common(a, b):
    c = ''
    for valuea in a:
        for valueb in b:
            if valuea == valueb:
                if valuea not in c:
                    c += valuea
    return c

def uncommon(a, b):
    c = common(a, b)
    
    r = ''
    for valuea in a:
        if valuea not in c:
            r += valuea

    for valueb in b:
        if valueb not in c:
            r += valueb

    return r

def getNumbers(inputs):
    num = {}
    unqLen = {2 : 1, 4 : 4, 3 : 7, 7 : 8} #len : number
    len_5 = []
    len_6 = []
    for inp in inputs:
        if len(inp) in unqLen:
            num[unqLen[len(inp)]] = ''.join(sorted(inp))
        elif len(inp) == 5:
            len_5.append(''.join(sorted(inp)))
        elif len(inp) == 6:
            len_6.append(''.join(sorted(inp)))

        
    return num, len_5, len_6

    
def rules(num, len_5, len_6):
    for l5 in len_5:
        if len(common(l5, num[1])) == 2:
            num[3] = l5
    
    for l6 in len_6:
        if len(uncommon(l6, num[3])) == 1:
            num[9] = l6

    for l5 in len_5:
        if len(uncommon(l5, num[9])) == 3:
            num[2] = l5

    for l5 in len_5:
        if l5 not in num.values():
            num[5] = l5


    for l6 in len_6:
        if len(uncommon(l6, num[5])) == 3:
            num[0] = l6

    for l6 in len_6:
        if l6 not in num.values():
            num[6] = l6

    return num

def part2(inputs, outputs):
    ret = ''
    total = 0
    for input, output in zip(inputs, outputs):
        num, len_5, len_6 = getNumbers(input)
        num = rules(num, len_5, len_6)
        number = 0
        for out in output:
            outs = ''.join(sorted(out))
            for key, value in num.items():
                if outs == value:
                    number = (number * 10) + key
                    break
        ret += "{} : {}\n".format(output, number)
        total += number
    return ret + '\n{}'.format(total)

def main():
    fileName = 'd8.txt'
    inputs, outputs = readContents(fileName)
    #print(f'Ans 1: {part1(outputs)}')
    print(f'Ans 2: \n{part2(inputs, outputs)}')

if __name__ == "__main__":
    main()

    # num = {
    #     0 : 'abcefg',
    #     1 : 'cf',
    #     2 : 'acdeg',
    #     3 : 'acdfg',
    #     4 : 'bcdf', 
    #     5 : 'abdfg',
    #     6 : 'abdefg',
    #     7 : 'acf',
    #     8 : 'abcdefg',
    #     9 : 'abcdfg'
    # }

    # a = num[5]
    # b = num[9]
    # print('Common', common(a, b))
    # print('Uncommon', uncommon(a, b))