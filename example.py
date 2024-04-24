import networkx as nx
from recviz import trace_call_graph, show_graph


g = nx.DiGraph()
@trace_call_graph(g)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
fib(10)
    
show_graph(g, 'fib_10.png')

g2 = nx.DiGraph()
_fib = {}
@trace_call_graph(g2)
def fib2(n):
    if n not in _fib:
        if n == 1 or n == 2:
            _fib[n] = 1
        else:
            _fib[n] = fib2(n-1) + fib2(n-2)
    return _fib[n]

fib2(10)
    
show_graph(g2, 'fib2_10.png')