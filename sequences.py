#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibonacci(n):
    """Function docstring
    All functions should have their own documentation via docstrings.
    Standard indent size in python is 4 spaces, no tabs. Arguments are
    positional, unless given a default value as a keyword-argument.
    Here args is a list of all positional arguments beyond those listed.
    Here kwargs is a list of all keyword arguments beyond those listed.
    
    
    
    The function doc string should describe the name of the function, 
    its return value and type (if any), and its list of arguments and
    their expected types (if any). Both positional and keyword arguments
    should be listed separately.
    
    For more detailed examples from Google about how to use docstrings see,
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    """
    f1=1
    f2=1
    out=[]

    for i in range (0,n):
        out.append(f1)
        fn=f1+f2
        f1=f2
        f2=fn
   
    out.append(f1)
    return out

    
