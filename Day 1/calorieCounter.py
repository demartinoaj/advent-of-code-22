#!/usr/bin/env python3
import argparse

def getArgs():
    '''
    This function gets the file names from the command line, or assigns the default
    :return: inFile
    '''
    parser = argparse.ArgumentParser(description="Advent of Code Day 1", prog="Calorie Input Counter")
    parser.add_argument('-i', type=str, help='Input File')

    args = parser.parse_args()
    inFile = args.i

    return inFile


def probTwo():
    '''
    This function solves the second word problem
    :return: None
    '''
    elfs = []
    total = 0

    with open(getArgs()) as my_file:
        nums = [int(x.strip()) if x.strip().isdigit() else None for x in my_file.readlines()]
        for cal in nums:
            if cal == None :
                elfs.append(total)
                total = 0
            else :
                total += cal
        elfs.sort(reverse=True)
        print("Top three elves calorie Total: " + str(sum(elfs[:3])))


def probOne():
    '''
    This function solves the first word problem
    :return: None
    '''
    elfs = []
    total = 0

    with open(getArgs()) as my_file:
        nums = [int(x.strip()) if x.strip().isdigit() else None for x in my_file.readlines()]
        for cal in nums:
            if cal == None :
                elfs.append(total)
                total = 0
            else :
                total += cal
        print("Top elf calorie Total: ", max(elfs))

def main():
    probOne()
    probTwo()

if __name__ == "__main__":
    exit(main())