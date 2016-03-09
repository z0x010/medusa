"""
Programming languages support decomposing problems in several different ways:

    Most programming languages are procedural: programs are lists of instructions that tell the computer
    what to do with the program’s input. C, Pascal, and even Unix shells are procedural languages.

    In declarative languages, you write a specification that describes the problem to be solved,
    and the language implementation figures out how to perform the computation efficiently.
    SQL is the declarative language you’re most likely to be familiar with; a SQL query describes
    the data set you want to retrieve, and the SQL engine decides whether to scan tables or use indexes,
    which subclauses should be performed first, etc.

    Object-oriented programs manipulate collections of objects.
    Objects have internal state and support methods that query or modify this internal state in some way.
    Smalltalk and Java are object-oriented languages.
    C++ and Python are languages that support object-oriented programming,
    but don’t force the use of object-oriented features.

    Functional programming decomposes a problem into a set of functions.
    Ideally, functions only take inputs and produce outputs,
    and don’t have any internal state that affects the output produced for a given input.
    Well-known functional languages include the ML family (Standard ML, OCaml, and other variants) and Haskell.
"""
