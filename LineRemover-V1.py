# Created by Express | 21/09/2020 | 18:59
# Program for line suppression based on blacklisted words

import os
import time
from tqdm import tqdm

words = []
while True:
    blacklist = input("Enter all blacklisted words one by one : ")
    words.append(blacklist)
    if blacklist == "exitprogram":
        words.remove("exitprogram")
        break
    else:
        continue

print(words)

directory = input("Enter the *.txt file directory : ")

while os.path.isfile(directory) == False:
    print("File not found, retry !")
    directory = input("Enter the *.txt file directory : ")
    if os.path.isfile(directory) == True:
        print("File found !")
        break

exitfile = input("Enter the output file directory : ")

with open(directory) as oldfile, open(exitfile, 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in words):
            newfile.write(line)
oldfile.close()
newfile.close()


