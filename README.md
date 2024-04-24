# recursive_trace
Python wrapper to render a trace graph of the function calls for a recursive function. 

Source: https://www.quora.com/How-can-I-draw-visualization-for-function-calls-in-a-recursive-function-in-Python

## Install These Before Use
The wrapper depends on having the `networkx` and `pygraphviz` packages in your conda environment.  Open anaconda and launch a 'CMD.exe Prompt'.  Then run the following two lines of code, answering 'y' when prompted:

```Bash
conda install networkx
```

```Bash
conda install --channel conda-forge pygraphviz
```

You will have to relaunch Spyder from Anaconda after doing this.

## How to Use the Wrapper
The wrapper is defined in file `recviz.py`.  So at the start of your python file where the recursive function is defined, include the following lines:

```Python
import networkx as nx
from recviz2 import trace_call_graph, show_graph
```

The wrapper uses `networkx` which is a common python package for doing computations with graphs.  We use the `DiGraph` class.  So add the following lines directly above your recursive function:

```Python
g = nx.DiGraph()
@trace_call_graph(g)
```

With the recursive function, the whole code will look like:

```Python
import networkx as nx
from recviz2 import trace_call_graph, show_graph

g = nx.DiGraph()
@trace_call_graph(g)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

Then, after you call the recursive function, `fib(10)`, a graph representation of the recursive function calls can be rendered and saved using function `show_graph` from the `recviz.py` file:

```Python
show_graph(g, 'fib_10.png')
```

This function takes the `DiGraph` object and the name you want your picture to be saved as.  It then saves the picture of the graph to your current working directory.  An example is included, `example.py`, which saves the recursive trace graph for fib(10) and another version of the function that is memoised.