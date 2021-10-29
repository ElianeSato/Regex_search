#! python3
# Usage: this program opens all *.txt* files in a folder and searches for any line that matches
# a user-supplied regular expression. The results will be printed to the screen.

from pathlib import Path
import os, re

cwd = Path.cwd()
folder_content = os.listdir(cwd)

pattern = input("Enter a pattern of text to search for: ")
regex = re.compile(pattern)


for file in folder_content:
    if ".git" != file and (".txt" in file):
        with open(file) as file:
            for line in file.readlines():
                if regex.search(line):
                    print(file.name)
                    print(line)

