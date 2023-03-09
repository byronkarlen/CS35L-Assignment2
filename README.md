# CS35L-Assignment2

### Project Spec

__Part 1:__

Use the Emacs command M-x what-line and see what it does.

M-x what-line simply tells you what line you are on, not how many lines are in the buffer. Design and implement an Emacs Lisp command M-x gps-line that acts like M-x what-line except that it says “Line 27/106” in contexts where M-x what-line would merely say “Line 27”; here, it’s assumed the buffer has 106 lines. 

When counting all the lines in a buffer, simply count the number of newline characters that it contains. This means that if a buffer ends in a non-newline, you should not count the characters after the last newline to be part of another line. Also, an empty buffer has zero lines.

Test your function on buffers that do not end in newline. Your function should be able to say things like “Line 1/0” and “Line 3/2”.

__Part 2:__

Consider the old-fashioned Python 2 script randline.py

Write a new script shuf.py in the style of randline.py but using Python 3 instead. Your script should implement the GNU shuf command that is part of GNU Coreutils. GNU shuf is written in C, whereas you want a Python implementation so that you can more easily add new features to it.

Your program should support the following shuf options, with the same behavior as GNU shuf: --echo (-e), --input-range (-i), --head-count (-n), --repeat (-r), and --help. As with GNU shuf, if --repeat (-r) is used without --head-count (-n), your program should run forever. Your program should also support zero non-option arguments or a single non-option argument “-” (either of which means read from standard input), or a single non-option argument other than “-” (which specifies the input file name). Your program need not support the other options of GNU shuf. As with GNU shuf, your program should report an error if given invalid arguments.

Your solution should use the argparse module instead of the obsolescent optparse. It should not import any modules other than argparse, string and the non-optparse modules that randline.py already imports. Don’t forget to change its usage message to accurately describe the modified behavior.

See more info about project spec here: 
https://web.cs.ucla.edu/classes/winter23/cs35L/assign/assign2.html 
