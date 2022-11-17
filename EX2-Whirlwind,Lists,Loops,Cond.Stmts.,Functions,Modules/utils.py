from operator import contains
import sys, os

def get_file_names(folderpath,out):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    # Iterate directory
    for path in os.listdir(folderpath):
        # check if current path is a file
        if os.path.isfile(os.path.join(folderpath, path)):
            with open(out, 'a') as file_object:
                file_object.write(path + '\n')

def get_all_file_names(folderpath,out):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    path = os.path.join(folderpath, "targetdirectory")

    for path, subdirs, files in os.walk(folderpath):
        for name in files:
            with open(out, 'a') as file_object:
                file_object.write(os.path.join(path + '\n', name + '\n'))

def print_line_one(*fileNames):
    """takes a list of filenames and print the first line of each"""
    for name in fileNames:
        with open(name) as file:
            print(file.readline())
            

def print_emails(*file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for n in file_names:
        with open(n) as file_object:
            for line in file_object:
                if "@" in line:
                    print(line)

def write_headlines(out, *md_files):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    for n in md_files:
        with open(n) as file_object:
            for line in file_object:
                if line.startswith("#"): # all headlines
                # if line.startswith("# "): # only the biggest headines
                    print(line)

# Calling functions for testing

# get_file_names("./","output.txt")
# get_all_file_names("../", "output2.txt")
# print_line_one("output.txt", "output2.txt", "emailsAndOtherStuff.txt")
    # shoud be: 01-Exercise.ipynb, ../, something here
# print_emails("emailsAndOtherStuff.txt", "emailsAndOtherStuff2.txt", "emailsAndOtherStuff3.txt")
    # shoud be 
        # something@gmail.com
        # fake@email.com
        # anotherFakeEmail@myEmail.com
        # myEmail@gmail.com
        # hihi@gmail.com
        # hoho@gmail.com
        # johoi@gmail.com
        # hahahhah@email.com
        # something@hotmail.com
# write_headlines("outputMD.txt", "mdFile.md", "mdFile2.md", "mdFile3.md")