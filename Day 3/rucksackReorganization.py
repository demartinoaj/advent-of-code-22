#!/usr/bin/env python3
import argparse
import numpy as np

def getArgs():
    '''
    This function gets the file names from the command line, or assigns the default
    :return: inFile
    '''
    parser = argparse.ArgumentParser(description="Advent of Code Day 3",)
    parser.add_argument('-i', type=str, help='Input File')

    args = parser.parse_args()
    inFile = args.i

    return inFile

def strReplace(letters):
    val = []
    for letter in letters:
        if ord(letter) >= ord('a') :
            val.append(ord(letter) - ord('a') + 1)
        else:
            val.append(ord(letter) - ord('A') + 27)
    return set(val)

def probTwo():
    '''
    This function solves the second word problem
    :return: None
    '''
    totalBadge = 0

    with open(getArgs()) as my_file:
        sacks = [ strReplace(x.strip()) for x in my_file.readlines()]
        sacks = np.array_split(sacks, len(sacks)/3)

        for group in sacks:
            totalBadge = totalBadge + sum(group[0] & group[1] & group[2])

    print("Sum of Badges: " + str(totalBadge))


def probOne():
    '''
    This function solves the first word problem
    :return: None
    '''
    totalPriority = 0

    with open(getArgs()) as my_file:
        sacks = [ [strReplace(x[:len(x)//2].strip()), 
            strReplace(x[len(x)//2:].strip())] for x in my_file.readlines()]
        
        for sack in sacks:
            totalPriority = totalPriority + sum(sack[0] & sack[1])

    print("Sum of priorities: " + str(totalPriority))

def main():
    probOne()
    probTwo()

if __name__ == "__main__":
    exit(main())