#READING AND WRITING FILES
definition = """
A computer file is a computer resource for recording data discrete
ly in a
computer storage device. Just as words can be written
to paper, so can information be written to a computer
this is overriden
"""

#we will write this into file named "file_definition.txt"
# file1 = open("file_definition.txt", "w").write(definition)

#reading "file_definition.txt"
text = open("file_definition.txt").read()
# print(text)

#____________________________________________________
#if file is too large it is inefficient to read in one string object.
#so we read file line by line.
# with open("large_file.txt", "r") as file:
#     for line in file:
        # print(line.strip())/
# ____________________________________________________________________
#READING LINE BY LINE FROM ONE FILE AND WRITE THE CHANGED CONTENT INTO ANOTHER FILE
# with open("pythonista_and_python.txt") as infile:
#     with open("python_newbie_and_guru.txt", "w") as outfile:
#         for line in infile:
#             line = line.replace("Pythonista", "Python newbie")
#             line = line.replace("Python snake", "Python guru")
#             print(line.rstrip())
#             #write the line into file:
#             outfile.write(line)

# ________________________________________________________________________________________
#if file is not that large and if it needed replacement in content we can use read() which returns string containing the complete content of the file, including the
#carriage returns and line feeds. There is no need of with construct because there will be no reference to the file ie. ite will be immediately deleted after reading
# and writing

# txt = open("pythonista_and_python.txt").read()
# txt = txt.replace("Pythonista", "Python noob")
# txt = txt.replace("Python snake", "Python Pro")
# open("python_noob_and_the_pro.txt", "w").write(txt)

#_______________________________________________________________________________________________________________________________________________
#RESETTING THE FILES CURRENT POSITION

txt = open("small_text.txt", "w").write("brown is her favorite color")

fh = open("small_text.txt")
# print(fh.tell())
# print(fh.read(5))
# print(fh.tell())
# print(fh.read())
# print(fh.tell())

# print(fh.seek(5))
# print(fh.read())
# print(fh.tell())
# print(fh.read())
# print(fh.tell())

#________________________________________________________________
# txt = "Görüşürüz, yarın geleceğim."
# number_of_chars_written = open("see_you_tomoroow.txt", "w").write(txt)
# print(number_of_chars_written)

# text = open("see_you_tomoroow.txt", "r").read()
# print("text mode: ", text)

# text_binary = open("see_you_tomoroow.txt", "rb").read()
# print("binary mode: ", text_binary)
# t = text_binary.decode("utf-8")

# print(t)
# ____________________________________________________________________________________________
#READING AND WRITING TO SAME FILE
#if the file doesn't exist it will be created.
#if you want to open existing file for read and write you should use "r+" so that the existing 
#content is not deleted
fh = open("colours.txt", "w+")
fh.write("The colour brown")

#go to the 12th byte in file, counting starts with 0
fh.seek(11)
print(fh.read(5))
print(fh.tell())
fh.seek(11)
print(fh.read())