from time import *#Used to see how long it takes
inputFile = open("input.txt","r")#Opens the file
table = []#This is the table that holds the whole grid
table.append(inputFile.readline().strip('\n').split(" "))#Reads in the first line of the table from the file
linecount = len(table[0])-1#This is so the following for loop doesn't read in too many lines from the file
for i in range (linecount):#Reads in the rest of the table. It read in 1 line first to count how big the square is
	table.append(inputFile.readline().strip('\n').split(" "))#Reads in the file
words = []#This is the list of keywords
words = inputFile.read().strip("\n").split("\n")#Read in the list of keywords
inputFile.close()
linecount +=1 #Returns linecount to the actual number of lines.
startTime = time()#Records the start time
for x in range (linecount):#Iterates through the rows
	for y in range (linecount):#Iterates through the columns (yes, I know x and y are flipped. I'm retarded)
		numwords = len(words)#This checks how many words have yet to be found.
		if (numwords==0):#If no more words have yet to be found,
			print "That took",time()-startTime,"seconds!"#print how long it took
			quit()#and then quit.
		letter = table[x][y]#If there are still words to find, assign the new letter from the table to be found
		t = 0#This is the variable used to iterate through the list of words that could be at the current letter in the table.
		while (t < numwords):#This will search to see if the words in the list exist at the current point
			word = words[t]#Get the word
			if word[0] == letter:#If the first letter of the selected word matches the selected letter from the table,
				wordLen = len(word)#get the length of the word, and search in the following directions from the original point. 			
				#RIGHT
				found = 1#Boolean value, assuming that the word was found
				for i in range(1,wordLen):#Searches only as long as the word is
					if y+i < linecount:#Makes sure the code won't search off the end of the grid in the given direction
						if table[x][y+i] != word[i]:#Iterates in the given direction, and if the letters don't match at all
							found = 0#then it's not found
							break#and break out of this for loop.
					else:
						found = 0#if the search goes off the edge of the board, assume it isn't here
				if found == 1:#if the word wasn't not found (if that makes sense) then assume it was found!
					print word,"found! At",x+1,y+1,"going right"#Print that it was found
					words.remove(word)#remove the word from the list
					numwords-=1#Reduce the number of remaining words
					continue#Then move on to see if the next word in the list of words exists at this point.
				#DOWN
				found = 1
				for i in range(1,wordLen):
					if x+i < linecount:
						if table[x+i][y] != word[i]:
							found = 0
							break
					else:
						found = 0
				if found == 1:
					print word,"found! At",x+1,y+1,"going down"
					words.remove(word)
					numwords-=1
					continue
				#DOWN RIGHT
				found = 1
				for i in range(1,wordLen):
					if y+i < linecount and x+i < linecount:
						if table[x+i][y+i] != word[i]:
							found = 0
							break
					else:
						found = 0
				if found == 1:
					print word,"found! At",x+1,y+1,"going down right"
					words.remove(word)
					numwords-=1
					continue			
				#DOWN LEFT
				found = 1
				for i in range(1,wordLen):
					if y-i < linecount and x+i < linecount:
						if table[x+i][y-i] != word[i]:
							found = 0
							break
					else:
						found = 0
				if found == 1:
					print word,"found! At",x+1,y+1,"going down left"
					words.remove(word)
					numwords-=1
					continue
				#LEFT
				found = 1
				for i in range(1,wordLen):
					if y-i < linecount:
						if table[x][y-i] != word[i]:
							found = 0
							break
					else:
						found = 0
				if found == 1:
					print word,"found! At",x+1,y+1,"going left"
					words.remove(word)
					numwords-=1
					continue	
				#UP
				found = 1
				for i in range(1,wordLen):
					if x-i < linecount:
						if table[x-i][y] != word[i]:
							found = 0
							break
					else:
						found = 0
				if found == 1:
					print word,"found! At",x+1,y+1,"going up"
					words.remove(word)
					numwords-=1
					continue	
				#UP RIGHT
				found = 1
				for i in range(1,wordLen):
					if y+i < linecount and x-i < linecount:
						if table[x-i][y+i] != word[i]:
							found = 0
							break
					else:
						found = 0
				if found == 1:
					print word,"found! At",x+1,y+1,"going up right"
					words.remove(word)
					numwords-=1
					continue
				#UP LEFT
				found = 1
				for i in range(1,wordLen):
					if y-i < linecount and x-i < linecount:
						if table[x-i][y-i] != word[i]:
							found = 0
							break
					else:
						found = 0
				if found == 1:
					print word,"found! At",x+1,y+1,"going up left"
					words.remove(word)
					numwords-=1
					continue
			t+=1#If the word was not found, move on to the next word to see if it is at that point.
if len(words)>0:
	print "Not all the words were found. Oops."
print "That took",time()-startTime,"seconds!"#print how long it took
