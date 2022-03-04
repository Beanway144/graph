import math
import os
from time import sleep

GWIDTH = 100
GHEIGHT = 30
xInterval = 1
yInterval = 1

#the graph is initialized as a GWIDTH by GHEIGHT matrix of False
graph = [[False for i in range(GWIDTH)] for j in range(GHEIGHT)]

#prints the graph
def printGraph():
    for h in range(0, GHEIGHT - 1):
        line = ""
        for w in range(0, GWIDTH - 1):
            newChar = " "
            if h == (GHEIGHT / 2) - 1:
                newChar = "-"
            if w == (GWIDTH / 2) - 1:
                newChar = "|"
            if w == (GWIDTH / 2) - 1 and h == (GHEIGHT / 2) - 1:
                newChar = "+"
            if (graph[h])[w]:
                newChar = "*"
            line += newChar
        print(line)
    
#turns a coordinate from the array index into an axies-centered index
#i.e. array coordinates to cartesian coordinates, where axies are centered
def getAxiedNumber(x, y):
    y = (int(GHEIGHT / 2) - y - 1) * yInterval
    x = (int(GWIDTH / 2) - x -1) * xInterval
    return (x, y)

#turns a blank in the graph to a + given an x and y
def turnOn(x, y):
    (x, y) = getAxiedNumber(x, y)
    (graph[y])[x] = True

#returns the graph to a blank graph
def resetGraph():
    for h in range(GHEIGHT):
        for w in range(GWIDTH):
            graph[h][w] = False

def makeHorzLine(y):
    for x in range(0, GWIDTH - 1):
        turnOn(x, y)

#make a line via slope-intercept form: y = mx + b
def makeLine(m, b):
    for x in range(0, GWIDTH - 0):
        oldX = x
        (x, _dummy) = getAxiedNumber(x, 0)
        y = int(-m*x+b) #i'm not sure why i have to negate this here but it works; i think some indexing is backwards
        if y < GHEIGHT / 2 and y > - GHEIGHT / 2:
            turnOn(x, y)

def parse(inp):
    #only works for linear parsing
    inp = inp.replace(" ", "").split("x")
    m = int(inp[0])
    b = int(inp[1])
    return (m, b)

def clearScreen():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def runREPL():
    print("Please enter a linear function to graph of the form mx + b.\n")
    while 1:
        inp = input("[-]")
        try:
            (m, b) = parse(inp)
        except:
            print("Input must be of the form mx + b, e.g. 3x - 7.")
            continue
        clearScreen()
        resetGraph()
        makeLine(m, b)
        printGraph()


def main():
    clearScreen()
    runREPL()

main()