#!/usr/bin/env python3
import sequences

def main(local_argv):
    """Main function
    See below for why this would exist. The local_argv argument lists command
    line arguments taken from sys.argv within the protected main block below.
    """
    firstargv = int(local_argv[0])
    ret=sequences.fibonacci(firstargv)
    print(firstargv)
    print(ret[len(ret)-1])
    return

# After the body of the module, you can optionally create a protected main 
# section to place executable scripting code.

if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    main(sys.argv)
    
