import string  # import string module for string.punctuation

file = open("sampletext.txt", "r")  # opening the sample text file to read
content = file.read()  # variable consisting of the contents of the sample text
nopunc = content  # declaring another variable with the same contents for the for loop

for x in string.punctuation:  # for loop to replace the punctuations with " "
    nopunc = nopunc.replace(x, " ")

contentword = nopunc.split()  # split the text into a list of the words

words = len(contentword)  # variable containing the number of the words
characters = len(nopunc) - nopunc.count(" ")  # length of the words without the spaces
avg = characters // words  # average length of each word

# printing the sum of words, lengths and average number
print("The sum of words in the text is:", words)
print("The sum of the lengths of the word tokens in the text is:", characters)
print("The average number of characters in one word is:", avg)
