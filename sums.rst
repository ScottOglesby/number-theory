===========
Subset Sums
===========
-----------
The problem
-----------
This project is a variation of the `Subset Sum Problem <https://en.wikipedia.org/wiki/Subset_sum_problem>`_
with the following parameters.

Given a set of integers *B*, each of which has prime factors no larger than *P*, and an input integer *N*:

- how can *N* be expressed as the sum of no more than *M* integers from *B*?
- given *P* and *M*, what is the smallest integer *N* (greater than 2) than cannot be summed this way?

For example, with *P* = 3, *M* = 3, and *N* = 239:

- *B* is [2, 3, 6, 8, 9, 12, 16, 18, 24 ...] (all of the form 2^*x* * 3^*y*)
- 239 has one solution: 128, 108, 3. (Many numbers have multiple solutions.)
- the smallest number that cannot be summed this way is 431.

With *P* = 5, *M* = 3, and *N* = 239:

- *B* is [2, 3, 5, 6, 8, 9, 10, 12, 15, ...] (less sparse than above)
- 239 has 47 solutions, such as 100, 75, 64.
- the smallest number that cannot be summed is 1771.
- the algorithm takes much longer to run.

Running with *P* greater than 5 is not recommended :-)

It seems (but I haven't proven) that numbers already in set B have only a single solution; in other words, the only solution for a number like 576 is 576 itself.

------------------
The implementation
------------------

The "find all possible solutions" algorithm lends itself to a recursive implementation. The terminating conditions are:

- the sum in progress already has *M* elements and is not a solution
- all elements of *B* have been tried

----------
How to run
----------

* python sums.py: find smallest number that cannot be summed with *P* = 3, *M* = 3
* python sums.py --single 239: show all solutions for *N* = 239
* python sums.py maxfactor 5 --single 239: show all solutions for *P* = 5, *M* = 3, *N* = 239
* python sums.py -h: show other options