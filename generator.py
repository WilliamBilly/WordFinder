import random

#Gets the direction and length of the word
def getDirAndLen(x,y,size):
	directionAndLen = []
	possibleDirs = [1,2,3,4,5,6,7,8]#1 is up, goes counterclockwise
	if x == 1:
		possibleDirs.remove(6)
		possibleDirs.remove(7)
		possibleDirs.remove(8)
	if x == size:
		possibleDirs.remove(2)
		possibleDirs.remove(3)
		possibleDirs.remove(4)
	if y == 1:
		possibleDirs.remove(1)
		if x != size:
			possibleDirs.remove(2)
		if x != 1:
			possibleDirs.remove(8)
	if y == size:
		if x != size:
			possibleDirs.remove(4)
		possibleDirs.remove(5)
		if x != 1:
			possibleDirs.remove(6)
	directionAndLen.append(possibleDirs[random.randint(0,len(possibleDirs)-1)])
	directionAndLen.append(getLength(x,y,directionAndLen[0],size))
	return directionAndLen

def getLength(x,y,direction,size):
	if direction == 1:#Up
		maxLen = y
	if direction == 3:#Right
		maxLen = size-x+1
	if direction == 5:#Down
		maxLen = size-y+1
	if direction == 7:#Left
		maxLen = x
	if direction == 2:
		if x>size-y+1:#UP RIGHT
			maxLen = size-x+1
		else:
			maxLen = y		
	if direction == 4:#DOWN RIGHT
		if x>y:
			maxLen = size-x+1
		else:
			maxLen = size-y+1		
	if direction == 6:#DOWN LEFT
		if x>size-y+1:
			maxLen = size-y+1
		else:
			maxLen = x		
	if direction == 8:#UP LEFT
		if x>y:
			maxLen = y
		else:
			maxLen = x
	return random.randint(2,maxLen)

def checkDups(words):
	if len(words) != len(set(words)):
		return 1
	return 0

#This reads in the user input stuff.
numWords = 0
while numWords < 1:
	print"How many words to find?"
	numWords = int(raw_input(""))
size = 0
while size <= 2:
	print "How big of a board do you want? Must be larger than 2."
	size = int(raw_input(""))
print "Creating board!"

#This makes the board
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
row = []
board = []
for x in range(size):
	for y in range(size):
		row.append(letters[random.randint(0,25)])
	board.append(row)
	row = []#Clears the row variable for the next row
print "Printing board!"

#This prints the board
inputFile = open("input.txt",'w')
s=""#The string to print
for x in range(size):
	for y in range(size-1):
		s += str(board[x][y])+" "
	s += str(board[x][size-1])+'\n'
	inputFile.write(s)
	s=""#Clears the string again
print "Finding words!"

count = 1
words = []
for i in range(numWords):
	while True: #Repeat the following until a word is found that hasn't been used yet.
		startx = random.randint(1,size)
		starty = random.randint(1,size)
		directionAndLen = []
		directionAndLen = getDirAndLen(startx,starty,size)
		direction = directionAndLen[0]
		length = directionAndLen[1]
		word = str(board[startx-1][starty-1])
		if direction == 1:
			for t in range(1,length):
				word = word+str(board[startx-1][starty-1-t])
		if direction == 2:
			for t in range(1,length):
				word = word+str(board[startx-1+t][starty-1-t])
		if direction == 3:
			for t in range(1,length):
				word = word+str(board[startx-1+t][starty-1])
		if direction == 4:
			for t in range(1,length):
				word = word+str(board[startx-1+t][starty-1+t])
		if direction == 5:
			for t in range(1,length):
				word = word+str(board[startx-1][starty-1+t])
		if direction == 6:
			for t in range(1,length):
				word = word+str(board[startx-1-t][starty-1+t])
		if direction == 7:
			for t in range(1,length):
				word = word+str(board[startx-1-t][starty-1])
		if direction == 8:
			for t in range(1,length):
				word = word+str(board[startx-1-t][starty-1-t])
		words.append(word)
		if checkDups(words) == 0:
			print "Found word",str(len(words)),"of",str(numWords)
			count = 1
			break
		words.remove(word) 
		count += 1
		if count >= 100000:
			print "Too many words; try less." 
			break
	if count >= 100000:
		break

if checkDups(words) == 0 and count < 100000:
	print "Success! Board and unique words list generated!"
else:
	print "Not all words were found, but list generated anyway.",len(words),"words were made."
for word in words:
	inputFile.write(word+"\n")
