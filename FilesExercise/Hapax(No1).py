import string  # import string for string.punctuation

excerpt = open("sampletext.txt", "r")  # opens sample text file to read
excerptcontent = excerpt.read()  # gets the contents of sample text file into a variable
for x in string.punctuation:  # for loop to replace the punctuations with " "
    excerptcontent = excerptcontent.replace(x, " ")
excerptfinal = excerptcontent.lower()  # final sample text, without punctuation and capitalization


def hapax(excerptfinal):  # defining function to return the list of all the words and frequencies
    wordslist = {}
    splitexcerpt = excerptfinal.split()
    for words in splitexcerpt:
        wordslist[words] = wordslist.get(words, 0)+1
    return wordslist


hapaxlist = hapax(excerptfinal)  # global variable from function's return

print("The hapaxes in the text are: ")
for y, value in hapaxlist.items():  # for loop to print all the words that only appeared once
    if value == 1:
        print(y)
