import networkx as nx 
import functools 
 
def call_label( name, args, kwargs ): 
    str_args = [ str(a) for a in args ] + [ str(k) + "=" + str(v) for k,v in kwargs.items() ] 
    return name + "(" + ",".join( str_args ) + ")" 
     
def next_node_id( graph ): 
    if "next_id" in graph.graph: 
        i = graph.graph["next_id"] 
    else: 
        i = 1 
    graph.graph["next_id"] = i+1 
    return i 

def trace_call_graph(graph, call_stack=[]): 
    def trace(func): 
        @functools.wraps(func) 
        def wrapper( *args, **kwargs ): 
            n = next_node_id( graph ) 
            graph.add_node( n, label=call_label( func.__name__, args, kwargs ) )                         
            if len( call_stack ) > 0: 
                graph.add_edge( call_stack[-1], n ) 
            call_stack.append( n ) 
            ret = func( *args, **kwargs ) 
            call_stack.pop() 
            return ret 
        return wrapper 
    return trace 

def show_graph(g, name): 
    # nx.draw_planar( g, with_labels=True, 
    #                   labels=dict( g.nodes.data("label" ) ), 
    #                   node_color="white", 
    #                   node_size=10,
    #                   font_size=3) 
    A = nx.nx_agraph.to_agraph(g)
    A.draw(name, prog="neato")