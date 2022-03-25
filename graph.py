import math
import os
from time import sleep
import numpy as np

GWIDTH = 100
GHEIGHT = 30
xInterval = 1
yInterval = 1


#the graph is initialized as a GWIDTH by GHEIGHT matrix of False
# graph = [[False for i in range(GWIDTH)] for j in range(GHEIGHT)]
graph = np.zeros((GHEIGHT,GWIDTH))

#prints the graph
def printGraph():
    for i in range(GWIDTH):
        if (i == GWIDTH - 1): break
        c1 = graph[:,i]; c2 = graph[:,i+1]
        i1 = np.argwhere(c1 == 1); i2 = np.argwhere(c2 == 1)
        if (len(i1) != 0 and len(i2) != 0):
            i1 = i1[0,0]; i2 = i2[0,0]
            if (abs(i1-i2) > 1):
                graph[min(i1,i2):max(i1,i2),i] = np.ones(abs(i1-i2))

    g = np.full((GHEIGHT, GWIDTH), " ")
    g[GHEIGHT // 2] = np.full(graph.shape[1], "-")
    g[:,GWIDTH // 2] = np.full(graph.shape[0], "|")
    g[GHEIGHT // 2, GWIDTH // 2] = "+"
    g[graph == 1] = "*"
    g = np.hstack((g, np.full((GHEIGHT, 1), "\n")))

    print(str.replace(g.tobytes().decode("utf-8"), "*", "⠁"))
    
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
    x_vals = (np.arange(GWIDTH) - GWIDTH // 2) * xInterval
    y_vals = (m * x_vals + b)

    x_plot = np.arange(GWIDTH, dtype='int32')
    y_plot = (y_vals // yInterval) * -1

    ind = np.argwhere(np.abs(y_plot) < GHEIGHT // 2)
    
    graph[y_plot[ind].astype('int32') + GHEIGHT // 2, x_plot[ind]] = 1

#of the form a * sin(b*x) + c
def makeSin(a, b, c):
    x_vals = (np.arange(GWIDTH) - GWIDTH // 2) * xInterval
    y_vals = (a * np.sin(b * x_vals) + c)

    x_plot = np.arange(GWIDTH, dtype='int32')
    y_plot = (y_vals // yInterval) * -1

    ind = np.argwhere(np.abs(y_plot) < GHEIGHT // 2)
    
    graph[y_plot[ind].astype('int32') + GHEIGHT // 2, x_plot[ind]] = 1

#of the form a * cos(b*x) + c
def makeCos(a, b, c):
    x_vals = (np.arange(GWIDTH) - GWIDTH // 2) * xInterval
    y_vals = (a * np.cos(b * x_vals) + c)

    x_plot = np.arange(GWIDTH, dtype='int32')
    y_plot = (y_vals // yInterval) * -1

    ind = np.argwhere(np.abs(y_plot) < GHEIGHT // 2)
    
    graph[y_plot[ind].astype('int32') + GHEIGHT // 2, x_plot[ind]] = 1

def animateGraph(type):
    for b in range(-50, 50):
        resetGraph()
        if type == "sin":
            makeSin(10, b/100, 0)
        if type == "sinf":
            makeSin(10, (b + 51)/30, 0)
        if type == "cos":
            makeCos(10, b/100, 0)
        if type == "linear":
            makeLine(b/10, 0)
        clearScreen()
        printGraph()
        sleep(0.10)
    clearScreen()



def parse(inp):
    if inp == "exit":
        exit()
    
    if inp[0] == 'g' and inp[1] == 'o':
        animateGraph(inp.replace(" ", "").replace("go", ""))
        return

    #recursively parse multiple equations with // delim
    if inp.split("//")[0] != inp:
        inp = inp.split("//")
        parse(inp[0])
        parse(inp[1])
        return
    
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
            # acos(bx)+c
            inp = inp.split("cos")
            if inp[0] == '':
                a = 1.0
            else:
                a = float(inp[0])
            try: #this is really bad try-catch abuse. need to find a way to check if 'c' is plus or minus
                inp2 = inp[1].replace("x","").replace("(","").replace(")","").split("+")
                if inp2[0] == '':
                    b = 1.0
                else:
                    b = float(inp2[0])
                try:
                    c = float(inp2[1])
                except:
                    c = 0.0
            except:
                inp2 = inp[1].replace("x","").replace("(","").replace(")","").split("-")
                if inp2[0] == '':
                    b = 1.0
                else:
                    b = float(inp2[0])
                try:
                    c = -float(inp2[1])
                except:
                    c = 0.0
            makeCos(a, b, c)
    else: #sin --obvious code repetition can be cleaned up
        # asin(bx)+c
        inp = inp.split("sin")
        if inp[0] == '':
            a = 1.0
        else:
            a = float(inp[0])
        try: #this is really bad try-catch abuse. need to find a way to check if 'c' is plus or minus
            inp2 = inp[1].replace("x","").replace("(","").replace(")","").split("+")
            if inp2[0] == '':
                b = 1.0
            else:
                b = float(inp2[0])
            try:
                c = float(inp2[1])
            except:
                c = 0.0
        except:
            inp2 = inp[1].replace("x","").replace("(","").replace(")","").split("-")
            if inp2[0] == '':
                b = 1.0
            else:
                b = float(inp2[0])
            try:
                c = -float(inp2[1])
            except:
                c = 0.0
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