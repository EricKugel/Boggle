board = [[],[],[],[]]
words = []
dictionary = {}

class Cell():
    def __init__(self, coords):
        self.coords = coords
        self.letter = board[coords[1]][coords[0]]
        self.neighbors = []

    def getNeighbors(self):
        neighbors = []
        for xOffset in range(3):
            for yOffset in range(3):
                x = self.coords[0] - 1 + xOffset
                y = self.coords[1] - 1 + yOffset
                if (x >= 0 and y >= 0 and x < 4 and y < 4):
                    currentCell = Cell((x,y))
                    neighbors.append(currentCell)
        return neighbors

    def isSameAs(self, cell):
        if self.coords == cell.coords:
            return True
        return False

def main():
    
    # set board to letters in board.txt
    boardFile = open("board.txt")
    lines = boardFile.readlines()
    boardFile.close()
    for lineIndex in range(len(lines)):
        line = lines[lineIndex]
        for letter in line:
            if letter != "|" and letter != "\n":
                board[lineIndex].append(letter.lower())

    # set board to letters in board.txt
    dictFile = open("dictionary.txt")
    global dictionary
    dictionary = set(dictFile.readlines())
    dictFile.close()

    # loop through each cell for each word length
    for iter in range(5):
        wordLength = iter + 3
        for x in range(len(board)):
            for y in range(len(board[0])):
                startingCell = Cell((x, y))
                word = [startingCell]
                recurse(word, wordLength)

def recurse(word, wordLength):
    if len(word) < wordLength:
        startingCell = word[-1]
        neighbors = startingCell.getNeighbors()
        for neighbor in neighbors:
            newWord = word.copy()
            isDuplicate = False
            for cell in word:
                if cell.isSameAs(neighbor):
                    isDuplicate = True
                    break
            if not isDuplicate:
                newWord.append(neighbor)
                recurse(newWord, wordLength)
                
                
    elif len(word) == wordLength:
        wordString = wordToString(word) + "\n"
        if not wordString in words:
            if wordString in dictionary:
                words.append(wordString.strip())
                print(wordString.strip())

def wordToString(word):
    wordString = ""
    for cell in word:
        wordString += cell.letter
    return wordString

if __name__ == "__main__":
    main()