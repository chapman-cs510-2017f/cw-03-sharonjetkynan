def test1():
    """Test function for nosetests
    Any function name starting with prefix test_ will be automatically run
    by nose. Ideally these should be put in a separate file that also
    begins with the prefix test_.
    
    In a test function, use an assert command to test a Boolean statement
    about how your code executed.  If the assert fails, it throws
    an exception, which is caught by nose and reported as a failure.
    Anything that is printed to the screen during this function is
    suppressed unless there is a failure, where it can be used for
    debugging.
    """
    know=[1,1,2,3,5]
    ret=fibonacci(5)
    
    assert type(ret) == list
    
    print(ret)
    
    assert len(ret) == len(know)
    
    assert know == ret
    
        
    return

def test2():
    """Test function for nosetests
    Any function name starting with prefix test_ will be automatically run
    by nose. Ideally these should be put in a separate file that also
    begins with the prefix test_.
    
    In a test function, use an assert command to test a Boolean statement
    about how your code executed.  If the assert fails, it throws
    an exception, which is caught by nose and reported as a failure.
    Anything that is printed to the screen during this function is
    suppressed unless there is a failure, where it can be used for
    debugging.
    """
    f_list = fibonacci(8)
    print(f_list[7])
    assert f_list[7] == 21
    
    
    t=-1
    asset fibonacci(t) == False
  

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
    if type(n) != int:
        print("not a integer")
        return False

    if n <= 0:
        print("not a postive integer")
        return False
    
    f1=1
    f2=1
    out=[]

    for i in range (0,n):
        out.append(f1)
        fn=f1+f2
        f1=f2
        f2=fn
   
    """out.append(f1) WRONG!!""" 
    return out

n=8
ret=fibonacci(n)




print("test1")
test1()

f8=21
print("test2")
test2()





