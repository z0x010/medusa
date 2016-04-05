#!/usr/bin/env python
# coding:utf-8

"""
vagrant@precise64:~$ kernprof --help
Usage: kernprof [-s setupfile] [-o output_file_path] scriptfile [arg] ...

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -l, --line-by-line    Use the line-by-line profiler from the line_profiler
                        module instead of Profile. Implies --builtin.
  -b, --builtin         Put 'profile' in the builtins. Use 'profile.enable()'
                        and 'profile.disable()' in your code to turn it on and
                        off, or '@profile' to decorate a single function, or
                        'with profile:' to profile a single section of code.
  -o OUTFILE, --outfile=OUTFILE
                        Save stats to <outfile>
  -s SETUP, --setup=SETUP
                        Code to execute before the code to profile
  -v, --view            View the results of the profile in addition to saving
                        it.
"""

@profile
def calculate(n):
    s = 0
    for i in range(n):
        s += i
    for i in xrange(n):
        s += i
    for i in range(n):
        s *= i
    for i in xrange(n):
        s *= i
    return s

print calculate(10000)

"""
vagrant@precise64:~$ kernprof -l -v line_profiler_demo.py
0
Wrote profile results to line_profiler.py.lprof
Timer unit: 1e-06 s

Total time: 0.173917 s
File: line_profiler.py
Function: calculate at line 25

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    25                                           @profile
    26                                           def calculate(n):
    27         1            3      3.0      0.0      s = 0
    28     10001        20990      2.1     12.1      for i in range(n):
    29     10000        21504      2.2     12.4          s += i
    30     10001        22206      2.2     12.8      for i in xrange(n):
    31     10000        21380      2.1     12.3          s += i
    32     10001        20933      2.1     12.0      for i in range(n):
    33     10000        21329      2.1     12.3          s *= i
    34     10001        21841      2.2     12.6      for i in xrange(n):
    35     10000        23729      2.4     13.6          s *= i
    36         1            2      2.0      0.0      return s
"""
