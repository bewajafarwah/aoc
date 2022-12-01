import numpy as np

def readContents(filename):
    lines = open(filename, 'r').readlines()

    seq = lines[0].strip().split(',')
    
    boards = []
    board = []
    for line in lines[2:]:
        if line == '\n':
            boards.append(board)
            board = []
            continue

        col = []
        nums = line.strip().split(' ')
        for num in nums:
            if num == '':
                continue
            col.append(num)
        board.append(col)
    boards.append(board)

    return seq, boards

def checkInBoard(number, board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if number == board[r][c]:
                return r, c

def isWinState(score, length=5):
    for r in range(len(score)):
        countc = 0
        countr = 0
        for c in range(len(score[r])):
            if score[r][c] == 1:
                countr += 1
            if score[c][r] == 1:
                countc += 1
        if countc == length or countr == length:
            return True
    
    return False

def printBox(arr, index=''):
    print('INDEX', index)
    for line in arr:
        print(line)
    print()

def getUnmarkedSum(board, score):
    total = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if score[r][c] == 0:
                total += int(board[r][c])
    return total

def main():
    filename = 'd4.txt'
    seq, boards = readContents(filename)

    square = 5
    winning_board = -1
    winning_number = -1
    win_flg = False

    score = np.zeros((len(boards), square, square))

    winning_boards = []

    for number in seq:
        for board_index in range(len(boards)):
            if board_index in winning_boards:
                continue
            board = boards[board_index]
            coord = checkInBoard(number, board)
            if coord is None:
                continue
            r, c = coord
            score[board_index][r][c] = 1
            if isWinState(score[board_index]):
                winning_boards.append(board_index)
                if len(winning_boards) == len(boards):
                    winning_board = board_index
                    winning_number = number
                    win_flg = True
                    break
        
        if win_flg:
            break

    #print(winning_board, winning_number)
    
    unmarkedSum = getUnmarkedSum(boards[winning_board], score[winning_board])
    print(unmarkedSum, int(winning_number))
    print(unmarkedSum * int(winning_number))



if __name__ == '__main__':
    main()
