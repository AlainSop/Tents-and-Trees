# Tents-and-Trees
Automatic solver of a grid of the game "Tents and Trees" by formalizing the instance into clauses.

Execution of the program :

./main.py < problem-file > < final-result-file > < SAT-solver > < sat-To-3-Sat >

If you enter "input" in < problem-file >, you will be guided to input your own instantiation
(files called "TestAxA.txt" are some examples of problem files).

The SAT-solver can be "minisat" (a common SAT-solver) or "walksat" (our own SAT-solver).

If < sat-To-3-Sat > is not empty, all the clauses will be of length 3.
