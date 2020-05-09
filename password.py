#! /usr/bin/python

import string
import sys
import getopt
from random import randint 

argumentList = sys.argv[1:] 
options = "hrdc:f:ls"
long_options = ["help", "random", "dictionary", "count =", "files =", "seperator", "leadingSymbol"] 
characters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)
count = 0
password = ""
file = open("dictionary.txt", "r").readlines()
seperator = False
leadingSymbol = False

def main():
    global count, file, seperator, leadingSymbol

    if len(argumentList) == 0:
        welcome()
    else:
        parse()

def welcome():
    text = ("" +
"  _____                                    _    _____                           _             \n" +
" |  __ \                                  | |  / ____|                         | |            \n" +
" | |__) |_ _ ___ _____      _____  _ __ __| | | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ \n" + 
" |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|\n" + 
" | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   \n" + 
" |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   \n\n")
                                                                                              
    print(text)
    print("Choose one of the options below to generate a password.")
    print("For additional options use the command line parameters.")
    print("1. Random")
    print("2. Dictionary")
    print("3. Show all options")
    selection = int(input("Selection: "))

    if selection == 1:
        random()
    elif selection == 2:
        dictionary()
    else:
        showOptions()

def parse():
    try: 
        arguments, values = getopt.getopt(argumentList, options, long_options) 
        
        for currentArgument, currentValue in arguments: 
            # Set variables passed in.
            if currentArgument in ("-c", "--count"): 
                count = int(currentValue)
            if currentArgument in ("-s", "--seperator"): 
                seperator = True
            if currentArgument in ("-l", "--leadingSymbol"): 
                leadingSymbol = True
            if currentArgument in ("-f", "--file"): 
                file = open(currentValue, "r").readlines()

            # 
            if currentArgument in ("-h", "--help"): 
                showOptions()
                print("showed options")
            elif currentArgument in ("-r", "--random"): 
                random() 
            elif currentArgument in ("-d", "--dictionary"): 
                dictionary()   
    except getopt.error as err: 
        print (str(err)) 

def random():
    global count, file, password

    if count == 0: count = 20

    for x in range(count):
        value = randint(0, 20)
        if (value % 20) == 0: # 10% symbols
            password += symbols[randint(0, len(symbols) - 1)]
        elif (value % 4) == 0: # 20% numbers
            password += digits[randint(0, len(digits) - 1)]
        else: # 70% letters
            password += characters[randint(0, len(characters) - 1)]
    
    print("The generated password is: " + password)

def dictionary():
    global count, file, password, seperator, leadingSymbol

    if count == 0: count = 3
    if leadingSymbol: password = symbols[randint(0, len(symbols) - 1)]

    for x in range(count):
        password += file[randint(0, len(file) - 1)].capitalize().rstrip("\n").replace(" ", "_")
        if seperator and x + 1 < count: password += "-"

    print("The generated password is: " + password)

def showOptions():
    print("-r, --random            Generate a random password.")
    print("                        Will default to 20 characters if no argument is supplied for '--count'.")
    print("                        Example usage: password.py -c <count> -r")
    print("/n                        Note: Random takes precidence over dictionary, due to inherent strength advantage.
    print("-d, --dictionary        Generate a random password using a dictionary of words.")
    print("                        Will default to 3 words if no argument is supplied for '--count'.")
    print("                        Will default to built in dictionary if no list is supplied using '--file'.")
    print("                        Example usage passoword.py -c <count> -file <dictionary> -d")
    print("-c, --count             Specify the number of characters in the '--random' option or number of words in the '--dictionary' option.")
    print("-f, --file              Specify a custom dictionary file to be used in the '--dictionary' option.")
    print("-s, --seperator         Specify if the words in the '--dictionary' option should be seperated with a '-'.")
    print("-l, --leadingSymbol     Specify if the password should start with a symbol in the '--dictionary' option .")

if __name__=="__main__":
  main()
