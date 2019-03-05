#! /usr/bin/env python3

''' Python script to test-use argparse module '''

import argparse

# Python consists of module for parsing the options through the command line.
# These are getopt, optparse and argparse, out of which the argparse is much more convenient and flexible.

# Adavantages of argparse (over optparse, which is more user-friendly than getopt):
#   - handling positional arguments
#   - supporting sub-commands
#   - allowing alternative option prefixes like + and /
#   - handling zero-or-more and one-or-more style arguments
#   - producing more informative usage messages
#   - providing a much simpler interface for custom types and actions

# argparse is a module that allows for neat and familiar option and argument parsing for our python programs, has
# inbuilt help functions. Auto-formats the output for the console and automaticaaly generates the usage.

# How it works!!!
#   - Interfaces with the python system module to grab the arguments from the command line
#   - Supports checking and making sure required arguments are provided.

# So we can create an example fibonacci program - by taking the num parsed value.
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def main():
    # Positional Arguments
    #   - Positional arguments are required arguments that we need for our program to complete.
    #   - Positional arguments do not require the dash (-) because it is not an option.
    parser = argparse.ArgumentParser()      # makes a ArgumentParser object
    parser.add_argument('num', help='the fibonacci number you wish to calculate.', type=int)  # the parser will be defined to take a necessary argument num (also called the positional argument)

    # Optional Arguments
    #   - The -h option is already inbuilt by default
    #   - we can create as many as we like and argparse will handle it.
    #   - like the positional arguments the help will be automatically added to the help output
    parser.add_argument('-o', '--output', help='Output result to a file', action='store_true')

    # Mutually Exclusive Arguments
    #   - You can select one option or other option, but not both!
    #   - This can be done with a group
    #   - Automatically generates an output telling the user can only pick one, should they try to use both
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')

    args = parser.parse_args()      # args from the console is taken
    print('n = {}'.format(args.num))    # accessing the argument by the name as defined in the add_argument method
    
    result = fib(args.num)
    if args.verbose:
        print('The {}th fib number is: {}'.format(args.num, result))
    elif args.quiet:
        print(result)
    else:
        print('fib({}) = {}'.format(args.num, result))

    if args.output:
        with open('fib.txt', 'a') as f:
            f.write(str(result) + '\n')

if __name__ == '__main__':
    main()

# Why use it?
#   - argparse makes it easy to handle command line options and arguments
#   - comes default with python
#   - genreates and formats usage and help output
#   - allows dynamic data input to change the output of your program