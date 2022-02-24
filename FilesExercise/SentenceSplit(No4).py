import re  # importing re for splitting the sentences (heuristics set)

excerpt = open("miyagitest.txt", "r")  # opening the test file
text = excerpt.read()  # variable consisting of the content from the test file

text = re.sub(r"\n", " ", text)  # removing original newlines

# if statements to replace titles with alternative words (remove periods)
if "Mr." in text:  # replace Mr. with Mister
    text = text.replace("Mr.", "Mister")
if "Mrs." in text:  # replace Mrs. with Miss
    text = text.replace("Mrs.", "Miss")
if "Dr." in text:  # replace Dr. with Doctor
    text = text.replace("Dr.", "Doctor")
if "Jr." in text:  # replace Jr. with Junior
    text = text.replace("Jr.", "Junior")

text = re.sub(r"\.\s([A-Z])", r".\n\1", text)  # must be followed by a space and an uppercase letter for newline
text = re.sub(r"!\s", "!\n", text)  # newline after ! (with space)
text = re.sub(r"\?\s", "?\n", text)  # newline after ? (with space)

# if statements to change back the alternative words to the titles
if "Mister" in text:  # replace Mister with Mr.
    text = text.replace("Mister", "Mr.")
if "Miss" in text:  # replace Miss with Mrs.
    text = text.replace("Miss", "Mrs.")
if "Doctor" in text:  # replace Doctor with Dr.
    text = text.replace("Doctor", "Dr.")
if "Junior" in text:  # replace Junior with Jr.
    text = text.replace("Junior", "Jr.")

# printing the text after splitting sentences
print(text)
