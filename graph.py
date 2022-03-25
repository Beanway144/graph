import math
import os
from time import sleep
from tkinter import XView
import numpy as np
import operator as op

GWIDTH = 100
GHEIGHT = 30
xInterval = 1
yInterval = 1

ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}


#the graph is initialized as a GWIDTH by GHEIGHT matrix of False
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
                if i1 < i2:
                    graph[i1:i2,i] = 1
                else:
                    graph[i2:i1,i+1] = 1

    g = np.full((GHEIGHT, GWIDTH), " ")
    g[GHEIGHT // 2] = np.full(graph.shape[1], "―")
    g[:,GWIDTH // 2] = np.full(graph.shape[0], "|")
    g[GHEIGHT // 2, GWIDTH // 2] = "+"
    g[graph == 1] = "⋅"

    for j in range(GHEIGHT):
        print(''.join(g[j]))
    
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
    if inp == "exit": exit()

    inp = ''.join(inp.split())

    if inp.count('=') == 1:
        left,right = inp.split('=')
        left = left.strip(); right = right.strip()
        if (left != 'y'): print('Please use y = f(x) format')
        else:
            x = (np.arange(GWIDTH) - GWIDTH // 2) * xInterval
            y_vals = eval(right)
            x_plot = np.arange(GWIDTH, dtype='int32')
            y_plot = (y_vals // yInterval) * -1

            ind = np.argwhere(np.abs(y_plot) < GHEIGHT // 2)
            
            graph[y_plot[ind].astype('int32') + GHEIGHT // 2, x_plot[ind]] = 1
        

def clearScreen():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def runREPL():
    print("Please enter a function in the form y = f(x) and use explicit multiplication:")
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