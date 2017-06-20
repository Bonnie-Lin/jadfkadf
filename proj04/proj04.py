# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
userinputlist2 = []
userinput = raw_input ("Enter a string!")
userinputlist = []
for letters in userinput:
    userinputlist.append(letters)

    length = len(userinputlist)
    userinputlist2 = [letters] + userinputlist2
if userinputlist == userinputlist2:
    print "Your string is a palindrome"
else:
    print "Your string is not a palindrome"
print "your word backwards is:"
print userinputlist2





