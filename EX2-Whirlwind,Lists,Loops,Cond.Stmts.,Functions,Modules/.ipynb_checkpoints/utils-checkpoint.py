import os
def get_file_names(folderpath,out):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(folderpath):
        # check if current path is a file
        if os.path.isfile(os.path.join(folderpath, path)):
            res.append(path)
    print(res)

# def get_all_file_names(folderpath,out=output.txt):
#     """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

# def print_line_one(file_names):
#     """takes a list of filenames and print the first line of each"""

# def print_emails(file_names):
#     """takes a list of filenames and print each line that contains an email (just look for @)"""

# def write_headlines(md_files, out=output.txt):
#     """takes a list of md files and writes all headlines (lines starting with #) to a file"""

get_file_names("./","output.txt")