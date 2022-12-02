#!/usr/bin/env python3
import argparse

def getArgs():
    '''
    This function gets the file names from the command line, or assigns the default
    :return: inFile
    '''
    parser = argparse.ArgumentParser(description="Advent of Code Day 2",)
    parser.add_argument('-i', type=str, help='Input File')

    args = parser.parse_args()
    inFile = args.i

    return inFile


def probTwo():
    '''
    This function solves the second word problem
    :return: None
    '''
    score = 0

    with open(getArgs()) as my_file:
        games = [x.strip() for x in my_file.readlines()]
        for game in games:
            op = game[0]
            res = game[2]

            if res  == 'X' : #lose
                if op == 'A' :
                    score += 3 #scissors
                elif op == 'B' :
                    score += 1 #rock
                else :# 'C'
                    score += 2 #paper

            elif res == 'Y' : #draw
                score += 3
                if op == 'A' :
                    score += 1 #rock
                elif op == 'B' :
                    score += 2 #paper
                else :# 'C'
                    score += 3 #scissors

            else : # z, win
                score += 6
                if op == 'A' :
                    score += 2 #paper
                elif op == 'B' :
                    score += 3 #scissor
                else : # 'C'
                    score += 1 #rock

    print("Score: " + str(score))


def probOne():
    '''
    This function solves the first word problem
    :return: None
    '''
    score = 0

    with open(getArgs()) as my_file:
        games = [x.strip() for x in my_file.readlines()]
        for moves in games:
            op = moves[0]
            me = moves[2]
            if me  == 'X' :
                score += 1
                if op == 'A' :
                    score += 3
                elif op == 'C' :
                    score += 6

            elif me == 'Y' :
                score += 2
                if op == 'B' :
                    score += 3
                elif op == 'A' :
                    score += 6

            else : # 'Z'
                score += 3
                if op == 'C' :
                    score += 3
                elif op == 'B' :
                    score += 6

    print("Score: " + str(score))

def main():
    probOne()
    probTwo()

if __name__ == "__main__":
    exit(main())