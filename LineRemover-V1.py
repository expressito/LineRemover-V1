# Created by Express | 22/04/2020 | 18:59
# Contributors: Rififi | 23/04/2020 | 12:21
# Program for line suppression based on blacklisted words.

import os

words = []
rawIn = None
while rawIn != "":
    rawIn = input("Enter all blacklisted words one by one : ")
    if rawIn != "":
        words.append(rawIn)

print("Black listed words are : ", words)

fileFound = None
while not fileFound:
    inFilePath = input("Enter the input file's path : ")
    fileFound = os.path.isfile(inFilePath)
    print("File found !" if fileFound else "File not found, please retry !")

outFilePath = input("Enter the output file's path : ")#Todo : check validity of entered path.

with open(inFilePath) as oldFile, open(outFilePath, 'w') as newFile:
    for line in oldFile:
        if not any(bad_word in line for bad_word in words): #Todo : with a RegEx, be sure to only find whole words (between spaces/delimiters), be cause if "bon" is blacklisted, "bonjour" will trigger the program for example.
            newFile.write(line)
    oldFile.close()
    newFile.close()
