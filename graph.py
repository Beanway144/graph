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

#turns a blank in the graph to a * given an x and y
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
        (x, _dummy) = getAxiedNumber(x, 0)
        y = int(-m*x+b) #i'm not sure why i have to negate this here but it works; i think some indexing is backwards
        diff = y - (-m*(x+1)+b) #gets the difference of f(x) and f(x+1) so that it can filler
        if y < GHEIGHT / 2 and y > - GHEIGHT / 2:
            turnOn(x, y)

        #### filler (for lines with large slopes) ####
        diff = int(y - (-m*(x+1)+b)) #gets the difference of f(x) and f(x+1)
        for d in range(0, abs(diff) - 1):
            if diff < 0:
                print("hi")
                if y+d < GHEIGHT / 2 and y+d > - GHEIGHT / 2:
                    turnOn(x, y+d)
            elif diff > 0:
                if y-d < GHEIGHT / 2 and y-d > - GHEIGHT / 2:
                    turnOn(x, y-d)

def makeSin(a, b, c):
    for x in range(0, GWIDTH - 1):
        oldX = x
        (x, _dummy) = getAxiedNumber(x, 0)
        y = int(a * math.sin(b*x) + c)
        if y < GHEIGHT / 2 and y > - GHEIGHT / 2:
            turnOn(x, y)

#of the form a * sin(b*x)
def makeCos(a, b, c):
    for x in range(0, GWIDTH - 1):
        oldX = x
        (x, _dummy) = getAxiedNumber(x, 0)
        y = int(a * math.cos(b*x) + c)
        if y < GHEIGHT / 2 and y > - GHEIGHT / 2:
            turnOn(x, y)

def parse(inp):
    #only works for linear parsing
    inp = inp.replace(" ", "") #remove spaces
    if inp.split("sin")[0] == inp:
        if inp.split("cos")[0] == inp: #linear
            inp = inp.split("x")
            try:
                if inp[0] == "-":
                    m = -1.0
                else:
                    m = float(inp[0]) #if slope not specified, it's 1
            except:
                m = 1
            try:
                b = float(inp[1])
            except:
                b = 0
            makeLine(m, b)
        else: #cos
            inp = inp.replace(")", "").replace("(", "").split("cos", "x")
            a = float(inp[0])
            b = float(inp[1])
            c = float(inp[2])
            makeCos(a, b, c)
    else: #sin
        inp = inp.replace(")", "").replace("(", "").split("sin", "x")
        a = float(inp[0])
        b = float(inp[1])
        c = float(inp[2])
        makeSin(a, b, c)
        

def clearScreen():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def runREPL():
    print("Please enter a function to graph of the form mx + b or a sin(b x) + c.\n")
    while 1:
        inp = input("[-]")
        clearScreen()
        resetGraph()
        # try:
        #     parse(inp)
        # except:
        #     print("Input must be of the form mx + b, e.g. 3x - 7.")
        #     continue
        parse(inp)
        printGraph()


def main():
    clearScreen()
    makeSin(10, 1/10, 0)
    makeCos(10, 1/10, 0)
    printGraph()
    runREPL()

main()