# Name: Jeffrey, Bonnie
# Date:6/22/18


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
randomword=choose_word(wordlist)

print randomword
#list1=[]
blanks=[]
list3=[]#actual list for a bunch of blanks
list4=[]
correctword = (randomword)
print correctword
wordlength2=len(blanks)
wordlength=len(correctword)
wordlength3 = len(list3)#setting the lenghth of what the blanks are naming it
while wordlength3 < wordlength:
    list3.append('-')
    wordlength3 = wordlength3+1
print list3
playerinput = raw_input("enter your letter")
index=0
#if playerinput==correctword(index):

while index < wordlength3 + 1:
    index = index + 1
    print list3
    if playerinput == correctword[index]:
        list3[index] = playerinput

    elif playerinput != correctword[index]:






#while wordlength3 < wordlength:
    #list3.append('-')
    #indexnumber = 0
    #while indexnumber < wordlength:
        #indexnumber = indexnumber + 1
        #print list3




#print blanks
#print len(blanks)

#for letters in (correctword):

    #if playerinput == correctword[indexnumber]: #this part is for placing correct letters

        #wordlength3 = len(list3)


    #else:
        #while indexnumber < wordlength:
            #indexnumber = indexnumber + 1
    #list4.append(playerinput)
    #print list4
