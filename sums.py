import argparse

"""Variation of the subset sum problem:
    given a set B ("blocks"), of integers > 1, each with prime factors <= P:
    * can an integer n be expressed as the sum of m or fewer numbers from B?
    * what is the lowest number n that cannot be expressed that way?
"""

# largest prime factor that a number can have to be an adding block
max_prime_factor = 3

# largest number of blocks to use in a sum
max_block_count = 3

# largest integer to consider as a block
max_block_size = 1000

# list of blocks to use
summing_blocks = []

# set of all summing solutions for the current number.
# this is cleared each time a new number is examined.
solution_set = []


def largest_prime_factor(num):
    """Find the largest prime factor of the provided integer."""
    largest = 2
    while largest < num:
        if num % largest == 0:
            num /= largest
        else:
            largest += 1
    return largest


def build_block_list(max_block_value):
    """Build the list of small-prime factor blocks to use for summing.
    For convenience, the list is in descending order."""
    for num in range(2, max_block_value):
        if largest_prime_factor(num) <= max_prime_factor:
            summing_blocks.insert(0, num)


def compose_inner(num, solution):
    """Look for a subset sum solution for the provided number.
    If one is found, add it to the global solution set and return.
    Terminating conditions:
    * block count exceeds max
    * no blocks smaller than num are available
    """
    if len(solution) >= max_block_count:
        return
    for block in summing_blocks:
        if len(solution) > 0 and block > solution[-1]:
            continue
        if block == num:
            solution.append(block)
            solution_set.append(solution)
            return
        if block < num:
            trial = list(solution)
            trial.append(block)
            compose_inner(num - block, trial)


def compose(num):
    """Look for all subset sum solutions for the provided number."""
    global solution_set
    solution_set = []
    compose_inner(num, [])


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--maxfactor",
                    help="Max prime factor value for all blocks.")
parser.add_argument("-m", "--maxblockcount",
                    help="Max number of blocks in a sum solution.")
parser.add_argument("-n", "--maxblocksize",
                    help="Highest block value to consider for a sum.")
parser.add_argument("-s", "--single",
                    help="Show all solutions for the provided number and exit.")
args = parser.parse_args()

if args.maxfactor:
    max_prime_factor = int(args.maxfactor)
if args.maxblockcount:
    max_block_count = int(args.maxblockcount)
if args.maxblocksize:
    max_block_size = int(args.maxblocksize)

build_block_list(max_block_size)

if args.single:
    compose(int(args.single))
    if len(solution_set) > 0:
        for sol in solution_set:
            print "found solution:", sol
    else:
        print "No solutions found."
    exit(0)

# default action:
# find smallest number that cannot be summed with given parameters
to_try = 2
while True:
    compose(to_try)
    if len(solution_set) == 0:
        print "First failed number:", to_try
        exit(0)
    to_try += 1
