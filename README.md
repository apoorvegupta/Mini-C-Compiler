# Mini-C-Compiler
This project being a Mini Compiler for the C programming language, focuses on generating an intermediate code for the language for specific constructs. It works for constructs such as conditional statements, loops and the if-else operator. The main functionality of the project is to generate an optimized intermediate code for the given C source code.

Following are the things which are being added in this projecs while making :-

Local and global variables, parameters.
Functions, if, while, do``while, return.
=, ?: (ternary), ||, &&, ==, !=, <, >=, +, -, *, ++, -- (post-ops), !, - (unary), [], ()
Integer, character, true and false literals. String literals, with automatic concatenation.
The language it implements is typeless. Everything is a 4 byte signed integer.
Pointer indexing works in increments of 4 bytes, pointer arithmetic is byte-by-byte.
and most importantly  :- The general philosophy was only include a feature if it reduces the total code size. This is taken to its extreme in the insane branch.
