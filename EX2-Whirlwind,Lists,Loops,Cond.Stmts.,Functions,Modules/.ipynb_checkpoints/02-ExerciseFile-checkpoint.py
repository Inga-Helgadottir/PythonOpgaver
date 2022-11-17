import csv
import platform
import argparse

def print_file_content(filename):
    # that can print content of a csv file to the console
    with open(filename) as f_obj:
        content = f_obj.readlines()

    for line in content[:20]:
        print(line.strip().split(','))
           
def write_list_to_file(output_file, mytuple) :
    # that can take a tuple of strings and write each element to a new line in file 1. 
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        
        output_writer.writerow(mytuple)
        
def write_list_to_file_rewrite(output_file, *multibleInputs) :
    # rewrite the function so that it gets an arbitrary number of strings instead of a list
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        
        output_writer.writerow(multibleInputs)
    
myList = []

def read_csv(filename) :
    # that take a csv file and read each row into a list. Print the list.
    with open(filename) as f_obj:
        content = f_obj.readlines()

    for line in content[:20]:
        myList.append(line.strip());
        
    for i in myList:
        print(i)

myCSVList = []   

def read_csv_add(path, possibleFile="not") :
    # Add a functionality so that the file can be called from cli(command line interface) with 2 arguments:
    # path to csv file
    # an argument --file file_name that if given will write the content to file_name 
    # or otherwise will print it to the console.
    # Add a --help cli argument to describe how the module is used
    if possibleFile == "not":
        # print it to the console.
        with open(path) as f_obj:
            content = f_obj.readlines()

        for line in content[:20]:
            print(line.strip().split(','))
    else:     
        # will write the content to file_name 
        reader = csv.reader(open(path, 'r'))
        writer = csv.writer(open(possibleFile, 'w'))
        for row in reader:
            writer.writerow(row)
            
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='the file can be called from cli(command line interface) with 2 arguments, file and possible file, the first is necessary and the second is optional. If you send 2 arguments it takes the content from one at puts it in the other, if not it just prints the content.')
    
        print(parser.parse_args())

# Calling all functions below for testing ----------------------------------------------------
# print_file_content('myCSVFile.csv') 
# mytuple = ("apple", "banana", "cherry")
# write_list_to_file('file.csv', mytuple)
# write_list_to_file_rewrite('file2.csv', "first value", "second", "third")
# read_csv('myCSVFile.csv')
# read_csv_add('file.csv')
read_csv_add('file.csv', 'file_name2.csv')