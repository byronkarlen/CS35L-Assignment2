#!/usr/local/cs/bin/python3

import random, sys, string
import argparse

def parse_ranged_input(input_range):
    if(len(input_range) < 3 or input_range.count('-') != 1):
        print('shuf: invalid input range: ' + input_range)
        return (-1, -1)
    lo, hi = input_range.split('-')
    try:
        lo = int(lo)
        hi = int(hi)
    except:
        print('shuf: invalid input range: ' + input_range)
        return (-1, -1)
    if lo - hi == 1:
        return (-1, -1)
    if hi < lo:
        print('shuf: invalid input range: ' + input_range)
        return (-1, -1)

    return (lo, hi+1)

def shuffle(lines, numlines, repeat, remove_newline):
    if remove_newline:
        str_end=''
    else:
        str_end='\n'
        
    if repeat:
        i = 0
        while(i < numlines):
            print(random.choice(lines), end=str_end)
            i+=1
    else:
        random.shuffle(lines)
        if(numlines > len(lines)):
           numlines = len(lines)

        i = 0
        while(i < numlines):
            print(lines[i], end=str_end)
            i+=1

def main():
    version_msg = "%prog 1.0"
    usage_msg = """%prog [OPTION]... FILE
Outputs a random permutation of input lines from FILE."""
    
    parser = argparse.ArgumentParser(description=usage_msg)
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-n', '--head-count=COUNT', type=int, dest='count', help='output at most n lines')
    parser.add_argument('-e', '--echo', nargs='*', action='store', dest='cmd_line_input', help='treat each argument as an input line')
    parser.add_argument('-i', '--input-range=LO-HI', action='store', dest='ranged_input', help='Treat each input LO-HI as an input line.')
    parser.add_argument('-r', '--repeat', action='store_true', dest='repeat', default=False, help='Repeat output values, that is, select with rneplacement')

    
    args = parser.parse_args()
    arg_dict = vars(args)

    match arg_dict:
        #no options given
        case{'cmd_line_input': None,'ranged_input': None, 'count': None,  'repeat': False}:
           mylines = args.filename.readlines()
           fromFile = True
           if(args.filename == sys.stdin):
               fromFile = False
               
           shuffle(mylines, len(mylines), False, fromFile)

        # -n
        case{'cmd_line_input': None,'ranged_input': None, 'repeat': False}:
            mylines = args.filename.readlines()

            if args.count > len(mylines):
                args.count = len(mylines)
            elif args.count < 0:
                print('shuf: invalid line count: ' + str(args.count))
                return
            
            fromFile = True
            if(args.filename == sys.stdin):
                fromFile = False
                
            shuffle(mylines, args.count, False, fromFile)

        # -r
        case{'repeat': True, 'cmd_line_input': None, 'ranged_input': None, 'count': None}:
            mylines = args.filename.readlines()
            fromFile = True
            if(args.filename == sys.stdin):
                fromFile = False
            shuffle(mylines, float('inf'), True, fromFile)

        # -r -n
        case{'repeat': True, 'cmd_line_input': None, 'ranged_input': None}:
            mylines = args.filename.readlines()
            if args.count < 0:
                print('shuf: invalid line count: ' + str(args.count))
                return
            fromFile = True
            if(args.filename == sys.stdin):
                fromFile = False
            shuffle(mylines, args.count, True, fromFile)

        # -e
        case{'ranged_input': None, 'count': None,  'repeat': False}:
            mylines = args.cmd_line_input
            shuffle(mylines, len(mylines), False, False)

        # -e -n
        case{'ranged_input': None, 'repeat': False}:
            mylines = args.cmd_line_input
            if args.count > len(mylines):
                args.count = len(mylines)
            elif args.count < 0:
                print('shuf: invalid line count: ' + str(args.count))
                return
            shuffle(mylines, args.count, False, False)
                        
        # -e -r
        case{'ranged_input': None, 'count': None,  'repeat': True}:
            mylines = args.cmd_line_input
            shuffle(mylines, float('inf'), True, False)
        
        # -e -n -r
        case{'ranged_input': None, 'repeat': True}:
            mylines = args.cmd_line_input
            if args.count < 0:
                print('shuf: invalid line count: ' + str(args.count))
                return
            shuffle(mylines, args.count, True, False)
            
        # -i
        case{'cmd_line_input': None, 'count': None,  'repeat': False}:
            if str(args.filename) != "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>":
                print('shuf: input file is not readable')
                return
            lo, hi  = parse_ranged_input(args.ranged_input)
            if lo == -1 and hi == -1:
                return

            mylines = [str(x) for x in range(lo, hi)]
            shuffle(mylines, len(mylines), False, False)

        
        # -i -n
        case{'cmd_line_input': None, 'repeat': False}:
            if str(args.filename) != "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>":
                print('shuf: input file is not readable')
                return
            lo, hi  = parse_ranged_input(args.ranged_input)
            if lo == -1 and hi == -1:
                return
            
            if args.count < 0:
                print('shuf: invalid line count: ' + str(args.count))
                return

            mylines = [str(x) for x in range(lo, hi)]

            if args.count > len(mylines):
                args.count = len(mylines)
            shuffle(mylines, args.count, False, False)
            
        # -i -r
        case{'cmd_line_input': None, 'count': None,  'repeat': True}:
            if str(args.filename) != "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>":
                print('shuf: input file is not readable')
                return
            lo, hi  = parse_ranged_input(args.ranged_input)
            if lo == -1 and hi == -1:
                return

            mylines = [str(x) for x in range(lo, hi)]
            shuffle(mylines, float('inf'), True, False)
            
        # -i -r -n
        case{'cmd_line_input': None, 'repeat': True}:
            if str(args.filename) != "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>":
                print('shuf: input file is not readable')
                return
            lo, hi  = parse_ranged_input(args.ranged_input)
            if lo == -1 and hi == -1:
                return

            if args.count < 0:
                print('shuf: invalid line count: ' + str(args.count))
                return

            mylines = [str(x) for x in range(lo, hi)]
            shuffle(mylines, args.count, True, False)    
            
        # -e -i
        case _:
            print("shuf: cannot combine -e and -i options")
   
if __name__ == "__main__":
   main()
