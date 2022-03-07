# Command Line Graphing Calculator
This python script allows you to graph basic functions from the command line.
![sin and cos example graph](sincosEX.png)
## How to Graph:
As of now, type `python3 graph.py` in the directory with `graph.py`. Type in a function of the form `ax + b`, `asin(bx) + c`, or `acos(bx)+c`. You can graph multiple functions at once with the deliminator `//`. For example, `10sin(0.1x) // 10cos(0.1x)` results in the graphs in the image above. Note that as of now, the window is fixed at 30x100 (*-50 < x < 50*, *-15 < y < 15*) with an interval of 1 in both coordinate directions.
## Todo:
- functionality for polynomials, exponentials, tangent
- make the parser into a syntax tree instead of the omega cursed mess it is rn
- allow for changing intervals and window size
- make better error messages for incorrect format
