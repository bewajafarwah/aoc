def str2dec(value):
    dec = 0
    i = len(value) - 1
    j = 0
    while i >= 0:
        dec += (int(value[i]) * (2 ** j))
        j+=1
        i-=1
    return dec

def getAcceptedIndices(bit, bin, at, accepted):
    acc = []
    for i in accepted:
        if(bin[i][at] == bit):
            acc.append(i)
    return acc

def main(filename):
    fi = open(filename, 'r').readlines()

    bin = []
    for b in fi:
        bin.append(b.strip())
    
    binary_len = len(bin[0])
    accepted = [*range(len(bin))]

    ogr = ""
    for i in range(binary_len):
        c1 = 0
        c0 = 0
        for j in accepted:
            bits = bin[j]
            bit = bits[i]
            if(bit == '1'):
                c1+=1
            else:
                c0+=1
    
        if c1 >= c0:
            b = '1'
        else:
            b = '0'
        
        prev_accepted = accepted
        accepted = getAcceptedIndices(b, bin, i, accepted)
        if(len(accepted) == 0):
            break
        ogr+=b

    if(len(ogr) != binary_len):
        for s in range(i, binary_len):
            ogr+=bin[prev_accepted[0]][s]
    #print(ogr)


    accepted = [*range(len(bin))]
    co2 = ""
    for i in range(binary_len):
        c1 = 0
        c0 = 0
        for j in accepted:
            bits = bin[j]
            bit = bits[i]
            if(bit == '1'):
                c1+=1
            else:
                c0+=1
    
        if c0 <= c1:
            b = '0'
        else:
            b = '1'
        
        prev_accepted = accepted
        accepted = getAcceptedIndices(b, bin, i, accepted)
        if(len(accepted) == 0):
            break
        co2+=b
    
    if(len(co2) != binary_len):
        for s in range(i, binary_len):
            co2+=bin[prev_accepted[0]][s]

    print(ogr, co2)
    print(str2dec(ogr), str2dec(co2), str2dec(ogr) * str2dec(co2))
if __name__ == '__main__':
    filename = "d3.txt"
    main(filename)