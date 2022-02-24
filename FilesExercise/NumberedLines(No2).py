firstfile = open("sampletext.txt", "r")  # opening the first file (i used the sampletext file out of convenience)
firstcontent = firstfile.readlines()  # variable consisting of the file lines

newfile = open("numberedline.txt", "w")  # opening/creating a new file
num = 1  # num for the lines

for x in firstcontent:  # for loop that loops through all the lines in the first file
    numbered = str(num) + ". " + x  # what would be written (ex: 1. line)
    newfile.write(numbered)  # writing the content in the new file
    num += 1  # number goes up by 1 every loop so the text is numbered by each line
